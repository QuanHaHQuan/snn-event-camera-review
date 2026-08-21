---
tags: [event-based-deblurring, video-restoration, frequency-domain, temporal-alignment, event-dataset]
---

# Summary V2｜Frequency-aware Event-based Video Deblurring for Real-World Motion Blur

## 1. Core Understanding

本文提出一个面向 event-based video deblurring 的 ANN 框架，输入连续 blurry frames 和对应 event streams，输出每个时间位置的 sharp frames。它针对两个缺口：传统视频去模糊虽然利用邻帧，但严重连续运动会使 frame alignment 变得困难；已有 event-based deblurring 又主要处理单幅图像或相邻图像，没有充分利用长时间视频上下文。

方法由三个互补模块组成。Frequency-aware Cross-Modal Feature Enhancement（FCFE）在频域中用 event features 自适应增强 blur features；Event-guided Local-windowed Temporal Propagation（ELTP）在低分辨率上用左右邻帧和事件完成局部 alignment；Bidirectional Temporal Feature Fusion（BTFF）在高分辨率上沿前向和后向传播 long-range temporal features。论文同时用硬件同步的 RGB-event hybrid camera system 采集 REVD 真实数据集。

本文不是 SNN。Event stream 先被转换为 voxel grid，之后由 3D convolution、FFT、cross-attention、GEGLU、ResBlocks 和 transposed convolution 等 ANN-style continuous operations 处理。因而它对 SECNet 的价值主要在于 event/frequency interface、temporal alignment 和真实 event restoration benchmark，而不是提供 spike、membrane potential 或 neuromorphic energy 机制。

## 2. Problem and Motivation

帧相机在曝光时间内积分亮度，物体或相机运动会把多个时刻的内容混合成 blur，导致从 blurry frame 恢复 latent sharp frame 成为 ill-posed inverse problem。事件相机以微秒级时间分辨率记录逐像素 brightness changes，可以补充曝光期间的 motion trajectory 和 high-frequency structure，因此适合辅助恢复清晰帧。

作者指出，传统 video deblurring 会从连续视频中聚合邻帧信息，并使用 optical flow 或 deformable convolution 做 temporal alignment；但严重、连续 blur 会降低这些对齐方法的可靠性。另一方面，已有 event-based motion deblurring 通常围绕 single-image restoration，最多使用一对相邻图像。因此本文的目标是同时利用 event 的高时间分辨率、视频帧的互补内容和更长时间范围的 temporal dependency。

作者进一步观察到，events 主要记录 scene brightness changes，因而包含大量与运动、边缘和局部突变相关的高频信息；这些高频成分也是 latent sharp frame 中需要恢复的部分。FCFE 据此在 spectral domain 中建立 blur/event correlation，而 ELTP 与 BTFF 负责把事件中的时间信息转化为局部和长期的 feature alignment。

## 3. Method Overview

### Input representation and multiscale encoder

事件流首先被转换为 voxel grid。对第 $i$ 个视频时间位置，event voxel 的形状为 $E_iinmathbb{R}^{B	imes H	imes W}$，其中 $B$ 是 temporal bins；blur frame 为 $B_i$。给定连续输入 ${B_i}_{i=1}^{T}$ 与 ${E_i}_{i=1}^{T}$，作者先通过 kernel 为 $1	imes3	imes3$ 的 3D convolution 提取事件和图像特征，再通过两个 kernel 为 $3	imes3	imes3$、stride 为 $1	imes2	imes2$ 的 3D convolutions 逐步降低空间尺寸，形成多尺度特征 $F(E)^s_i$ 和 $F(B)^s_i$。

尺度因子 $s$ 下的空间尺寸定义为：

$$
H_s=\frac{H}{2^s},\qquad W_s=\frac{W}{2^s}.
$$

整体顺序是：在最低分辨率 $s=2$ 上执行 FCFE；随后用 ELTP 对相邻帧进行局部 temporal alignment；上采样到 $s=1$ 后，用 BTFF 汇聚更长范围的双向时间信息；最后预测 sharp frame。最终重建公式为：

$$
S_i=\operatorname{Conv}_{3\times3}\left(U\left(\widetilde{H}^{(B)}_i\right)\right)+B_i,
\qquad i=1,\ldots,T,
$$

其中 $\widetilde{H}^{(B)}_i$ 是 BTFF 聚合后的特征，$U$ 是 transposed 2D convolution upsampling block，$B_i$ 是输入 blurry frame，$S_i$ 是估计的 sharp frame。残差形式让网络主要学习 blur 到 sharp 之间的恢复量。

## 4. Key Components and Mechanisms

### FCFE：spatial frequency 与 time-channel joint frequency

给定尺度 $s=2$ 的 blur/event features，FCFE 先对两种模态分别做 LayerNorm，在 channel dimension 拼接，再用 $1\times1$ convolution 得到 cross-modal correlated feature：

$$
F(C)_i=\operatorname{Conv}_{1\times1}\left(\operatorname{Concat}\left(\operatorname{LN}(F(B)_i),\operatorname{LN}(F(E)_i)\right)\right),
\qquad F(C)_i\in\mathbb{R}^{C\times H_s\times W_s}.
$$

#### Spatial frequency filtering

对每个 channel 的 $H_s\times W_s$ feature map 执行 2D FFT。为了让普通 real-valued convolution 处理 complex spectrum，作者将 real 和 imaginary parts 沿 channel dimension 拼接。论文将这个结果简写为同一个符号，但其实际含义是：

$$
\mathcal{F}(C)_i=\operatorname{FFT}(F(C)_i),
\qquad
\mathcal{F}(C)_i\in\mathbb{R}^{2C\times H_s\times\left(\left\lfloor\frac{W_s}{2}\right\rfloor+1\right)}.
$$

这里 $2C$ 来自 $[\operatorname{Re},\operatorname{Im}]$ 拼接；$\lfloor W_s/2\rfloor+1$ 来自 real input 的 conjugate symmetry，只保留宽度方向非冗余频率。对 blur feature 也进行 FFT，得到：

$$
\mathcal{F}(B)_i\in\mathbb{R}^{C\times H_s\times\left(\left\lfloor\frac{W_s}{2}\right\rfloor+1\right)}.
$$

作者通过 convolution、ReLU 和 Sigmoid，从 cross-modal frequency representation 生成 spatial frequency filter：

$$
f_s=\operatorname{Sigmoid}\left(\operatorname{ReLU}\left(\operatorname{Conv}(\mathcal{F}(C)_i)\right)\right),
\qquad
f_s\in\mathbb{R}^{C\times H_s\times\left(\left\lfloor\frac{W_s}{2}\right\rfloor+1\right)}.
$$

然后用事件/图像相关性生成的 filter 逐频率调节 blur spectrum：

$$
\widehat{\mathcal{F}(B)}_i=\mathcal{F}(B)_i\otimes f_s,
$$

其中 $\otimes$ 是 element-wise multiplication。该操作对每个 spatial frequency bin 赋予自适应权重；它不是直接恢复像素，而是先选择性增强或抑制空间频率。之后通过 convolution、ReLU 和 inverse FFT 回到 spatial domain：

$$
\widehat{F(B)}_i
=\operatorname{iFFT}\left(\operatorname{ReLU}\left(\operatorname{Conv}_{1\times1}\left(\widehat{\mathcal{F}(B)}_i\right)\right)\right).
$$

作者依据 convolution theorem 将频域逐元素乘法解释为具有大 receptive field 的 dynamic filtering。这里的“dynamic”来自 filter $f_s$ 由当前 blur/event content 生成，而不是使用固定卷积核。

#### Global channel filtering

Spatial filtering 后的特征形状为 $T\times C\times H_s\times W_s$。作者将时间和通道合并为 $M=T C$，得到：

$$
\{\widehat{F(B)}_i\}_{i=1}^{T}
\in\mathbb{R}^{T\times C\times H_s\times W_s}
\rightarrow
\widehat{F(B)}_{1:T}\in\mathbb{R}^{M\times H_s\times W_s}.
$$

沿这个展平轴执行 1D FFT：

$$
\widehat{\mathcal{F}(B)}_{1:T}
=\operatorname{1D\text{-}FFT}\left(\widehat{F(B)}_{1:T}\right),
\qquad
\widehat{\mathcal{F}(B)}_{1:T}
\in\mathbb{R}^{\left(\left\lfloor\frac{M}{2}\right\rfloor+1\right)\times H_s\times W_s}.
$$

从张量操作看，这不是只沿原始 channel 维度做滤波，而是在每个空间位置上对 time-channel joint sequence 做频率建模。作者称其为 global channel filtering，是因为该联合轴覆盖了全部时间位置和通道。

为了生成 global filter，作者先通过 skip connection 融合 cross-modal correlated feature 与 spatially filtered feature：

$$
\widetilde{F(C)}_i=F(C)_i+\widehat{F(B)}_i,
$$

再经过 channel attention 得到 $A_i\in\mathbb{R}^{C\times1\times1}$，并进行通道调制：

$$
\widehat{F(C)}_i=\widetilde{F(C)}_i\otimes A_i.
$$

将 $\{\widehat{F(C)}_i\}_{i=1}^{T}$ 展平为 $\widehat{F(C)}_{1:T}\in\mathbb{R}^{M\times H_s\times W_s}$ 后，通过 $1\times1$ convolution 生成 global channel filter：

$$
f_t=\operatorname{Conv}_{1\times1}\left(\widehat{F(C)}_{1:T}\right),
\qquad
f_t\in\mathbb{R}^{\left(\left\lfloor\frac{M}{2}\right\rfloor+1\right)\times H_s\times W_s}.
$$

频谱调制和恢复过程为：

$$
\widetilde{\mathcal{F}(B)}_{1:T}
=\widehat{\mathcal{F}(B)}_{1:T}\otimes f_t,
$$

$$
\widetilde{F(B)}_{1:T}
=\operatorname{1D\text{-}iFFT}\left(\widetilde{\mathcal{F}(B)}_{1:T}\right).
$$

随后 reshape 回 $T\times C\times H_s\times W_s$。最后，Transformer-style cross-attention 融合 event feature $F(E)_i$ 和 filtered blur feature $\widetilde{F(B)}_i$，GEGLU 的结果与原 blur feature 通过 residual connection 相加，得到 FCFE 输出。需要注意：PDF 的若干符号复用了同一个 $F(B)$，这里用 $\mathcal{F}$ 区分 frequency-domain tensor，以避免把变换前后混淆。

### ELTP：event-guided local-windowed temporal propagation

ELTP 在尺度 $s=2$ 上处理 reference frame $i$ 的左右邻帧。对于左侧和右侧 supporting blur features，作者分别拼接 supporting blur feature、当前 event feature 和 supporting event feature，并通过 ResBlocks 生成 forward/backward aligned features：

$$
G^{(B)f}_i
=\operatorname{Res}\left[\widetilde{F(B)}_{i-1},F(E)_i,F(E)_{i-1}\right],
$$

$$
G^{(B)b}_i
=\operatorname{Res}\left[\widetilde{F(B)}_{i+1},F(E)_i,F(E)_{i+1}\right].
$$

方括号表示 channel-wise concatenation。这里的 alignment 是 synthesis-based：网络不显式估计 optical flow，而是利用当前帧与 supporting frame 之间的 event motion context，学习将 supporting feature 变换到 reference frame。

两个方向的 aligned features 先融合：

$$
G^{(B)bf}_i
=\operatorname{Conv}_{3\times3}\left([G^{(B)b}_i,G^{(B)f}_i]\right).
$$

随后，作者对 $G^{(B)bf}_i$ 和当前 $\widetilde{F(B)}_i$ 做 FFT，并拼接它们的 real/imaginary parts，通过 $1\times1$ convolution 得到频域联合特征：

$$
Y_F=\operatorname{Conv}_{1\times1}\left[
R(G^{(B)bf}_i),I(G^{(B)bf}_i),
R(\widetilde{F(B)}_i),I(\widetilde{F(B)}_i)
\right].
$$

其中 $R$、$I$ 分别表示 real 和 imaginary parts。频域 channel attention map 为：

$$
K_i=\sigma\left(F_{\mathrm{conv}}\left[
\operatorname{AvgPool}(Y_F),\operatorname{MaxPool}(Y_F)
\right]\right),
$$

$$
F_{\mathrm{conv}}=\operatorname{Conv}_{1\times1}-\operatorname{ReLU}-\operatorname{Conv}_{1\times1}.
$$

作者沿 channel dimension 将 $K_i$ split 成 $K^1_i$、$K^2_i$，分别作用于两个 frequency-domain blur features；再经过 $F_{\mathrm{conv}}$、inverse FFT 和 ResBlocks，并与 current event feature 拼接，得到 ELTP 输出的局部对齐特征 $\widetilde{G(B)}_i$。

### BTFF：bidirectional temporal feature fusion

BTFF 在尺度 $s=1$ 的较高空间分辨率上运行。它与 ELTP 的区别是：ELTP 只使用左右邻帧并强调低分辨率细节 alignment，BTFF 通过递归 hidden features 把更远的帧信息传播到当前时间位置。

前向分支先融合相邻 event features：

$$
S(E)^f_i=\operatorname{Conv}_{3\times3}\left([F(E)_{i-1},F(E)_i]\right),
$$

然后将当前局部对齐特征、事件 motion feature 和上一个时间位置的前向 hidden feature 输入前向递归模块：

$$
H^{(B)f}_i
=F^f_{\mathrm{Res}}\left[
\widetilde{G(B)}_i,S(E)^f_i,H^{(B)f}_{i-1}
\right],
$$

其中 $F^f_{\mathrm{Res}}$ 是 $\operatorname{Conv}_{3\times3}$、ReLU 和 ResBlocks 的组合。后向分支为：

$$
S(E)^b_i=\operatorname{Conv}_{3\times3}\left([F(E)_i,F(E)_{i+1}]\right),
$$

$$
H^{(B)b}_i
=F^b_{\mathrm{Res}}\left[
\widetilde{G(B)}_i,S(E)^b_i,H^{(B)b}_{i+1}
\right].
$$

最后聚合两个方向：

$$
\widetilde{H}^{(B)}_i
=\operatorname{Conv}_{3\times3}\left([H^{(B)b}_i,H^{(B)f}_i]\right).
$$

这组递归使每个 $i$ 同时接收局部 ELTP feature、相邻 event motion 和来自更远时间位置的 forward/backward context，之后由式（11）重建 sharp frame。

## 5. Experiments and Main Evidence

### Dataset and training

GoPro 用于 synthetic event comparison，事件由 ESIM 生成。REVD 包含 21 段真实城市视频，13 段训练、8 段测试，图像和事件分辨率为 $1024\times768$，覆盖 ego-motion、object motion 以及二者组合。REVD 使用两台相同的 FLIR BlackFly frame cameras 和一台 Prophesee Gen4 event camera，通过 two-way 50:50 beam splitter 共轴对齐，并由 microcontroller 做 hardware-level synchronization。Blur camera 的 exposure 为 32 ms，sharp camera 为 4 ms；作者通过光强调整和 25% neutral-density filter 补偿不同曝光及 beam splitter 的光强差异。

训练使用 batch size 8、event voxel bin size 16、同步随机裁剪 $256\times256$、AdamW、初始 learning rate $1\times10^{-4}$ 和 Charbonnier loss。论文在当前正文中没有给出更完整的 loss 展开或训练 schedule，不能从常见 restoration practice 补写：`Needs further check`。

### Synthetic GoPro comparison

GoPro 表中本文 PSNR/SSIM 为 $36.70$ dB/$0.978$，高于表中 frame-based 和 event-based comparators。相对已有 event-based methods，作者报告 PSNR 差距为 $0.83$--$8.01$ dB。部分方法没有公开 GoPro 结果，作者使用相同 raw event data 和 event representation 从头训练，并以 † 标记；因此这些结果是统一复现实验下的比较，不能都视为原论文报告值。

### Real-world REVD comparison

REVD 上本文为 $32.99$ dB PSNR、$0.9326$ SSIM，优于第二名 UEVD 的 $31.97$ dB 和 $0.9211$ SSIM，PSNR 差距为 $1.02$ dB。RNN-MBP 的 PSNR 为 $31.77$ dB，但处理五段视频的 FLOPs 为 $153.5$ T、单帧 inference time 为 $2238$ ms；本文为 $30.27$ T 和 $484$ ms。这里的效率证据是 NVIDIA RTX A6000 GPU 上的 wall-clock inference time 与 FLOPs estimate，不是 hardware energy measurement，也不能直接推出 neuromorphic efficiency。

作者指出真实事件中的 noise 比 synthetic data 更严重，且 saturated pixels 无法通过单帧 blur kernel 恢复，所以真实数据恢复更困难。该解释是对误差来源的作者分析，并不等同于独立的 noise ablation。

### Ablation evidence

GoPro 的 baseline PSNR 为 $31.14$ dB。逐步加入模块后，单独 ELTP 为 $35.36$ dB，单独 BTFF 为 $36.08$ dB，ELTP+BTFF 为 $36.45$ dB，三者完整配置为 $36.70$ dB。FCFE 替代 baseline 的普通 3D convolution fusion 后，baseline 提升 $2.25$ dB；在包含 alignment 的配置上，加入 FCFE 仍有 $0.23$--$0.52$ dB 增益。ELTP 和 BTFF 相对 baseline 的提升分别为 $4.22$ dB 和 $4.94$ dB，二者结合比单独 BTFF 再提升 $0.37$ dB。这些结果支持 frequency-domain cross-modal enhancement、local alignment 与 long-range fusion 的互补性，但只是在 GoPro 配置上的模块消融证据。

## 6. Strengths and Limitations

**Strengths。** 本文将 event 的高时间分辨率与 video 的长期上下文结合，不再局限于 single-image 或相邻帧去模糊；FCFE 明确区分 spatial frequency filtering 和 time-channel joint filtering，ELTP/BTFF 分别承担局部细节对齐与 long-range consistency；REVD 通过硬件同步 hybrid camera system 提供高分辨率真实 RGB-event pairs。

**Limitations。** 本文是 ANN framework，voxelization、3D convolution、FFT、cross-attention 和 ResBlocks 都不是 spike-native computation，不能直接作为 SNN event processing 证据。REVD 只有 21 段序列，真实 event noise、saturated pixels 和跨传感器 optical differences 仍限制泛化。效率比较只覆盖 RTX A6000 的 inference time 与 FLOPs，不是实际 energy 或 neuromorphic hardware measurement。FCFE 将 $T$ 与 $C$ 展平后定义 global channel frequency，联合轴的具体实现和复杂频谱张量的 real/imaginary layout 仍需代码确认：`Needs further check`。

## 7. Relation to SECNet Extension Direction

本文对 SECNet 的直接参考价值是 frequency/Fourier mechanism 与 Event Cloud interface，而不是论文间 Survey genealogy。

**Frequency/Fourier mechanism。** FCFE 提供一个清晰的两级频率接口：对 feature-map spatial axes 做 2D FFT，用 event/frame correlation 生成 $f_s$ 过滤空间频率；再对展平的 $T\times C$ 轴做 1D FFT，用 $f_t$ 建模 time-channel joint spectrum。对于 SECNet，可以借鉴“由 event-derived feature 生成频率选择器”的思想，但不能直接假设 raw Event Cloud 已经是规则的 dense image grid。Event Cloud 需要先经过 voxelization、projection、splatting 或 point/graph aggregation，才能应用本文的 dense FFT。

**Event Cloud interface。** 本文的事件输入是 $E_i\in\mathbb{R}^{B\times H\times W}$ voxel grid，空间位置和时间 bin 已被规整为 dense tensor。因此它验证的是“规整后的 event representation 与 RGB/frame feature 在频域融合”的可行性，不是对原始不规则 event points 或异步 event-by-event stream 的直接处理。若迁移到 SECNet，必须明确 Event Cloud 到 $H\times W$ feature map 的投影、时间聚合和稀疏性损失。

**SNN coupling。** 本文没有 spike、membrane potential、surrogate gradient 或 SNN state update。FFT、频域逐元素乘法、cross-attention、GEGLU 和 dense convolution 都属于 ANN operations，因此它不能直接支持“frequency module 已经适合 SNN hardware”的结论。可迁移的只是频率分解、频率选择和跨模态 alignment 的结构位置；若与 SNN 结合，还需要重新设计 complex spectrum 的 real/imaginary representation、signed coefficient 编码、memory state 和 event-driven execution。

**可迁移性与边界。** 最可迁移的是 FCFE 的内容自适应频率 filter，以及 ELTP/BTFF 的局部加长期时间建模。最难直接迁移的是 2D FFT 所需的规则空间网格、time-channel flattening 的语义、复杂数运算和 dense residual reconstruction。REVD 的真实噪声与饱和像素也提示 SECNet 评估时应区分 synthetic event 与 real event，不应仅用 GoPro/ESIM 结果证明真实场景鲁棒性。

## 8. Survey-Usable Takeaways

- Event-based deblurring 的关键不只是拼接 event voxel 与 blur frame，而是让 event information 参与 spatial frequency selection、frame alignment 和 long-range temporal propagation。
- FCFE 的两个频率轴分别是 feature-map spatial frequency 和展平后的 time-channel joint frequency，不是对 raw event timestamps 直接做 Fourier analysis。
- ELTP 与 BTFF 形成局部和长程的互补 temporal modeling：低分辨率频域 alignment 偏向细节，高分辨率双向 recurrence 偏向整体一致性。
- REVD 的硬件同步 hybrid camera protocol 能暴露 synthetic event/noise 与真实数据之间的泛化差异，但数据规模仍然有限。
- 对 SECNet 而言，本文最有价值的是 frequency filter 与 Event Cloud interface 的设计问题；其 ANN dense operations、GPU FLOPs 和 inference time 不能直接解释为 SNN energy evidence。

## Supplement Points

### Questions and Clarifications

#### 1. 2D FFT 后为什么会有实部和虚部，维度为什么变化？

对一个 $H_s\times W_s$ 的 real-valued feature map 做 2D FFT 后，每个频率位置得到一个 complex coefficient：

$$
Z[u,v]=\sum_{h=0}^{H_s-1}\sum_{w=0}^{W_s-1}X[h,w]e^{-j2\pi(uh/H_s+vw/W_s)}.
$$

因为 $e^{-j\theta}=\cos\theta-j\sin\theta$，每个系数都可以写成 $Z[u,v]=R[u,v]+jI[u,v]$。实部是输入与 cosine basis 的匹配，虚部是输入与 sine basis 的匹配；二者共同记录 frequency amplitude 和 phase。它们不是额外的物理像素，也不是网络另行预测的两组信息，而是同一个 feature map 经过 Fourier projection 得到的两种坐标。

如果输入形状是 $C\times H_s\times W_s$，FFT 输出是 $\mathbb{C}^{C\times H_s\times W_s}$。作者把 real/imaginary parts 在 channel dimension 拼接，于是变为 $\mathbb{R}^{2C\times H_s\times W_s}$。由于输入是 real-valued，频谱具有 conjugate symmetry，只保留宽度方向的非冗余部分后变为 $\mathbb{R}^{2C\times H_s\times(\lfloor W_s/2\rfloor+1)}$。之后生成的 $f_s$ 对这些 frequency bins 逐元素加权，再 inverse FFT 回到 spatial domain。

#### 2. Global channel filtering 在做什么？

Spatial filtering 处理 $H_s,W_s$ 两个空间轴；global channel filtering 则将 $T$ 个时间步和 $C$ 个通道展平为 $M=T C$，对每个空间位置上的长度为 $M$ 的序列做 1D FFT：

$$
\widehat{F(B)}\in\mathbb{R}^{T\times C\times H_s\times W_s}
\rightarrow
\widehat{F(B)}_{1:T}\in\mathbb{R}^{M\times H_s\times W_s}.
$$

这一步得到的不是 image spatial spectrum，而是 time-channel joint spectrum。事件与 blur features 生成 channel attention 和 filter $f_t$，再执行频域逐元素乘法与 inverse 1D FFT，恢复原来的 $T\times C$ 排列。论文称其为 global channel filtering，但从实际 reshape 看，它同时混合了时间和通道；这是作者的联合轴设计，而非纯粹的 channel-only filter。

#### 3. $\widetilde{G(B)}_i$ 是什么，怎么得到？

$\widetilde{G(B)}_i$ 是 ELTP 输出的局部时间对齐特征。以第 $i$ 帧为 reference，先将左、右 supporting blur features 分别与当前/邻帧 event features 拼接并输入 ResBlocks，得到前向和后向 aligned features $G^{(B)f}_i$、$G^{(B)b}_i$。再把两个方向的结果和当前 blur feature 一起送入频域融合：FFT、real/imaginary concatenation、frequency-domain channel attention、inverse FFT 和 ResBlocks。最后与当前 event feature 拼接，形成 $\widetilde{G(B)}_i$。

因此它不是原始 blur feature，也不是 optical flow；它表示“当前帧特征 + 左右邻帧内容 + event-guided local alignment + frequency-domain enhancement”的结果。BTFF 以它为输入，在更高分辨率上继续做前向/后向 long-range propagation。
