---
tags: [event-camera, event-cloud, Fourier, FFT, frequency-aware-learning, scalability]
---

# Summary V2｜Scalable Event Cloud Network for Event-based Classification

## 1. Core Understanding

SECNet 是一个直接处理 Event Cloud 的轻量级 event-based vision backbone，面向 object classification、action recognition 和 human pose estimation。它试图在 raw event 的 fine-grained temporal information、polarity 和 sparsity 与可扩展计算之间取得平衡。

SECNet 的核心数据流是：将 raw events 仅通过 random downsampling 组织为 Event Cloud；先用 Event-based Grouping and Sampling（G&S）构造包含 polarity-aware topology 的局部 groups，再用 Spatial Frequency-aware（SFA）在 grouped feature 的 channel dimension 上做 FFT-filter-iFFT，用 AGG 聚合邻居，最后用 Temporal Frequency-aware（TFA）沿 chronological event/group dimension 做全局 temporal frequency mixing。每个 stage 还通过 CES 更新 Event Cloud 的 centroid coordinates，并通过 residual module 输出更高层 feature。

论文报告 SECNet 在十个 datasets、三类任务上具有有竞争力的结果，并强调 Event Cloud 相比 frame/voxel representation 减少 preprocessing、保留事件顺序，相比 Point Cloud representation 能处理更多 events。SECNet 本身是连续值的 ANN-style event network，不是 fully spiking SNN；它对本项目的直接价值是 Event Cloud hierarchy、空间/时间 Fourier interface 和硬件可实现性，为后续 SECNet-to-TPAMI 的 SNN coupling 提供基线。

## 2. Problem and Motivation

事件相机在局部 illumination change 超过 threshold 时异步产生 event。每个 event 包含 spatial coordinates、timestamp 和 polarity，可写成：

$$
e_i=(x_i,y_i,t_i,p_i).
$$

Frame representation 将一段 event stream 汇总为静态图像，容易接入 VGG、ResNet 等 backbone，但会损失事件顺序和 sparsity。Voxel representation 通过 time bins 保留更多时间结构，但需要将不规则 events 量化到规则网格，增加 transformation 和 memory cost。Point Cloud representation 避免部分转换并保留 coordinates，但已有方法可能忽略 polarity、把 $t$ 当作类似空间坐标 $z$，且在输入点数增大时难以进行充分的长时空 feature extraction。

SECNet 采用 Event Cloud：

- 直接保留 event-level $(x,y,t,p)$ attributes；
- 只进行 downsampling，而不是空间/时间 grid quantization；
- 保留 chronological order，使 temporal index 可以参与后续 TFA；
- 通过 D-FPS、EF-KNN 和 CES 让 polarity 和 learned feature similarity 参与 topology construction；
- 通过 SFA 和 TFA 的 frequency-domain filtering 处理局部 feature interaction 与长距离 temporal dependency。

## 3. Method Overview

原始 event set 为：

$$
E=\{e_i=(x_i,y_i,t_i,p_i)\mid i\in I\},\qquad I=[1,2,\ldots,n].
$$

Event Cloud 是有序子集：

$$
EC=\{e_j=(x_j,y_j,t_j,p_j)\mid j\in J\},\qquad J\subseteq_{\mathrm{ord}}I.
$$

令 $|J|=T_0$，则：

$$
EC\in\mathbb{R}^{T_0\times4}.
$$

Event Cloud 按事件发生顺序排列，并经过 Min-Max normalization。Embedding 后：

$$
F_0=\operatorname{Embed}(EC).
$$

实现中 embedding 是一层 one-dimensional convolution，将 4 维输入映射为 64 维 feature。

第 $i$ 个 stage 的流程是：

$$
G_i,F_{G_i},EC'=G\&S(EC,F_{i-1}),
$$

$$
F_{S_i}=SFA(F_{G_i}),\qquad F_{A_i}=AGG(F_{S_i}),
$$

$$
F_{T_i}=TFA(F_{A_i}),\qquad F_{R_i}=RES(F_{T_i}),
$$

$$
F_i=F_{R_i},\qquad EC=EC'.
$$

经过 $m$ 个 stages 后：

$$
F_{\mathrm{end}}=F_{R_m}.
$$

最终 feature 做 mean/max pooling 并拼接：

$$
F_{\mathrm{final}}=\operatorname{Mean}(F)\oplus\operatorname{Max}(F).
$$

classification head 输出 category，regression head 输出 human pose 的 13 个 skeleton points。SECNet 的三个 hierarchy loops 中，group/centroid 数量逐层减半，feature dimension 逐层增加：

$$
64\rightarrow132\rightarrow268\rightarrow540.
$$

## 4. Key Components and Mechanisms

### 4.1 Event-based Grouping and Sampling

输入第 $i$ 个 G&S stage 的 Event Cloud 和 feature 可抽象为：

$$
EC\in\mathbb{R}^{T_{i-1}\times4},\qquad
F_{i-1}\in\mathbb{R}^{T_{i-1}\times D_{i-1}}.
$$

#### D-FPS

作者使用 learnable scaling vector 对四个 event attributes 进行缩放，然后用 Farthest Point Sampling（FPS）选出一半 events 作为 centroids：

$$
C_i=\operatorname{FPS}(\alpha\cdot EC),
\qquad \alpha\in\mathbb{R}^{4},
\qquad C_i\in\mathbb{R}^{\frac{T_{i-1}}{2}\times4}.
$$

$\alpha$ 的四个分量分别影响 $x,y,t,p$ 在 sampling distance 中的相对作用，因此 polarity 和 temporal coordinate 不只是被拼接到普通输入中，还会影响 centroid 的选择。

#### EF-KNN

以 centroid feature 和当前 feature 为输入，作者根据 feature distance 而不是单纯 coordinate distance 寻找每个 centroid 的 $K$ 个邻居：

$$
G_i,F_{G_i}=\operatorname{KNN}(F_{C_i},F_i,K).
$$

其中：

$$
G_i\in\mathbb{R}^{\frac{T_{i-1}}{2}\times K\times4},
$$

$$
F_{G_i}\in\mathbb{R}^{\frac{T_{i-1}}{2}\times K\times D_{i-1}}.
$$

第一维是 group/centroid 数量，第二维是每个 group 的邻居数，最后一维分别是 coordinate 或 feature dimension。EF-KNN 让 learned feature similarity 参与 neighborhood formation；两个事件即使几何距离不近，也可能因为 feature 相似而被归入同一 group。

#### CES

作者对每个 group 的 coordinates 沿邻居维度求平均，得到更新后的 Event Cloud：

$$
EC'=\operatorname{Mean}(G_i),qquad
EC'\in\mathbb{R}^{\frac{T_{i-1}}{2}\times4}.
$$

因此，每个新的 coordinate token 表示一组 events 的平均 spatial location、average timestamp 和 average polarity。下一 stage 使用更新后的 $EC'$，所以 coordinates 会随层数发生 evolution。

#### Group feature construction

先将 grouped feature 与 grouped coordinates 拼接：

$$
F_{G_i}=F_{G_i}\oplus G_i,
$$

$$
F_{G_i}\in\mathbb{R}^{\frac{T_{i-1}}{2}\times K\times(D_{i-1}+4)}.
$$

随后用 group mean 做 standardization：

$$
M=\operatorname{Mean}(F_{G_i}),
$$

$$
F_{G_i}=\frac{F_{G_i}-M}{\operatorname{Std}(F_{G_i},M)}.
$$

其中：

$$
M\in\mathbb{R}^{\frac{T_{i-1}}{2}\times(D_{i-1}+4)}.
$$

最后，将 centroid feature $F_{C_i}$ broadcast 到 $K$ 个邻居，并与 normalized group feature 拼接：

$$
F_{G_i}=F_{G_i}\oplus F_{C_i},
$$

$$
F_{G_i}\in\mathbb{R}^{\frac{T_{i-1}}{2}\times K\times(2D_{i-1}+4)}.
$$

因此，dimension progression 遵循：

$$
D_i=2D_{i-1}+4.
$$

### 4.2 Fourier Module

SECNet 将 Event Cloud feature 视为一维 ordered signal。对长度为 $T$ 的 signal $x$，DFT 为：

$$
X[k]=\sum_{n=0}^{T-1}x[n]e^{-j\frac{2\pi}{T}kn},
\qquad k=0,1,\ldots,T-1.
$$

inverse DFT 为：

$$
x[n]=\frac{1}{T}\sum_{k=0}^{T-1}X[k]e^{j\frac{2\pi}{T}kn},
\qquad n=0,1,\ldots,T-1.
$$

对于实值输入：

$$
X[T-k]=X^*[k].
$$

因此频谱具有 conjugate symmetry。得到 spectrum 后，作者使用 learnable filter $V$ 做 Hadamard product，再通过 iFFT 返回 feature domain：

$$
X=\operatorname{FFT}(x),
$$

$$
\widehat{X}=V\odot X,
$$

$$
\widehat{x}=\operatorname{iFFT}(\widehat{X}),
$$

$$
\widehat{x}=\sigma(\widehat{x}).
$$

这里 $V$ 可以调节各 frequency component；频域逐元素乘法具有 global mixing 的效果，但实际 efficiency 仍取决于 FFT implementation、memory access 和 hardware mapping。

### 4.3 Spatial-FA、AGG 与 Temporal-FA

#### Spatial-FA

G&S 后的 grouped feature 可写为：

$$
F_{G_i}\in\mathbb{R}^{T_i\times K\times D_i}.
$$

SFA 沿 channel dimension $D_i$ 做 Fourier transform。这里的 $D_i$ 不是原始图像的 $x$ 或 $y$ 轴；原始 spatial information 已经被 embedding 和 G&S 抽象到 feature channels 中。对每个 group 和 neighbor 的 feature vector，SFA 做 channel-wise frequency mixing。

作者将单次 MLP-based channel transformation 的 complexity 视为：

$$
O(D_i^2),
$$

而 FFT-based transformation 约为：

$$
O(D_i\log_2D_i).
$$

因此，SFA 用 frequency-domain multiplication 替代 repeated MLP，降低局部 feature abstraction 的理论复杂度。

#### AGG

SFA 输出 $F_{S_i}$ 后，AGG 在 $K$ 个 neighbors 上计算 soft attention：

$$
A_i=\operatorname{SoftMax}(\operatorname{MLP}(F_{S_i})),qquad
A_i\in\mathbb{R}^{T_i\times K}.
$$

然后加权求和：

$$
F_{A_i}=A_i\cdot F_{S_i},qquad
F_{A_i}\in\mathbb{R}^{T_i\times D_i}.
$$

AGG 没有显式 Fourier transform；它沿 neighbor dimension 压缩局部 group：

$$
[T_i,K,D_i]\rightarrow[T_i,D_i].
$$

其物理含义是把一个 local event neighborhood 总结成一个 group-level token，attention weight 较大的 neighbors 对该局部表示贡献更大。

#### Temporal-FA

AGG 后，events/groups 仍然按 chronological order 排列。TFA 沿 event/group number dimension $T_i$ 做 Fourier transform：

$$
[T_i,D_i]\rightarrow\text{FFT along }T_i\rightarrow\text{global temporal filtering}\rightarrow[T_i,D_i].
$$

因此，TFA 中的 frequency bin 描述 group feature 沿事件顺序的变化速度。低频可表示较慢的 long-range trend，高频可表示较快的 temporal variation。

不过，$T_i$ 首先是按照事件发生顺序排列的离散 index，不一定是等间隔 physical time sampling。因此 TFA 的 frequency 更准确地称为 event-order/group-sequence frequency；在采样间隔近似均匀时，才可以更直接解释为物理 temporal frequency。

SFA 与 TFA 的区别是：SFA 处理一个 local group 内 learned feature channels 的变化，AGG 将 neighbors 压缩，TFA 再处理不同 ordered groups 之间的长距离 temporal dependency。

### 4.4 Residual Module and Final Heads

TFA 输出通过 basic residual module 得到：

$$
F_{R_i}=RES(F_{T_i}).
$$

每个 stage 结束后更新 $F_i=F_{R_i}$，同时用 CES 更新 Event Cloud。完成全部 stages 后，对最终 feature 做 mean/max pooling，并将结果送入 classification 或 pose regression head。SECNet 是连续值 network，本文没有使用 spiking neuron、membrane state 或 surrogate-gradient training。

## 5. Experiments and Main Evidence

作者在十个 event-based datasets、三类任务上评估 SECNet：object classification 使用 NMNIST、N-Caltech101、CIFAR10-DVS、N-CARS 和 ASL-DVS；action recognition 使用 DVS128 Gesture、Daily DVS、UCF101-DVS 和 THUE-ACT-50；human pose estimation 使用 DHP19。

实现使用 AdamW、initial learning rate 0.001、Cosine scheduler、最多 150 epochs，并在 AMD 7950X、RTX 4090 上训练。classification 和 action recognition 使用 Accuracy，pose estimation 使用 MPJPE；姿态输出包含 13 个 skeleton key points。

Event Cloud 的 preprocessing time 在作者测试的三个 datasets 上最短；voxel representations 即使 backbone 较轻，也需要接近 Event Cloud 十倍的 data transformation time。该结果支持 Event Cloud 减少 representation-conversion overhead 的主张，但属于特定 datasets、实现和硬件设置下的计时证据。

在 object classification 上，SECNet 相比此前 SOTA Point Cloud method 提升 27%，并在各 object datasets 上与 voxel-based SOTA 具有竞争力。作者将其归因于 Event Cloud 同时保留更高 event density、polarity 和 raw coordinates。

在 action recognition 上，SECNet 在三个 datasets 上取得平均 SOTA；在 UCF101-DVS 上比 VMST-Net 高 16%。该结果支持保留细粒度 timestamp 对动作任务的重要性，但不能单独证明所有提升都来自 representation，因为 backbone 和 frequency modules 也同时发生变化。

在 high-resolution setting 中，SECNet 比其他方法高 5%，并且相对 EV-ACT 使用约一个数量级更少的 hardware resources，报告为 1.27M parameters / 0.971 GMACs 对比 21.3M / 14.5 GMACs。SECNet 在 human pose estimation 中达到 point-based 和 voxel-based methods 的 SOTA，model GMACs 为 0.160，约为 Point Transformer 的 2%，server inference time 为 4.37 ms/sample。

消融实验显示：移除 D-FPS 中的 $α$ 或 EF-KNN 后，三个 datasets 上性能均下降；移除 SFA 或 TFA 也会降低结果，DHP19 对 TFA removal 尤其敏感；只在 input level 使用 polarity，或完全移除 polarity，均不如 structural-level integration。这些结果支持 G&S、SFA、TFA 和 polarity structural modeling 的联合贡献，但不能把每项增益完全归因于单一机制。

随着 input event number 增加，SECNet 的性能能够继续提升，而 PointNet++ 和 TTPOINT 的收益更早饱和。SECNet 的 Temporal-FA 在 frequency domain 中建模 global temporal relationships，因此作者认为它比 LSTM 更适合较长 event sequences。

硬件效率证据包含 server runtime 和 FPGA measurement。Zynq UltraScale+ MPSoC 在 200 MHz 下的实验中，spatial MLP 在三个 stages 分别需要 6,302,723、12,595,715 和 25,191,430 cycles，对应 31.51、62.98 和 125.96 ms；FFT-based SFA accelerator 需要 393,859 cycles，对应 1.97 ms，并且约比 spatial baseline 少 16、32 和 64 倍 cycles。SECNet server throughput 报告为 229.7 FPS。上述结果是具体硬件和实现上的 measurement，不应与 MAC/GMAC operation estimate 混为真实通用能耗结论。

## 6. Strengths and Limitations

本文的优势是保留 raw event 的 event-level coordinates、timestamp 和 polarity，同时通过 hierarchy、feature-based grouping 和 frequency-domain feature extraction 扩展到较大事件数量。SFA 为 local channel mixing 提供了较低复杂度的替代路径，TFA 则在 chronological groups 上提供 global temporal modeling。作者还给出了 preprocessing、server runtime 和 FPGA cycles 等多层效率证据。

主要限制包括：Event Cloud 虽然保留事件顺序，但 TFA 的 event number axis 不一定是均匀物理时间轴；SFA 的 channel-frequency 不是可以直接解释为 physical spatial frequency。D-FPS、EF-KNN、CES、attention aggregation 和 FFT 同时改变了 representation 与计算路径，因此消融不能将全部增益唯一归因于 Fourier。

此外，SECNet 不是 SNN；论文没有给出 spike、membrane potential 或 neuromorphic event-driven arithmetic。FFT/filter/iFFT 的复杂数和 memory behavior 也需要专门硬件映射。效率结论应区分 preprocessing time、GMAC estimate、server latency、FPGA cycles 和真实 chip energy。随着 event number 增加，runtime 和 GMACs 仍会增加，所以 scalability 是相对改善而不是对输入规模完全不敏感。

## 7. Relation to SECNet Extension Direction

SECNet 本身就是 SECNet-to-TPAMI extension 的 starting point，因此本节不建立 Survey paper-to-paper edge，只讨论其对后续方向的直接接口。

最值得保留的是三层 frequency interface。第一，SFA 将 G&S 后的 local Event Cloud group feature 沿 channel axis 做 frequency mixing，可作为局部空间关系与 feature topology 的轻量替代。第二，AGG 将邻居维度压缩为 group token，提供 local-to-global 的接口。第三，TFA 沿 chronological group axis 做 global temporal filtering，为 Event Cloud 的长时序建模提供外部 global path。

对 SNN coupling，不能直接把 SECNet 的 continuous FFT module 宣称为 spiking module。后续需要明确 complex spectrum 如何编码为 spikes 或 membrane states，frequency filter 如何在 sparse event transition 下实现，以及 CES、normalization、attention 和 residual state 的 memory/access cost。SpikF 等 SNN-Fourier 工作可作为 coupling 机制参考，但 SECNet 的 Event Cloud 是 irregular event set，不能直接套用规则 time-series S-FFT。

对 Event Cloud extension，建议分别定义 spatial、temporal 和 joint spatiotemporal frequency。SFA 当前的 spatial frequency 实际位于 learned channel axis；若要获得更直接的 physical spatial spectrum，需明确 Event Cloud 到规则 spatial grid、point neighborhood 或 graph coordinate 的接口。TFA 当前依赖 chronological order；对于异步硬件和不规则 timestamp，必须区分 event-order frequency 与 physical-time frequency。

## 8. Survey-Usable Takeaways

- Event Cloud 的核心不是新的 dense voxel，而是接近 raw event 的有序 event subset：保留 $(x,y,t,p)$，只用 downsampling 控制规模。
- Polarity 在 SECNet 中参与 D-FPS、EF-KNN、coordinate evolution 和 grouped feature construction，因此是 structural information，而不只是 input channel。
- SFA 沿 learned channel dimension 做 local frequency mixing；AGG 压缩 neighbors；TFA 沿 chronological group dimension 做 long-range temporal mixing。
- SECNet 的频率轴必须结合 tensor axis 解释：SFA 的频率不是直接 physical spatial frequency，TFA 的频率也不必然是严格 Hz。
- 论文提供 preprocessing、GMAC、server runtime 和 FPGA cycles 等不同证据；这些指标不能互相替代，也不能自动等同于真实 neuromorphic energy。
- 对 TPAMI extension，最关键的开放接口是 Event Cloud hierarchy 如何与 SNN spike/membrane computation 结合，并且如何在不规则 timestamp 下保持 frequency semantics。

## Supplement Points

### Questions and Clarifications

#### 1. Farthest Point Sampling 是什么？

Farthest Point Sampling（FPS）不是随机挑点，而是尽量从输入点中选出分布较分散的代表点。先选择一个点，再计算每个未选点到已选点集合的最小距离，并选择这个最小距离最大的点，重复直到达到目标数量：

$$
d(p)=\min_{q\in S_{\mathrm{selected}}}\operatorname{dist}(p,q),
$$

$$
p_{\mathrm{next}}=\arg\max_{p\notin S_{\mathrm{selected}}}d(p).
$$

SECNet 使用 D-FPS：

$$
C_i=\operatorname{FPS}(\alpha\cdot EC).
$$

其中 $α$ 是四维 learnable scaling vector，会改变 $x,y,t,p$ 在 sampling distance 中的相对影响。因此 SECNet 学习的不只是“选哪些点”，还包括空间、时间和 polarity 哪些维度应该更影响采样。

#### 2. $C_i$ 的维度和“对一半 events 进行 downsampling”是什么意思？

若第 $i-1$ 个 stage 有 $T_{i-1}$ 个 events，SECNet 选出其中一半作为 centroids，因此 centroid 数量是 $T_{i-1}/2$。每个 centroid 仍有四个属性 $(x,y,t,p)$，所以：

$$
C_i\in\mathbb{R}^{\frac{T_{i-1}}{2}\times4}.
$$

例如，若输入有 10240 个 events，则第一个 stage 可选择 5120 个 centroids；下一 stage 再减半为 2560。这里减少的是 event/token 的数量，不是把每个 event 的四个属性删掉一半。经过 CES 后，下一层还会使用每个 group 的平均 coordinate 作为更新后的 Event Cloud coordinate。

#### 3. Event-based G&S 的完整流程是什么？

输入可写为：

$$
EC\in\mathbb{R}^{T_{i-1}\times4},qquad
F_{i-1}\in\mathbb{R}^{T_{i-1}\times D_{i-1}}.
$$

首先，embedding 将 4 维 event attributes 映射为 learned feature；然后 D-FPS 选出一半 centroids。接着，EF-KNN 根据 feature distance 为每个 centroid 找 $K$ 个 neighbors，生成：

$$
G_i\in\mathbb{R}^{\frac{T_{i-1}}{2}\times K\times4},qquad
F_{G_i}\in\mathbb{R}^{\frac{T_{i-1}}{2}\times K\times D_{i-1}}.
$$

CES 沿 $K$ 个 neighbors 求坐标平均：

$$
EC'=\operatorname{Mean}(G_i).
$$

随后将 feature 和 coordinate 拼接、按 group mean standardize，再与 centroid feature 拼接，最终得到：

$$
F_{G_i}\in\mathbb{R}^{\frac{T_{i-1}}{2}\times K\times(2D_{i-1}+4)}.
$$

因此，一个 stage 同时完成三件事：减少 group 数量、根据 feature similarity 构造 local neighborhoods、增加每个 group 的 feature dimension。下一 stage 使用 $EC'$ 和新的 grouped feature，而不是完全回到原始 events。

#### 4. 为什么 frequency-domain multiplication 的 complexity 是 $O(D_i\log_2D_i)$？

如果 MLP 将 $D_i$ 维 feature 映射到相近维度，weight matrix 近似为 $D_i\times D_i$，矩阵乘法成本约为：

$$
O(D_i^2).
$$

FFT 和 iFFT 对长度为 $D_i$ 的 signal 的成本约为：

$$
O(D_i\log_2D_i).
$$

频域中的 Hadamard product：

$$
\widehat X=V\odot X
$$

只需逐元素处理，成本约为 $O(D_i)$，因此整体由 FFT/iFFT 主导，写成 $O(D_i\log_2D_i)$。当 $D_i=540$ 时，$D_i^2=291600$，而 $D_i\log_2D_i$ 约为 4900，理论上约有 60 倍的单次复杂度差异。实际 network 还要在 $T_i\times K$ 个位置重复执行，且真实 runtime 受 FFT implementation、memory access 和硬件并行度影响。

#### 5. SFA、AGG、TFA 分别处理什么频率变化？

若 grouped feature 为：

$$
F_{G_i}\in\mathbb{R}^{T_i\times K\times D_i},
$$

SFA 固定一个 group 和 neighbor，沿 $D_i$ channel dimension 做 Fourier transform。它描述的是 learned feature channels 的变化模式：channel response 平滑时偏低 channel-frequency，channel response 快速交替时偏高 channel-frequency。它不是直接对原始 $x,y$ 图像轴做 FFT，因此不能直接解释为 physical spatial frequency。

AGG 不执行 Fourier transform，而是在 $K$ 个 neighbors 上计算 attention 并加权求和：

$$
[T_i,K,D_i]\rightarrow[T_i,D_i].
$$

它把一个 local event neighborhood 压缩为一个 group-level token。attention weight 是任务相关的 learned contribution，不应直接解释为某个物理事件的因果重要性。

TFA 固定一个 feature channel，沿按 chronological order 排列的 $T_i$ 个 groups 做 Fourier transform：

$$
[T_i,D_i]\rightarrow\text{FFT along }T_i\rightarrow[T_i,D_i].
$$

它描述 group feature 随事件顺序变化的快慢，因此比 SFA 更接近 temporal frequency。但如果事件 timestamp 不均匀，TFA 首先表示 event-order frequency，不是严格物理 Hz。

#### 6. 结合 Appendix F 和 G，SECNet 的完整算法流程是什么？

Appendix F 规定 FFT 的轴：SFA 作用于 channel dimension，例如 132；该轴承载已经由 feature abstraction 编码的 spatial information。TFA 作用于 event number dimension，例如 2048；events 严格按 emitted order 排列，因此该轴承载 discretized temporal information。

Appendix G 的完整流程是：

$$
EC\rightarrow F=\operatorname{Embedding}(EC)
$$

重复 $m$ 个 stages：

$$
G,F_G,EC'=G\&S(EC,F),
$$

$$
F_S=SFA(F_G),
$$

$$
F_A=AGG(F_S),
$$

$$
F_T=TFA(F_A),
$$

$$
F_R=RES(F_T),qquad F=F_R,quad EC=EC'.
$$

实现中 embedding 后 feature dimension 为 64，三个 loops 中逐渐变为 132、268、540；group/centroid 数量在每个 loop 减半。最后：

$$
F_{\mathrm{final}}=\operatorname{Mean}(F)\oplus\operatorname{Max}(F),
$$

再输入 classifier 或 regressor。它体现的层级逻辑是：先在 local group 内做 channel-frequency mixing，再聚合 neighbors，随后在 ordered groups 上做 global temporal-frequency mixing。

#### 7. 为什么 SFA 和 TFA 的“物理含义”不同？

SFA 处理的是网络内部的 channel axis。原始 $x,y$ 的空间信息在 embedding、G&S 和 feature concatenation 后被编码进 channels，因此 SFA frequency 是 learned representation 的变化频率。它可以反映局部空间关系、时间连续性和 polarity relevance 的组合，但论文没有证明某个 channel-frequency bin 对应某个明确的 physical spatial wavelength。

TFA 处理的是 ordered group axis。由于 groups 继承了 events 的 chronological order，TFA 可以让早期和晚期 groups 通过 global frequency coefficients 发生交互，建模 long-range temporal dependency。但 group index 可能不是等间隔 physical time，因此需要在 extension 中明确 timestamp weighting、resampling 或 continuous-time Fourier semantics。
