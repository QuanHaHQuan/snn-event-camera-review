---
tags: [SNN, spiking-transformer, frequency-domain, high-frequency-information, neuromorphic-computing]
---

# Summary V2｜Spiking Neural Networks Need High-Frequency Information

## 1. Core Understanding

本文挑战了“ SNN 与 ANN 的性能差距主要来自二值 spike 的 representation error”这一常见解释。作者提出，SNN 的另一个更根本的限制是 frequency bias：脉冲神经元在网络级信息传播中倾向于保留 low-frequency information，同时快速衰减 high-frequency components，而 high-frequency details 对边缘、纹理和细粒度视觉表示很重要。

作者从 LIF 的 membrane charging dynamics 出发，用 Z-transform 推导出一阶 IIR low-pass transfer function，并进一步说明该低通项在多层级联后会累积。需要区分的是，尖锐的 spike waveform 本身会在频谱中制造宽频谐波，但这些波形诱导的高频不等于输入高频信息被有效保留；经过 weighting 和后续膜电位积分后，高频仍然难以跨层传播。

基于这一诊断，作者提出 Max-Former 和 Max-ResNet，用 Max-Pool 与 Depth-Wise Convolution（DWC）在早期阶段恢复局部高频细节，同时在后期保留 Spiking Self-Attention（SSA）以建模更全局的信息。实验覆盖静态图像、神经形态事件数据、Transformer 和 convolutional SNN，结果支持“高频传播是 SNN 表示能力的重要限制因素”这一设计假设。

## 2. Problem and Motivation

现有 SNN 工作常把性能不足归因于 sparse/binary activation，然而低 bit 或 binary ANN 并不总是存在同等严重的性能问题，且跨多个 simulation timesteps 的 spike train 仍可表达比单步 binary activation 更高的精度。作者因此转而研究 frequency-domain behavior。

LIF 的膜电位会对过去状态进行积分和衰减。缓慢变化的输入更容易在膜电位中持续累积，快速变化的输入则更容易被平滑或抵消。作者认为，这种 temporal low-pass tendency 在网络深度增加后可能导致 high-frequency local details 快速消失。直接把 ANN Transformer 的 Avg-Pooling 或 self-attention 设计移植到 SNN，可能进一步加剧这一问题。

本文的问题是：SNN 是否在网络级天然抑制高频？如果是，增加高频保留操作能否在不增加大量参数和计算的情况下改善 SNN 的表示和准确率？

## 3. Method Overview

作者先分析 LIF 的充电过程。论文使用的离散 LIF update 为：

$$
U[n]=\beta V[n-1]+(1-\beta)I[n],
$$

其中 $I[n]$ 是当前输入电流，$V[n-1]$ 是上一时刻 reset 后的 membrane potential，$U[n]$ 是当前发放判断前的 membrane potential，$\beta$ 是 decay factor。发放和 soft reset 为：

$$
S[n]=H(U[n]-V_{\mathrm{th}}),
$$

$$
V[n]=
\begin{cases}
U[n]-V_{\mathrm{th}}, & S[n]=1,\\
U[n], & S[n]=0.
\end{cases}
$$

对充电式递推进行 Z-transform，得到：

$$
H(z)=\frac{V(z)}{I(z)}=\frac{1-\beta}{1-\beta z^{-1}},
\qquad 0\leq\beta<1.
$$

该式是一阶 IIR low-pass filter。若在阈值附近将非线性 spike generation 以 firing-rate gain $k$ 局部线性化，并令 spike 经过 causal synaptic kernel $w[n]$，则单层 input-to-output transfer function 近似为：

$$
k=\left.\frac{\partial f_r}{\partial V}\right|_{V=V_{\mathrm{th}}},
\qquad S(z)\approx kV(z),
$$

$$
y[n]=w[n]*s[n],
\qquad Y(z)=W(z)S(z),
$$

$$
H'(z)=\frac{Y(z)}{I(z)}
\approx kW(z)\frac{1-\beta}{1-\beta z^{-1}}.
$$

经过 $L$ 层级联后：

$$
H'_L(z)=\frac{Y_L(z)}{I(z)}
=\left(\prod_{i=1}^{L}k_iW_i(z)\right)
\left(\frac{1-\beta}{1-\beta z^{-1}}\right)^L.
$$

无泄漏 IF 的充电过程为 $V[n]=V[n-1]+I[n]$，对应：

$$
H(z)=\frac{1}{1-z^{-1}},
$$

即离散积分器，仍然偏向长期累积和低频变化。该结论是在阈值、reset 和局部线性化假设下的分析，不是对任意训练后 SNN 的完整精确线性描述。

## 4. Key Components and Mechanisms

### 4.1 Frequency interpretation of spiking neurons

作者用输入 $x(t)=\frac{1}{3}[\sin(2\pi100t)+\sin(2\pi200t)+\sin(2\pi300t)]$ 对 ReLU 和 LIF 做时频比较。ReLU 截断负值，会改变波形并扩展频率带宽；LIF 输出是尖锐 spike，单独观察其频谱时会出现大量高频谐波。但这些高频可能由 spike 的尖锐 waveform 产生，而不是输入中的对应高频被独立保留。

图 3 的三个面板形成一条链：图 3(a) 看 time-domain activation，图 3(b) 看 activation 本身的 Fourier spectrum，图 3(c) 看 activation 经过 CONV/MLP 等 linear weighting 后的 spectrum。图 3(b) 中 spike 频谱看起来很宽，不足以证明高频信息被传播；图 3(c) 中高频随后续处理衰减，才支持 network-level low-pass interpretation。

### 4.2 Max-Former input and hierarchical stages

Max-Former 有三个阶段，token resolution 分别为 $H/4\times W/4$、$H/8\times W/8$ 和 $H/16\times W/16$。它支持两类输入。事件 $e=[x,y,t,p]$ 通过 temporal binning 聚合：

$$
I_t=\sum_{k=\alpha t}^{\alpha(t+1)-1}S_k\in\mathbb{R}^{2\times h\times w},
$$

其中 $S_k$ 是原始事件数据，$\alpha$ 控制原始和目标 temporal resolution。静态图像则重复 $T$ 次，再通过 spiking embedding 编码为 spike sequence：

$$
I=\operatorname{Spiking\_Embed}(\{I_t\}_{t=1}^{T}).
$$

### 4.3 Patch embedding and high-frequency restoration

输入 spike tensor 为 $\{S\}\in\mathbb{R}^{T\times C\times H\times W}$，patch embedding 为：

$$
Y=G_1(\{S\})+G_2(\{S\}),
\qquad Y\in\mathbb{R}^{T\times C'\times H'\times W'},
$$

$$
C'=2C,\qquad H'=\left\lfloor\frac{H}{P}\right\rfloor,\qquad W'=\left\lfloor\frac{W}{P}\right\rfloor,
\qquad P=4.
$$

三种配置为：

$$
(G_1,G_2)=(\operatorname{Embed},\operatorname{Embed}),
$$

$$
(G_1,G_2)=(\operatorname{Max\text{-}Embed},\operatorname{Embed}),
$$

$$
(G_1,G_2)=(\operatorname{Max\text{-}Embed},\operatorname{Max\text{-}Embed}),
$$

其中：

$$
\operatorname{Embed}=\{\operatorname{LIF}-\operatorname{CONV}-\operatorname{BN}\},
$$

$$
\operatorname{Max\text{-}Embed}=\{\operatorname{LIF}-\operatorname{CONV}-\operatorname{BN}-\operatorname{MaxPool}\}.
$$

Max-Pool 在局部窗口中保留较强响应，有助于保留边缘和纹理，但它不是严格的线性 high-pass filter；论文对它的“frequency-enhancing”解释是功能性和经验性的。

### 4.4 Token mixing

作者在早期阶段以 DWC 替代 SSA。给定 $Y\in\mathbb{R}^{T\times C\times H\times W}$，每个 channel 的 spiking DWC 为：

$$
Z_c(Y)[i]=\operatorname{LIF}\left(\sum_{j\in\Omega(i)}w_{c,j}\cdot Y_c[j]\right).
$$

其中 $\Omega(i)$ 是位置 $i$ 的局部邻域。固定局部 kernel 使 DWC 的计算随 token 数量近似线性，而 self-attention 的 token-to-token interaction 通常具有二次复杂度。DWC-3 在实验中比 DWC-1 更能进行局部空间混合，又比 DWC-5/7 少引入过度平滑。

最后阶段仍使用 SSA：

$$
Z=\operatorname{LIF}(\operatorname{BN}(YW)),
\qquad Z\in\{Q,K,V\},
$$

$$
\operatorname{SSA}(Q,K,V)=\operatorname{LIF}(QK^TV\cdot s).
$$

因此设计遵循“早期局部高频、后期全局语义”的层级分工，而不是在所有阶段都使用同一种 mixing operator。

### 4.5 Membrane Shortcut

本文比较 Vanilla、Pre-Spike 和 Membrane Shortcut。Vanilla 将 binary spike 直接接到 continuous membrane potential，存在表示分布不匹配；Pre-Spike 将 spike 相加后可能产生 $\{0,1,2\}$ 的 ternary transmission，破坏标准 binary spike flow。Membrane Shortcut 在 membrane space 进行残差融合，再由 LIF 输出 binary spike，兼顾 identity mapping 和 spike-driven computation，也更适合作为公平比较的 shortcut 方案。

## 5. Experiments and Main Evidence

作者在 CIFAR-10、CIFAR-100、ImageNet、CIFAR10-DVS 和 DVS128 Gesture 上评估 Max-Former，并用 Max-ResNet 检验卷积架构的通用性。

在 CIFAR-10，Max-Former 在 $T=4$ 下达到 97.04%，使用 6.57M 参数，超过 Spikformer 的 95.51%、S-Transformer 的 95.60% 和 QKFormer 的 96.18%。CIFAR-100 上达到 82.65%，高于 Spikformer 78.21%、S-Transformer 78.40% 和 QKFormer 81.57%。与使用相同训练设置和 Membrane Shortcut 的 MS-QKFormer 比较，Max-Former 在 CIFAR-10/CIFAR-100 分别高 0.20/1.08 个百分点，且参数略少。

在 DVS128 Gesture 上达到 98.6%；在 CIFAR10-DVS 上达到 84.2%，比 MS-QKFormer 高 1.9 个百分点。这说明高频恢复在事件帧式神经形态输入上也有帮助，但本文仍先通过 temporal binning 形成输入帧，不能直接等同于 fully asynchronous event-level processing。

ImageNet 上，Max-Former-10-768 在 $T=4$ 达到 82.39%，使用 63.99M 参数；论文报告其相比 Spikformer 74.81%、66.34M 参数高 7.58 个百分点，并在采用的 theoretical energy model 下从 21.48 mJ 降至 14.87 mJ，约低 30%。该能耗是 SOP/MAC/AC proxy，不是完整真实芯片测量。Max-Former-10-384 达到 77.82%，能耗 4.89 mJ，低于 MS-QKFormer 的 5.52 mJ、S-Transformer 的 6.10 mJ 和 Meta-Spikformer 的 32.8 mJ。

消融实验显示，去掉 patch embedding 中的 Max-Pool 会使 CIFAR-100 从 82.65% 降至 81.63%，CIFAR10-DVS 从 84.2% 降至 81.5%。全 SSA 在 CIFAR-100 为 82.23%，早期使用 DWC 的 Max-Former 为 82.65%；CIFAR10-DVS 上 DWC-3+SSA 为 84.2%，全 SSA 为 83.9%。DWC-5/7 由于过度平滑而下降，DWC-1 则局部过滤不足。这些结果支持“频率平衡”而非“高频越多越好”。

在 Max-ResNet 中，仅增加两个 Max-Pool、保持模型规模不变，也能相对 MS-ResNet 提升：block configuration $[2,2,2,2]$ 在 CIFAR-10 从 94.4% 到 96.81%，CIFAR-100 提升 6.48 个百分点；$[3,3,2]$ 在 CIFAR-10/CIFAR-100 分别提升 2.25/6.65 个百分点。该跨架构结果支持高频恢复不是 Spiking Transformer 特有现象，但仍不能证明所有性能增益只来自频率，而不受局部归纳偏置、下采样和优化变化影响。

理论能耗使用：

$$
\operatorname{SOPs}(l)=f_r\times T\times\operatorname{FLOPs}(l),
$$

其中 $f_r$ 是 layer 的 input spike firing rate。若第一层把连续静态图像转换为 spike，则用 MAC energy；后续 spike layers 用 AC energy。取文献芯片参考值 $E_{\mathrm{MAC}}=4.6$ pJ、$E_{\mathrm{AC}}=0.9$ pJ：

$$
E_{\mathrm{SNN}}=E_{\mathrm{MAC}}\times\operatorname{FLOP}^{1}_{\mathrm{CONV}}+E_{\mathrm{AC}}\times\left(\sum_{n=2}^{N}\operatorname{SOP}^{n}_{\mathrm{SNN\ Conv}}+\sum_{j=1}^{M}\operatorname{SOP}^{j}_{\mathrm{SNN\ FC}}\right).
$$

非脉冲 ANN 估算为：

$$
E_{\mathrm{ANN}}=E_{\mathrm{MAC}}\times\operatorname{FLOPs}.
$$

BN 在部署时可与卷积融合，因此没有单独计入。该估算没有完整覆盖 memory access、routing、membrane-state communication 和控制逻辑。

## 6. Strengths and Limitations

本文的优点是把 SNN 的性能差距从单纯 binary representation 问题扩展到 frequency-domain information flow，并用解析推导、patch/token-mixing 消融、跨数据集和跨架构结果共同支持这一视角。Max-Former 的修改简单、参数效率较高，且不依赖显式 Fourier module。

主要边界是：LIF transfer-function 分析包含线性化和网络近似；Max-Pool/DWC 同时改变局部归纳偏置、感受野、下采样和优化路径，因此实验不能把全部增益唯一归因于高频恢复。事件数据实验使用 temporal binning，而不是原始异步 event-level network；因此对 fully asynchronous Event Cloud 或 event graph 的迁移仍需验证。能效结论是基于参考芯片 operation estimate，不是真实 hardware measurement。作者还承认手工平衡频率成分需要经验，直接 Fourier/Wavelet learning 可能更系统，但高效 spike-based frequency representation 仍是挑战。

## 7. Relation to SECNet Extension Direction

本文对 SECNet 的直接价值是提供一个可检验的 frequency-aware SNN design principle：SNN 中的 LIF temporal integration 可能削弱高频时空变化，而 Event Cloud 中的局部边缘、短时事件簇和细粒度运动都可能依赖这类信息。Max-Pool 和 DWC 不能直接当作 Event Cloud interface，因为本文事件输入先经过 temporal binning；更直接的迁移方向是研究在 event-level 或 spatiotemporal Event Cloud 上保留高频时空结构的局部 operator，并区分 spatial high frequency、temporal high frequency 与 joint spatiotemporal frequency。

若将该机制与 SNN coupling，必须明确 continuous membrane、binary spike、event timestamp 和 polarity 各自在哪一步交互；不能只把 ANN frequency module 叠加到 SNN 后就假设高频信息已恢复。对于 SECNet，本文最适合作为诊断和设计假设来源：测试不同 temporal leak、local event aggregation、frequency-preserving projection 以及 layer-wise frequency response，而不是直接复用 Max-Former 的图像 patch embedding。当前论文没有证明在 fully asynchronous Event Cloud、event graph 或逐事件预测上仍然成立，因此这一迁移属于待验证扩展。

## 8. Survey-Usable Takeaways

- SNN 的表示能力不能只用 binary/sparse activation 的 representation error 解释；LIF 的 temporal integration 还会造成 network-level frequency bias，使 high-frequency local details 更容易在跨层传播中衰减。
- 读取 SNN 的频率分析时必须区分 spike waveform 的 spectral harmonics 与输入信息中的真实 high-frequency components。单个 spike 的频谱很宽，不等于高频信息已被有效编码并传到下一层。
- 高频恢复应与网络层级匹配：早期阶段使用 Max-Pool 或 DWC 保留边缘、纹理和局部时空变化，后期阶段再使用 SSA 建模更广泛的全局关系；实验不支持“高频越多越好”。
- 本文在 CIFAR10-DVS 和 DVS128 Gesture 上的结果支持高频恢复对事件帧式 SNN 有帮助，但事件先经过 temporal binning，因此不能直接作为 fully asynchronous Event Cloud 或 event-level SNN 的证据。
- 对 SECNet extension，本文提供的是 frequency-aware diagnosis 和可检验设计假设：需要分别测量 spatial、temporal 与 joint spatiotemporal frequency response，并验证 frequency-preserving operator 是否能与 event-level SNN coupling 兼容。
- Max-Pool/DWC 带来的性能增益不能完全归因于频率因素；局部归纳偏置、感受野、下采样和优化路径也同时变化。能效数字属于 SOP/MAC/AC operation estimate，不能替代真实硬件测量。

## Supplement Points

### Questions and Clarifications

#### 1. 图 3、Z-transform 和一阶 IIR low-pass filter 是什么？IF 和 LIF 的公式如何理解？

我一开始不理解图 3，因为它把 time-domain signal、frequency spectrum、neuron dynamics 和后续 weighting 放在了一起。需要区分：图 3(a) 看输入、ReLU output 和 LIF spike 在时间上如何变化；图 3(b) 看这些 activation 本身的 Fourier spectrum；图 3(c) 看 activation 经过 CONV/MLP 或 synaptic weighting 后哪些频率还能继续传播。

输入由三个正弦波组成：

$$
x(t)=\frac{1}{3}\left(\sin(2\pi100t)+\sin(2\pi200t)+\sin(2\pi300t)\right).
$$

ReLU 是 $r(t)=\max(0,x(t))$；LIF 先积累输入到 membrane potential，再在超过 threshold 时发放 spike。spike waveform 很尖，所以单看图 3(b) 的 $|S(f)|$ 会看到很多高频，但这些可能是尖脉冲形状带来的 harmonics，不等于输入 high-frequency information 被保留。图 3(c) 经过 weighting 后，绿色高频逐渐衰减，作者据此强调 network-level low-pass，而不是只看单个 spike 的宽频谱。

IF 的积分过程是：

$$
U[n]=V[n-1]+I[n],
$$

$$
S[n]=H(U[n]-V_{\mathrm{th}}),
$$

$$
V[n]=U[n]-V_{\mathrm{th}}S[n].
$$

LIF 加入 leak：

$$
U[n]=\beta V[n-1]+(1-\beta)I[n],
$$

$$
S[n]=H(U[n]-V_{\mathrm{th}}),
\qquad V[n]=U[n]-V_{\mathrm{th}}S[n].
$$

从连续模型 $\tau\frac{dV}{dt}=-V+I$ 做 Euler 离散化，可得：

$$
V[n]=\left(1-\frac{\Delta t}{\tau}\right)V[n-1]+\frac{\Delta t}{\tau}I[n].
$$

令 $\beta=1-\frac{\Delta t}{\tau}$ 就得到论文使用的形式。$\beta$ 越大，记忆越长、平滑越强、低频偏好越明显；$\beta$ 越小，响应越快。

Z-transform 将递推关系转换为代数关系。对 $V[n-1]$ 有：

$$
\mathcal{Z}\{V[n-1]\}=z^{-1}V(z).
$$

因此：

$$
V(z)=\beta z^{-1}V(z)+(1-\beta)I(z),
$$

$$
H(z)=\frac{V(z)}{I(z)}=\frac{1-\beta}{1-\beta z^{-1}}.
$$

该系统的一次 impulse response 是 $(1-\beta),\beta(1-\beta),\beta^2(1-\beta),\ldots$，因此响应理论上无限延续，称 IIR。它对慢变化信号保留更多、对快速交替信号衰减更多，所以称 low-pass。

#### 2. 理想冲激是什么？脉冲的高度、宽度和面积是什么？

普通矩形脉冲可以用“高度乘宽度”计算面积。若信号高度为 $h$，持续时间为 $w$，则：

$$
A=h\times w.
$$

例如高度 2、宽度 0.5 s 的矩形脉冲面积为 1；高度 10、宽度 0.1 s 的脉冲面积也为 1。面积表示信号强度在时间上的累计量。

让矩形脉冲宽度变成 $\varepsilon$，高度变成 $1/\varepsilon$：

$$
p_{\varepsilon}(t)=
\begin{cases}
1/\varepsilon, & 0\leq t<\varepsilon,\\
0, & \text{otherwise},
\end{cases}
$$

则面积始终是：

$$
\frac{1}{\varepsilon}\times\varepsilon=1.
$$

当 $\varepsilon\to0$ 时，它趋近于理想冲激 $\delta(t)$：宽度趋近 0、高度趋近无穷大，但总面积为 1。它不是现实中可直接制造的无限大信号，而是表示“某一瞬间发生了一次总量为 1 的事件”的数学极限。

单个冲激写作 $\delta(t-t_0)$，表示事件发生在 $t_0$；周期冲激序列为：

$$
s(t)=\sum_{m=-\infty}^{+\infty}\delta(t-mT).
$$

若 $T=10$ ms，则每隔 10 ms 发放一次，基本重复频率为 $f_0=1/T=100$ Hz。

#### 3. 为什么窄脉冲需要更多高频？

低频正弦波变化慢、曲线圆滑；高频正弦波变化快，可以表示短时间尺度的局部变化。一个每隔 10 ms 重复的宽脉冲和窄脉冲都有 $100$ Hz 的基本重复节奏，但窄脉冲的上升沿和下降沿更突然，因此需要加入更多 $200,300,400,\ldots$ Hz 的整数倍 harmonics 来重建尖锐边缘。

这不是说脉冲中存在一组独立的高频事件，而是说：用很多变化速度不同的正弦波叠加，可以把平滑波形塑造成一个短促尖峰。基本频率主要描述“多久重复一次”；更高次谐波主要帮助描述“每个脉冲有多窄、多尖”。

#### 4. 为什么周期冲激序列的频谱出现在 $100,200,300,\ldots$ Hz？

单个理想冲激的 Fourier transform 为：

$$
\mathcal{F}\{\delta(t-t_0)\}=e^{-j2\pi ft_0},
$$

其幅值为 1。周期序列则为：

$$
s(t)=\sum_m\delta(t-mT).
$$

由于它每隔 $T$ 秒重复一次，Fourier series 只能在基本频率整数倍 $kf_0$ 处出现频率成分：

$$
f_k=kf_0=\frac{k}{T}.
$$

当 $T=10$ ms、$f_0=100$ Hz 时，就是 $100,200,300,400,\ldots$ Hz。$100$ Hz 表示整个脉冲图案每 10 ms 重复一次；$200,300,400$ Hz 等 harmonics 主要帮助形成每个周期内部的尖锐形状。

如果输入 A 只有 100 Hz 正弦，输入 B 同时含 100、200、300 Hz，但它们经过 threshold neuron 后都只在每个大峰值处发放一次，则两者可能产生相似的 spike sequence。这个相似 spike 的频谱仍会包含 100 Hz 的整数倍。因此其中的 200/300 Hz 不能自动解释为神经元准确保留了输入 B 的独立 200/300 Hz 信息，它们也可能只是输出 spike waveform 的 harmonics。

#### 5. 图 3(a)、(b)、(c) 到底如何联系？

三幅图是同一条处理链：

$$
\text{input }x(t)\rightarrow\text{activation}\rightarrow\text{Fourier spectrum}\rightarrow\text{weighting spectrum}.
$$

图 3(a) 的蓝线是输入，红线是 ReLU output，绿线是 LIF spike output；图 3(b) 是这三条时间曲线各自的 Fourier spectrum；图 3(c) 则进一步观察它们经过 CONV/MLP 或 synaptic weighting 后的频谱。

图 3(b) 中绿色 spike 的频谱很宽，只说明尖锐 spike waveform 包含许多频率成分；它还不能证明这些高频是输入信息被有效保留。图 3(c) 中，绿色高频成分经过后续处理后随频率升高而衰减，说明这些 waveform-induced harmonics 难以有效进入下一层的 membrane integration 和 spike generation。作者由此得到：单个 spike 看起来频谱很宽，但完整 SNN 信息路径在网络级仍表现为 low-pass。

#### 6. 公式（23）如何得到？

SNN 的能耗估算采用：

$$
\text{energy}=\text{number of operations}\times\text{energy per operation}.
$$

第 $l$ 层的 SOP 近似为：

$$
\operatorname{SOPs}(l)=f_r\times T\times\operatorname{FLOPs}(l).
$$

其中 $T$ 是 simulation timesteps，$f_r$ 是输入 spike firing rate，$\operatorname{FLOPs}(l)$ 是该层每个时间步处理 dense input 时的操作规模。若 $f_r=0.1$、$T=4$、$\operatorname{FLOPs}=1{,}000{,}000$，则 SOPs 为 $400{,}000$。

对于二值 spike $s_i\in\{0,1\}$：

$$
s_iw_i=
\begin{cases}
0,&s_i=0,\\
w_i,&s_i=1,
\end{cases}
$$

因此非零 spike 可以被近似为 AC，而连续静态输入的第一层仍使用 MAC。取参考值 $E_{\mathrm{MAC}}=4.6$ pJ、$E_{\mathrm{AC}}=0.9$ pJ：

$$
E_{\mathrm{SNN}}=E_{\mathrm{MAC}}\times\operatorname{FLOP}^{1}_{\mathrm{CONV}}+E_{\mathrm{AC}}\times\left(\sum_{n=2}^{N}\operatorname{SOP}^{n}_{\mathrm{SNN\ Conv}}+\sum_{j=1}^{M}\operatorname{SOP}^{j}_{\mathrm{SNN\ FC}}\right).
$$

第一项是静态输入进入 spike domain 前的连续 MAC；第二项是后续 spike convolution 和 spike fully connected layers 的 AC。ANN 则按：

$$
E_{\mathrm{ANN}}=E_{\mathrm{MAC}}\times\operatorname{FLOPs}.
$$

这只是基于参考芯片 operation cost 的理论 proxy，不是完整 hardware power measurement；memory access、routing、membrane-state communication 和控制逻辑没有完全包含。
