---
tags:
  - event-camera
  - event-cloud
  - point-based-network
  - camera-pose-relocalization
  - temporal-attention
  - Bi-LSTM
  - non-spiking
---

# Summary V2｜A Simple and Effective Point-based Network for Event Camera 6-DOFs Pose Relocalization

## 1. Core Understanding

PEPNet 是一个面向 event-camera 6-DOFs Camera Pose Relocalization（CPR）的 **non-spiking point-based network**。它将事件表示为 $(x, y, t)$ Event Cloud，通过 hierarchical point structure 提取空间特征和隐式时间特征，再利用 Attentive Bi-directional LSTM（A-Bi-LSTM）建模显式时间依赖，最终回归相机的三维平移与三维 Euler-angle rotation。

本文不包含 spiking neuron、membrane dynamics、surrogate gradient 或 spike-driven computation，因此不属于 SNN 方法。在综述中，它更适合作为 **Event Cloud representation 与 non-spiking temporal modeling** 的代表性对照。

## 2. Problem and Motivation

现有 event-based CPR 方法通常先将事件聚合为 event image、time surface 或其他 frame-like representation，再使用 CNN、LSTM 或 DSAC-style hybrid pipeline。此类方法便于复用传统视觉网络，但会将大量具有不同 timestamp 的事件压缩到少量图像或通道中，难以完整保留单事件级别的时间信息；复杂的去噪、卷积和几何求解流程也会增加部署成本。

将事件写成 $(x, y, t)$ pseudo-Point Cloud，可以避免 event-to-frame conversion，并保留稀疏的时空分布。然而，Event Cloud 与普通 $(x, y, z)$ Point Cloud 并不等价：$t$ 是时间坐标，而不是空间深度；事件之间还具有明确的时间先后关系。传统 point network 的 set-based aggregation 和缺少 recurrent temporal modeling 等设计，不能充分表达事件沿时间轴的动态联系。

PEPNet 因此采用 point hierarchy 处理稀疏 event points，并通过 temporal aggregation 与 A-Bi-LSTM 补充时间建模，同时控制参数量和 FLOPs。

## 3. Method Overview

原始事件序列表示为：

$$
\mathcal{E}
=
\left\{
e_k = (x_k, y_k, t_k, p_k)
\right\}_{k=1}^{n}.
$$

针对每个 pose label，模型从事件流中截取一个 sliding window，将窗口内事件采样为固定数量的 points，并归一化为：

$$
P_i^{N}
=
\left(
\frac{X_i}{w},
\frac{Y_i}{h},
\frac{T_i-t_j}{t_l-t_j}
\right).
$$

IJRR 中默认使用 $N = 1024$，M3ED 中使用 $N = 2048$。从正文给出的输入维度和公式看，主干网络使用 normalized $(x, y, t)$；虽然原始事件定义包含 polarity $p$，论文未说明其被作为额外 point feature 输入主干。

随后，三个 hierarchy stages 依次执行：

$$
\text{FPS}
\rightarrow
\text{KNN}
\rightarrow
\text{standardization}
\rightarrow
\text{local residual MLP}
\rightarrow
\text{temporal aggregation}
\rightarrow
\text{global residual MLP}.
$$

最终 stage 输出按 timestamp 组织的高层 point-feature sequence。该序列经过 A-Bi-LSTM 和 temporal attention 后被汇聚为一个全局特征，再由 fully connected regressor 输出：

$$
\hat{\mathbf{p}}\in\mathbb{R}^{3},
\qquad
\hat{\mathbf{q}}\in\mathbb{R}^{3},
$$

分别表示 translation 和 rotational Euler angles。

## 4. Key Components and Mechanisms

### 4.1 Event Cloud Hierarchy

PEPNet 不将事件转换为 frame，但仍包含 sliding-window segmentation、fixed-number sampling 和 normalization。因此，论文所说的 “raw Event Cloud” 更准确地理解为：**未经过 frame-like representation conversion，但已经经过窗口截取、采样和归一化的 event points**。

每个 hierarchy stage 使用：

$$
P_i^{S}
=
\operatorname{FPS}(P_i^{N}),
\qquad
P_i^{G}
=
\operatorname{KNN}(P_i^{N},P_i^{S}).
$$

FPS 选择 centroids，KNN 为每个 centroid 构造 $K = 24$ 个局部邻居。邻居坐标相对于 centroid 做中心化，并按照 local standard deviation 进行缩放，再由带 residual connection 的 MLP 提取特征。标准 PEPNet 的三个 stage feature dimensions 为 $[64, 128, 256]$，PEPNettiny 为 $[16, 32, 64]$。

由于 normalized $t$ 与 $x, y$ 一同参与 point processing，时间坐标会影响 neighborhood construction 和 feature extraction。但 $t$ 与空间坐标并非同一种物理量，论文没有系统分析该距离度量对 window length、sensor resolution 和 motion scale 的敏感性。

### 4.2 Temporal Aggregation

对一个 local group 的 features：

$$
F_{\mathrm{local}}
=
\left(
F_{t_1},
F_{t_2},
\ldots,
F_{t_K}
\right),
$$

PEPNet 计算每个 point 的 scalar attention weight：

$$
A
=
\operatorname{SoftMax}
\left(
\operatorname{MLP}(F_{\mathrm{local}})
\right),
$$

并进行加权聚合：

$$
F_{\mathrm{aggre}}
=
\sum_{k=1}^{K}
a_{t_k}F_{t_k}.
$$

与 MaxPooling 相比，该方法允许多个 event points 共同参与输出，而不是只保留各 feature channel 的最大响应。需要注意的是，weighted sum 本身仍然属于集合聚合，并不直接表达事件之间的先后转移；它主要保留的是已经编码在 timestamp-conditioned point features 中的时间信息。

### 4.3 A-Bi-LSTM

Hierarchy 中的 point features 虽然受到 $t$ 的影响，但主要由并行 point processing 得到，缺少显式 recurrent dependency。PEPNet 将最终 hierarchy stage 的 chronological feature sequence 输入 Bi-LSTM：

$$
\overrightarrow{h}_t
=
\operatorname{LSTM}
\left(
x_t,\overrightarrow{h}_{t-1}
\right),
$$

$$
\overleftarrow{h}_t
=
\operatorname{LSTM}
\left(
x_t,\overleftarrow{h}_{t+1}
\right).
$$

正向与反向输出拼接后，再通过 attention 沿 sequence dimension 汇聚。Fig. 6 显示序列起点和终点附近的 attention weights 较高，作者据此推测 CPR 更依赖窗口首尾之间的 feature difference。

由于模型包含 backward recurrence，PEPNet 必须等待完整 event window 后才能输出 pose，因此它属于 window-level inference，而不是严格的 causal event-by-event processing。论文式（14）—（16）只是 bidirectional recurrence 的概念性简写，并不是标准 LSTM gates 的完整公式。

### 4.4 Pose Regression Loss

Pose regressor 使用 translation loss、rotation loss 和 weight regularization：

$$
\mathcal{L}
=
\alpha
\left\|
\hat{\mathbf{p}}-\mathbf{p}
\right\|_2
+
\beta
\left\|
\hat{\mathbf{q}}-\mathbf{q}
\right\|_2
+
\lambda
\sum_i w_i^2.
$$

其中，$\alpha$ 和 $\beta$ 用于平衡 translation 与 rotation。论文公式写成 L2 norm，但实验部分又使用 MSE 表述，因此训练实现究竟采用 norm 还是 squared error，正文并不完全一致。Rotation 使用三维 Euler angles，而不是 quaternion。

## 5. Experiments and Main Evidence

实验使用室内 IJRR 和室外夜间 M3ED。IJRR 同时采用 random split 和 chronological novel split。Random split 随机选择 70% sequences 作为训练集，train/test 分布较为接近；novel split 使用前 70% sequences 训练、后 30% sequences 测试，更容易暴露 temporal distribution shift。

在 IJRR random split 上，PEPNet 的平均 translation error 和 rotation error 分别为 0.013 m 和 0.904°。模型包含 0.774 M parameters，计算量为 0.459 G FLOPs。作为对比，CNN-LSTM 的平均误差为 0.019 m 和 1.591°，参数量为 12.63 M，计算量为 1.998 G FLOPs。PEPNettiny 仅包含 0.064 M parameters，约为 CNN-LSTM 的 0.5%，平均误差仍达到 0.019 m 和 1.306°。摘要中的 IJRR “38% improvement”与 translation 和 rotation 的综合相对改善大致一致。

在 novel split 上，PEPNet 的平均误差上升至 0.029 m 和 2.13°，说明其对时间分布变化存在较明显的 overfitting。尽管如此，它仍略优于论文列出的 AECRN，后者的平均误差为 0.035 m 和 2.23°。论文在 RTX 4090 server 上报告的推理时间为 6.7 ms per sample，主要耗时来自 grouping and sampling；该结果不是 edge-device latency，也未明确覆盖完整的 sensor-to-pose pipeline。

在 M3ED 的五个 outdoor-night sequences 上，PEPNet 的平均误差为 0.372 m 和 1.04°，优于 CNN-LSTM 的 0.430 m 和 2.197°，但并非在每个 sequence、每个指标上都领先。摘要中的 33% improvement 是 translation error 和 rotation error 两项相对改善百分比的平均值，而不是统一的 $T + R$ metric。

Ablation results 表明，temporal aggregation 和 recurrent temporal modeling 都能带来收益。完整的 hierarchy + Bi-LSTM + temporal aggregation 在 `shape translation` sequence 上达到 0.011 m 和 0.582°。Bi-LSTM 相比单向 LSTM 的独立增益较小，主要优势来自 hierarchy、attention 与 recurrent modeling 的组合。

## 6. Strengths and Limitations

**Strengths**

- 避免 event-to-frame conversion，直接处理 normalized $(x, y, t)$ Event Cloud。
- 将 hierarchical point processing、attention aggregation 与 recurrent temporal modeling 组合为轻量 CPR pipeline。
- 参数量和 FLOPs 明显低于主要 frame-based baselines，PEPNettiny 展示了较好的 accuracy–size trade-off。
- 同时报告 random split、novel split、M3ED、module ablation 和 server inference time。

**Limitations / Questions**

- 本文不是 SNN；Event Cloud 的稀疏输入不等同于 spike-driven computation。
- Polarity 未出现在主干输入公式和维度中，论文也未说明其被作为额外 feature 使用。
- 论文声称 FPS/KNN 后严格保持 timestamp order，但没有充分说明具体的重排序实现。
- Bi-LSTM 是非因果模块，必须等待完整 window 后才能输出。
- Novel split 暴露出较明显的 distribution shift 和 scene-specific overfitting。
- 参数量、FLOPs 与 RTX 4090 latency 不能直接证明 ultra-low-power edge deployment；论文没有提供真实 energy measurement。
- Euler-angle regression 和固定的 translation–rotation weights 可能对场景与旋转表示较为敏感。

## 7. Relation to Other Papers and Survey Taxonomy

相较于 event-image + CNN/LSTM 方法，PEPNet 保留了单事件 timestamp；相较于 RWEI + DSAC*，它避免了复杂的 representation conversion 与 geometric hybrid pipeline；相较于普通 PointNet/PointNet++，它针对 Event Cloud 增加了 temporal aggregation 和 A-Bi-LSTM。

在综述 taxonomy 中，它属于：

- **Event Cloud / point-based event representation**
- **Non-spiking temporal modeling**
- **Event-based camera pose relocalization**
- **Lightweight ANN comparator for SNN methods**

它适合用于说明：event timing 可以通过 point coordinates、attention 和 recurrent networks 加以利用，而不一定依赖 SNN；同时，sparse event input 与 spike-driven computation 是两个不同概念。

## 8. Survey-Usable Takeaways

- Takeaway 1: PEPNet 将 normalized $(x, y, t)$ Event Cloud 直接输入 hierarchical point network，避免 frame-like representation，但仍依赖 windowing、fixed-point sampling、FPS 和 KNN。
- Takeaway 2: Hierarchy 编码 timestamp-conditioned implicit temporal features，A-Bi-LSTM 则显式建模高层 feature sequence 的前后依赖。
- Takeaway 3: Temporal attention 比 MaxPooling 保留更多 local point information，但 weighted sum 本身并不直接建模 temporal order。
- Takeaway 4: PEPNet 在 IJRR 和 M3ED 的论文协议中取得了有竞争力的结果，并显著降低参数量和 FLOPs，但 novel split 显示其泛化仍受到 distribution shift 的影响。
- Takeaway 5: PEPNet 是 non-spiking point-based event-camera method，可作为 point-SNN 或其他稀疏 SNN pipeline 的 ANN 对照。

## Supplement Points

### Additional Technical Details

#### 1. Permutation invariance 的含义，以及 Event Cloud 真正需要解决的问题

普通 Point Cloud 表示无序几何集合。只要每个 point 的坐标不变，输入排列不应影响模型输出：

$$
F(p_1, p_2, \ldots, p_N)
=
F(p_{\pi(1)}, p_{\pi(2)}, \ldots, p_{\pi(N)}).
$$

PointNet 常通过 MaxPooling 等 symmetric function 实现 permutation invariance，因为普通 $(x, y, z)$ Point Cloud 的几何意义由 point coordinates 决定，而不是由数据在内存中的排列顺序决定。

Event Cloud 中每个 point 为 $(x, y, t)$。严格来说，只要 timestamp $t$ 保留在每个 tuple 中，把这些 tuples 重新排列并不会改变同一个 Event Cloud。因此，“Event Cloud 与 permutation invariance 冲突”这一表述并不完全严谨。

真正的问题是：传统 set-based point network 通常不会显式建模：

$$
t_1<t_2<\cdots<t_N
$$

所对应的 temporal dependency，并且常通过 symmetric pooling 将一组 point features 压缩为无序表示。Event-camera motion information 需要保留 timestamp-conditioned features，并进一步建模前后事件之间的动态联系。PEPNet 真正针对的是“仅把 events 当作无序几何集合、缺少显式时间关系建模”的处理方式，而不是否定 permutation invariance 本身。

#### 2. 隐式时间特征与显式时间特征

PEPNet 将 timestamp $t$ 作为 point coordinate：

$$
p_i = (x_i, y_i, t_i).
$$

因此，$t_i$ 会参与 normalization、FPS/KNN neighborhood、local standardization、MLP feature extraction 和 attention aggregation。即使 hierarchy 没有 recurrent state，其输出 feature 也已经受到时间位置和时空邻域的影响。作者将这种通过坐标与并行 point processing 编码的时间信息称为 **implicit temporal feature**。

隐式时间特征具有以下特点：

- feature 能够包含 point 的 temporal position；
- neighborhood construction 可以受到 temporal distance 的影响；
- point processing 仍主要并行完成；
- 没有显式状态递推来表达前后时间位置之间的依赖。

A-Bi-LSTM 提取的是 **explicit temporal feature**。最终 hierarchy 输出被组织为 chronological feature sequence：

$$
x_1,x_2,\ldots,x_T,
$$

并通过：

$$
\overrightarrow{h}_t
=
\operatorname{LSTM}
\left(
x_t,\overrightarrow{h}_{t-1}
\right),
$$

$$
\overleftarrow{h}_t
=
\operatorname{LSTM}
\left(
x_t,\overleftarrow{h}_{t+1}
\right)
$$

显式建立当前 feature 与前后时间位置之间的 recurrent dependency。

简而言之：

- **隐式时间特征**：时间作为 coordinate 和 point feature 被静态、并行地编码；
- **显式时间特征**：不同时间位置通过 recurrent state 建立序列依赖。
