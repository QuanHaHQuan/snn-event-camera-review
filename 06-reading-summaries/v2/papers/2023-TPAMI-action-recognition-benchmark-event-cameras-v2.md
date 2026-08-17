---
tags: ["event camera", "action recognition", "EV-ACT", "LMFR", "EVF", "ESFN", "ESTA", "THU E-ACT-50", "benchmark", "non-SNN"]
---

# Summary V2｜Action Recognition and Benchmark Using Event Cameras

## 1. Core Understanding

本文提出了一个面向 event-camera action recognition 的 CNN-based framework：EV-ACT，并构建 THU E-ACT-50 与 THU E-ACT-50-CHL 两个大规模 benchmark。方法由 Event Voxel Filtering、Learnable Multi-Fused Representation、Event-based Slow-Fast Network 和 Event-based Spatial Temporal Attention 组成。

本文不是 SNN 方法。它将异步 events 转换为 grid-based tensors，再交给 ImageNet-pretrained ResNet 处理，因此在综述中应归入 **non-spiking event-CNN、event representation、action-recognition benchmark 与 embedded deployment baseline** 路线。

## 2. Problem and Motivation

本文试图同时解决 event-based action recognition 的数据和方法两方面不足。

一方面，早期 PAF、DHP19、N-HAR、DailyAction 等公开数据集在样本量、动作类别或现实应用覆盖上有限，难以系统评估复杂动作、交互动作、健康监测动作以及不同光照和视角条件。另一方面，event stream 是不规则 tuple list，不能直接输入标准 CNN；Event Frame、Event Count、SAE、Event Voxel、EST 等 grid-based representations 分别保存 polarity、event density、timestamp 或 temporal bins，没有单一表示能够完整保留所有信息。

因此，作者不仅提出识别网络，也发布 50 类、超过 12,830 条录制的 benchmark，并设计从 event filtering、representation fusion、dual-temporal modeling 到 attention 的完整 pipeline。论文的主要价值不是单一高度原创的模块，而是 benchmark、representation study、系统整合和部署验证的组合。

## 3. Method Overview

原始 event stream 表示为：

$$
E
=
\left\{e_k\right\}_{k=1}^{N}
=
\left\{
\left(x_k,y_k,t_k,p_k\right)
\right\}_{k=1}^{N}
$$

其中 `x,y` 是像素坐标，`t` 是时间戳，`p` 是 polarity。

完整流程为：

```text
Raw event stream
→ Event Voxel Filtering
→ Variance-based post-processing
→ Multiple basic event representations
→ Learnable Multi-Fused Representation
→ Slow / Fast dual pathways
→ Spatial-temporal attention
→ Pooling, concatenation and classifier
→ Action class
```

EVF 先把 events 看成 `X-Y-T` point cloud，并将 polarity 作为属性，在时空 voxel 内用平均坐标替代多个原始 events。LMFR 再把 filtered events 构造成多种基础表示，经 learnable convolution 和 normalization 后沿 channel dimension 拼接为：

$$
R_f\in\mathbb{R}^{C\times T\times H\times W}
$$

ESFN 并不是把一个固定 tensor 直接变形为 slow/fast 两路，而是对同一段 filtered events 使用两种 time-bin discretization，分别得到 coarse-temporal 和 fine-temporal representations。两路 backbone 提取特征后，经 ESTA 加权、pooling、concat 和 linear layer 输出类别。

## 4. Key Components and Mechanisms

### 4.1 Event Voxel Filtering

EVF 对 positive 和 negative events 分开处理，在归一化后的 `X-Y-T` 空间中划分 voxels。同一 voxel 内、同一 polarity 的 events 被压缩为一个代表点，其坐标为该 voxel 内坐标的均值：

$$
\bar{x}*i=
\frac{1}{N_i^p}
\sum*{k=1}^{N_i^p}x_k
$$

$$
\bar{y}*i=
\frac{1}{N_i^p}
\sum*{k=1}^{N_i^p}y_k
$$

$$
\bar{t}*i=
\frac{1}{N_i^p}
\sum*{k=1}^{N_i^p}\alpha F(t_k)
$$

这里 `F` 对 timestamp 归一化，`alpha` 将时间尺度调整到与空间坐标相近。随后，variance-based post-processing 删除 event count 过低的 voxels，以进一步过滤孤立噪声。原文写成删除“低于 3 个标准差”的 voxels，但没有清晰给出阈值公式，属于 `Needs further check`。

EVF 的主要作用不是大幅提升 accuracy，而是将 event points 平均减少约 `5–10` 倍，从而降低 representation construction、memory 和后续网络处理负担。适中的时空 voxel size 最好；过小不能有效降采样，过大则损失动作结构。

### 4.2 Learnable Multi-Fused Representation

Event Frame、Event Count、SAE、Event Voxel 和 EST 分别侧重 polarity、count、timestamp 或 temporal resolution。单一表示中，Event Voxel 与 EST 在论文实验中较强，Event Frame 最弱，但不存在跨任务绝对最优表示。

LMFR 将多个基础表示统一为：

$$
T\times H\times W
$$

再为第 `j` 个表示学习一个卷积变换，最后拼接：

$$
R_f=
\left[
\phi(R_1);
\phi(R_2);
\ldots;
\phi(R_C)
\right]
$$

其中 `phi` 包含 normalization。其本质是 **hand-crafted base representations + learnable transformation + channel fusion**，而不是直接从 raw events 学习完全自由的 event representation。

### 4.3 Event-Based Slow-Fast Network

同一段 events 采用较少 time bins 时，每个 bin 的时间宽度更大，能积累更多 events，形成较完整的人体轮廓和动作语义；采用更多 time bins 时，时间宽度更小，更适合捕获快速运动细节。

因此：

$$
R_{\mathrm{slow}}
\in
\mathbb{R}^{
C\times T_{\mathrm{slow}}\times H\times W
}
$$

$$
R_{\mathrm{fast}}
\in
\mathbb{R}^{
C\times T_{\mathrm{fast}}\times H\times W
}
$$

且：

$$
T_{\mathrm{slow}}<T_{\mathrm{fast}}
$$

Slow pathway 强调 accumulated contour / appearance-like semantics，Fast pathway 强调 short-term motion dynamics。两路分别通过 ResNet backbone，而不是共享一个已经生成好的 `T` 维 tensor 后再随意改变时间长度。

### 4.4 Event-Based Spatial Temporal Attention

ESTA 为 slow/fast features 分别学习 spatial-temporal weights，使网络更关注动作发生的空间位置和活跃 time bins，并减弱静态区域、噪声区域和无动作时间段的影响。加权后的两路特征经过 pooling、normalization 和 concat，再进入 linear classifier。

ESTA 是普通 CNN attention，不是 spiking attention，也不引入 membrane dynamics。

## 5. Experiments and Main Evidence

论文评估 PAF、DHP19、DailyAction、THU E-ACT-50 和 THU E-ACT-50-CHL。THU E-ACT-50 包含 50 类、105 名 subjects、10,500 条 recordings，分辨率为 `1280×800`；CHL 版本包含 2,330 条 recordings，覆盖 corridor、open hall、复杂光照、不同视角和较小动作幅度。

EV-ACT 在 PAF、DailyAction、THU E-ACT-50-CHL 和 THU E-ACT-50 上分别取得 `92.6%`、`97.9%`、`58.5%` 和 `92.7%` Top-1 accuracy。相对 HMAX SNN、Motion SNN 等方法，论文报告 `14.5%`、`7.6%`、`11.2%` 和 `7.4%` 的提升，但比较应谨慎：EV-ACT 使用 ImageNet-pretrained ResNet，且新数据集上的 SNN baselines 来自代码复现。

Ablation 表明 LMF、EVF、ESFN 和 ESTA 均有效。EVF 的 accuracy 增益较小，但能显著减少 events；LMFR 相比单一 representation 更稳定；ESFN 对复杂场景和需要同时依赖 slow semantics 与 fast motion 的动作更有帮助；移除 ESTA 会造成约 `1.5%–3.7%` Top-1 下降。CHL 上，LMFR event input 的 `58.5%` 明显高于 RGB 的 `30.8%`、frame differentiation 的 `44.4%` 和 optical flow 的 `46.8%`。

Cross-view evaluation 中，训练视角与测试视角不同，所有方法均明显下降。EV-ACT 比 SNN baselines 更稳健，但仍未解决 viewpoint shift，说明 event data 不会自动产生 view-invariant action features。

Embedded evaluation 在 Jetson AGX Xavier 上完成：ResNet-18 为 `11.2M` parameters、`14.5` GFLOPs、`5.4W`、`72.8 ms/sample`；ResNet-34 为 `21.3M`、`29.0` GFLOPs、`7.2W`、`76.9 ms/sample`。系统报告平均 `326,140 EPS` 和 `1.3GB` memory，但 EPS 的计时边界未完全展开。

## 6. Strengths and Limitations

**Strengths**

* 同时贡献 benchmark、representation analysis 和完整 action-recognition framework。
* THU E-ACT-50 / CHL 显著扩展了 event action datasets 的类别、样本和现实条件。
* 系统比较多种 event representations，并明确展示 count、polarity 和 timestamp 信息的互补性。
* EVF、LMFR、ESFN、ESTA 形成逻辑完整的 preprocessing-to-classification pipeline。
* Cross-view、input-source 和 Jetson deployment 提供了比单纯 accuracy 更丰富的实验维度。

**Limitations / Questions**

* 本文不是 SNN，不能作为 spiking architecture 或 neuromorphic energy 的直接证据。
* 与 SNN baselines 的比较受到 CNN backbone 和 ImageNet pretraining 影响。
* LMFR 仍建立在 hand-crafted representations 上，并非完全 event-native end-to-end representation learning。
* Variance-based threshold、voxel size 和 slow/fast time bins 具有明显超参数依赖。
* 主实验使用 `Tslow=4、Tfast=16`，类别级分析使用 `6、18`，论文解释不足。
* Jetson 功耗属于普通 CNN embedded system 指标，不能外推到 SNN hardware。
* Event cameras 减少颜色和纹理暴露，但不等于绝对隐私保护。

## 7. Relation to Other Papers and Survey Taxonomy

EV-ACT 与 TTPOINT 都处理 event-camera action recognition，但技术路线不同。TTPOINT 将 events 保持为 sparse `x-y-t` point cloud，使用 point-based network；EV-ACT 则先做 point-cloud-style voxel filtering，再转换为 dense grid-based tensors，使用 ResNet / SlowFast-style CNN。

在综述 taxonomy 中，本文适合归入：

* event-based action recognition benchmark；
* grid-based event representation；
* learnable multi-representation fusion；
* temporal multi-granularity modeling；
* non-spiking CNN baseline；
* embedded event-camera system；
* open challenges: cross-view generalization。

它不是核心 SNN architecture paper，但可作为 SNN 方法必须面对的强 non-spiking benchmark 与系统参照。

### PDF-verified relation backfill

主要路线是建立 EV-ACT benchmark，并组合 voxel filtering、多种 dense event representations 与 SlowFast-style temporal modeling。

- **End-to-End Learning of Representations for Asynchronous Event-Based Data (Daniel Gehrig et al., ICCV 2019)** — `baseline`。该工作是 learned event representation 的实验 comparator；当前论文与其主要区别在于本文第 3–4 节所述的核心机制。 对应 Sections 2 and 5: representation and action recognition。证据：Related Work and Experiments, PDF pp.3 and 9, citation and bibliography [35]。 当前 active corpus 未覆盖。 值得 backward search。
- **SlowFast Networks for Video Recognition (Christoph Feichtenhofer et al., ICCV 2019)** — `foundation`。该工作提供 multi-rate temporal modeling 的基础机制；当前论文将其用于自身的 event/SNN pipeline，而不是把该前驱本身作为新贡献。 对应 Section 5: action recognition。证据：Related Work and Method, PDF pp.3 and 5-6, citation and bibliography [24]。 当前 active corpus 未覆盖。

## 8. Survey-Usable Takeaways

* Takeaway 1: Event representation 不是中性的预处理；count、polarity、timestamp 和 temporal bins 保留的信息不同，并会直接影响 action-recognition performance。
* Takeaway 2: 同一段 event stream 可通过不同 time-bin discretization 构造 coarse / fine temporal inputs，而不是对一个固定 tensor 简单 reshape。
* Takeaway 3: Event Voxel Filtering 的主要价值是大幅降低 event 数量和处理负担，accuracy 提升只是附加收益。
* Takeaway 4: Event cameras 不天然具备跨视角不变性，cross-view generalization 应作为独立评估维度。
* Takeaway 5: EV-ACT 展示了成熟 non-spiking CNN 在 event action recognition 中的竞争力，因此 SNN 方法应与此类强 event-CNN baseline 公平比较。

## Supplement Points

### 1. Grid-Based Event Representations

不同表示方法可以理解为：把原始 event tuple list 映射到规则网格，但保留的信息不同。

#### Event Frame

在一个时间窗口内累加 event polarity：

$$
R(x,y)
=

\sum_{e_k}
p_k
\cdot
\mathbf{1}
\left[
(x_k,y_k)=(x,y)
\right]
$$

它能表达正负亮度变化的净结果，但不同时间顺序可能得到相同 frame，且正负 events 可能互相抵消。

#### Event Count

分别统计 positive / negative event 数量：

$$
R^+(x,y),\qquad R^-(x,y)
$$

形成：

$$
2\times H\times W
$$

它保留 polarity 与 event density，但不保留窗口内的精细先后关系。

#### SAE / Time Surface

每个像素保存最近一次 event timestamp：

$$
R(x,y)=t_{\mathrm{last}}(x,y)
$$

或进一步做 exponential decay。它强调最近活动和运动轨迹，但通常忽略更早 events 的累计数量。

#### Event Voxel

将时间划分为 `T` 个 bins：

$$
R\in\mathbb{R}^{T\times H\times W}
$$

每个 event 按 timestamp 映射到相邻 temporal bins，常使用 bilinear interpolation。它同时保留粗时间结构与 event count，但 representation 更大。

#### EST

EST 同时显式保留 polarity 和时间：

$$
R\in\mathbb{R}^{2\times T\times H\times W}
$$

信息最完整，但 memory 和 computation 更高。

#### Memory Surface、TORE 与 Time Image

Memory Surface 使用 binning、linear 或 exponential temporal kernels 累积历史 events；TORE 保存每个像素最近若干个 event timestamps；Time Image 还依赖运动假设。它们更强调 event history，但结构和超参数也更复杂。论文对这些方法主要作为 related work 讨论，没有全部纳入 LMFR 主配置。

### 2. Point Cloud 中的坐标与属性

一般点云可写为：

$$
\mathcal{P}
=
\left\{
\left( \mathbf{x}_i,\mathbf{f}*i \right)
\right\}*{i=1}^{N}
$$

其中：

* `x_i` 是坐标；
* `f_i` 是可选属性。

普通 3D point cloud 可以只有：

$$
(x,y,z)
$$

也可以附加 RGB、强度、法向量等：

$$
(x,y,z,r,g,b)
$$

EVF 中：

$$
\mathbf{x}_i=(x_i,y_i,t_i)
$$

$$
\mathbf{f}_i=p_i
$$

即时间被当作第三个坐标，polarity 作为属性。

TTPOINT 的输入明确为：

$$
1024\times3
$$

且定义为归一化的 `(x,y,t)`，没有第四个 polarity channel，因此判断其未显式使用 polarity，是根据输入公式与维度，而不是仅根据“point cloud”名称。

CNN 图像也有属性：像素的 RGB 是规则网格上的 channel values；区别在于图像坐标由数组位置隐式给出，点云坐标则是显式输入。

---

### 3. EVF + LMFR 数值例子

假设一个 positive-polarity voxel 中有四个 events：

$$
(10,20,0.10,+1)
$$

$$
(11,20,0.12,+1)
$$

$$
(10,21,0.11,+1)
$$

$$
(11,21,0.13,+1)
$$

EVF 用均值代表这四个 events：

$$
\bar{x}=10.5
$$

$$
\bar{y}=20.5
$$

$$
\bar{t}=0.115
$$

得到代表点：

$$
(10.5,20.5,0.115,+1)
$$

假设另一个 voxel 只有一个孤立 event，variance-based rule 认为其 density 过低，则该 voxel 可能被删除。

之后，将 filtered events 放入某个 time bin：

* Event Frame 在对应像素累加 `+1` 或 `-1`；
* Event Count 在 positive / negative channels 中分别加 1；
* SAE 在对应像素写入最近 timestamp；
* Event Voxel 将 event 分配到相邻 temporal bins。

假设三种基础表示经过各自 convolution 后得到：

$$
R_1,R_2,R_3
\in
\mathbb{R}^{1\times T\times H\times W}
$$

沿 channel concat 后：

$$
R_f
\in
\mathbb{R}^{3\times T\times H\times W}
$$

这就是 LMFR：同一批 events 被编码成多种互补的 grid features，再由网络联合利用。

---

### 4. Backbone 与 Slow/Fast 维度流

LMFR 不会先生成一个固定：

$$
C\times T\times H\times W
$$

再直接把 `T` 改成 `Tslow` 或 `Tfast`。

正确流程是：对同一段 filtered event clip 分别重新分 bin。

若 clip 长度为 1 秒：

#### Slow branch

$$
T_{\mathrm{slow}}=4
$$

每个 bin 长度：

$$
\Delta t_{\mathrm{slow}}=250\ \mathrm{ms}
$$

得到：

$$
R_{\mathrm{slow}}
\in
\mathbb{R}^{C\times4\times H\times W}
$$

#### Fast branch

$$
T_{\mathrm{fast}}=16
$$

每个 bin 长度：

$$
\Delta t_{\mathrm{fast}}=62.5\ \mathrm{ms}
$$

得到：

$$
R_{\mathrm{fast}}
\in
\mathbb{R}^{C\times16\times H\times W}
$$

随后两路分别进入 ResNet backbone。概念上，每经过一个 spatial stage：

```text
H, W 下降
channel dimension 上升
temporal dimension 通常保留或按具体网络设计处理
```

例如可理解为：

```text
[B, C, T, H, W]
→ [B, 64, T, H/4, W/4]
→ [B, 128, T, H/8, W/8]
→ [B, 256, T, H/16, W/16]
→ [B, 512, T, H/32, W/32]
```

论文未逐层给出准确 shape，因此这只是 ResNet-style dimension flow 的解释，不应视为其代码的精确输出尺寸。

两路最终经过 ESTA、average pooling 和 batch normalization，变成固定长度 vectors，再 concat 后送入 classifier。

---

### 5. Cross-View Generalization

Cross-view evaluation 的核心是：

```text
Train on one camera view
Test on another unseen camera view
```

它测试的不是新 subject，而是新的观察几何。相同动作在不同视角下会发生：

* 运动方向变化；
* 身体部位遮挡；
* 轮廓形状变化；
* event density 和空间分布变化；
* 左右运动关系变化。

因此，正面训练、侧面测试通常比同视角 subject-disjoint testing 更难。

论文中所有方法跨视角都明显下降，说明 event data 即使缺少颜色和纹理，也仍然强烈依赖观察视角。EV-ACT 降幅相对较小，只能说明其 representation fusion 和 temporal modeling 更稳健，不能说明其已经实现 view invariance。

---

### 6. 为什么主实验使用 `4/16`，类别级消融使用 `6/18`？

论文的 time-bin sensitivity 结果显示：

* time bins 太少会压缩时间信息；
* `6–8` 附近较适合积累 spatial semantics；
* `16–18` 附近较适合 fast motion；
* bins 太多则增加 memory 和 computation。

因此类别级分析使用：

$$
T_{\mathrm{slow}}=6
$$

$$
T_{\mathrm{fast}}=18
$$

可能是为了选择两个较优且差异更明显的 temporal granularities。

但主实验仍使用：

$$
4,\ 16
$$

论文没有清晰解释为什么不统一，因此这是实验配置不一致，而不是理论上必须使用两套设置：

`Needs further check`

---

### 7. EPS 如何衡量？

EPS 即 Event Per Second：

$$
\mathrm{EPS}
=

\frac{
\text{系统处理的 event points 总数}
}{
\text{运行时间}
}
$$

例如 10 秒处理：

$$
3{,}261{,}400
$$

个 events，则：

$$
\mathrm{EPS}
=

326{,}140
$$

FPS 衡量每秒处理多少 frames，而 EPS 衡量每秒吞吐多少 events。

问题在于论文没有完整说明计时是否包含：

* sensor acquisition；
* EVF；
* LMFR construction；
* host-device transfer；
* CNN inference；
* visualization。

因此 EPS 可以作为 embedded system throughput，但不能与纯模型 FLOPs、sensor event rate 或 neuromorphic throughput 直接等同。

---

### 8. Personal Reflection

这篇论文单看算法模块，确实没有特别强的单点突破：

* EVF 来源于 point-cloud voxel filtering；
* LMFR 是已有表示的 learnable fusion；
* ESFN 是 SlowFast 在 event domain 的迁移；
* ESTA 属于常见 attention design。

因此，将其理解为“多个中等强度贡献组合成完整期刊工作”是合理的。更准确地说，它的 TPAMI 价值主要来自：

1. 大规模 benchmark；
2. 系统 representation comparison；
3. 完整且可复现的 processing pipeline；
4. 多角度实验，包括 challenging illumination、cross-view 和 input-source comparison；
5. embedded deployment。

所以这篇工作更像 **benchmark-and-system paper**，而不是依靠单个算法创新取胜。长期来看，THU E-ACT-50 / CHL 和 representation study 可能比 EV-ACT 网络结构本身更有综述价值。
