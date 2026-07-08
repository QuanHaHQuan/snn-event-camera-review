---
title: "SDTrack: A Baseline for Event-based Tracking via Spiking Neural Networks"
authors: ["Yimeng Shan", "Zhenbang Ren", "Haodi Wu", "Wenjie Wei", "Rui-Jie Zhu", "Shuai Wang", "Dehao Zhang", "Yichen Xiao", "Jieyuan Zhang", "Kexin Shi", "Jingzhinan Wang", "Jason K. Eshraghian", "Haicheng Qu", "Malu Zhang"]
year: 2026
venue: "CVPR"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2026/A/2026-CVPR-A-sdtrack-a-baseline-for-event-based-tracking-via-spiking-neural-networks.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Shan_SDTrack_A_Baseline_for_Event-based_Tracking_via_Spiking_Neural_Networks_CVPR_2026_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Shan_SDTrack_A_Baseline_for_Event-based_Tracking_via_Spiking_Neural_Networks_CVPR_2026_paper.pdf"
local_pdf_status: "unavailable"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "tracking", "SDTrack", "GTP", "spike-driven Transformer"]
---

# Summary V1｜SDTrack: A Baseline for Event-based Tracking via Spiking Neural Networks

## 1. One-sentence Summary

本文提出 SDTrack，用 Global Trajectory Prompt 聚合 event frames，并结合 fully spike-driven SNN backbone 与 tracking head 构成 Transformer-based event tracking pipeline。

## 2. Research Problem

event-based tracking 适合高速、高动态范围场景，但现有 ANN/SNN hybrids 结构不够匹配，可能牺牲能效或 tracking accuracy。

## 3. Background and Motivation

event cameras 输出稀疏异步事件，SNN 用 discrete spikes 表示信息，二者天然契合。tracking 还需要把稀疏短时事件转成能支持 template-search matching 的稳定表示。

## 4. Method Overview

SDTrack pipeline 包含 Global Trajectory Prompt (GTP) event frame aggregation 与 Transformer-based tracker。GTP 将 global trajectory information 与 event streams 聚合为 event frames；tracker 包含 fully spike-driven SNN backbone 和 simple tracking head；官方摘要称 end-to-end，无 data augmentation 或 post-processing。

## 5. Technical Details

### 1. Event Representation

GTP 是核心 event frame aggregation method，用全局轨迹提示增强 spatiotemporal representation。
### 2. Spiking Module

backbone 为 fully spike-driven SNN；具体 neuron model 和 surrogate gradient 需 PDF 核验。
### 3. Architecture

Transformer-based tracker + simple tracking head。
### 4. Efficiency

官方摘要给出 SDTrack-Tiny 19.61M parameters 与 8.16mJ energy consumption。
### 5. Experiments

Base version 声称在 three datasets 上达到 SOTA accuracy；具体数据集和指标需核验。

## 6. Experiments

PDF 未能下载。source card/official abstract 可确认 SDTrack-Tiny 为 19.61M parameters、8.16mJ energy consumption，Base version 在三个数据集上达到 SOTA accuracy。具体 benchmark、success/precision 指标、baseline 和能耗计算方法为 Needs human verification。

## 7. Main Contributions

1. 提出 Transformer-based Spike-Driven Tracking pipeline。
2. 提出 GTP 聚合 event stream 为更强 event frame representation。
3. 提供 Tiny/Base 两种规模的 accuracy-efficiency trade-off。
4. 把 event-based tracking 明确作为 SNN benchmark/baseline。

## 8. Limitations and Risks

- PDF 未下载，不能确认三个数据集和指标细节。
- energy consumption 是否包括 event aggregation 和 tracking head 未知。
- GTP 是否削弱 event-by-event/asynchronous 优势需要人工判断。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。它直接面向 event-based tracking，是 survey 中 tracking subsection 的核心候选。

## 10. Relation to Survey Taxonomy

- Event-based tracking
- SNN architectures for event cameras
- Event representations for SNNs
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- SDTrack：Spike-Driven Tracking pipeline。
- GTP：Global Trajectory Prompt。
- Spike-driven backbone：以 spike activations 为主的 SNN feature extractor。
- mJ：能耗单位，需确认测量范围。

## 12. Questions for Human Deep Reading

1. GTP 的数学定义和 aggregation window 是什么？
2. SNN backbone 使用何种 neuron model？
3. tracking head 是否 spiking？
4. 三套 tracking datasets 是哪些？
5. 8.16mJ 包含哪些模块？
6. 没有 data augmentation/post-processing 的设置是否与 baseline 公平？

## 13. Evidence Notes

- Source card / official abstract: GTP、fully spike-driven SNN backbone、19.61M parameters、8.16mJ。
- Local PDF: unavailable after repeated download attempts.

## 14. Draft Survey-Usable Sentences

Draft material: SDTrack frames event tracking as a spike-driven Transformer pipeline, with GTP acting as a bridge from asynchronous events to trackable event frames.

Draft material: The reported 8.16mJ figure is promising but should be cited only after verifying the measurement scope.
