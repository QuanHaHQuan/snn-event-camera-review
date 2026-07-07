---
title: "EAS-SNN: End-to-End Adaptive Sampling and Representation for Event-based Detection with Recurrent Spiking Neural Networks"
authors: ["Ziming Wang", "Ziling Wang", "Huaning Li", "Lang Qin", "Runhao Jiang", "De Ma", "Huajin Tang"]
year: 2024
venue: "ECCV"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ECCV2024/A/2024-ECCV-A-eas-snn-end-to-end-adaptive-sampling-and-representation-for-event-based-detection-with-rec.md"
official_page: "https://eccv.ecva.net/virtual/2024/poster/711"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07766.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "object detection", "adaptive sampling", "RSNN", "Gen1", "N-Caltech101", "1Mpx"]
---

# Summary V1｜EAS-SNN: End-to-End Adaptive Sampling and Representation for Event-based Detection with Recurrent Spiking Neural Networks

## 1. One-sentence Summary

EAS-SNN 将 recurrent convolutional SNN 用作 event stream 的 learnable adaptive sampler，并通过 RPD 与 SAT 缓解 spike-based sampling degradation，从而提升 event-based object detection 的精度与效率。

## 2. Research Problem

本文关注 event-based object detection 中的 event sampling / representation 问题。多数方法把精力放在更强的 detection backbone 或固定 event representation 上，而事件流在进入 detector 前如何根据运动和纹理动态采样仍没有被充分处理。

这个问题对 SNN + event camera 很关键：event cameras 产生异步、稀疏、高时间分辨率数据；如果用固定时间窗口或固定事件数切片，容易在 fast/slow motion、blurred/sparse texture 场景中丢掉时间信息。SNN 的 membrane potential accumulation 与 threshold firing 与“信息积累到足够程度时采样”的理想 sampler 很接近，因此作者把 SNN 明确建模为 adaptive temporal sampler。

## 3. Background and Motivation

event cameras 具备高动态范围、高时间分辨率和低功耗优势，适合快速运动和复杂光照下的 detection。现有 dense ANN detector 往往需要把 event stream 聚合为 dense tensor，可能牺牲事件数据稀疏性。SNN 虽然适合 event-driven computation，但深层 SNN 训练和长 time steps 带来性能与效率挑战。

论文的核心动机是：与其只设计后端 detector，不如把 sampling 和 aggregation 本身做成端到端可学习模块，让 spiking neuron 的 firing time 决定采样窗口，并把累积的 membrane potential 作为下游 detector 的 embedding。

## 4. Method Overview

整体 pipeline 是：raw event stream 先经过 early aggregation 得到细粒度 event cells；recurrent convolutional SNN / ARSNN 按 membrane potential 和 spike firing 自适应采样；每次 firing 对应一个 sampled event group 或 potential embedding；随后送入 spike-based YOLOX-style detector 完成 object detection。

输入是 event camera stream，事件包含空间坐标、polarity 和 timestamp。方法不是简单固定 bin，而是用 spiking neuron 在不同位置、polarity 和时间上决定何时采样。模型包含 recurrent spiking sampling module、RPD、SAT、spiking backbone / FPN / detection head 的不同组合。输出是 object bounding boxes。

## 5. Technical Details

### Event Representation

论文把事件流先转换为高时间分辨率的 event inputs，再由 adaptive sampler 决定有效采样窗口。与 Event Count、Voxel Grid、Time Surface、Voxel Cube 等固定表示相比，ARSNN 允许每个 spatial-polarity 位置根据自身活动产生不同 sampling interval。

### Spiking Neuron / SNN Module

核心是 recurrent convolutional SNN。每个位置的 spiking neuron 接收局部 event input，membrane potential 按 LIF dynamics 积累并衰减，达到阈值时 firing。作者把 firing 解释为一次 sampling action；potential accumulation 则被用作 embedding，避免 sampling 与 aggregation 完全分离造成训练不稳定。

### Network Architecture

EAS-SNN 的 adaptive representation 由 SNN、RSNN 和 ARSNN 逐步发展而来。实验中的 detector 采用 SYOLOX-S / SYOLOX-M 结构，包含 spiking backbone、FPN 和 YOLOX detection head 的不同 spiking/non-spiking 配置。

### Training Strategy

训练使用 BPTT 与 surrogate gradient。作者提出 Residual Potential Dropout (RPD)，丢弃最后一次 spike 后残留的事件信息，防止 neuron 不 firing 也能通过残余 potential 给出表示，从而削弱学习正确 firing time 的动力。Spike-Aware Training (SAT) 则用于引导 threshold 附近的 gradient，使 firing time 更新更稳定。

### Loss Function

论文未把检测损失作为新贡献；检测部分沿用 YOLOX-style object detection loss。方法层面的关键是 RPD/SAT 对 adaptive sampling module 的训练约束。

### Inference Process

推理时，event stream 连续输入 SNN sampler；spikes 触发采样并生成 representation；detector 在较少 time steps 下运行。Table 3 中 EAS-SNN 使用 3 timesteps，与若干 SNN baseline 的 5 timesteps 相比更少。

## 6. Experiments

数据集包括 N-Caltech101、Prophesee Gen1 和 1Mpx。N-Caltech101 含 8,709 event streams，并带 bounding box / contour annotations；Gen1 含超过 39 小时 automotive recordings，含 228k+ car labels 和 28k pedestrian labels；1Mpx 为 1280x720 高分辨率 driving recordings，含超过 24M labels。

Table 1 的 ablation 显示，ARSNN + RPD + SAT 在 N-Caltech101 达到 0.664 mAP50 / 0.437 mAP50:95，在 Gen1 达到 0.731 mAP50 / 0.409 mAP50:95，高于 RSNN 的 0.634 / 0.412 与 0.719 / 0.399。

Table 2 显示 ARSNN 优于 Event Count、Voxel Grid、Time Surface、Voxel Cube、SNN 和 RSNN，在 N-Caltech101 和 Gen1 上均达到最高 mAP50:95。

Table 3 的 Gen1 comparison 中，EAS-SNN(M) with YOLOX non-spiking FPN/head 达到 0.731 mAP50 / 0.409 mAP50:95，25.3M params，3 timesteps；EAS-SNN(S) 达到 0.687 / 0.372，8.92M params，3 timesteps。它超过 EMS-ResNet34 的 0.590 / 0.310，并接近部分 ANN/RNN 方法，但低于 RVT / ERGO / ASTMNet 等强 dense 或 recurrent methods。

Table 5 在 1Mpx 上报告 EAS-SNN(M) 达到 0.651 mAP50 / 0.362 mAP50:95，是论文声称的 first spike-based result on 1Mpx。论文还报告相比 ANN 有 5.85x less energy consumption，但能耗计算细节需要人工进一步核验。

## 7. Main Contributions

1. 将 recurrent convolutional SNN 显式建模为 event stream adaptive sampler。
2. 提出 ARSNN，把 adaptive sampling 与 potential aggregation 结合为端到端检测表示。
3. 提出 RPD 和 SAT，缓解 spike-based sampling module 的 non-firing collapse / sampling degradation。
4. 在 N-Caltech101、Gen1、1Mpx 上展示 SNN-based detection 的性能与效率优势。
5. 证明 adaptive sampling 思路也可迁移到 conventional dense neural networks。

## 8. Limitations and Risks

EAS-SNN 在 Gen1 上仍低于 RVT、ERGO-12、ASTMNet 等强 ANN/RNN/Transformer methods，因此不能被描述为 event-based detection overall SOTA。

Table 3 同时包含 spiking backbone、spiking/non-spiking FPN 和 detection head 的多种设置；survey 中需要区分 fully spiking 与 hybrid spiking/dense head。

能耗优势来自计算估计和模型结构对比，硬件部署细节不如 Loihi-style 实测充分，需要人工核验 supplement 或代码。

ARSNN 仍依赖初始 event aggregation 和 detector recipe；其泛化到更多 detection head、真实 neuromorphic hardware 和复杂场景需进一步确认。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

它直接处理 event camera detection，并把 SNN 作为 event sampling 和 representation learning 的核心机制，而不是仅用 SNN 做后端分类器。它特别适合 survey 中讨论“SNN 如何替代固定 event representation / slicing”。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：adaptive sampling / potential aggregation。
- SNN architectures for event cameras：recurrent convolutional SNN sampler。
- Hybrid ANN-SNN models：不同 FPN/head 配置需要细分。
- Event-based object detection：Gen1、N-Caltech101、1Mpx detection。
- Efficiency, latency, and energy：3 timesteps、参数量、能耗估计。
- Open challenges：与 dense SOTA 差距、硬件验证、公平比较。

## 11. Key Terms and Concepts

- ARSNN：Adaptive Recurrent SNN，用于动态采样和表示事件流。
- RPD：Residual Potential Dropout，丢弃最后 spike 后残余 potential。
- SAT：Spike-Aware Training，改善 spike timing gradient guidance。
- Potential aggregation：把 membrane potential accumulation 作为下游 embedding。
- Gen1 / 1Mpx：event-based automotive detection benchmarks。
- mAP50 / mAP50:95：object detection 精度指标。

## 12. Questions for Human Deep Reading

1. ARSNN 的 firing interval 与传统 fixed-duration/fixed-count slicing 的可视化差异是否稳定？
2. RPD 是否会丢失 last spike 之后的重要事件？
3. SAT 的 gradient redirection 是否对 surrogate gradient 形状敏感？
4. Table 3 中 spiking head 为什么显著降低性能？
5. 5.85x energy saving 的计算假设是什么？
6. 1Mpx 上是否有完整 SNN baseline，还是主要是 first spike-based result？
7. ARSNN 是否能和更强 detector head 结合？
8. 代码是否复现 Gen1 0.409 mAP50:95？

## 13. Evidence Notes

- Abstract / Introduction：说明 adaptive event sampling 未充分研究，并提出 EAS-SNN。
- Section 3：描述 recurrent convolutional SNN、RPD、SAT。
- Section 4.1，第 9 页：给出训练设置和 N-Caltech101、Gen1、1Mpx 数据集。
- Table 1-2，第 10 页：ablation 和 representation comparison。
- Table 3-5，第 11-12 页：Gen1、N-Caltech101、1Mpx benchmark comparison。
- Figure 5-6，第 13 页：sampling behavior 和 qualitative comparison。

## 14. Draft Survey-Usable Sentences

Draft material: EAS-SNN reframes SNNs as adaptive event samplers, using spike firing times to determine event grouping rather than relying on fixed temporal windows.

Draft material: Its results suggest that adaptive spiking sampling can improve SNN-based event detection, although the best dense recurrent and transformer-based detectors remain stronger on Gen1.

Draft material: For taxonomy, EAS-SNN is a key example of event representation learning inside an SNN rather than outside it.

