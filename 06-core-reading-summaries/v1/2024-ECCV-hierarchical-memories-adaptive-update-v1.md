---
title: "Efficient Learning of Event-based Dense Representation using Hierarchical Memories with Adaptive Update"
authors: ["Uday Kamal", "Saibal Mukhopadhyay"]
year: 2024
venue: "ECCV"
level: "B"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ECCV2024/B/2024-ECCV-B-efficient-learning-of-event-based-dense-representation-using-hierarchical-memories-with-ad.md"
official_page: "https://eccv.ecva.net/virtual/2024/poster/650"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10733.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "dense prediction", "hierarchical memory", "adaptive update", "event-by-event"]
---

# Summary V1｜Efficient Learning of Event-based Dense Representation using Hierarchical Memories with Adaptive Update

## 1. One-sentence Summary

本文提出 hierarchical latent memory representation 和 adaptive update mechanism，用 event-by-event processing 高效支持 event-based dense prediction tasks。

## 2. Research Problem

dense prediction 需要 pixel-level association，但 event-by-event processing 是稀疏、异步和非结构化的；把 events 聚合成静态 frame 会降低处理频率并增加计算成本。

## 3. Background and Motivation

event cameras 的价值在于高 temporal resolution。为了在 segmentation/depth/flow 等 dense tasks 中利用这一点，模型需要在保留像素结构的同时避免固定频率全量更新。

## 4. Method Overview

框架把 sparse asynchronous events 作为 unstructured set 处理，并投影到 hierarchical multi-level latent memory space。attention-based spatial association 把低层事件编码进 latent structures；adaptive update recurrently 跟踪过去 memory states，只在有足够新信息时更新对应 memory stacks。

## 5. Technical Details

### 1. Event Representation

事件以 set-based/event-by-event 方式输入，而非先固定聚合成 frame。
### 2. Memory Architecture

多层 latent memory 保留 pixel-level structure。
### 3. Adaptive Update

根据新信息量决定是否更新 memory stack，以降低 latency。
### 4. Training / Tasks

官方摘要称覆盖不同 event-based dense prediction tasks；PDF 可读但表格数值需人工深读。
### 5. SNN Module

无明确 SNN/spiking neuron，是 event-camera representation background。

## 6. Experiments

PDF 和 card 显示方法在多种 event-based dense prediction tasks 上取得 competitive performance，同时相对 existing methods 有更低 latency。具体 datasets、metrics、ablation 和 latency 数值需要人工核验。

## 7. Main Contributions

1. 提出 hierarchical memory space 表示 event-based dense features。
2. 用 attention-based spatial association 建立 event 到 pixel-level memory 的联系。
3. 提出 data-adaptive update rate，避免固定频率更新。
4. 面向 dense prediction 展示 event-by-event representation 的效率潜力。

## 8. Limitations and Risks

- 不是 SNN 方法，不能直接作为 SNN architecture 证据。
- “competitive performance” 和 “much lower latency” 需要表格数值支撑。
- adaptive update threshold/criterion 的鲁棒性需要人工核验。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background。它为 SNN event representation 提供可借鉴的 memory/update 思路，但不是 spiking neural network 论文。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs
- Event reconstruction
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- Hierarchical memory：多层 latent memory representation。
- Adaptive update：按信息量触发更新。
- Dense prediction：需要像素级输出的任务，如 segmentation/depth/flow。

## 12. Questions for Human Deep Reading

1. 具体 dense prediction tasks 是哪些？
2. adaptive update 的判据是否可微？
3. latency 如何测量，是否包含 event preprocessing？
4. memory size 与 image resolution 如何 scaling？
5. 能否与 SNN neuron state 类比或结合？

## 13. Evidence Notes

- Source card / official abstract: hierarchical memories、adaptive update、dense prediction motivation。
- PDF available locally; detailed tables need human verification.

## 14. Draft Survey-Usable Sentences

Draft material: Hierarchical adaptive memories offer a non-spiking reference point for efficient event-by-event dense representation.

Draft material: The paper can motivate survey discussion on whether SNN membrane states and event-memory representations solve similar temporal update problems.
