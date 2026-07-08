---
title: "EventMG: Efficient Multilevel Mamba-Graph Learning for Spatiotemporal Event Representation"
authors: ["Sheng Wu", "Lin Jin", "Hui Feng", "Bo Hu"]
year: 2025
venue: "NeurIPS"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/B/2025-NEURIPS-B-eventmg-efficient-multilevel-mamba-graph-learning-for-spatiotemporal-event-representation.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/73d829353fdd9749f9b6cf26c5387f2e-Abstract-Conference.html"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/73d829353fdd9749f9b6cf26c5387f2e-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "Mamba", "graph neural network", "state space model", "event representation"]
---

# Summary V1｜EventMG: Efficient Multilevel Mamba-Graph Learning for Spatiotemporal Event Representation

## 1. One-sentence Summary

EventMG 提出一个 Mamba-Graph collaborative architecture，在 micro-level event graph 与 macro-level component graph 上联合建模 event streams，用于高效学习 spatiotemporal event representation。

## 2. Research Problem

论文关注 event camera 数据表示学习：事件流具有稀疏、异步、不规则和高时间分辨率等特点，直接建模很难，转换成 frame/voxel 又会损失微秒级时序结构并引入冗余。该问题是 event-camera side 的核心背景，也会影响 SNN 方法如何选择输入表示。

已有 frame-based representations 可复用 CNN/Transformer，但牺牲稀疏性；point/graph 方法保留事件结构，但可能难以捕获长程依赖；Mamba/SSM 有线性复杂度和长序列优势，但需要合适的 event scanning 顺序。EventMG 的目标是同时利用 graph 的局部拓扑能力和 Mamba 的长序列建模能力。

## 3. Background and Motivation

Event camera 输出 `(x, y, t, p)` 事件点，天然类似 spatiotemporal point cloud。对这类数据，局部事件簇、事件间拓扑关系和跨时间长程依赖都很重要。

Graph Neural Networks 可以处理局部邻域和拓扑，但长序列扩展成本较高。Mamba/SSM 适合线性复杂度序列建模，但 event stream 没有天然的规则扫描顺序。论文动机是通过 Spatiotemporal-aware Event Scanning Technology (SEST) 让 event graph 能以更适合 Mamba 的序列方式被处理。

## 4. Method Overview

EventMG 的 pipeline 包括三部分：Graph Construction、Mamba-Graph Architecture 和 Multilevel Fusion。输入为 sparse event stream；先构建 micro-level Event Graph 和 macro-level Component Graph；然后在 micro level 用 SSM-based Mamba 捕捉事件节点长程依赖，在 macro level 用 Component Graph 编码 event clusters 的局部语义和全局拓扑；最后融合多层级输出，供 object detection 或 action recognition 等下游任务使用。

论文没有把 EventMG 作为 SNN 方法，而是 event representation / event-camera backbone。它与 SNN 的关系主要在于提供事件表示和基线比较，尤其 Table 1/2/3 中包含 Spiking DenseNet、Motion-based SNN、Two-stream SNN 等。

## 5. Technical Details

### Event Representation

EventMG 直接面向事件点构图，而不是先把全部事件密集化成图像帧。micro level 关注 single event nodes，macro level 关注 event clusters/components。

### Spiking Neuron / SNN Module

论文没有提出 spiking neuron 或 SNN module。SNN 只作为 related work/baseline 出现。因此不能把 EventMG 写成 SNN paper。

### Network Architecture

核心由 Event Graph、Component Graph、SEST 和 Multilevel Fusion 组成。SEST 包括 Adaptive Perturbation Network (APN) 和 Multi-directional Scanning Module (MSM)。APN 通过 local/global feature paths 预测 `(Delta x, Delta y, Delta t)` perturbations，调整事件排列；MSM 用多方向扫描让 Mamba 捕捉不同时空轨迹。

### Training Strategy

论文在 object detection 和 action recognition 两类任务上训练和评估。具体任务头依下游任务变化；object detection 使用 mAP 和 inference time，action recognition 使用 accuracy、Params 和 GFLOPs。

### Loss Function

核心论文摘要未把 loss 作为主要创新。检测任务应使用对应 detector 的 detection losses，识别任务使用分类损失；具体细节需要人工核对实验设置。

### Inference Process

推理时模型先对 event stream 构图和扫描，再用 Mamba/SSM 对序列化后的图信息做线性复杂度时序建模，最后输出检测或识别结果。

## 6. Experiments

Object detection 在 Gen1 和 1Mpx datasets 上评估，指标包括 Params、mAP 和 backbone inference time。Table 1 显示 EventMG 使用 GNN + SSM backbone，参数约 1.96M；在 Gen1 上 mAP 53.7、time 8.66 ms；在 1Mpx 上 mAP 47.4、time 9.63 ms。与 ERGO-12、RVT-B、GET-T、S5-ViT-B 等相比，Gen1 mAP 最高，同时参数较少。

Action recognition 在 THUE-ACT-50-CHL、DVS Action、HMDB51-DVS、UCF101-DVS 上评估。Table 2 中 EventMG 在 THUE-ACT-50-CHL 上 accuracy 0.588，略低于 EventMamba 0.594，但参数和 GFLOPs 更低。Table 3 中 EventMG 在 DVS Action 达到 0.933 accuracy，高于 TTPOINT、EventMamba 和 Two-stream SNN。Table 4 中 EventMG 在 HMDB51-DVS / UCF101-DVS 上分别为 0.712 / 0.796，低于 EventMamba 0.864 / 0.979，但计算量更低。

Ablation Table 5 显示 Component Graph、APN、MSM 都有贡献；完整模型在 Gen1 detection mAP 0.537、THUE-ACT-50-CHL accuracy 0.588，移除任一模块均下降。

## 7. Main Contributions

- 提出 Mamba-Graph collaborative architecture，在 micro event nodes 和 macro event clusters 上联合建模。
- 提出 SEST，使 Mamba 更适配 event stream 的稀疏、不规则时空结构。
- 将 APN 和 MSM 组合，用 learnable perturbation 和 multidirectional scanning 改善事件序列化。
- 在 object detection 和 action recognition 上展示较强 accuracy-efficiency trade-off。

## 8. Limitations and Risks

论文 Conclusion 中提到未来需进一步探索 generalization across diverse tasks、robustness under extreme conditions、hyperparameter tuning 和 interpretability。V1 额外推断：EventMG 模块较多，构图、扰动、扫描方向等设计可能对数据集和实现细节敏感；在 HMDB51-DVS/UCF101-DVS 上不如 EventMamba，说明效率优势不总等于最高精度。

对综述风险：它不是 SNN 方法，不能作为 SNN architecture 证据；应放在 event representation / SSM event model 背景中，用来说明 SNN 之外的高效事件表示竞争路线。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background；同时属于 advisor-track support。

理由是论文核心是 event representation learning 和 Mamba-Graph event backbone，没有 spiking neuron 机制；但它处理的 sparse event representation、event graph 和效率问题会影响 SNN for Event Cameras 的背景与对比。

## 10. Relation to Survey Taxonomy

可支持的章节包括：

- Event representations for SNNs
- Event-based object detection
- Event-based tracking
- Datasets and benchmarks
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- Event Graph：以单个事件为节点构建的 micro-level spatiotemporal graph。
- Component Graph：以事件簇或 connected components 表示 macro-level structure。
- Mamba / SSM：线性复杂度序列建模模块，用于长程依赖。
- SEST：Spatiotemporal-aware Event Scanning Technology，使事件图可被 Mamba 有效扫描。
- APN：Adaptive Perturbation Network，学习事件坐标/时间扰动。
- MSM：Multi-directional Scanning Module，沿不同方向扫描事件结构。

## 12. Questions for Human Deep Reading

1. Event Graph 和 Component Graph 的构建细节是否依赖 hand-tuned thresholds？
2. APN 的 perturbation 是否可能改变事件的物理时序解释？
3. Table 1 中 backbone time 是否与其他方法的时间口径一致？
4. EventMG 在 1Mpx 上 mAP 与 S5-ViT-B 持平，优势主要来自参数还是速度？
5. 在 HMDB51-DVS/UCF101-DVS 上落后 EventMamba 的原因是什么？
6. SEST 的扫描方向 ablation 是否充分？
7. 该方法能否为 SNN 提供输入 representation，还是需要完整替代 SNN backbone？
8. 是否有 noise robustness 或 sensor domain shift 实验？

## 13. Evidence Notes

- Abstract：定义 EventMG、micro/macro multilevel modeling、SEST、APN、MSM。
- Figure 1：展示 Graph Construction、Mamba-Graph Architecture、Multilevel Fusion。
- Table 1：Gen1 和 1Mpx object detection 对比。
- Table 2-4：THUE-ACT-50-CHL、DVS Action、HMDB51-DVS、UCF101-DVS action recognition 对比。
- Table 5：Component Graph、APN、MSM ablation。
- Conclusion and Discussion：给出 generalization、robustness、hyperparameter tuning、interpretability 限制。

## 14. Draft Survey-Usable Sentences

草稿句 1：EventMG is not an SNN method, but it is useful background for SNN-event-camera surveys because it shows how sparse event streams can be modeled directly through graph construction and state-space sequence modeling.

草稿句 2：Its micro/macro Mamba-Graph design provides a non-spiking comparator for event representation learning, especially when discussing whether SNNs preserve event sparsity more naturally than dense frame-based pipelines.

草稿句 3：For survey writing, EventMG should be cited as event-camera representation background rather than as evidence for spiking computation.
