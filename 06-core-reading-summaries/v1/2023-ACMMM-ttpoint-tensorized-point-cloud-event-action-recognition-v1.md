---
title: "TTPOINT: A Tensorized Point Cloud Network for Lightweight Action Recognition with Event Cameras"
authors: ["Hongwei Ren", "Yue Zhou", "Haotian Fu", "Yulong Huang", "Renjing Xu", "Bojun Cheng"]
year: 2023
venue: "ACM MM"
level: "B"
priority: "SECNet reference-only"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "SECNet references / 00-index/reading-plan-core.md"
official_page: "https://doi.org/10.1145/3581783.3612258"
pdf_link: "https://arxiv.org/pdf/2308.09993"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "TTPOINT", "point cloud", "tensor-train decomposition", "action recognition", "Daily DVS", "DVS128 Gesture", "SECNet reference"]
---

# Summary V1｜TTPOINT: A Tensorized Point Cloud Network for Lightweight Action Recognition with Event Cameras

## 1. One-sentence Summary

TTPOINT 提出一个 tensorized point cloud network，通过 subwindow sampling、hierarchical local/global feature extraction 和 tensor-train decomposition，实现轻量级 event-based action recognition。

## 2. Research Problem

本文解决 event camera action recognition 中精度与计算成本的权衡问题。frame-based methods 把 event streams 转成 dense frames，容易丢失 fine-grained temporal information，并增加 memory / FLOPs；point-based methods 保留 sparsity，但以往精度常低于 frame-based methods。

作者希望设计一个可以直接处理 event points 的 lightweight network，让 DVS / event camera 的低功耗、低延迟优势不被后端算法抵消。

## 3. Background and Motivation

DVS event stream 包含 coordinate、timestamp 和 polarity。把事件视为 `(x, y, t)` points 可以避免 modality transformation，并保留 sparse temporal structure。

但 point-based methods 通常只随机采样少量 points。由于 event density 随时间变化，random sampling 可能忽略低密度但关键的动作片段。另一方面，PointNet/PointNet++ 风格网络仍可能参数较多。TTPOINT 的动机是通过 subwindow sampling 保住 temporal coverage，并用 tensor-train decomposition 压缩 feature extractors。

## 4. Method Overview

TTPOINT 的 pipeline 是：将 event stream 切成 fixed-length sliding windows；在每个 window 内再划分多个 subwindows 并采样 points；把采样点送入 hierarchical point cloud structure；用 residual local extractors 和 residual global extractors 提取 spatiotemporal features；用 MLP classifier 输出 action class。

输入数据是 event camera stream / Event Cloud，表示为 point cloud-style `(x, y, t)` samples。模型不是 SNN，而是 ANN point network with tensor-train compressed layers。输出是 action recognition label。

## 5. Technical Details

### Event Representation

事件被直接表示为 points。作者强调 event streams 的时序密度不均匀，因此在 sliding window 内使用 subwindow sampling，保证时间轴上不同片段都能被采样，而不是只从高密度区域抽点。

### Spiking Neuron / SNN Module

本文没有 spiking neuron 或 SNN module。它在 conclusion 中把 future work 指向 point cloud processing network 和 SNN 的结合，但当前 TTPOINT 是 non-spiking point-based ANN。

### Network Architecture

TTPOINT 包含 sampling、hierarchical feature extraction 和 classifier。hierarchical structure 类似 point cloud network，包含 local extractor 和 global extractor。local extractor 对邻域几何/时空局部模式建模；global extractor 聚合更高层 feature。

### Training Strategy

论文在五个 event-based action recognition datasets 上训练同一类架构，主要通过调整输出类别数适配不同数据集。训练设置包括 Adam / cosine schedule 等，具体超参数在 Section 4.2。

### Loss Function

任务是 classification，主要使用 standard classification objective。论文核心不是新 loss，而是 sampling 与 tensorized architecture。

### Inference Process

推理时每个 event stream/window 被采样为固定数量 points，经 TTPOINT backbone 和 classifier 输出类别。作者强调该流程适合 low-latency / limited-computation devices。

## 6. Experiments

数据集包括 Daily DVS、DVS128 Gesture、DVS Action、HMDB51-DVS 和 UCF101-DVS。Table 1 给出每个数据集的 classes、sensor resolution、avg length、train/test samples、sliding window 和 overlap。

Daily DVS 上，TTPOINT 报告 0.335M params、0.587 GFLOPs、99.1% accuracy。DVS128 Gesture 上，0.334M params、0.587 GFLOPs、98.8% accuracy。DVS Action 上，0.334M params、0.587 GFLOPs、92.7% accuracy。

在 larger datasets 上，HMDB51-DVS 为 56.9%，UCF101-DVS 为 72.5%。作者指出对大数据集可能需要更复杂结构或更高 rank，否则 compression 会导致 underfitting。

Ablation 方面，Table 7 比较 subwindow length：在 DVS128 Gesture 上从 no subwindow 97.0% 提升到 97.8%；在 DVS Action 上从 87.5% 提升到 92.7%。Table 8 比较 uncompressed model、TTPOINT 和 TTPOINT_tiny：compression 在 Daily DVS、DVS Action 和 DVS128 Gesture 上几乎不损失甚至提升，但在 HMDB51-DVS 上下降更明显。

local/global extractor ablation 显示 DVS128 Gesture sliding-window accuracy：only local 为 96.19%，only global 为 90.2%，local+global 为 97.78%，说明 local extractor 是关键，global extractor 提供额外提升。

## 7. Main Contributions

1. 提出 lightweight point-based network TTPOINT，用于 event camera action recognition。
2. 设计 subwindow sampling，缓解 random sampling 对 temporal density 不均的敏感性。
3. 在 hierarchical point feature extraction 中引入 tensor-train decomposition，显著降低参数量。
4. 在五个 action recognition datasets 上系统比较 accuracy、params 和 GFLOPs。
5. 为 EventMamba / SECNet 这条 advisor-track point/event cloud 方法链提供前序 baseline。

## 8. Limitations and Risks

TTPOINT 不是 SNN，不能作为 SNN efficiency 的直接证据。

在 HMDB51-DVS 和 UCF101-DVS 上，TTPOINT 与更强 frame/voxel methods 仍有差距；作者也承认相同结构未针对大数据集优化。

tensor-train compression 对小/中数据集可能有 regularization 效果，但对大数据集可能 underfit。survey 使用时应避免笼统声称 compression 总是有效。

ACM official page 需要人工核验 DOI 与 arXiv PDF 版本是否完全一致；PDF 首页的 DOI 字段是 placeholder。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background；advisor-track support。

TTPOINT 是 event camera point representation 和 lightweight event recognition 的重要背景，不是 SNN core paper。它对 survey 的价值在于说明 event streams 可以被 sparse point cloud pipeline 处理，并为后续 SpikePoint / EventMamba / SECNet 提供表示和效率参照。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：event stream as point cloud。
- Event-based action recognition：五个 action datasets。
- Efficiency, latency, and energy：params、GFLOPs、lightweight inference。
- Datasets and benchmarks：Daily DVS、DVS128 Gesture、DVS Action、HMDB51-DVS、UCF101-DVS。
- Open challenges：sampling robustness、large dataset scaling、compression trade-off。

## 11. Key Terms and Concepts

- TTPOINT：tensorized point cloud network for event action recognition。
- Subwindow sampling：在 sliding window 内按时间子窗口采样，保持 temporal coverage。
- Tensor-train decomposition：把 dense feature extractor 压缩为 tensorized layer，减少参数。
- Local/global extractor：分别提取邻域局部结构和全局上下文。
- DVS Action / Daily DVS：用于 event-based action recognition 的真实 event datasets。

## 12. Questions for Human Deep Reading

1. ACM final version 与 arXiv version 是否一致？
2. subwindow sampling 的具体实现是否会引入 dataset-specific tuning？
3. Table 8 中 compression 对不同 dataset 的影响是否和 dataset size 直接相关？
4. TTPOINT 的 0.587 GFLOPs 是否包含 sampling / preprocessing？
5. local/global extractor 的详细结构与 PointNet++ Set Abstraction 的差异是什么？
6. 对 SECNet 来说，TTPOINT 的哪些模块被继承或替代？
7. 是否有 real hardware latency / energy measurement，还是仅报告 FLOPs？
8. 该方法能否扩展到 detection / tracking，而不仅是 classification？

## 13. Evidence Notes

- Abstract，第 1 页：说明 TTPOINT、tensor-train compression、SOTA claims 和 55% parameter compression。
- Section 1，第 2 页：提出 subwindow sampling、hierarchical structure、TTD module 和三条 contributions。
- Section 4.1 / Table 1，第 6-7 页：datasets and splits。
- Table 2-6，第 7 页：main action recognition results。
- Table 7-8，第 8 页：subwindow 和 tensor-train compression ablations。
- Conclusion，第 8 页：指出 future work 会结合 point cloud processing network 与 SNN。

## 14. Draft Survey-Usable Sentences

Draft material: TTPOINT is an early lightweight point-based baseline showing that event streams can be processed directly as sparse point samples instead of dense event frames.

Draft material: Its subwindow sampling strategy highlights a practical issue for event-cloud methods: uniform random sampling may miss temporally sparse but semantically important motion segments.

Draft material: For SNN-oriented surveys, TTPOINT is best treated as event-camera representation background and as a non-spiking efficiency baseline rather than as evidence for neuromorphic computation.
