---
tags:
  - event-camera
  - dense-prediction
  - hierarchical-memory
  - adaptive-update
  - event-representation
  - non-spiking
---

# Summary V2｜Efficient Learning of Event-based Dense Representation using Hierarchical Memories with Adaptive Update

## 1. Core Understanding

本文提出一种面向 event-based dense prediction 的 non-spiking hierarchical memory network。其核心目标是在不把事件长期聚合成静态 frame-like representation 的前提下，将稀疏、异步、非结构化的事件流持续编码为具有规则空间结构的多层 latent memories，并通过 adaptive update 跳过不必要的高层 memory computation。

模型首先把事件的相对位置、相对时间戳和 polarity 编码为 event embeddings，再通过 selective cross-attention 写入最低层 memory。更高层 memory 使用 window-based cross-attention 从相邻低层 memory 中提取信息。为避免每个时间步都更新全部层，模型对相邻 memory levels 做 global pooling，并利用 GRU 生成 update score；只有当该 score 超过人工设定的 threshold 时，才执行高层 memory update。

本文没有 spiking neuron、membrane potential、surrogate gradient 或 spike-driven layer，因此不属于 SNN。它更适合作为 event-camera adaptive state update 与 dense representation learning 的 non-spiking reference。

## 2. Problem and Motivation

Event camera 以微秒级时间分辨率异步输出亮度变化事件，但 semantic segmentation、object detection 和 depth estimation 等 dense tasks 要求规则的空间表示与明确的位置对应。

现有 frame-like representations 通常把一段事件聚合为 dense tensor，再交给 CNN 或 RNN。这种方式便于复用传统视觉网络，但会压缩事件级时间结构，并在相邻输入变化很小时重复执行完整 dense computation。

另一类 sparse methods，例如 graph、PointNet 或 event Transformer，可以保留事件的非结构化和稀疏特性，但较难直接形成适合 dense decoder 的多尺度 pixel-aligned features。Matrix-LSTM 具有显式位置对应，但为每个像素独立维护 recurrent state，随分辨率增加会带来较高计算与存储开销。

HMNet 已提出 hierarchical latent memories，将事件编码为适合 dense tasks 的多尺度 structured representation，但其 memory update rates 由人工固定。本文进一步解决的问题是：如何根据当前输入和历史 memory state，自适应决定高层 memory 是否值得更新。

## 3. Method Overview

在时间区间 τ 内，事件集合表示为：

$$
\mathcal{E}_{\tau}
=
\left\{
(x_k,y_k,t_k,p_k)
\mid
t_k\in\tau
\right\}.
$$

模型学习映射：

$$
\mathcal{F}:
\mathcal{E}_{\tau}
\rightarrow
\left\{
M_{\mathcal{E}_{\tau}}^{i}
\right\},
$$

其中 i 表示 memory hierarchy 的层级。

完整流程包括：

1. 将当前时间步内的事件按 spatial window 分组；
2. 分别编码 event position、timestamp 和 polarity；
3. 使用 selective cross-attention 将事件写入最低层 memory；
4. 使用 downsampling 与 window-based cross-attention 在相邻 memory levels 之间传递信息；
5. 使用 global pooling、GRU 和 scalar update score 决定是否执行高层更新；
6. 通过 readout buffers 将多尺度 memory states 转换为 decoder-ready features；
7. 使用 UPerNet、YOLOX 或 UNet 完成对应 dense task。

论文采用三层 memories，通道维度为 32、64 和 128，对应 spatial strides 为 4、8 和 16。

## 4. Key Components and Mechanisms

### 4.1 Event Encoding and Lowest-Level Memory

每个事件被转换为：

$$
\pi_k
=
\operatorname{LN}
\left(
\left[
F_{\mathrm{pos}}(\hat{x}_k,\hat{y}_k),
F_t(\hat{t}_k),
F_p(p_k)
\right]
\right),
$$

其中三支 MLP 分别编码相对位置、相对时间戳和 polarity。

最低层 memory 与规则 image-plane windows 一一对应。对于某个 window 内的 n 个事件，memory cell 作为 query，event embeddings 作为 key 和 value：

$$
q_{ij}
=
\mathcal{Q}(s_{ij}),
\qquad
K
=
\mathcal{K}(\pi),
\qquad
V
=
\mathcal{V}(\pi),
$$

$$
s_{ij}^{\mathrm{new}}
=
\operatorname{softmax}
\left(
\frac{q_{ij}K^{\mathsf{T}}}{\sqrt{D}}
\right)
V.
$$

只有接收到事件的 windows 才进行这一步更新，因此最低层能够利用输入 sparsity。需要注意的是，这里建立的是 window-level spatial association，而不是每个原始像素对应一个独立 memory cell。

### 4.2 Hierarchical Memory Update

相邻 memory levels 之间使用 window-based multi-head cross-attention。高层 memory 提供 query，经过 downsampling 的低层 memory 提供 key 和 value。其结构等价于：

$$
\hat{M}_{n+1}
=
\operatorname{WCA}
\left(
M_{n+1},
\operatorname{Down}(M_n)
\right)
+
M_{n+1},
$$

$$
M_{n+1}^{\mathrm{updated}}
=
\operatorname{MLP}
\left(
\operatorname{LN}(\hat{M}_{n+1})
\right)
+
\hat{M}_{n+1}.
$$

这使高层 memory 在保留历史状态的同时，吸收来自低层的新信息。

### 4.3 Adaptive Update Decision

模型先对相邻 memory levels 做 global pooling：

$$
M_n^{G}
=
\operatorname{GPool}(M_n),
\qquad
M_{n+1}^{G}
=
\operatorname{GPool}(M_{n+1}).
$$

随后使用 GRU 和 linear mapping 得到 scalar update score：

$$
\widehat{Th}
=
\mathcal{R}
\left(
M_{n+1}^{G},
M_n^{G}
\right),
$$

$$
Th
=
\operatorname{sigmoid}
\left(
\operatorname{MLP}(\widehat{Th})
\right).
$$

当 score 大于人工设置的 threshold 时，执行高层 memory update；否则保留过去状态。每次真正更新后，GRU hidden state 被 reset，使其重新累计自上次更新以来的新信息。

论文学习的是 content-dependent update score，而不是 threshold 本身。默认 threshold 为 0.5，因此所谓 adaptive update rate 实际由 learned score 与 fixed threshold 共同决定。

### 4.4 Readout Buffers

每一层 memory 通过 readout module 转换为 task decoder 使用的 feature：

$$
ro_n
=
c_{\mathrm{ro}}
\left(
\operatorname{LN}(M_n)
\right).
$$

该模块包含 point-wise convolution、Group Normalization 和 SiLU activation。多层 readout states 组成多尺度 feature pyramid，并输入对应的 dense task head。

## 5. Experiments and Main Evidence

实验覆盖 DSEC-Semantic segmentation、GEN1 object detection 和 MVSEC depth estimation。所有 latency 均在 NVIDIA Tesla V100 GPU 上测量。

在 DSEC-Semantic 上，本文取得 49.9 mIoU 和 4.5 ms latency。HMNet-B3 为 53.9 mIoU 和 9.7 ms，HMNet-L3 为 57.1 mIoU 和 13.9 ms。本文相对两者分别减少约 54% 和 68% latency，但 mIoU 分别低 4.0 和 7.2 points。

在 GEN1 上，本文取得 44.8 mAP 和 3.2 ms latency。HMNet-B3 为 45.2 mAP 和 7.0 ms，HMNet-L3 为 47.1 mAP 和 7.9 ms。本文相对 HMNet-L3 减少约 60% latency，但 mAP 低 2.3 points。

在 MVSEC 上，本文 latency 为 2.3 ms，低于 RAMNet 的 9.0 ms、HMNet-B3 的 5.0 ms 和 HMNet-L3 的 6.9 ms。其 depth error 优于 RAMNet，但整体仍高于固定更新的 HMNet variants。

Ablation 表明，adaptive update 相比 uniform update 将 latency 从 5.8 ms 降至 4.5 ms，同时 mIoU 从 49.7 略升至 49.9。Threshold sensitivity experiment 显示：threshold 从 0.3 增至 0.7 时，latency 从 4.8 ms 降至 4.1 ms，但 mIoU 从 49.8 降至 46.8。该结果说明模型形成了明确的 accuracy–latency trade-off。

## 6. Strengths and Limitations

**Strengths**

- 将 sparse event input 映射为适合 dense tasks 的 hierarchical structured memories。
- Lowest-level memory 通过 selective cross-attention 利用事件稀疏性。
- Adaptive update 能跳过高层 WCA 和 MLP，显著降低 latency。
- 在 segmentation、detection 和 depth 三类 dense tasks 上验证了方法的通用性。
- Ablation 支持 adaptive update 相比 uniform update 的计算优势。

**Limitations**

- 本文不是 SNN，threshold-triggered module update 不等于 neuronal firing。
- Update threshold 仍需人工设置，且结果对该参数敏感。
- Hard decision 的具体可微训练方式没有充分说明。
- 相邻 memory levels 的 global vectors 维度不同，GRU 输入如何对齐也未详细展开。
- Higher-level memories 和 dense decoders 并不保持纯 sparse computation。
- 主要优势是 latency，而不是最高任务精度；与 fixed-update HMNet 相比存在明显 accuracy loss。
- Latency 来自 V100 GPU，不能直接等同于 edge-device energy efficiency。

## 7. Relation to Other Papers and Survey Taxonomy

本文直接建立在 HMNet 的 hierarchical memory framework 上，主要新增 adaptive update decision。相较 Matrix-LSTM，它不为每个像素独立维护 recurrent unit；相较 EventFormer，它保留规则空间索引和多尺度 feature hierarchy，更适合 dense prediction；相较 frame-like CNN methods，它避免在每个时间步重建完整 event representation。

在综述 taxonomy 中，它属于：

- **Hierarchical event-memory representation**
- **Non-spiking adaptive computation**
- **Event-based dense prediction**
- **Conditional state update**
- **Latency-oriented ANN comparator for SNNs**

它适合与 SNN 的 membrane-state accumulation、threshold triggering 和 sparse temporal update 进行概念比较，但不能作为 SNN architecture 的实例。

### PDF-verified relation backfill

主要路线是把 raw-event encoding 写入规则索引的 hierarchical memories，并以 content-dependent gate 减少高层更新。

- **Hierarchical Neural Memory Network for Low Latency Event Processing (Ryuhei Hamaguchi et al., CVPR 2023)** — `extends`。当前论文沿用该工作的 hierarchical event memory updates，并针对当前任务增加新的结构或训练约束。 对应 Sections 2 and 6: dense representation and conditional computation。证据：Introduction, Related Work and Experiments, PDF pp.2-4 and 10-12, citation and bibliography [17]。 当前 active corpus 未覆盖。 值得 backward search。
- **Matrix-LSTM: A Differentiable Recurrent Surface for Asynchronous Event-Based Data (Marco Cannici et al., ECCV 2020)** — `alternative`。两者都处理 stateful event representation，但采用不同 representation、state 或 computation route。 对应 Section 2: event representation。证据：Related Work 2, PDF p.4, citation and bibliography [7]。 当前 active corpus 未覆盖。 值得 backward search。
- **Associative Memory Augmented Asynchronous Spatiotemporal Representation Learning for Event-based Perception (Uday Kamal et al., ICLR 2023)** — `same_task_different_mechanism`。两者解决相同任务中的 memory-based event representation，但核心计算机制不同。 对应 Section 2: event representation。证据：Introduction and Related Work, PDF pp.2 and 4, citation and bibliography [21]。 当前 active corpus 未覆盖。

## 8. Survey-Usable Takeaways

- Takeaway 1: 本文将 sparse event sets 写入具有规则空间索引的 hierarchical memories，从而连接 event-level input 与 dense prediction decoder。
- Takeaway 2: Lowest-level memory 利用 selective cross-attention，仅更新接收到事件的 windows；高层 memory 则采用 conditional update。
- Takeaway 3: Global pooling 与 GRU 用于累计自上次更新以来的 global context，并生成 content-dependent update score。
- Takeaway 4: Adaptive update 的主要收益是减少高层 memory recomputation，而不是提升最高任务精度。
- Takeaway 5: 该方法是 non-spiking memory network，可作为 SNN adaptive state update 的模块级 ANN 对照。

## Supplement Points

### Questions and Clarifications

#### 从输入事件到最终输出的数据流及维度如何变化？

以 DSEC-Semantic 的 480 × 640 输入为例，假设当前时间步包含 N 个事件。原始输入维度为：

$$
E_t
\in
\mathbb{R}^{N\times4},
$$

其中四个属性为 x、y、t 和 p。

事件经过 position、timestamp 和 polarity MLP 后，形成 32 维 embeddings：

$$
\Pi_t
\in
\mathbb{R}^{N\times32}.
$$

第一层 memory 的 stride 为 4，因此空间尺寸为 120 × 160，对应：

$$
M_1
\in
\mathbb{R}^{120\times160\times32}.
$$

每个 4 × 4 spatial window 对应一个 memory cell。假设某个 window 内有 7 个事件，则该 window 的 event features 为 7 × 32，memory query 为 1 × 32，cross-attention 输出仍为 1 × 32。

第二层 memory 的 stride 为 8：

$$
M_2
\in
\mathbb{R}^{60\times80\times64}.
$$

第一层经过 downsampling 后变成 60 × 80 × 64，再根据 update score 决定是否通过 WCA 更新第二层。

第三层 memory 的 stride 为 16：

$$
M_3
\in
\mathbb{R}^{30\times40\times128}.
$$

第二层经过 downsampling 后变成 30 × 40 × 128，再根据独立的 update score 决定是否更新第三层。

因此，hierarchical memory pyramid 为：

$$
120\times160\times32
\rightarrow
60\times80\times64
\rightarrow
30\times40\times128.
$$

三个 memory levels 经 readout buffers 转换为多尺度 decoder features。对于 DSEC-Semantic 的 11 类 segmentation，UPerNet 最终输出：

$$
Y
\in
\mathbb{R}^{11\times480\times640}.
$$

经过逐像素 argmax 后，得到：

$$
\hat{Y}
\in
\mathbb{R}^{480\times640}.
$$

完整数据流可概括为：

```text
N × 4 raw events
→ N × 32 event embeddings
→ 120 × 160 × 32 memory level 1
→ 60 × 80 × 64 memory level 2
→ 30 × 40 × 128 memory level 3
→ multi-scale readout features
→ 11 × 480 × 640 semantic logits
→ 480 × 640 semantic mask
```

需要注意：论文没有明确给出 readout convolution 的最终 channel 数，也没有完整说明不同维度 global vectors 输入 GRU 前的 projection，因此这些实现细节仍需结合代码进一步确认。
