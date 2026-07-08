---
title: "Efficient Event Camera Data Pretraining with Adaptive Prompt Fusion"
authors: ["Quanmin Liang", "Qiang Li", "Shuai Liu", "Xinzi Cao", "Jinyi Lu", "Feidiao Yang", "Wei Zhang", "Kai Huang", "Yonghong Tian"]
year: 2025
venue: "ICCV"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICCV2025/B/2025-ICCV-B-efficient-event-camera-data-pretraining-with-adaptive-prompt-fusion.md"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Liang_Efficient_Event_Camera_Data_Pretraining_with_Adaptive_Prompt_Fusion_ICCV_2025_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/ICCV2025/papers/Liang_Efficient_Event_Camera_Data_Pretraining_with_Adaptive_Prompt_Fusion_ICCV_2025_paper.pdf"
local_pdf_status: "unavailable"
status: "auto-generated; needs human review"
tags: ["event camera", "pretraining", "adaptive prompt fusion", "STP", "N-ImageNet", "advisor-track"]
---

# Summary V1｜Efficient Event Camera Data Pretraining with Adaptive Prompt Fusion

## 1. One-sentence Summary

本文提出 STP adaptive prompt fusion，将 event data representation 调整到 image-pretrained models 可接受的形式，并以轻量 spatiotemporal prompting 提升 event pretraining efficiency。

## 2. Research Problem

event camera data 稀缺且稀疏，大规模 pretraining 容易 overfit；直接套用 RGB SSL/pretraining 难以保留 event spatiotemporal structure。

## 3. Background and Motivation

image pretrained models 含有强视觉先验。event-camera pretraining 的关键是把 sparse temporal signals 映射到 image-model compatible representation，同时保留 event 的 temporal dynamics。

## 4. Method Overview

STP (SpatioTemporal information fusion Prompting) 使用 dynamic perception module 和 multi-scale spatiotemporal receptive fields，逐步融合 event data 的时空特征，减少 sparse regions，并沿 temporal dimension 做 global information exchange。输出 prompt-enhanced event representation 用于分类、语义分割和 optical flow fine-tuning。

## 5. Technical Details

### 1. Event Representation

把 event data representation 与 image pretrained models 对齐，同时保留 spatiotemporal structure。
### 2. Prompt Module

STP 是 lightweight prompt/fusion 方法，不是 SNN。
### 3. Dynamic Perception

multi-scale spatiotemporal receptive fields 捕获局部和全局时序信息。
### 4. Training Strategy

pretraining-finetuning paradigm；官方摘要称仅用 1/10 pretraining parameters 和 1/3 training epochs。
### 5. Experiments

classification、semantic segmentation、optical flow；N-ImageNet top-1 accuracy 68.87% (+4.04%)。

## 6. Experiments

PDF 未能下载。source card/official abstract 可确认任务包括 classification、semantic segmentation、optical flow estimation；N-ImageNet top-1 accuracy 为 68.87%，提升 +4.04%，且使用 1/10 pretraining parameters 和 1/3 training epochs。其余数据集和表格需人工核验。

## 7. Main Contributions

1. 提出面向 event camera data 的 efficient pretraining/fine-tuning framework。
2. 提出 lightweight STP prompt fusion。
3. 展示从 image pretrained models transfer 到 event domain 的有效性。
4. 在多个 downstream tasks 报告 SOTA 改善。

## 8. Limitations and Risks

- PDF 不可用，不能确认实验设置和 baseline fairness。
- 不是 SNN 方法，主要是 event pretraining background。
- 依赖 image pretrained models，可能与 neuromorphic/SNN low-power 目标存在距离。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background; advisor-track support。它对 survey 的 pretraining/representation 章节有帮助，但不应作为 SNN evidence。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs
- Datasets and benchmarks
- Event-based object detection
- SNN training methods
- Open challenges

## 11. Key Terms and Concepts

- STP：SpatioTemporal information fusion Prompting。
- Adaptive Prompt Fusion：动态融合 event spatiotemporal information 的 prompt 机制。
- N-ImageNet：event-based classification benchmark。

## 12. Questions for Human Deep Reading

1. STP 插入 image pretrained model 的哪些层？
2. pretraining 数据集规模和来源是什么？
3. 68.87% 的 baseline 是哪一个？
4. segmentation/optical flow 的提升是否同样稳定？
5. 该 representation 能否喂给 SNN？

## 13. Evidence Notes

- Source card / official abstract: STP、dynamic perception、N-ImageNet 68.87%。
- Local PDF: unavailable after repeated download attempts.

## 14. Draft Survey-Usable Sentences

Draft material: Adaptive prompt fusion is a non-spiking route for transferring image-model priors into event-camera representations.

Draft material: Its efficiency claims should be kept separate from neuromorphic energy efficiency.
