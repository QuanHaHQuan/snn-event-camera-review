---
tags: [SNN, spiking-transformer, wavelet-transform, frequency-learning, event-vision, neuromorphic-computing]
---

# Summary V2｜Spiking Wavelet Transformer

## 1. Core Understanding

本文提出 Spiking Wavelet Transformer（SWformer），目标是解决现有 Spiking Transformer 对局部边缘、纹理、移动边界和像素级 brightness changes 等 high-frequency patterns 建模不足的问题。作者去掉 self-attention token mixer，改用 Frequency-Aware Token Mixer（FATM）。FATM 由 Frequency Learner（FL）、Spatial Learner（SL）和 Channel Mixer（CM）三条并行分支组成，分别使用 spiking Haar wavelet、$3\times3$ convolution 和 $1\times1$ pointwise convolution 处理频率、空间和通道关系。

本文的关键接口是：Haar high-pass coefficients 天然包含正负差分，但普通 binary SNN 只能输出 $\{0,1\}$ spikes。因此作者只在 wavelet forward/inverse 中引入 negative spike dynamics，试图将频率表示扩展到声称的 $\{-1,0,1\}$，其余网络仍以 LIF、binary spikes 和 membrane potentials 工作。SWformer 是 hybrid-in-the-state SNN architecture：spikes 负责层间脉冲通信，continuous membrane potentials 负责神经元状态和 shortcut；它不是所有中间计算都离散化的纯 binary system。

本文不是新的 event representation。Static image 被重复输入 $T$ 个 timesteps，neuromorphic data 被组织成 $T$ 个 frames，再进入 time-stepped network。对 SECNet 的主要价值是提供一个 wavelet/Fourier alternative：如何将局部、多尺度、signed frequency representation 放在 spike communication 与 membrane-state computation 之间；它没有直接处理 raw Event Cloud，也没有证明真实 event-by-event asynchronous deployment。

## 2. Problem and Motivation

事件相机和 SNN 都具有稀疏、时间驱动的特征，但事件主要记录亮度变化和移动边缘，包含大量 local high-frequency information。作者认为，现有 Spiking Transformer 从 Vision Transformer 继承 global self-attention，跨 non-overlapping patch tokens 做全局聚合，更擅长 global shape 和 low-frequency structure，而高频 edge/texture 会在网络深层被削弱。

直接把 Fourier transform 引入 SNN 又有两个困难：Fourier coefficient 是 complex-valued，需要分别处理 real/imaginary responses；Fourier transform 依赖级联矩阵乘法，与 neuromorphic chip 的 sparse binary communication 不自然匹配。作者选择 Haar wavelet，因为 Haar 用局部平均和差分构造 low-frequency approximation 与 high-frequency detail，具有空间定位、多尺度和稀疏性质，且更容易映射为 add/subtract 操作。

论文的证据主要来自 feature-spectrum visualization、FATM ablation 和 static/neuromorphic classification accuracy。它支持“本文比较的 gSSA/Spiking Transformer 配置中，FATM 更能保留高频信息”，但不能推广为所有 self-attention 都是 low-pass，或所有 low-frequency information 都无用。

## 3. Method Overview

### LIF spiking layer

SWformer 使用 Leaky Integrate-and-Fire（LIF）neuron。对时间步 $n$，空间输入 $I[n]$ 先与上一时刻的 membrane potential $V[n-1]$ 相加：

$$
U[n]=V[n-1]+I[n].
$$

随后根据阈值产生 spike：

$$
s[n]=H\left(U[n-1]-V_{\mathrm{th}}\right),
$$

其中 $H(x)=1$ 当 $x\geq0$，否则为 $0$。膜电位更新为：

$$
V[n]=V_{\mathrm{reset}}s[n]+\left(\beta U[n]\right)\left(1-s[n]\right).
$$

按作者文字，$U[n]$ 是当前整合后的 potential，$s[n]$ 是 binary spike，$V[n]$ 是下一步携带的 temporal state；不发放时，膜电位按 decay factor $\beta$ 保留。PDF 的式（2）使用 $U[n-1]$ 判断发放，而文字描述是“当前 $U[n]$ 超过阈值”，存在 indexing ambiguity，不能自行改写成另一种实现。

### SPS 与 Spiking Encoder

输入序列为：

$$
I\in\mathbb{R}^{T\times C\times H\times W}.
$$

Static dataset 将同一 image 重复 $T$ 次；neuromorphic dataset 已经提供 $T$ 个 frame-like slices。Spiking Patch Splitting（SPS）中的 Patch Splitting Module（PSM）使用四个 initial spiking Conv layers，将输入转为：

$$
U=\operatorname{PSM}(I),
\qquad
U\in\mathbb{R}^{T\times N\times D}.
$$

经 spiking layer、relative position embedding 和膜电位 shortcut：

$$
s=\operatorname{Spk}(U),
\qquad s\in\mathbb{R}^{T\times N\times D},
$$

$$
\operatorname{RPE}=\operatorname{ConvBN}(s),
\qquad \operatorname{RPE}\in\mathbb{R}^{T\times N\times D},
$$

$$
U_0=U+\operatorname{RPE},
\qquad U_0\in\mathbb{R}^{T\times N\times D}.
$$

其中 $N$ 是 patch/token 数量，$D$ 是 embedding/channel dimension；$U$ 与 $U_0$ 是 membrane-potential tensors，而 $s$ 是 spike tensor。随后串联 $M$ 个 Spiking Encoder Blocks，每个 block 依次包含 FATM 和 Spiking MLP，并在 membrane potentials 上应用 residual connections。

整体 encoder 写为：

$$
S_0=\operatorname{Spk}(U_0),
\qquad S_0\in\mathbb{R}^{T\times N\times D},
$$

$$
U_l=\operatorname{FATM}(S_{l-1})+U_{l-1},
\qquad U_l\in\mathbb{R}^{T\times N\times D},
\quad l=1,\ldots,M,
$$

$$
S_l=\operatorname{Spk}\left(\operatorname{MLP}\left(\operatorname{Spk}(U_l)\right)+U_l\right),
\qquad S_l\in\mathbb{R}^{T\times N\times D},
$$

$$
Y=\operatorname{CH}\left(\operatorname{GAP}(S_M)\right).
$$

PDF 将最后输出写为 $S_N$，但前面用 $N$ 表示 token count、用 $M$ 表示 block count；按数据流应理解为最后一个 block 的 $S_M$，原符号存在冲突。

## 4. Key Components and Mechanisms

### FATM：三分支 token mixer

FATM 是 self-attention 的替代品。它并行处理三条 branch：FL 在 wavelet time-frequency domain 学习频率模式；SL 用 $3\times3$ convolution 建模 local spatial features；CM 用 $1\times1$ spiking pointwise convolution 做 cross-channel fusion。

为降低 FL 的参数量，作者将输入 feature sequence 按 $k$ 个 weight blocks 分组。由 $S_l\in\mathbb{R}^{T\times N\times D}$ reshape 成带空间结构的 $S'_l$，论文写为：

$$
S_l\rightarrow S'_l\in\mathbb{R}^{Tk\times N/k\times H\times W}.
$$

三条分支分别输出 membrane responses：

$$
U^l_{\mathrm{FL}}=\operatorname{FL}(S'_l),
\qquad U^l_{\mathrm{FL}}\in\mathbb{R}^{Tk\times N/k\times H\times W},
$$

$$
U^l_{\mathrm{SL}}=\operatorname{ConvBN}(S'_l),
\qquad U^l_{\mathrm{SL}}\in\mathbb{R}^{Tk\times N/k\times H\times W},
$$

$$
U^l_{\mathrm{CM}}=\operatorname{ConvBN}(S'_l),
\qquad U^l_{\mathrm{CM}}\in\mathbb{R}^{Tk\times N/k\times H\times W},
$$

$$
U^l_{\mathrm{FATM}}=U^l_{\mathrm{FL}}+U^l_{\mathrm{SL}}+U^l_{\mathrm{CM}}.
$$

融合后 reshape 回 $T\times N\times D$。SL 使用 $3\times3$ convolution，CM 使用 $1\times1$ convolution；作者同时在 SL/CM 中减少 channels，因此随着 $k$ 增加，参数量也线性下降。PDF 给出的 reshape 在一般符号下可能不满足元素守恒，实际 channel grouping/layout 需要代码确认：`Needs further check`。

### FL：Spiking Haar frequency representation

FL 将输入映射到 transform domain，学习并加权特定 frequency modes，再映射回原 domain。作者选择 Haar wavelet 而不是 complex Fourier transform，以避免 complex-valued spike banks，并利用 Haar 的稀疏局部平均/差分结构。

二维 Haar forward/inverse 写为：

$$
H_f=\operatorname{Spk}\left(W_{\mathrm{haar}}\cdot\operatorname{Spk}\left(I\cdot W_{\mathrm{haar}}^{\top}\right)\right),
$$

$$
I=\operatorname{Spk}\left(W_{\mathrm{haar}}^{\top}\cdot\operatorname{Spk}\left(H_f\cdot W_{\mathrm{haar}}\right)\right).
$$

右乘和左乘分别沿两个 spatial axes 做一维 Haar transform。$[1,1]$ 分支形成局部 average，$[1,-1]$ 分支形成局部 difference。理想的正交 Haar matrix 满足 inverse 可恢复输入；但每一步插入 spike quantization 后，整个过程不再严格可逆。

Haar matrix 递归定义为：

$$
W_{\mathrm{haar}}(n)=
\begin{cases}
[1], & n=1,\\
\frac{1}{\sqrt{2}}
\begin{bmatrix}
W_{\mathrm{haar}}(n-1)\otimes[1,1]\\
I_{2^{n-1}}\otimes[1,-1]
\end{bmatrix}, & n>1.
\end{cases}
$$

这里 $\otimes$ 是 Kronecker product，$I_{2^{n-1}}$ 是 identity matrix。Haar transform 同时给出 coarse low-frequency approximation 与 localized high-frequency details，因此比 global Fourier basis 更容易保留“频率出现在哪里”的信息。

### Negative spike dynamics

Binary spike 只能表达 $0/1$，而 Haar high-pass difference 含有负项。作者因此在 wavelet transform 部分使用 negative spike dynamics，并声称把 spike values 扩展为 $\{-1,0,1\}$。给出的 integrate-and-fire equations 是：

$$
U[n]=V[n-1]+I[n],
$$

$$
s[n]=H_{\mathrm{sym}}\left(U[n-1]-V_{\mathrm{th}}\right),
$$

$$
V[n]=V_{\mathrm{reset}}s[n]+U[n](1-s[n]).
$$

作者定义 symmetric Heaviside 为：

$$
H_{\mathrm{sym}}(x)=
\begin{cases}
1, & x\geq0,\\
-1, & x<0.
\end{cases}
$$

并使用 integrate-and-fire，即 LIF 中 $\beta=1$ 的情况。负 spike 只在 spiking Haar forward/inverse 中使用，网络其他部分仍按 binary LIF 运行。这里存在需要保留的正文疑点：$H_{\mathrm{sym}}$ 的定义本身只产生 $\{-1,+1\}$，没有 $0$ region；式中仍使用 $U[n-1]$ 判断 spike，且 negative spike 代入 reset equation 后的 state semantics 不清楚。因此不能仅凭正文重建真正的 ternary neuron implementation：`Needs further check`。

Figure 4 的 PSNR 直接展示了 quantization/reconstruction trade-off：binary Haar forward 为 25.22、ternary forward 为 28.34；binary inverse 为 8.77、ternary inverse 为 10.76。ternary dynamics 改善了 signed coefficient representation，但 inverse reconstruction 仍有明显误差。

### Block-diagonal weight matrix

FL 将 dense $d\times d$ matrix 拆成 $k$ 个独立的 $d/k\times d/k$ weight blocks。参数量从 $O(d^2)$ 降为：

$$
k\left(\frac{d}{k}\right)^2=\frac{d^2}{k}.
$$

每个 block 只在一个 feature subspace 内做 projection，类似 multi-head attention 中的一个 subspace，但不等价于完整 attention head，因为没有 QK similarity 或跨组 attention。作者给出的 block-wise computation 为：

$$
\widetilde{y}^{\ell}_{m,n}=W^{\ell}_{m,n}x^{\ell}_{m,n},
\qquad \ell=1,\ldots,k,
\quad (m,n)\in H\times W.
$$

其中 $m,n$ 是 spatial token 坐标，$\ell$ 是 block id。若 $W^{\ell}_{m,n}$ 真正随每个空间位置变化，则会与前述参数量推导矛盾；更可能是共享 block weight 的记号简写，仍需代码确认。

### Membrane shortcut

SWformer 使用 membrane shortcut，而不是简单相加 spikes。FATM 输出 membrane response 与上一层 membrane potential 相加，Spiking MLP 也在 membrane path 上形成 residual。这样既保留 identity mapping，又避免直接相加 binary spikes 后产生 integer-driven activation；代价是系统必须保存和访问 continuous membrane states。

因此“multiplication-free”应理解为在 spike-aware hardware 上，binary/signed activation 与 weight 的乘法可以映射成 conditional skip、addition 或 subtraction；它不意味着 GPU computation graph 中完全没有 multiplication。Haar normalization、BN、membrane decay、continuous residual 和 classification head 的无乘法硬件实现，正文没有完整给出：`Needs further check`。

## 5. Experiments and Main Evidence

### Setup and datasets

Static datasets 包括 CIFAR-10、CIFAR-100 和 ImageNet；neuromorphic datasets 包括 CIFAR10-DVS、N-Caltech101、N-Cars、ActionRecognition、ASL-DVS 和 NavGesture。Static image 在每个 timestep 重复，neuromorphic input 被组织成 frame sequence。因此这些实验是 time-stepped evaluation，不等价于逐 event asynchronous chip deployment。

### Static classification

ImageNet 上，SWformer Transformer-6-512、Block=2、$V_{\mathrm{th}}=0.5$ 达到 $74.98\%$，比同配置 SpikFormer 的 $72.46\%$ 高 2.52 points，比 SD Transformer 的 $74.11\%$ 高 0.87 points。Block=4、Transformer-8-512、$V_{\mathrm{th}}=1$ 达到 $75.29\%$，参数量为 23.14M；该 configuration 比 SpikFormer Transformer-8-512 的 29.68M 少约 22.03%。标准 non-spiking wavelet baseline 通常更高，说明准确频率表示与 spike-driven compatibility 存在 precision trade-off。

CIFAR-10/100 上，4 timesteps 的 SWformer 分别为 $96.1\%/79.3\%$；CIFAR10-DVS 上，16 timesteps 达到 $83.9\%$。这些是表内 SNN comparison，不应无条件写成所有 ANN/SNN 的 overall SOTA。

### Neuromorphic classification

SWformer 报告 N-Caltech101 $88.45\%$、N-Cars $96.32\%$、Action Recognition $88.88\%$、ASL-DVS $99.88\%$、NavGesture $98.49\%$。相对表中 comparator，作者报告 N-Caltech101/N-Cars 比 NDA 高 4.75/4.42 points，Action Recognition 比 Mb-SNN 高 10.78 points，ASL-DVS 比 Meta-SNN 高 3.84 points 且使用少 10 倍 timesteps，NavGesture 比 KNN 高 2.59 points。数据经过 frame/sequence representation 后进入 SNN，不能把这些准确率直接当成 raw asynchronous event processing 证据。

### Ablation and efficiency evidence

CIFAR100 上，base 为 $79.31\%$；NoHaar、NoNeg、NoInv 分别为 $78.89\%$、$78.64\%$、$78.79\%$，MaskDC 反而为 $79.34\%$。CIFAR10-DVS 上，base 为 $83.9\%$，NoPool 降为 $81.8\%$，MaskDC 为 $84.0\%$。这些结果支持 Haar、negative spikes、inverse transform 和 pooling 在当前配置中的作用，但 MaskDC 只说明作者定义的 DC coefficient 在该实验中并非必要，不能推出所有 low-frequency information 都有害。

Block 数从 2 增加到 4，参数量约降低 16%，同时保持相近 accuracy。Table 1 的 Power（mJ）和 time steps 是论文报告的 efficiency indicators；正文没有给出足以独立复核的完整 energy accounting，不能把它们升级为 neuromorphic chip power measurement。作者声称提高 $V_{\mathrm{th}}$ 可降低 58.4%--60.1% power，但比较基准和表内具体复现关系不完全清楚：`Needs further check`。

## 6. Strengths and Limitations

**Strengths。** 论文把 frequency prior 直接放入 spike token mixer，而不是只做频谱可视化；FL 具有 forward-transform、frequency weighting 和 inverse-transform 的完整结构；negative spike dynamics 正面处理了 signed Haar coefficients；FATM 同时提供 frequency、spatial 和 channel mixing；Haar、negative spike、inverse、DC、pooling 和 block-count ablations 为机制贡献提供了对应证据。

**Limitations。** 正文中的 ternary neuron、LIF indexing、reset semantics、FATM reshape 和 Eq.（12）weight sharing 存在符号或实现疑点。事件数据被分帧，模型不是 event-by-event asynchronous system；continuous membrane、BN、normalization、residual state 和 classifier 也使“multiplication-free”不能直接等于全栈无乘法。Power 证据不是完整硬件测量；高频优势主要由指定 Spiking Transformer 配置的 visualization 和 ablation 支持，不能推广成 self-attention 或 low-frequency structure 普遍无效。

## 7. Relation to SECNet Extension Direction

本文对 SECNet 的直接价值是 wavelet-side frequency mechanism，而不是 Survey 文献关系。

**Frequency mechanism。** SWformer 用 Haar 的 local average/detail decomposition 替代 complex Fourier representation，把 low-frequency approximation 和 high-frequency differences 放进 token mixer。对 SECNet 而言，可借鉴“先做多尺度 frequency decomposition，再让 event-derived sparse features 选择 frequency modes”的结构；但必须区分 image spatial frequency、event temporal frequency、spike firing rate 和 wavelet scale，不能把它们统一称作 frequency。

**Event Cloud interface。** SWformer 的输入是 $T\times C\times H\times W$ 的 dense frame sequence，而不是原始 Event Cloud。若迁移到 SECNet，需要明确 Event Cloud 如何投影到规则空间网格、如何保留 timestamp/polarity、如何组织 $T$，以及 Haar transform 后的 spatial locality 是否仍然有意义。本文没有验证 point-wise Event Cloud 或异步 event-by-event wavelet processing。

**SNN coupling。** 最可迁移的接口是 signed frequency coefficients 与 sparse spike communication 之间的设计问题：binary spike 会丢失 Haar difference 的 sign，negative/signed spike 可以减少误差，但需要明确 $0$ region、threshold、reset、memory state 和 hardware support。本文没有给出可以直接移植到 SECNet 的 signed Event Cloud encoder 或 surrogate-gradient implementation。

**效率边界。** 作者的 multiplication-free claim 依赖对 spike-aware hardware 的映射假设，不能由 GPU formula、参数量或 Table 1 的 Power 数字单独证明。对 SECNet，应该把 wavelet transform cost、signed spike storage、membrane access、BN/normalization 和 event sparsity 分开评估。

## 8. Survey-Usable Takeaways

- SWformer 是 frequency-aware SNN token mixer：FATM 用 FL、SL、CM 分别处理 wavelet frequency、local spatial 和 cross-channel information。
- Haar 的 local average/difference 适合 SNN 的 sparse add/subtract，但插入 spike quantization 后不再严格可逆；negative spike 只缓解 signed coefficient loss，并没有消除 amplitude/reconstruction error。
- membrane shortcut 说明 spike-driven communication 与 continuous membrane residual 可以同时存在，因此“Spiking Transformer”不等于所有中间量都为 spikes。
- 论文的 accuracy evidence 较完整，真实 hardware/energy evidence 较弱；Table 1 的 Power 应限定为论文报告的 efficiency estimate/indicator。
- 对 SECNet，最值得迁移的是 signed frequency interface、局部多尺度 decomposition 和 frequency-aware token mixing；最需要重新设计的是 Event Cloud projection、异步执行、signed spike state 和 memory/normalization cost。

## Supplement Points

### Questions and Clarifications

#### 1. FT、FFT、STFT 和 Wavelet 分别是什么？

频域不是另一份数据，而是用不同变化速度的模式重新描述同一信号。时域或空间域说明某个时间/位置的值；频域说明由哪些 frequency components 组成、各自多强、以什么 phase 对齐。图像中的缓慢亮度变化和大尺度结构偏 low frequency，边缘、纹理和像素突变偏 high frequency；噪声也可能是 high frequency，所以 high frequency 不自动等于有用细节。事件相机记录 brightness changes，但单个 event 不是 frequency coefficient，必须对 event representation 或 feature tensor 做 transform。

Fourier Transform（FT）把信号分解为覆盖全局的 complex sinusoids：

$$
X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2\pi ft}\,dt.
$$

$X(f)$ 的 magnitude 表示该频率有多强，phase 表示它如何与时间/空间位置对齐。DFT 是有限离散信号上的 Fourier basis expansion；FFT 不是新变换，而是利用 periodicity 和 symmetry 将 DFT 从 $O(N^2)$ 加速到 $O(N\log N)$ 的算法。

FT 的 basis 覆盖全局，能说明“有哪些频率”，却不擅长说明“频率在哪里出现”。STFT 用固定滑动窗口做局部 FT，得到 time-frequency map，但固定窗口存在 resolution trade-off：短窗口定位好、测频差；长窗口相反。

Wavelet 使用可平移、可缩放的局部 wavelet。小 scale 对应局部 high-frequency change，大 scale 对应较慢、较大范围结构。二维 DWT 通过 horizontal/vertical low-pass 与 high-pass filtering 得到 LL、LH、HL、HH；Haar 的核心是相邻样本的平均与差分：

$$
L=\frac{x_0+x_1}{\sqrt2},\qquad H=\frac{x_0-x_1}{\sqrt2}.
$$

它既保留局部位置，又表达多尺度频率，因此适合边缘和 event features，也更容易用 add/subtract 映射到 spikes。

#### 2. 连续 FT 的积分、逆变换、负指数和负频率是什么？

Fourier analysis 是正交基分解。周期为 $T_0$ 的连续信号使用 $\phi_k(t)=e^{j2\pi kt/T_0}$ 作为 basis；系数由 conjugate basis 投影得到：

$$
x(t)=\sum_{k=-\infty}^{\infty}c_k e^{j2\pi kt/T_0},
$$

$$
c_k=\frac1{T_0}\int_0^{T_0}x(t)e^{-j2\pi kt/T_0}\,dt.
$$

负指数来自 complex inner product 对 basis 取 conjugate。匹配频率时，$e^{j2\pi ft}e^{-j2\pi ft}=1$，积分会累积；不匹配频率仍旋转，在完整周期上抵消。令 $T_0\rightarrow\infty$，频率间隔趋于零，Fourier series 变为：

$$
X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2\pi ft}\,dt,
$$

$$
x(t)=\int_{-\infty}^{\infty}X(f)e^{j2\pi ft}\,df.
$$

正变换用 conjugate basis 做 projection，逆变换用原 basis 合成，所以指数符号相反。Negative frequency 不是负的物理振荡次数，而是 complex plane 中相反的 rotation direction；real cosine 同时由正、负两种 complex rotations 构成：

$$
\cos(2\pi ft)=\frac12e^{j2\pi ft}+\frac12e^{-j2\pi ft}.
$$

#### 3. 为什么 DFT 是 complex exponential 的 $N\times N$ matrix？

长度为 $N$ 的 sequence 是 $N$-dimensional vector，需要 $N$ 个 independent basis vectors。DFT 使用：

$$
\phi_k[n]=e^{j2\pi kn/N},\qquad k=0,\ldots,N-1.
$$

第 $k$ 个 frequency coefficient 是：

$$
X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}.
$$

令 $F_{k,n}=e^{-j2\pi kn/N}$，则：

$$
\mathbf{X}=\mathbf{F}\mathbf{x},
\qquad \mathbf{F}\in\mathbb{C}^{N\times N}.
$$

矩阵有 $N$ 行，因为输出有 $N$ 个 frequency bins；有 $N$ 列，因为每个 bin 都使用全部 $N$ 个 samples。其正交性为：

$$
\mathbf{F}^{H}\mathbf{F}=N\mathbf{I},
$$

因此 inverse DFT 为：

$$
\mathbf{x}=\frac1N\mathbf{F}^{H}\mathbf{X}.
$$

#### 4. DC 是什么？

DC 来自 Direct Current，在 signal processing 中表示 zero-frequency component。DFT 的 $k=0$ 项为：

$$
X[0]=\sum_{n=0}^{N-1}x[n],
$$

除以 $N$ 就是平均值；对 image/feature map，它对应整体亮度或 average activation，而不是 edge、texture 或 local change。

本文在 ablation 中突然使用 “MaskDC”，但正文此前没有给出独立定义。因为 SWformer 使用 Haar transform，这里的 DC 更可能是最粗尺度的 global-average/lowest-frequency coefficient，而不一定是 DFT 的 $X[0,0]$。具体 mask 哪个 coefficient 需要查看 code：`Needs further check`。MaskDC 提升 accuracy 只说明作者定义的 DC 在当前配置中不是必要信息，不能推出所有 low-frequency information 都有害。
