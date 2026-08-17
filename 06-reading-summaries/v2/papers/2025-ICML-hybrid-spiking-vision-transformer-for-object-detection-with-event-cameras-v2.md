---
tags: [event-based-object-detection, hybrid-ann-snn, spiking-transformer, temporal-modeling, fall-detection]
---

# Summary V2｜Hybrid Spiking Vision Transformer for Object Detection with Event Cameras

## 1. Core Understanding

HsVT 是一个面向 event-based object detection 的 **ANN + LSTM + SNN hybrid detector**。它沿用 RVT 的 multi-stage、spatial-temporal 分工：convolution 与 MaxViT-style attention 提取局部和全局空间特征，recurrent module 沿时间传递状态；其主要改动是在 spatial path 中加入 SpikingMLP，并在最后一个 stage 用 Spiking Temporal Feature Extraction（STFE）替代 LSTM，以降低参数量和计算量。

该模型不是 fully spiking，也没有完全移除 LSTM。默认四个 Blocks 的 temporal modules 依次为 LSTM、LSTM、LSTM、STFE，之后接 FPN 和 detection head。论文也不是逐 event 的 fully asynchronous inference：原始事件先按固定时间窗口 $\Delta t$ 累积成 sequence，再由 recurrent backbone 跨窗口建模。

论文另一项贡献是 Fall Detection Dataset，但其真实生成链为 **Le2i frame videos $\rightarrow$ event-camera simulator $\rightarrow$ synthetic event streams**。因此 Abstract 中“captured using an event-based camera”的说法与 Sections 3.1、5.1 不一致；该数据集不能直接证明真实 DVS sensor noise、hardware timing 或真实采集条件下的泛化。

## 2. Problem and Motivation

Event camera 输出异步事件 $e_i = (t_i, x_i, y_i, p_i)$，具有高时间分辨率、宽动态范围和稀疏变化响应。传统 ANN detector 的 convolution/self-attention 擅长空间表征，但复杂 recurrent module 与 dense computation 可能增加参数和计算；SNN 的 membrane dynamics 和 sparse spikes 则天然包含时间状态。作者希望通过 hybrid design 保留 ANN 的空间建模能力，同时用部分 spiking computation 改善 temporal feature extraction 的参数效率。

已有 RVT 使用 convolution、local/global attention 和 LSTM，GET 用 graph tokens 组织 timestamp/polarity，SODFormer 融合 event 与 frame streams，SpikSSD 和 SpikingViT 则更接近 fully spiking detector。HsVT 的定位并非证明纯 SNN 优于 ANN，而是在 RVT-style detector 中探索有限比例 SNN module 的放置方式。

## 3. Method Overview

单个 event 表示为：

$$
e_i = (t_i, \langle x_i, y_i \rangle, p_i), \qquad p_i \in \{-1, +1\}.
$$

网络输入不是单个 event，而是时间窗口内的事件集合：

$$
E = \{e_i \mid e_i \text{ occurs within } \Delta t\}.
$$

作者在 GEN1、Fall、AIR 上分别采用 $\Delta t = 50\ \mathrm{ms}$、$200\ \mathrm{ms}$、$10\ \mathrm{ms}$；AIR 的 $10\ \mathrm{ms}$ 与 $100\ \mathrm{Hz}$ label frequency 对齐。每个窗口形成一次 recurrent input，网络同时沿两个方向传播：纵向经过 Block 1--4 逐级降采样和提取空间特征，横向把相邻时刻的 temporal state 传给同一 stage 的下一时刻。多尺度输出再进入 FPN 与 YOLOX-style detection head，预测 bounding boxes 和类别。

四个 stage 的 spatial path 均为：

$$
\text{Block-SA}
\rightarrow
\text{SpikingMLP}
\rightarrow
\text{Grid-SA}
\rightarrow
\text{SpikingMLP}.
$$

Block-SA 在局部 windows 内建模细粒度结构，Grid-SA 跨 feature map 建模长程空间关系。前三个 stages 的 temporal state 由 LSTM 维护；第四个 stage 使用 STFE，形成论文所称的 hybrid temporal encoder。

## 4. Key Components and Mechanisms

### 4.1 Spatial extraction 与 temporal recurrence

MaxViT attention 负责 spatial dependency，而非 spike-native temporal attention。LSTM 的 input、forget、output gates 在前三个 stages 保存短期与长期信息。STFE 仅出现在最后一个 stage：正文描述其数据流为 convolution $\rightarrow$ batch normalization $\rightarrow$ spiking neuron $\rightarrow$ LSTM-like temporal extraction。它包含 convolution、BN、spiking neuron 和类似 LSTM 的状态路径，但论文没有给出完整 state-update equations、gate definitions、tensor shapes 或 surrogate-gradient path，具体实现为 `Needs further check`。

SpikingMLP 位于 spatial path，因此“ANN 负责空间、SNN 负责时间”只是总体设计倾向，不是严格模块二分。FPN 和 detection head 是否包含 spiking neurons、是否保留跨时间状态，正文也没有完整说明。

### 4.2 Fall synthetic event generation

作者将带 frame-level bounding boxes 的 Le2i fall videos 输入 event-camera simulator，生成 event stream，先保存为 bag，再转换为 h5；annotation 从 $(x_1,y_1,x_2,y_2)$ 转成 GEN1-style $(t,x,y,w,h,\text{class id},\text{confidence},\text{track id})$。

论文引用 ESIM 说明 simulator 可与 rendering engine 结合并 adaptive query intermediate images。但本文输入是既有视频，而不是正文明确描述的 3D scene、camera trajectory 与连续 rendering pipeline。它是否完整复现 ESIM 的 adaptive rendering workflow、如何在低 frame-rate Le2i 视频之间恢复连续亮度轨迹，均为 `Needs further check`。

### 4.3 Training 与 efficiency accounting

HsVT 基于 RVT + YOLOX pipeline，使用 Adam、OneCycle schedule、mixed precision 和两张 RTX 4090；Tiny batch size 为 8，Small/Base 为 4。论文未完整报告 learning rate、epochs、augmentation、sequence unrolling length 和 loss weights，复现仍需代码。

Appendix 使用 45 nm arithmetic proxy 估计能耗：

$$
E_{\mathrm{ANN}} = 4.6\ \mathrm{pJ} \times \mathrm{FLOPs},
$$

$$
E_{\mathrm{SNN}}
= 0.9\ \mathrm{pJ} \times \mathrm{SOPs}
= 0.9\ \mathrm{pJ} \times f_r \times T \times \mathrm{FLOPs}.
$$

这只是 operation-level theoretical estimate，不是 neuromorphic hardware、GPU 或 wall-clock energy measurement，也未完整计入 memory access、state storage、data movement 和 hardware utilization。

## 5. Experiments and Main Evidence

### 5.1 Temporal-window 与 neuron ablation

Fall 上 $40/200/1000\ \mathrm{ms}$ 的 mAP 分别为 $0.445/0.487/0.405$。短窗口事件过稀、人体轮廓不完整；长窗口发生 temporal smearing 和 clutter；$200\ \mathrm{ms}$ 在该数据与配置下取得最佳平衡，但不是普适窗口。

SpikingMLP 中，LIF 在 Fall/AIR 上得到 $0.476/0.630$，IF 为 $0.441/0.587$。Surrogate ablation 没有单一赢家：ATan 在 Fall-$200\ \mathrm{ms}$ 和 AIR 更高，Sigmoid 在 Fall-$1000\ \mathrm{ms}$ 略高。作者后续采用 LIF。

### 5.2 STFE component 与 placement

AIR 上，STFE + LIFNode 以 $0.20$ M parameters、$101.19$ M FLOPs 得到 $0.640$ mAP；LSTM 为 $0.53$ M、$268.44$ M FLOPs、$0.604$ mAP。该结果支持 STFE 在此 ablation 中有更好的 parameter/FLOP-performance balance，但 FLOPs 不等于真实 energy。

Placement ablation 更关键：四层全 LSTM 为 $0.595$，仅 Block 4 使用 STFE 为最高的 $0.640$，四层全 STFE 反而只有 $0.602$。因此证据支持“晚期放置一个 STFE”，不支持“spiking modules 越多越好”，也说明 HsVT 的优势依赖 hybrid composition。

### 5.3 Detection comparison

GEN1 上，HsVT-T/S/B 分别以 $4.1/9.1/17.2$ M parameters 获得 $0.449/0.465/0.478$ mAP。HsVT-B 略高于 RVT 的 $0.472$，参数也略少于 RVT 的 $18.5$ M；但 ERGO-12 为 $0.504$，所以 HsVT 不是该表的 overall SOTA。Table 7 中 STAT 的 `49.9` 和 SpikSSD 的 `40.8` 与其他 $0.xx$ mAP 格式不一致，可能缺少小数点，但 PDF 未解释，不能擅自改为 $0.499/0.408$。

AIR/Fall 上，HsVT-T 相对 RVT-T 为 $0.641$ vs. $0.613$、$0.491$ vs. $0.487$；HsVT-S 为 $0.616/0.492$，HsVT-B 为 $0.618/0.486$。提升总体有限，且模型增大没有稳定改善结果。作者将其归因于小数据集 overfitting，但没有提供 train-test gap、regularization ablation 或多次运行统计，因此这是 author hypothesis。

Appendix 估计 HsVT-B 总能耗为 $134.5\ \mathrm{mJ}$，高于 SFOD 的 $7.26\ \mathrm{mJ}$ 和 EAS-SNN-M 的 $28.10\ \mathrm{mJ}$；论文自身并未展示 hybrid model 的能耗优势。Table 9 的 Tiny 行又给出 $1156$ M SOPs 与 $0.017\ \mathrm{mJ}$，按论文公式二者不能同时成立，属于 `Needs further check`。

## 6. Strengths and Limitations

**Strengths.** 论文在统一 RVT-style pipeline 中比较 LSTM 与多种 spiking temporal components，并通过 placement ablation 显示 hybrid composition 比全 LSTM 或全 STFE 更有效；GEN1 上以略少参数达到略高于 RVT 的 mAP；同时把 event-based fall detection 引入公开 benchmark 讨论。

**Limitations.** HsVT 不是 fully spiking，也不是原生异步 event processor；STFE 缺少可复现的完整数学定义；Fall 是由 frame videos 合成的 events，Abstract 对采集方式的表述不准确，隐私保护也没有独立审计；AIR 不公开；主要对比缺少方差或 significance test；energy 仅为 arithmetic proxy，且数表存在不一致；GEN1 结果未达到 overall SOTA。

## 7. Relation to Other Papers and Survey Taxonomy

在综述 taxonomy 中，HsVT 主要属于：**event-based object detection、hybrid ANN-SNN architecture、fixed-window event representation、recurrent temporal modeling、spiking Transformer components、synthetic event datasets、theoretical efficiency estimation**。

### PDF-verified literature relations

- **Recurrent Vision Transformers for Object Detection with Event Cameras (Mathias Gehrig et al., CVPR 2023)** — `baseline`。HsVT 明确受 RVT 的 multi-stage convolution、local/global attention 和 LSTM temporal recurrence 启发，并沿用 RVT + YOLOX 设置进行比较。证据：Introduction，PDF p.2，citation Gehrig & Scaramuzza (2023)；Experiments，PDF pp.6--9。
- **GET: Group Event Transformer for Event-Based Vision (Y. Peng et al., ICCV 2023)** — `alternative`。GET 用 timestamp/polarity-aware graph tokens 与 dual attention 组织异步事件；HsVT 则使用 fixed-window sequence 和 hybrid recurrent backbone。证据：Introduction/Related Work，PDF pp.2--3，citation Peng et al. (2023)。
- **SODFormer: Streaming Object Detection with Transformer Using Events and Frames (D. Li et al., TPAMI 2023)** — `same_task_different_mechanism`。SODFormer 融合 event 与 frame streams，HsVT 面向 event sequence 并以 ANN/LSTM/SNN hybrid modules 建模。证据：Related Work 2.3，PDF p.3，citation Li et al. (2023)。
- **SpikSSD: Better Extraction and Fusion for Object Detection with Spiking Neural Networks (Y. Fan et al., arXiv 2025)** — `contrasts_with`。SpikSSD 强调 fully spiking backbone 与 bidirectional fusion，HsVT 则保留 attention、LSTM、FPN/head 等 hybrid components。证据：Related Work 2.3，PDF p.3，citation Fan et al. (2025)；Table 7，PDF p.9。
- **SpikingViT: A Multiscale Spiking Vision Transformer Model for Event-Based Object Detection (L. Yu et al., TCDS 2025)** — `baseline`。二者均是 event detector 中的 spiking Transformer 路线，但 SpikingViT 以 residual voltage memory 和 spiking attention 保留时空特征，HsVT 采用 RVT-style hybrid recurrence。证据：Related Work 2.3，PDF p.3，citation Yu et al. (2025)；Table 7，PDF p.9。
- **ESIM: an Open Event Camera Simulator (H. Rebecq et al., CoRL 2018)** — `foundation`。Fall dataset 的 synthetic event generation 以 ESIM 作为 simulator 方法依据；本文是否完整采用其 rendering/adaptive-query pipeline 未说明。证据：Sample Processing 3.1，PDF p.3，citation Rebecq et al. (2018)。

## 8. Survey-Usable Takeaways

- Takeaway 1: HsVT 的有效配置是 ANN attention/convolution + 三层 LSTM + 一层 STFE，而不是 fully spiking Transformer；应将其作为 hybrid detector 案例。
- Takeaway 2: STFE placement 比 STFE 数量更重要；仅在最后 stage 替换 LSTM 最佳，全 STFE 反而退化。
- Takeaway 3: HsVT 仍依赖固定窗口事件累积，SNN module 没有把系统变成逐事件、完全异步处理器。
- Takeaway 4: Fall benchmark 来自 frame-video simulation，适合研究 synthetic event fall detection，但不等价于真实 DVS benchmark。
- Takeaway 5: 参数量和 FLOP/SOP proxy 可用于结构比较，却不能替代真实 hardware energy；本文估计中 HsVT-B 的能耗还明显高于 fully spiking comparators。

## Supplement Points

### Questions and Clarifications

#### 1. 为什么“相邻两帧做差再阈值化”不足以生成准确 events？

两帧差只能观察端点亮度 $L(t_0)$ 与 $L(t_1)$，不知道区间内亮度轨迹。若亮度快速上升后下降，端点可能相同但中间已跨过多个 contrast thresholds；若变化超过多个阈值，一次 frame difference 也无法可靠恢复每个 event 的数量、polarity、顺序和 timestamp。因此固定 frame-rate 差分容易漏 event、合并多个 events，并把 timestamp 粗略量化到 frame boundary。

#### 2. ESIM 的 rendering engine 做什么，为什么可以 adaptive query？

Rendering engine 持有 scene geometry、materials、lighting 和 camera trajectory，可在任意请求时刻执行 $\operatorname{Render}(\text{scene},t) \rightarrow I_t$。Event simulator 比较像素的 log-intensity trajectory；当运动或亮度变化快、当前采样不足以定位 threshold crossing 时，就向 renderer 请求更密的 intermediate images。这里的“任意查询”是根据连续场景模型重新渲染指定时间，并非从两张既有图片中任意创造真实细节。

#### 3. 如果 simulator 已知道光照强度，为什么还需要图像？

如果 simulator 已直接拥有每个像素的解析连续函数 $L_{x,y}(t)$，确实不需要完整图像；它可直接求 threshold crossing。实际 graphics simulator 通常只提供“给定时间渲染整幅 image”的接口，image 是所有 pixels 在该时刻亮度值的批量查询结果。Event simulation 再从这些查询值近似连续轨迹并生成 events。

#### 4. 为什么必须知道亮度在何时跨过阈值？

真实 event camera 在相对上一次 event 的 log-intensity change 达到正/负 contrast threshold 时立即发放。只知道一个长区间的总变化，无法确定 event timestamp，也无法判断期间发生了几次正负 crossing。Timestamp、event count 和 ordering 会直接影响 event stream 的运动结构以及后续时间窗口中的归属。

#### 5. 本文是否真的使用了完整 ESIM rendering pipeline？

`Needs further check`。正文先介绍 ESIM 的 rendering-engine/adaptive-query 优势，但实际数据源是既有 Le2i videos，只说“利用 event camera simulator 转换视频”。它没有报告 3D scene、camera trajectory、adaptive rendering rate、contrast threshold 或 interpolation method。因此可以确认 Fall events 是 simulator-generated，不能仅凭引用确认它完整采用了原始 ESIM 的连续 rendering workflow。
