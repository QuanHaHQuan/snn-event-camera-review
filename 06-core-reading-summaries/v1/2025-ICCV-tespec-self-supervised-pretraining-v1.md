---
title: "TESPEC: Temporally-Enhanced Self-Supervised Pretraining for Event Cameras"
authors: ["Mohammad Mohammadi", "Ziyi Wu", "Igor Gilitschenski"]
year: 2025
venue: "ICCV"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICCV2025/B/2025-ICCV-B-tespec-temporally-enhanced-self-supervised-pretraining-for-event-cameras.md"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Mohammadi_TESPEC_Temporally-Enhanced_Self-Supervised_Pretraining_for_Event_Cameras_ICCV_2025_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/ICCV2025/papers/Mohammadi_TESPEC_Temporally-Enhanced_Self-Supervised_Pretraining_for_Event_Cameras_ICCV_2025_paper.pdf"
local_pdf_status: "unavailable"
status: "auto-generated; needs human review"
tags: ["event camera", "self-supervised learning", "pretraining", "TESPEC", "masked image modeling", "advisor-track"]
---

# Summary V1｜TESPEC: Temporally-Enhanced Self-Supervised Pretraining for Event Cameras

## 1. One-sentence Summary

本文提出 TESPEC，用 long event sequences 和 pseudo grayscale video reconstruction target 进行 temporally-enhanced self-supervised pretraining，强化 event models 的长期时序理解。

## 2. Research Problem

event-based perception 需要 long-term temporal information，但现有 SSL pretraining 多模仿 RGB image 方法，只在短时间 raw events 上训练 feedforward models，忽略长时序。

## 3. Background and Motivation

raw events 只记录 brightness changes，需要历史信息理解场景语义。recurrent models 从头训练时有优势，但使用现有 SSL 权重时 feedforward models 可能更强，说明 event-specific pretraining 仍不足。

## 4. Method Overview

TESPEC 使用 masked image modeling paradigm，但设计新的 reconstruction target：把长 event sequences 累积为 pseudo grayscale videos，包含高层语义、对 sensor noise 鲁棒并减少 motion blur。模型通过重建该 target 学习长时序 event history。

## 5. Technical Details

### 1. Event Representation

long event sequences，而非短窗口 raw events。
### 2. Pretraining Target

pseudo grayscale videos from events。
### 3. Model Type

特别适合 recurrent models；具体 architecture 需 PDF。
### 4. Downstream Tasks

object detection、semantic segmentation、monocular depth estimation。
### 5. SNN Module

无明确 SNN，是 event SSL/pretraining background。

## 6. Experiments

PDF 未能下载。source card/official abstract 称 TESPEC 在 object detection、semantic segmentation、monocular depth estimation downstream tasks 达到 state-of-the-art。具体 datasets、metrics、pretraining epochs 和 ablation 需要人工核验。

## 7. Main Contributions

1. 提出面向 event cameras 的 temporally-enhanced SSL pretraining framework。
2. 首次利用 long event sequences 做 recurrent-friendly pretraining 的 claim 需要 PDF 核验。
3. 设计 pseudo grayscale video reconstruction target。
4. 覆盖 detection、segmentation、depth 多个 downstream tasks。

## 8. Limitations and Risks

- PDF 不可用，不能确认 SOTA 范围和实验设置。
- pseudo grayscale videos 可能引入 frame-like bias。
- 不是 SNN 方法，但可能对 SNN pretraining 有启发。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background; advisor-track support。它支撑 event pretraining 和 long-term temporal representation 讨论。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs
- SNN training methods
- Datasets and benchmarks
- Open challenges

## 11. Key Terms and Concepts

- TESPEC：Temporally-Enhanced Self-Supervised Pretraining for Event Cameras。
- Masked image modeling：遮盖输入并重建目标的 SSL 范式。
- Pseudo grayscale video：由 events 累积生成的重建目标。

## 12. Questions for Human Deep Reading

1. pseudo grayscale video 如何生成？
2. pretraining backbone 是 recurrent 还是 feedforward？
3. 下游三个任务分别用哪些数据集？
4. TESPEC 与 MAE/DINO 等 RGB SSL baseline 如何比较？
5. 能否用于 SNN surrogate-gradient pretraining？

## 13. Evidence Notes

- Source card / official abstract: long event sequences, pseudo grayscale videos, downstream tasks。
- Local PDF: unavailable after repeated download attempts.

## 14. Draft Survey-Usable Sentences

Draft material: TESPEC is relevant as event-camera pretraining background because it explicitly targets long-term temporal information rather than short event windows.

Draft material: Its direct relevance to SNNs remains speculative until architectures and training details are checked.
