---
title: "Spike-driven Discrete Aggregation for Event-based Object Detection"
authors: ["Huaning Li", "Ziming Wang", "Runhao Jiang", "Yan Rui", "Huajin Tang"]
year: 2026
venue: "CVPR"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2026/A/2026-CVPR-A-spike-driven-discrete-aggregation-for-event-based-object-detection.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Li_Spike-driven_Discrete_Aggregation_for_Event-based_Object_Detection_CVPR_2026_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Spike-driven_Discrete_Aggregation_for_Event-based_Object_Detection_CVPR_2026_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "object detection", "SDA", "MTF", "Gen1", "1Mpx", "N-Caltech101"]
---

# Summary V1｜Spike-driven Discrete Aggregation for Event-based Object Detection

## 1. One-sentence Summary

本文提出 Spiking Discrete Aggregation (SDA)，用 gated recurrent spiking neurons 自适应选择信息量更高的 events，并用 MTF 补充粗粒度时序上下文以提升 event-based object detection。

## 2. Research Problem

event-based object detection 不仅依赖 backbone，也依赖把 asynchronous events 转为 dense tensors 的 representation。连续累积所有 events 会引入无信息事件和噪声，降低检测精度。

## 3. Background and Motivation

现有方法常用固定时间窗口或连续聚合来构建 event frame/voxel。SNN 的 threshold firing 机制提供了离散选择机制，可用于过滤事件并保持 differentiability。

## 4. Method Overview

SDA 通过 gated recurrent spiking neurons 实现 Discrete Aggregation，按 spike-firing 机制选择 informative events 进行 differentiable aggregation。Multi-Timescale Fusion (MTF) 从连续事件流中引入 coarse-grained temporal features，增强 SDA representation。输出进入 fully spiking 或 non-spiking detector。

## 5. Technical Details

### 1. Event Representation

SDA 不是简单累积所有 events，而是 adaptive and discrete selection。
### 2. Spiking Neuron

使用 gated recurrent spiking neurons，受 threshold-based spike firing 启发。
### 3. Network Architecture

SDA 可与 fully spiking detector 结合，也展示与 ANN 的 compatibility。
### 4. Training Strategy

在 Gen1、1Mpx 和 N-Caltech101 上评估；Gen1 使用检测窗口，具体长度见 PDF Section 5。
### 5. Inference

通过稀疏选择减少无关 events，MTF 提供多时间尺度上下文。

## 6. Experiments

PDF Section 5 报告 Gen1、1Mpx、N-Caltech101 三个 neuromorphic datasets。摘要与 PDF key lines 显示 DASNN-MTF 在 Gen1 达到 43.4% mAP50:95，比 prior art 高 4.5%，并使用更少参数；论文还报告相比 fully spiking architectures 的 SOTA、对 noisy conditions 的 robustness，以及与 non-spiking models 的兼容性。具体 1Mpx/N-Caltech101 数值需人工复核。

## 7. Main Contributions

1. 提出 Discrete Aggregation 视角，把 event representation 设计为可学习的事件选择过程。
2. 实现 SDA module，用 spiking neurons 聚合 informative events。
3. 提出 MTF 加入 coarse temporal context。
4. 在 Gen1/1Mpx/N-Caltech101 展示 fully spiking detector 的精度、参数和噪声鲁棒性。

## 8. Limitations and Risks

- 需要核验 SDA 的离散选择是否带来 latency 或训练不稳定。
- Gen1 43.4% mAP50:95 是重要数字，引用前应核对 Table 1。
- SDA 与 ANN compatibility 不能等同于完整 SNN 系统优势。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。它直接针对 event representation for SNN detectors，是 survey 的核心方法论文。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs
- SNN architectures for event cameras
- Event-based object detection
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- SDA：Spiking Discrete Aggregation。
- MTF：Multi-Timescale Fusion。
- DASNN-MTF：结合 SDA/MTF 的 detector variant。
- mAP50:95：COCO-style detection metric。

## 12. Questions for Human Deep Reading

1. SDA 的 gating/spike surrogate 如何训练？
2. MTF 对不同速度目标的影响如何？
3. 43.4% mAP50:95 的 baseline 列表有哪些？
4. energy efficiency 的计算公式和硬件假设是什么？
5. 噪声实验使用何种噪声模型？
6. SDA 接入 ANN detector 时是否仍保留 spike sparsity？

## 13. Evidence Notes

- PDF Abstract and Section 4: SDA/MTF method。
- PDF Section 5: Gen1、1Mpx、N-Caltech101 datasets。
- PDF key line: 43.4% mAP50:95 on Gen1 (+4.5 over prior art)。
- PDF Conclusion: robustness, ANN compatibility, fewer parameters。

## 14. Draft Survey-Usable Sentences

Draft material: SDA shifts event-SNN detection from fixed accumulation toward learned spike-driven event selection.

Draft material: The Gen1 43.4% mAP50:95 result makes this paper a strong candidate for the event representation subsection, pending table-level verification.
