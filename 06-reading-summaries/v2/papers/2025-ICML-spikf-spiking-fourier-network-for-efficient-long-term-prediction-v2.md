---
tags: [SNN, Fourier, FFT, time-series-forecasting, long-term-prediction, energy-efficiency]
---

# Summary V2｜SpikF: Spiking Fourier Network for Efficient Long-term Prediction

## 1. Core Understanding

SpikF 是一个面向 multivariate long-term time-series forecasting 的 attention-free SNN framework。给定长度为 $L$、变量数为 $D$ 的历史序列，模型预测未来 $H$ 个时间点。论文试图解决两个问题：已有 temporal SNN encoding 将长序列作为整体处理，导致 hidden representation 和计算量扩大；Spiking Transformer 中的 self-attention 对 temporal order 不敏感，而现有 spiking positional encoding 尚未充分解决这一问题。

SpikF 的核心数据流是：将连续输入分成 patches，用 Spiking Patch Encoder（SPE）把每个局部子序列编码为 binary spike train；再将 spike patches 分组，通过 Spiking Frequency Selector（SFS）在 frequency domain 中选择重要成分，并用 S-FFT/S-iFFT 建立全局时间依赖；最后用 MLP Decoder 将 processed spikes 重建为连续预测。Fourier Transform 在这里不是单纯的后处理，而是 SNN 中连接局部 spike dynamics 与全局序列建模的 external dynamics。

作者在八个长期预测 benchmark 上报告，相比 iTransformer 平均降低 1.9% MAE；在 ECL 的代表性 energy analysis 中，SpikF 的 total energy 比 iTransformer 低 3.16 倍。SpikF 还在 Solar-energy 上验证 short-term prediction，并测试更长 look-back window。其价值主要是 SNN-side Fourier coupling 和长时序建模，不是 event-camera 或 Event Cloud architecture。

## 2. Problem and Motivation

传统 SNN 适合稀疏、事件驱动计算，但长期预测需要同时保留很长历史和较细的时间结构。Delta encoding、convolution encoding 和 linear encoding 往往直接处理完整长序列，可能将每个时间位置扩展到更高 hidden dimension，削弱 SNN 的 energy advantage。

另一方面，standard self-attention 具有 permutation-invariance：如果只对 token 做相同的线性变换、attention 和后续 permutation-equivariant 操作，打乱时间顺序只会同步打乱输出，而不会让模型获得时间位置本身。因此时间序列 Transformer 需要 positional encoding。作者认为现有 spiking positional encoding 对长期预测帮助有限，SpikF 改用 Fourier representation 的 rotation factor 隐式保留顺序结构。

本文的关键问题是：能否用 patch encoding 降低长序列的 SNN 计算负担，同时用 spike-compatible frequency selection 获得全局 receptive field 和 temporal order information？

## 3. Method Overview

问题设定为：

$$
x_{1:L}\in\mathbb{R}^{L\times D}
\rightarrow
y_{1:H}\in\mathbb{R}^{H\times D}.
$$

SpikF 包含三个组件：

$$
\text{continuous series}
\rightarrow
\text{SPE}
\rightarrow
\text{SFS feature extraction}
\rightarrow
\text{MLP Decoder}
\rightarrow
\text{continuous forecast}.
$$

SPE 负责 local patch-level encoding；SFS 负责 grouped S-FFT、learned frequency selector 和 S-iFFT；decoder 负责把 spike groups 映射回连续预测。模型采用 LIF neurons 和 surrogate-gradient STBP 训练，不是 ANN-to-SNN conversion。

## 4. Key Components and Mechanisms

### 4.1 LIF、SNN receptive field 与 Fourier external dynamics

论文使用的 LIF update 为：

$$
U[t]=V[t-1]+\frac{1}{\tau_m}\left(I[t]-V[t-1]+V_{\mathrm{rest}}\right),
$$

$$
S[t]=H(U[t]-V_{\mathrm{th}}),
$$

$$
V[t]=U[t](1-S[t])+V_{\mathrm{rest}}S[t],
$$

其中 $U[t]$ 是发放判断前的 membrane potential，$V[t]$ 是 reset 后的状态，$I[t]$ 是输入 current，$\tau_m$ 是 membrane time constant，$V_{\mathrm{rest}}$ 是 resting potential，$V_{\mathrm{th}}$ 是 threshold。突触 current 为：

$$
I[t]=WS^{\mathrm{pre}}[t].
$$

由于 hard reset，若两个不同刺激序列在 $t^*$ 前均没有发放、并在 $t^*$ 发放，则 $V[t^*]=V_{\mathrm{rest}}$，后续状态可能无法区分 reset 前的不同刺激。若 spike 发生在 $t_1,t_2,\ldots,t_s$，作者将 LIF 的 receptive field 描述为被切分到：

$$
[1,t_1],\ [t_1+1,t_2],\ \ldots,\ [t_{s-1}+1,t_s],\ [t_s+1,T].
$$

因此只依赖内部 membrane dynamics 可能不足以保存长距离依赖。SFS 用 Fourier Transform 建立 external global path：

$$
F[k]=\sum_{t=1}^{T}S[t]e^{-j\frac{2\pi}{T}kt}.
$$

每个 $F[k]$ 依赖整个 sequence；rotation factor 随时间位置 $t$ 改变，因此序列置换通常会改变 frequency coefficient。

### 4.2 Spiking Patch Encoder

输入长度为 $L$ 的序列被划分为 $N$ 个 patch。第 $k$ 个 patch 为：

$$
p_k=x_{\frac{L}{N}(k-1)+1:\frac{L}{N}k}.
$$

每个 patch 通过 shared learnable linear layer、BN 和 spiking neuron：

$$
S_{\mathrm{enc}}^{T_s(k-1)+1:T_sk}
=
\operatorname{SN}\left(\operatorname{BN}\left(\operatorname{LN}(p_k)\right)\right).
$$

这里 $T_s$ 是 temporal upsampling factor。作者使用 zero-order hold（ZOH）提高 patch 的时间分辨率，然后将其作为 LIF input current，输出 binary spike train。所有 patch 使用 shared encoder，以较少参数处理不同时间位置的局部子序列。

### 4.3 Spiking Frequency Selector

SPE 输出按固定间隔组成 $g$ 个 group：

$$
G_i=\left\{S_{\mathrm{enc}}^i,S_{\mathrm{enc}}^{i+g},\ldots,S_{\mathrm{enc}}^{i+(\frac{NT_s}{g}-1)g}\right\}.
$$

每个 group 经过两条并行路径。第一条进行 grouped S-FFT：

$$
F^i=\operatorname{SF}_g(G_i).
$$

第二条使用 linear projection、BN 和 spiking neuron 生成 selector：

$$
M_{\mathrm{sel}}^i
=
\operatorname{SN}\left(\operatorname{BN}\left(\operatorname{LN}(G_i)\right)\right).
$$

多个 group 的 selector 通过 spiking max-pooling 合并：

$$
M_{\mathrm{sel}}
=
\operatorname{SMP}(M_{\mathrm{sel}}^1,M_{\mathrm{sel}}^2,\ldots,M_{\mathrm{sel}}^g).
$$

然后用 Hadamard product 对频谱进行逐元素选择，并通过 grouped S-iFFT 返回时域：

$$
H_F^i
=
\operatorname{SF}^{-1}_g(M_{\mathrm{sel}}\odot F^i).
$$

最终的时域结果再次进入 BN 和 spiking neuron：

$$
S_F^i=\operatorname{SN}\left(\operatorname{BN}(H_F^i)\right).
$$

其中 $F^i$ 提供每个 frequency component 的内容，$M_{\mathrm{sel}}$ 决定保留或抑制哪些 component，S-iFFT 将被选择的全局频率结构重新分配到时域。论文声称 selector 利用 spike binary nature 动态学习频率，而不是像 FEDformer 或 FITS 那样使用固定/random modes 或人工 cutoff。当前论文没有在正文明确展开 complex representation、selector 与频谱的精确 broadcasting 规则，属于 `Needs further check`。

### 4.4 MLP Decoder 与 temporal synchronization

直接用 full-receptive-field MLP 解码高 temporal-resolution spike train 会增加参数和计算。作者先对 prediction target 做 temporal upsampling，使其时间尺度与 spiking patches 对齐；再把 spikes 和 target 划分为 $T_s$ 个 group，每个 spike group 使用共享 MLP 解码。

训练 loss 为：

$$
\mathcal{L}
=
\frac{1}{T_s}
\sum_{k=1}^{T_s}
\left\|\operatorname{MLP}(S^k)-Y\right\|.
$$

推理时将各 group 的输出平均并下采样：

$$
\hat{Y}
=
\frac{1}{T_s}
\sum_{k=1}^{T_s}\operatorname{MLP}(S^k).
$$

论文没有在该公式处明确说明范数是 MAE、MSE 还是其他 norm；实验中 SpikF 使用 MAE loss，但公式本身需结合实现解释。`Needs further check`

### 4.5 Fourier、FFT 和 S-FFT

长度为 $N$ 的 DFT 将 time-domain sequence $x[n]$ 变为 frequency-domain coefficients $X[k]$：

$$
X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}.
$$

每个 $X[k]$ 是一个复数，包含该 frequency bin 的 amplitude 和 phase；inverse DFT 为：

$$
x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}.
$$

FFT 是用 $O(N\log N)$ 的分解算法计算同一 DFT 结果。S-FFT 则试图把 FFT 的 real-number multiplication 转化为 inter-synaptic spike transitions，把 addition 转化为 presynaptic stimulation accumulation，从而利用 spike sparsity。

### 4.6 LIF 以外的 Fourier-capable SNN 方向

已有工作将 Fourier matrix multiplication 分解为多个 linear transformations，再用 spiking linear layers 近似执行这些矩阵变换；另一类工作使用 Resonate-and-Fire neuron 的内部振荡，使不同 neuron 对不同 resonance frequency 产生选择性响应。两个状态 $u[t],v[t]$ 可以写成：

$$
z[t]=u[t]+jv[t].
$$

这是一种把二维状态表示为复数的紧凑形式，可同时记录振幅和相位。若 RF neuron 的内部 resonance frequency $\omega_0$ 接近输入频率 $\omega$，输入与内部旋转相位更一致，贡献相加；若频率不匹配，相位逐步错开，贡献部分抵消。不同的 $\omega_0$ 可以构成不同频率通道。SpikF 当前方法采用 S-FFT/S-iFFT，并没有证据表明它使用 RF neuron。

## 5. Experiments and Main Evidence

作者使用 ECL、Weather、ETTh1、ETTh2、ETTm1、ETTm2、Traffic 和 Exchange 八个长期预测数据集，主要将 look-back window 固定为 96；Solar-energy 短期预测使用 128。长期预测指标为 MAE 和 MSE，短期预测使用 RSE。比较对象包括 Transformer-based、TCN-based 和 linear-based models。

SpikF 相比 iTransformer 平均降低 1.9% MAE，在 ETTm1 上降低 6.1%。在额外 FFT/SNN benchmark 中，SpikF 相比第二好的 SNN model，MSE/MAE 分别改善 1.4%/0.7%；相比第二好的 FFT-based model，分别改善 3.4%/3.6%。这些结果部分使用其他工作报告的 baseline，不能完全等同于所有模型在同一代码和训练预算下重训。

能效方面，SFS 相比 DLinear 的 time-domain linear transform 降低 42.66% operational energy；ECL 上 $T_s=4$ 时，SpikF 相比 iTransformer 降低 75.05% operational energy。更完整的 ACE 和 total energy 比较中，SpikF 分别低 6.27 倍和 3.16 倍。这里包含 operational、memory-access 和 addressing energy 的估算，不是实际芯片功耗测量。

消融结果为：SPE 相比 Delta Encoder 和 Convolutional Encoder 分别改善 6.6% 和 3.2%；SFS 比 iSSA 改善 1.6%；temporal synchronization 带来 0.5% 提升。改变 $T_s\in\{1,2,4,8,16\}$ 时，平均性能变化为 3.7%；patch dimension 在 ${4,8,16,32}$ 上平均变化为 1.2%。从 look-back 48 增加到 720 时，MSE 平均改善 9.0%，MAE 平均改善 2.4%。

图 7 的 shuffle test 中，SpikF 在输入保持有序时比 uniformly shuffled input 的 MAE 好 0.8%，而 iTransformer 没有性能改善，支持 SFS 对 temporal order 的利用。图 6、图 10 和图 11 的 selector visualizations 说明模型会选择不同 frequency bins，并且 shared selector 能够利用多变量之间的共同频率结构；但这些图是 selection probability，不等于直接的 physical-Hz amplitude spectrum。

## 6. Strengths and Limitations

本文的优势是把 long-term forecasting 引入 SNN benchmark，并将 patch encoding、SNN dynamics、Fourier global receptive field 和 frequency selection 结合起来。它保留了 spike-driven computation 的目标，同时避免依赖标准 self-attention。SFS 的 frequency selection 是输入依赖的，shared generator 也适合 multivariate series 的共同模式。

局限包括：S-FFT/S-iFFT 的 exact complex implementation、selector shape 和 broadcasting 在正文中不够透明；SOP/energy 是基于参考硬件和 firing-rate 假设的 proxy，不能替代真实硬件测量。decoder 的 loss norm 在公式中未明确；若不同 group 的误差相关，average pooling 的理论收益会低于独立误差假设。不同 baseline 部分来自已有论文，训练 loss、代码和预算未必完全一致。本文处理的是普通 multivariate time series，不是 raw event stream；其 Fourier coupling 尚未证明可以直接迁移到 Event Cloud 或 asynchronous event-level SNN。

## 7. Relation to SECNet Extension Direction

SpikF 对 SECNet extension 的主要启发是：可以把 frequency-domain global path 作为 SNN temporal dynamics 的补充，使 local spike state 不必独立承担全部 long-range dependency。对于 Event Cloud，不能直接把 SpikF 的一维 patch 和 time-series S-FFT 原样移植，因为 event input 具有 $(x,y,t,p)$ 的稀疏时空结构；需要研究 event-level 或 spatiotemporal grouping 如何定义 Fourier axes，并区分 spatial、temporal 和 joint spatiotemporal frequency。

其可迁移部分包括：用可学习 selector 动态选择频率、用 shared generator 建模跨变量或跨通道共同结构、将 selected frequency representation 回投到 spike-compatible temporal state。其边界包括：论文的 S-FFT 假设规则序列和固定长度 group，且 energy model 假设可以利用 zero-spike sparsity；这些假设在 irregular Event Cloud、极端稀疏事件和异步硬件上需要重新验证。对 SECNet，SpikF 更适合作为 SNN-Fourier coupling 的机制参考和实验假设，而不是现成的 Event Cloud interface。

## 8. Survey-Usable Takeaways

- SpikF 将 SNN 长序列问题拆成两个层次：SPE 负责降低长历史 encoding 的计算负担，SFS 负责补充 LIF reset 和局部 receptive field 对 long-range dependency 的限制。
- Fourier Transform 同时提供 global aggregation 和 phase-based order sensitivity，但它不是普通 positional embedding 的完全等价替代；是否能保留顺序必须通过 shuffle test 或其他 position-sensitive evaluation 验证。
- S-FFT 的效率依赖 spike firing rate 和硬件是否真的跳过 zero spike。SOP、ACE 和 theoretical energy estimate 必须与 memory access、addressing 和 state communication 区分报告。
- SpikF 的 selector 是 input-dependent 的，而不是固定 cutoff；但正文没有完全展开 selector 与 complex spectrum 的 tensor interface，复现时需要代码核查。
- 对 event-camera 方向，本文提供 SNN-side Fourier coupling foundation，但普通规则 time series 与 raw Event Cloud 的 sampling、axis、sparsity 和 phase semantics 不同，不能直接把结果当作 event-side evidence。

## Supplement Points

### Questions and Clarifications

#### 1. FFT 是从什么得到什么？

FFT 的输入是一段按时间排列的 signal values：

$$
x=[x_0,x_1,\ldots,x_{N-1}].
$$

输出是 frequency-domain coefficients：

$$
X=[X_0,X_1,\ldots,X_{N-1}].
$$

时域 $x[n]$ 回答“第 $n$ 个时间点的值是多少”；频域 $X[k]$ 回答“第 $k$ 个 frequency bin 的振荡成分有多强、相位是什么”。FFT 不创造新信息，而是把同一信号换一种表示。FFT 与 DFT 的数学结果相同，区别是 FFT 用 even/odd decomposition 和 butterfly 将直接 $O(N^2)$ 计算降为约 $O(N\log N)$。

DFT 为：

$$
X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}.
$$

每个 $X[k]$ 通常是复数：

$$
X[k]=\operatorname{Re}(X[k])+j\operatorname{Im}(X[k]).
$$

幅值和相位分别为：

$$
|X[k]|=\sqrt{\operatorname{Re}(X[k])^2+\operatorname{Im}(X[k])^2},
$$

$$
\phi_k=\operatorname{atan2}(\operatorname{Im}(X[k]),\operatorname{Re}(X[k])).
$$

iFFT 为：

$$
x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}.
$$

如果对频谱做 mask：

$$
\widetilde X[k]=M[k]X[k],
$$

再做 iFFT，就得到只包含被选择频率的新时域信号。这正是 SFS 中 $G_i\rightarrow F^i\rightarrow M_{\mathrm{sel}}\odot F^i\rightarrow H_F^i$ 的含义。

#### 2. 为什么两个 RF states 可以组成复数？为什么 RF neuron 对接近 $\omega_0$ 的输入响应更强？

两个状态：

$$
z[t]=u[t]+jv[t]
$$

可以看成复平面上的二维点。其模长表示响应强度，其 argument 表示相位。Fourier coefficient 本身也由 cosine correlation 和 sine correlation 两部分构成，因此天然是复数：

$$
X[k]=\sum_t x[t]\cos(2\pi kt/N)-j\sum_t x[t]\sin(2\pi kt/N).
$$

RF neuron 的内部 dynamics 可以近似包含旋转：

$$
z[t+1]=\rho e^{j\omega_0}z[t]+bI[t].
$$

若输入频率是 $\omega$，在 neuron 的内部旋转坐标中会出现相位差项：

$$
e^{j(\omega-\omega_0)t}.
$$

当 $\omega\approx\omega_0$ 时，该项变化慢，各时间步贡献方向相近，能够相加增强；当差距较大时，向量方向不断旋转，累加出现抵消。因此 RF neuron 像一个具有固有频率的 resonator。SpikF 当前论文没有使用 RF neuron，也没有给出 $\omega_0$ 的来源；它使用的是 S-FFT/S-iFFT。

#### 3. Spike train、global receptive field 和 temporal synchronization 是什么？

Spike train 是离散时间上的 binary sequence，例如：

$$
S=[0,0,1,0,1,0,0,1].
$$

其中 1 表示该 timestep 发放，0 表示没有发放。稀疏 spike train 中大部分位置为 0，若硬件支持 event-driven skip，就可能降低后续计算。

S-FFT 的 global receptive field 来自：

$$
F[k]=\sum_tS[t]e^{-j2\pi kt/T}.
$$

每个 $F[k]$ 都使用整个 group 的所有时间位置；某一个输入位置的改变会影响多个 frequency coefficients，mask 后再 iFFT 又会影响多个时域位置。因此它能把远距离时间点连接起来。rotation factor 随 $t$ 改变，所以顺序打乱通常会改变 $F[k]$，这与 permutation-invariant self-attention 不同。

Temporal synchronization 是把 target 的 temporal resolution 调整到 spiking patch representation 的时间尺度。若一个 patch 被展开成 $T_s$ 个 spike steps，而 prediction target 仍是较低分辨率，就先上采样 target，再让 spike groups 和 target 在相同时间粒度下计算 decoder loss。推理时各 group 通过共享 MLP 产生预测，再平均并下采样。

#### 4. 公式（9）–（11）和 selector 的维度如何理解？

把一个 group 抽象为：

$$
G_i\in\mathbb{R}^{B\times Q\times C},
$$

其中 $B$ 是 batch size，$Q$ 是 group 内的 patch/time positions，$C$ 是 feature dimension。S-FFT 沿 group 的 sequence axis 产生：

$$
F^i\in\mathbb{C}^{B\times Q\times C}.
$$

selector path 先做 linear projection：

$$
Z_i=G_iW_{\mathrm{sel}}^\top+b,
$$

再经过 BN 和 SN：

$$
M_{\mathrm{sel}}^i=\operatorname{SN}(\operatorname{BN}(Z_i)).
$$

如果 selector 已经被设计为与频谱逐元素对齐，它可以写成与 $F^i$ 相同或可 broadcast 的 shape，并执行：

$$
\widetilde F^i=M_{\mathrm{sel}}\odot F^i.
$$

selector 为 0 的位置抑制对应 frequency component，为 1 或较大的位置保留它。随后：

$$
H_F^i=\operatorname{SF}^{-1}_g(\widetilde F^i).
$$

但是，正文没有明确给出 complex real/imaginary channel 如何编码、$M_{\mathrm{sel}}$ 是否沿 group 广播、以及 $W_{\mathrm{sel}}$ 的确切输出维度。因此，上述维度是理解数据流的抽象表示，精确 implementation 需要代码核查，属于 `Needs further check`。

#### 5. 公式（15）和（16）如何理解？

论文用 firing rate $\alpha$ 表示输入位置发放 spike 的概率，用：

$$
\beta=1-\alpha
$$

表示 non-spiking ratio。若一个长度为 $q$ 的 block 中每个位置独立发放，则整个 block 为零的概率为：

$$
\beta^q,
$$

至少有一个 spike 的概率为：

$$
1-\beta^q.
$$

经典 FFT 每一层把序列拆成 even/odd，再用 butterfly 合并。一个 complex addition 计为 2 SOPs，一个 complex multiplication 计为 6 SOPs。第 $k$ 个 merge level 中，作者令：

$$
q_k=m\times2^{k-1}.
$$

当 even、odd 都非零时，执行完整的 complex multiplication 和 addition/subtraction，期望成本写成：

$$
8(1-\beta^{q_k})^2.
$$

当 odd 非零、even 为零时，只执行 complex multiplication，期望成本写成：

$$
6\beta^{q_k}(1-\beta^{q_k}).
$$

两个都为零时跳过计算。累加所有 $n$ 个 merge levels，再加上长度为 $m$ 的 base-case S-DFT：

$$
\operatorname{SOPs}(\mathrm{S\text{-}FFT})
=
\sum_{k=1}^{n}L\left[8(1-\beta^{m2^{k-1}})^2+6\beta^{m2^{k-1}}(1-\beta^{m2^{k-1}})\right]
+L(2m\alpha-2+2\beta^m).
$$

base case 的意思是：当输入长度 $L=m2^n$ 被反复二分后，递归停止在长度 $m$ 的小段，对每个小段执行直接 S-DFT。公式中的 $P_k$ 是一个长度为 $m$ 的 group 中恰有 $k$ 个 spike 的概率：

$$
P_k=\binom{m}{k}\alpha^k\beta^{m-k}.
$$

论文的 base-case expected cost 是：

$$
\sum_{k=1}^{m}2\times2^n\times m(k-1)P_k
=L(2m\alpha-2+2\beta^m).
$$

它表示对所有可能 spike count 按概率加权后的平均 S-DFT 成本，而不是普通 dense DFT 的固定 FLOPs。

S-iFFT 的成本为：

$$
\operatorname{SOPs}(\mathrm{S\text{-}iFFT})
=\operatorname{SOPs}(\mathrm{S\text{-}FFT})+6Lm\alpha.
$$

额外项来自 inverse transform 中非零 input 与 rotation factor 的 complex multiplication。复数乘法：

$$
(a+jb)(c+jd)=(ac-bd)+j(ad+bc)
$$

需要 4 次 real multiplication 和 2 次 real addition，因此按 6 SOPs 计。作者估计参与该项的非零输入数量约为 $Lm\alpha$，所以额外成本是 $6Lm\alpha$。这个数量依赖作者的 S-iFFT implementation 和稀疏统计假设，不是任意 iFFT 的普适公式。

#### 6. 图 6 怎么看？为什么论文说浅层选择有用频率、深层丢弃更多或保留更多？

图 6 的横轴是 frequency-bin index，纵轴是 feature dimension，颜色表示 selection probability。深紫色表示较低选择倾向，浅色表示较高选择倾向；虚线框标出作者关注的 noise frequencies 或 key frequencies。它不是原始 Fourier amplitude 图，也不能仅凭横轴数字直接推断 physical Hz。

浅层 SFS 接收更接近原始输入的 spike feature，可能同时包含有效模式和噪声，因此承担初步筛选。后续 SFS 接收经过处理的 feature，可以在较干净的候选频率中重新组合。作者同时使用“深层丢弃更多”和“去噪后更倾向保留更多”的表述；这可能分别指整体 selection rate 与剩余候选中的相对保留比例，但图注没有给出足够统计定义，不能把两句话当作无歧义的定量结论。

#### 7. Spiking Frequency Selector 如何利用 positional information 和 global receptive field？

SFS 使用：

$$
F[k]=\sum_{t=1}^{T}S[t]e^{-j\frac{2\pi}{T}kt}.
$$

所有时间位置都参与同一个 frequency coefficient，因此 $F[k]$ 具有全局依赖；而每个位置的 rotation factor 不同，因此交换时间位置会改变相位加权后的结果。selector 再通过：

$$
M_{\mathrm{sel}}\odot F^i
$$

选择频率，S-iFFT 将这种全局频率修改传播回多个时间位置。它不是显式的 $X[t]+P[t]$ positional embedding，而是将 position information 隐式编码到 Fourier phase 和 frequency coefficients 中。

#### 8. temporal synchronization 中 target 如何上采样、分组、计算 loss 并推理？

核心是：作者把每一个原始预测时间点复制成 $T_s$ 个更细的时间位置，让 spike 的时间分辨率和 prediction target 的时间分辨率一致；训练时每一个 spike group 都单独预测一次，推理时再把这些预测平均起来。

例如，假设预测未来 3 个时间点：

$$
Y=[10,20,30].
$$

若 $T_s=2$，可以先把每个目标值重复两次，得到上采样目标：

$$
Y_{\mathrm{up}}=[10,10,20,20,30,30].
$$

这不是说未来真的增加了 3 个时间点，而是把每个原始时间点展开成两个更细的子时间位置。将其按 phase 分成两个 group 后：

$$
Y^1=[10,20,30],
$$
$$
Y^2=[10,20,30].
$$

与此同时，假设经过 SPE 和 SFS 得到长度为 6 的 spike 序列：

$$
S=[1,0,0,1,1,1].
$$

按两个 phase 拆分为：

$$
S^1=[1,0,1],
$$
$$
S^2=[0,1,1].
$$

如果每个 spike 位置实际是 $C$ 维 feature vector，则可以抽象为 $S^k\in\{0,1\}^{H\times C}$，其中 $H$ 是 prediction length，$C$ 是 feature dimension，$k$ 表示第 $k$ 个 temporal phase。每个 group 使用同一个 shared MLP，分别得到：

$$
\hat Y^1=\operatorname{MLP}(S^1)=[9,21,29],
$$
$$
\hat Y^2=\operatorname{MLP}(S^2)=[11,18,32].
$$

训练时两个 group 都与同一个原始目标 $Y=[10,20,30]$ 比较。若用 MAE 理解公式（13），则：

$$
\operatorname{MAE}(\hat Y^1,Y)=\frac{|9-10|+|21-20|+|29-30|}{3}=1,
$$
$$
\operatorname{MAE}(\hat Y^2,Y)=\frac{|11-10|+|18-20|+|32-30|}{3}=\frac{5}{3}.
$$

总 loss 为：

$$
\mathcal L=\frac{1}{T_s}\sum_{k=1}^{T_s}\left\|\hat Y^k-Y\right\|=\frac{1}{2}\left(1+\frac{5}{3}\right)=\frac{4}{3}.
$$

也就是说，训练时不是只监督最后的平均预测，而是让每一个 phase group 都具备独立预测未来序列的能力。推理时才将各个 group 的预测逐元素平均：

$$
\hat Y=\frac{1}{T_s}\sum_{k=1}^{T_s}\hat Y^k=\frac{1}{2}([9,21,29]+[11,18,32])=[10,19.5,30.5].
$$

此时最终 MAE 为：

$$
\operatorname{MAE}(\hat Y,Y)=\frac{|10-10|+|19.5-20|+|30.5-30|}{3}=\frac{1}{3}.
$$
