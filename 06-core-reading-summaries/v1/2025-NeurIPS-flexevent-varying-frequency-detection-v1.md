---
title: "FlexEvent: Towards Flexible Event-Frame Object Detection at Varying Operational Frequencies"
authors: ["Dongyue Lu", "Lingdong Kong", "Gim Hee Lee", "Camille Simon Chane", "Wei Ooi"]
year: 2025
venue: "NeurIPS"
level: "B"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/B/2025-NEURIPS-B-flexevent-towards-flexible-event-frame-object-detection-at-varying-operational-frequencies.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/8064e4ebbcbe594628887b420956d8c3-Abstract-Conference.html"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/8064e4ebbcbe594628887b420956d8c3-Paper-Conference.pdf"
local_pdf_status: "unavailable"
status: "auto-generated; needs human review"
tags: ["event camera", "object detection", "event-frame fusion", "FlexEvent", "FlexFuse", "FlexTune"]
---

# Summary V1｜FlexEvent: Towards Flexible Event-Frame Object Detection at Varying Operational Frequencies

## 1. One-sentence Summary

本文提出 FlexEvent，通过 FlexFuse 和 FlexTune 让 event-frame object detector 在不同 operational frequencies 下保持检测性能。

## 2. Research Problem

现有 event detectors 常固定在特定 frequency/window 设置，无法充分利用 event data 的高 temporal resolution，也难以在动态环境下适配 20-180 Hz 等不同检测频率。

## 3. Background and Motivation

event cameras 可支持高频 real-time perception，但 detector 的 label、fusion 和 training protocol 往往固定频率。RGB frames 含语义，events 含高频运动，频率变化会影响二者融合。

## 4. Method Overview

FlexEvent 包含 FlexFuse 和 FlexTune。FlexFuse 是 adaptive event-frame fusion module，将 high-frequency event data 与 RGB frame semantic information 融合；FlexTune 是 frequency-adaptive fine-tuning mechanism，生成 frequency-adjusted labels，提高模型跨 operational frequencies 的泛化。输出为 object detections。

## 5. Technical Details

### 1. Event Representation

处理 varying operational frequencies 下的 event data。
### 2. Fusion Module

FlexFuse 自适应融合 event 与 frame features。
### 3. Training Strategy

FlexTune 通过 frequency-adjusted labels 做 fine-tuning。
### 4. Experiments

官方摘要称在 large-scale event camera datasets 上测试，覆盖 standard/high-frequency settings。
### 5. SNN Module

无 SNN，是 event-frame detection background。

## 6. Experiments

PDF 未能下载。官方摘要称 FlexEvent 在 standard 和 high-frequency settings 上超过 SOTA，从 20 Hz scaling 到 90 Hz 时保持 robustness，并可检测到 180 Hz。具体 datasets、mAP、FPS、label generation 和 baseline 需要人工核验。

## 7. Main Contributions

1. 提出 flexible event-frame object detection problem setting。
2. 设计 FlexFuse adaptive fusion module。
3. 设计 FlexTune frequency-adaptive fine-tuning 和 label adjustment。
4. 强调 20-90 Hz robustness 与 180 Hz high-frequency detection。

## 8. Limitations and Risks

- PDF 不可用，不能确认数据集和指标。
- 依赖 RGB-event fusion，可能不适用于 event-only/SNN low-power setting。
- frequency-adjusted labels 的生成可能引入额外假设。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background。它不含 SNN，但对 event detector 在不同推理频率下的鲁棒性讨论很重要。

## 10. Relation to Survey Taxonomy

- Event-based object detection
- Event representations for SNNs
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- FlexEvent：varying-frequency event-frame object detector。
- FlexFuse：adaptive event-frame fusion module。
- FlexTune：frequency-adaptive fine-tuning mechanism。
- Operational frequency：检测/输出频率。

## 12. Questions for Human Deep Reading

1. FlexTune 的 frequency-adjusted labels 如何生成？
2. 20/90/180 Hz 的 evaluation protocol 是什么？
3. large-scale event camera datasets 是哪些？
4. RGB frame frequency 与 event frequency 如何同步？
5. 能否转化为 event-only 或 SNN-friendly setting？

## 13. Evidence Notes

- Source card / official abstract: FlexFuse, FlexTune, 20 Hz to 90 Hz, up to 180 Hz。
- Local PDF: unavailable after repeated download attempts.

## 14. Draft Survey-Usable Sentences

Draft material: FlexEvent is useful background for the frequency-flexibility problem in event-based detection.

Draft material: Its RGB-event fusion design is not directly an SNN contribution, but it highlights evaluation settings that SNN detectors should eventually handle.
