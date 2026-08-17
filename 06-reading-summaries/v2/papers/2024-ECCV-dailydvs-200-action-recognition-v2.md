---
tags: [event-camera, action-recognition, dataset, benchmark, DailyDVS-200, SNN, temporal-representation]
---

# Summary V2｜DailyDVS-200: A Comprehensive Benchmark Dataset for Event-Based Action Recognition

## 1. Core Understanding

本文提出 **DailyDVS-200**，一个面向 event-based action recognition 的大规模真实场景 benchmark dataset。数据集使用 DVXplorer Lite 直接采集事件流，包含 200 类日常动作、47 名参与者和 22,046 条 event sequences，并为每条样本提供 14 类场景或动作属性标注。论文没有提出新的识别网络，而是建立 cross-subject、multi-group 和 temporal-representation benchmarks，系统比较 frame-based、learnable representation、token-based 与 spike-based pipelines。

论文的核心发现不是单纯“数据集更大”，而是：现有 event-action models 在 moving camera、micro-action、远距离、夜间和高机位等现实条件下仍明显退化；同时，event-frame 的时间聚合粒度会显著影响模型排名与准确率。该工作因此主要属于 **datasets and benchmarks**，并可作为检验 SNN 是否真正适应复杂真实事件数据的重要资源。

## 2. Problem and Motivation

现有 event-based action datasets 主要存在三类不足。第一，部分数据来自 RGB 图像或视频的屏幕重录、软件模拟，受原始 frame rate、dynamic range、motion blur 和 simulator assumptions 限制，无法完整保留真实 event sensor 的高时间分辨率及噪声特性。第二，已有真实数据集通常在类别数、样本量、参与者数量或场景多样性中至少有一项不足。例如 HARDVS 的样本与类别更多，但仅包含 5 名参与者；DvsGesture、PAF 和 DailyAction 的类别或规模较小；Bullying10K 的任务域较集中。第三，很多数据集缺少逐样本属性标注，难以分析模型在 camera motion、光照、距离或动作幅度变化下的鲁棒性。

DailyDVS-200 试图同时覆盖：
$$
\text{action diversity}
+
\text{subject diversity}
+
\text{real acquisition}
+
\text{attribute annotation}.
$$
其目标不是证明 event camera 自动优于 RGB camera，而是建立一个更困难、更接近实际应用的测试环境，检验 event representations、ANN、Transformer 与 SNN 在复杂条件下的真实能力。

## 3. Method Overview

数据使用分辨率为：
$$
320\times240
$$
的 DVXplorer Lite 采集，并同步记录 RGB video。原始数据保存为 `.aedat4`，其中包括：

- event stream；
- IMU stream；
- trigger stream。

同步 RGB 主要用于采集质量检查和动作、环境属性标注，而正式 benchmark 以 event data 为核心。47 名参与者包括 26 名男性和 21 名女性，动作类别覆盖家务、办公、运动、健康、互动、暴力和交通等七类日常场景。采集条件包括 front/lateral view、moving camera、最高约 3 m 的机位、最远约 30 m 的距离、昼夜、室内外、不同光照方向和背景复杂度。

论文建立两种主要评价协议：

1. **Cross-Subject Evaluation**：训练、验证和测试使用不同参与者，检验 unseen-subject generalization。
2. **Multi-Group Evaluation**：使用同一训练设置，将测试集按不同属性划分，分别计算各条件下的 accuracy。

总体指标为 clip-level Top-1 和 Top-5 accuracy。

## 4. Key Components and Mechanisms

### 4.1 十四类属性标注

每条样本具有以下属性：

- Background Complexity；
- Duration；
- Illumination Direction；
- Distance；
- Height；
- Location；
- Camera Motion；
- Person Number；
- Perspective；
- Props；
- Action Range；
- Shadow；
- Posture；
- Diurnality。

这些标注使研究者能够分析：
$$
\operatorname{Acc}
\left(
\text{model}\mid \text{specific condition}
\right),
$$
而不只是报告整体 accuracy。例如 Camera Motion 可分为 moving/static，Action Range 可分为 full-body/limbs/micro。

但这些属性不是严格正交变量。动作类别与场景存在天然关联，例如骑自行车通常属于室外、带道具和全身动作，剪指甲通常属于近距离、微动作和坐姿。因此 multi-group results 更适合解释为 **attribute-conditioned subset performance**，而不能直接视为单个属性的因果效应。

### 4.2 Representation 与 Backbone 的双轴分类

论文比较的方法可以分为两个不同维度：

```
Representation:
Event frame / Learnable representation / Token / Spike tensor

Backbone:
2D or 3D CNN / Transformer / Spiking Transformer
```

SNN 是模型或计算范式，并不是与 event frame、token、TORE 同层级的单一 representation。一个 SNN 仍可能接收由固定时间窗口生成的 dense spike tensor，而非直接处理原始异步 events。

### 4.3 Temporal discretization

对于持续时间为 $D$ 的事件视频，若每张 event frame 聚合：
$$
\Delta t
$$
秒事件，则 temporal steps 数为：
$$
T=\frac{D}{\Delta t}.
$$
在固定视频时长下：
$$
\Delta t\downarrow
\quad\Longrightarrow\quad
T\uparrow.
$$
更短的 integration interval 能保留更细的动作顺序，但会增加输入 frames、时间建模长度和计算成本。Frame gap 则决定生成的 event frames 中有多少被跳过；gap 增大通常意味着更少计算，但也损失更多时序信息。

## 5. Experiments and Main Evidence

论文测试了 12 种方法，包括 C3D、I3D、R2Plus1D、SlowFast、TSM、EST、TimeSformer、Swin-T、ESTF、GET、Spikformer 和 SDT。Table 2 的 frame-based baselines 使用 0.5 s event-frame setting。在这一条件下：

- Swin-T：48.06% Top-1，74.47% Top-5；
- TimeSformer：44.25%；
- SlowFast：41.49%；
- TSM：40.87%；
- Spikformer：36.94%；
- SDT：35.43%。

因此，在作者的默认设置下，token-based Swin-T 最优，而两个 tested spike-based Transformers 尚未表现出准确率优势。该结果不能推广为“SNN 普遍低于 Transformer”，因为模型规模、预训练、输入形式、simulation steps 和训练预算未被完全统一。

Temporal-setting experiment 更值得注意。Gap0 条件下，将 integration interval 从 0.5 s 缩短到 0.125 s 后：

- SlowFast：41.49% → 52.16% → 64.09%；
- TSM：40.87% → 49.55% → 61.76%；
- I3D：32.30% → 45.39% → 59.10%。

这说明更细的 temporal discretization 能显著提高识别性能，其影响甚至可能超过 backbone 之间的差异。它也表明 Table 2 中“Swin-T 最优”的结论依赖 0.5 s preprocessing：SlowFast 在 0.125 s 设置下达到 64.09%，明显超过 Swin-T 的 48.06%。

增大 frame gap 总体会降低 accuracy。例如 SlowFast 在 0.125 s 下由 gap0 的 64.09% 降至 gap2 的 44.81% 和 gap4 的 44.64%，说明连续 temporal observations 对动作顺序建模十分重要。

Camera motion 是最稳定、最严重的困难因素：

| 模型       | Moving | Static |
| ---------- | ------ | ------ |
| SlowFast   | 21.05  | 51.81  |
| TSM        | 26.88  | 50.16  |
| EST        | 13.52  | 41.51  |
| Spikformer | 13.74  | 46.15  |
| Swin-T     | 27.84  | 58.05  |

Moving camera 会使大量背景边缘产生 events，增加的主要是与 action label 无关的 nuisance information，而非有效动作线索。对 Spikformer 而言，moving/static 差距达到 32.41 个百分点，说明 spike-based processing 不会自动消除 camera-motion-induced background spikes。

Action Range 也表现出明显层次。Swin-T 在 full-body、limbs 和 micro-actions 上分别为：
$$
59.24\%,\quad43.15\%,\quad34.59\%.
$$
大幅度动作产生更明显的时空轨迹，微动作则容易因事件数量少、目标区域小和下采样而丢失。动作级分析进一步显示 hand-in-hand circling、push-up 较容易，而 pitch、playing table tennis、V sign 和 OK sign 等快速或微动作较难。

## 6. Strengths and Limitations

**优势：**

- 使用真实 event sensor 采集，而非由 RGB 数据转换；
- 同时覆盖较多动作类别和参与者；
- 提供逐样本 14-attribute annotation；
- 保留 event、IMU 和 trigger streams；
- 同时测试 frame、learnable、token 和 spike pipelines；
- temporal interval 与 frame-gap 实验揭示 preprocessing 对结果的重要影响；
- moving-camera subset 为 ego-motion robustness 提供了现实 benchmark。

**局限：**

- 正文给出的 cross-subject split 存在内部不一致：Subject 4 同时出现在 validation 和 test，需以发布的 split files 为准；
- 属性阈值、标注者数量和 inter-annotator agreement 未说明；
- 不同属性子集之间存在明显 class、scene 和 sample-distribution confounding；
- Table 2 的模型排名依赖并非最优的 0.5 s frame setting；
- 论文称“增加 event step length 提高性能”，但 Table 4 实际支持的是缩短 integration interval、增加 temporal steps；
- 不同模型的预训练、参数量、输入长度和训练预算缺乏完整统一说明；
- 未报告 SNN firing rate、energy、latency 或 neuromorphic hardware results；
- “event streams cannot be directly used for training”“完全消除隐私风险”等表述过强；
- 数据集并非在样本数和类别数上绝对最大，其主要优势应限定为 subject diversity 与 attribute annotations 的组合。

## 7. Relation to Other Papers and Survey Taxonomy

本文应归入：

- Datasets and Benchmarks；
- Event-Based Action Recognition；
- Real-World Robustness；
- Temporal Representation Design；
- ANN–SNN Comparative Evaluation；
- Open Challenges。

与 EV-ACT 相比，DailyDVS-200 提供更多动作类别、更丰富场景属性和更系统的 subgroup evaluation；与 TTPOINT、VMST-Net 相比，它本身不提出 point/voxel-token architecture，而是提供可用于比较这些 representation routes 的数据基础；与 SFOD 相比，它进一步说明“使用 SNN”不等于“直接处理原始异步 events”，representation 与 backbone 应分别记录。

与《State Space Models for Event Cameras》的联系在于，两篇论文都研究 temporal window 对 event models 的影响，但实验问题不同：

- DailyDVS-200：对不同 integration intervals 分别训练和测试，研究最佳 temporal granularity；
- SSM：仅在 20 Hz 训练，直接在 40–200 Hz 测试，研究跨 frequency distribution shift。

二者共同说明：event camera 的高时间分辨率只有在 representation 和 temporal dynamics 中被正确保留和适配，才能转化为性能优势。

### PDF-verified relation backfill

主要路线是大规模真实 event-action benchmark、attribute subgroup analysis 与 ANN/SNN backbone comparison。

- **A Low Power, Fully Event-Based Gesture Recognition System (Arnon Amir et al., CVPR 2017)** — `foundation`。该工作提供 real-world event gesture benchmark 的基础机制；当前论文将其用于自身的 event/SNN pipeline，而不是把该前驱本身作为新贡献。 对应 Sections 5 and 6: action datasets and robustness。证据：Introduction and Related Work, PDF pp.2-3, citation and bibliography [1]。 当前 active corpus 未覆盖。
- **Event-based Action Recognition Using Motion Information and Spiking Neural Networks (Qianhui Liu et al., IJCAI 2021)** — `baseline`。该工作是 daily event action dataset 的实验 comparator；当前论文与其主要区别在于本文第 3–4 节所述的核心机制。 对应 Section 5: action recognition。证据：Dataset comparison Table 1, PDF p.4, citation and bibliography [35]。 当前 active corpus 未覆盖。

## 8. Survey-Usable Takeaways

1. 大规模真实 event-action datasets 仍然稀缺，类别数量之外还必须重视 subject、scene 和 attribute diversity。
2. Event-frame temporal granularity 对性能的影响可能超过 backbone 差异。
3. 更短 integration interval 能保留更细动作顺序，但增加 temporal steps 和计算量。
4. Moving camera 是 event-based action recognition 的系统性难点。
5. Camera-motion-induced events 会降低 foreground selectivity，并可能破坏 SNN 的输入稀疏性。
6. DailyDVS-200 上 tested spike-based Transformers 尚未表现出 accuracy advantage。
7. SNN action-recognition studies 应同时报告 temporal steps、bin duration、firing rate、latency、energy 和硬件平台。
8. Micro-actions 需要高空间分辨率、细 temporal modeling 和更少的信息压缩。
9. Multi-group evaluation 有价值，但必须警惕属性与动作类别之间的 confounding。
10. 原始 event、IMU 和 trigger streams 为 ego-motion compensation、multimodal fusion 和 event-driven SNN 提供了后续研究空间。

## Supplement Points

### Event Video 如何构造成 Temporal Input

原始事件视频表示为：
$$
\mathcal E
=
\left\{
(x_i,y_i,t_i,p_i)
\right\}_{i=1}^{N}.
$$
选择 integration interval $\Delta t$ 后，第 $k$ 个 event frame 聚合时间区间：
$$
[(k-1)\Delta t,k\Delta t).
$$
若区分正负 polarity：
$$
X_k
\in
\mathbb R^{2\times H\times W}.
$$
整段视频形成：
$$
X
=
\{X_1,\ldots,X_T\},
$$
其中：
$$
T=\frac{D}{\Delta t}.
$$
对于 3D CNN，输入通常组织为：
$$
X
\in
\mathbb R^{B\times C\times T\times H\times W},
$$
时间 $T$ 是独立维度，3D kernel 同时沿 $T,H,W$ 滑动。另一种方案是把时间折叠到 channel：
$$
X_{\mathrm{fold}}
\in
\mathbb R^{B\times CT\times H\times W},
$$
再用 2D CNN，但这种方式需要固定 $T$，也不具备显式 temporal translation structure。

其他常见路线包括：

```
Event frames → 2D CNN → RNN/TSM/temporal pooling
Events → tokens → Transformer
Event/spike frames → multiple SNN simulation steps
```

------

### 多时间步下的 Loss 与 Accuracy

DailyDVS-200 是 clip-level action classification。一条完整 event sequence 通常只有一个动作标签：
$$
y\in\{1,\ldots,200\}.
$$
网络处理全部 temporal steps 后，产生一个 200 维 logits vector：
$$
\mathbf z\in\mathbb R^{200}.
$$
Cross-entropy 为：
$$
\mathcal L_{\mathrm{CE}}
=
-\log
\frac{e^{z_y}}
{\sum_{c=1}^{200}e^{z_c}}.
$$
对于逐步产生输出的 RNN 或 SNN，可以采用：

1. 最后一步 logits：

$$
\mathcal L
=
\operatorname{CE}(\mathbf z_T,y);
$$

1. 时间平均 logits：

$$
\bar{\mathbf z}
=
\frac1T\sum_{t=1}^{T}\mathbf z_t;
$$

1. 每步监督：

$$
\mathcal L
=
\frac1T
\sum_{t=1}^{T}
\operatorname{CE}(\mathbf z_t,y).
$$

SNN 还可使用 spike count、firing rate 或 accumulated membrane potential 进行 decoding。论文未逐一说明所有 baseline 的具体 decoding 和 temporal supervision，因此不能假设它们完全一致。

Top-1 accuracy 按完整样本统计：
$$
\operatorname{Top1}
=
\frac1N
\sum_{n=1}^{N}
\mathbf 1[
\arg\max_c z_c^{(n)}
=
y_n
].
$$
Top-5 则要求真实类别位于最高分的五个类别中。

------

### Temporal Steps、Integration Interval 与 Frame Gap

以 3 s 动作为例：

| $\Delta t$ | Temporal steps |
| ---------- | -------------- |
| 0.5 s      | 6              |
| 0.25 s     | 12             |
| 0.125 s    | 24             |

在总时长固定且全部 frames 被使用时：
$$
\Delta t\downarrow
\Longleftrightarrow
T\uparrow.
$$
较短 interval 可将“抬手—移动—接触—收回”等阶段分离，避免全部运动轨迹叠加到一张 event frame 中。

但若模型固定输入 frame 数，则：
$$
D=T\Delta t
$$
会随 $\Delta t$ 改变。此时不同设置不仅改变 temporal resolution，也改变 temporal coverage。DailyDVS-200 主文没有明确说明 Table 4 是否固定 clip duration、frame number、padding 或 sampling policy，因此提升可能同时来自更细时间粒度、更多 frames 和更高计算预算。

若 gap 表示每取一帧跳过 $g$ 帧，则有效时间间隔近似为：
$$
(g+1)\Delta t.
$$
Gap 增大通常减少计算，但丢失动作的连续时间信息。

------

### 与 SSM Frequency Experiment 的区别

假设一段事件视频持续 3 s。

DailyDVS-200 在 $\Delta t=0.125$ s 时：

```
3 s event stream
→ 24 event frames
→ 整个 clip 输入 action model
→ 输出一次动作类别
```

SSM object detection 在 40 Hz 时：
$$
\Delta t
=
\frac1{40}
=
25\ \mathrm{ms},
$$
3 s 中共有：
$$
3\times40=120
$$
个外部窗口。模型每个窗口都运行一次，并输出一次 bounding boxes：

```
Window 1 → Detection 1 → State 1
Window 2 → Detection 2 → State 2
...
Window 120 → Detection 120
```

DailyDVS-200 主要比较不同 temporal settings 下分别训练后的 clip classification；SSM 论文只在 20 Hz 训练一次，再直接改变 inference frequency，检验同一个模型能否适应新时间步。前者证明更细时间划分具有潜在收益，后者证明未经适配的 recurrent model 不会自动获得这种收益。

------

### IMU Stream

`.aedat4` 中的 IMU stream 通常可能包含：
$$
[a_x,a_y,a_z,\omega_x,\omega_y,\omega_z],
$$
即三轴加速度和三轴角速度。

对于 moving-camera samples，IMU 可用于：

- 估计 camera ego-motion；
- 区分人体运动和相机运动；
- 进行 global background motion compensation；
- 实现 event–IMU fusion；
- 抑制 camera-motion-induced background events；
- 构建 ego-motion-aware SNN。

------

### Trigger Stream

Trigger stream 通常用于保存硬件或软件同步事件，潜在用途包括：

- RGB–event synchronization；
- recording start/end markers；
- action segment boundaries；
- external device synchronization；
- 多传感器时间对齐。

一个 trigger 记录可能包含：
$$
(t_i,\operatorname{channel}_i,\operatorname{state}_i),
$$
其中 timestamp 表示触发时间，channel 表示触发源，state 表示 rising/falling edge 或触发状态。

------

### 十四类属性与 Confounding

属性组测试计算的是：
$$
\operatorname{Acc}
\left(
\mathcal D_{\mathrm{test}}^{\mathrm{attribute}}
\right).
$$
例如 moving-camera accuracy 只在标记为 moving 的样本上统计。

但这些 subsets 可能具有不同：

- action-class composition；
- subject distribution；
- scene distribution；
- sample count；
- duration；
- event density。

例如 complex-background subset 可能包含更多容易识别的全身动作，因此其 accuracy 反而高于 easy-background subset。双人动作也可能因动作幅度更大、类别更独特而比单人动作更容易。

因此 Table 3 应解释为：

> 模型在 DailyDVS-200 各属性子集上的经验表现。

不能直接解释为：

> 某一属性单独导致了多少 accuracy 变化。

此外，Long/Short、Near/Far、High/Low 和 Easy/Complex 的具体划分阈值未在正文明确给出，这限制了属性标注的可复现性。
