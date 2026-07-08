---
title: "PRE-Mamba: A 4D State Space Model for Ultra-High-Frequent Event Camera Deraining"
authors: ["Ciyu Ruan", "Ruishan Guo", "Zihang Gong", "Jingao Xu", "Wenhan Yang", "Xinlei Chen"]
year: 2025
venue: "ICCV"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICCV2025/B/2025-ICCV-B-pre-mamba-a-4d-state-space-model-for-ultra-high-frequent-event-camera-deraining.md"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Ruan_PRE-Mamba_A_4D_State_Space_Model_for_Ultra-High-Frequent_Event_Camera_ICCV_2025_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/ICCV2025/papers/Ruan_PRE-Mamba_A_4D_State_Space_Model_for_Ultra-High-Frequent_Event_Camera_ICCV_2025_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "deraining", "Mamba", "SSM", "PRE-Mamba", "EventRain-27K", "advisor-track"]
---

# Summary V1｜PRE-Mamba: A 4D State Space Model for Ultra-High-Frequent Event Camera Deraining

## 1. One-sentence Summary

本文提出 PRE-Mamba，一个 point-based event camera deraining framework，用 4D event cloud、STDF 和 MS3M 在保持高时间精度的同时去除 rain noise。

## 2. Research Problem

event cameras 在雨天会产生 dense noise；现有 event deraining 方法在 temporal precision、deraining effectiveness 和 computational efficiency 之间存在 trade-off。

## 3. Background and Motivation

raw events 的 point-based 形式保留高频时间信息，但也使噪声建模复杂。State Space Model/Mamba 适合长序列和多尺度动态建模，可用于捕获雨滴运动模式。

## 4. Method Overview

PRE-Mamba 输入 raw event/rain point cloud，构建 dual temporal scale 的 4D event cloud representation。STDF 做浅层 spatio-temporal decoupling and fusion；MS3M 捕获 dual-temporal 和 multi-spatial scales 下的 rain dynamics；frequency-domain regularization 辅助训练。输出为 derained event stream/labels。

## 5. Technical Details

### 1. Event Representation

4D event cloud 结合 inter- and intra-temporal windows 保留 native temporal resolution。
### 2. STDF

Spatio-Temporal Decoupling and Fusion module。
### 3. MS3M

Multi-Scale State Space Model，线性复杂度捕获多尺度雨动态。
### 4. Loss

PDF conclusion 提到 cross-entropy loss 与 frequency regularization。
### 5. Dataset

EventRain-27K，包含 synthetic 和 real-world rainy sequences。

## 6. Experiments

PDF abstract 报告 PRE-Mamba 在 EventRain-27K 上达到 0.95 SR、0.91 NR、0.4s/M events，参数量 0.26M。PDF key lines 显示 EventRain-27K 含 18K labeled synthetic 和 9K real-world sequences，并验证不同雨强、视角和雪天泛化。具体指标定义和 baseline 表格需人工核验。

## 7. Main Contributions

1. 提出首个 point-based event camera deraining framework PRE-Mamba。
2. 提出 4D event cloud representation。
3. 提出 STDF 和 MS3M 进行时空解耦/多尺度 SSM 建模。
4. 构建 EventRain-27K deraining dataset。
5. 报告轻量实时表现和跨天气泛化。

## 8. Limitations and Risks

- 不是 SNN 方法，属于 event-camera restoration/background。
- SR/NR 指标定义需要核验。
- 0.4s/M events 是否满足 real-time 取决于事件率和硬件。
- synthetic rain generation 与真实雨天 domain gap 需关注。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background; advisor-track support。它为 event restoration/noise filtering 和 SSM 模块提供参考。

## 10. Relation to Survey Taxonomy

- Event reconstruction
- Event representations for SNNs
- Efficiency, latency, and energy
- Datasets and benchmarks
- Open challenges

## 11. Key Terms and Concepts

- PRE-Mamba：point-based event camera deraining framework。
- 4D event cloud：包含空间、极性/事件和双时间尺度的表示。
- STDF：Spatio-Temporal Decoupling and Fusion。
- MS3M：Multi-Scale State Space Model。
- EventRain-27K：event deraining dataset。

## 12. Questions for Human Deep Reading

1. SR 和 NR 指标的准确定义是什么？
2. EventRain-27K 的 real-world labels 如何获得？
3. frequency regularization 的公式是什么？
4. MS3M 与普通 Mamba/SSM 的差异是什么？
5. derained events 对下游 SNN detection 是否有帮助？

## 13. Evidence Notes

- PDF Abstract: 0.95 SR, 0.91 NR, 0.4s/M events, 0.26M params。
- PDF Section 3: 4D event cloud, STDF, MS3M。
- PDF Section 4: EventRain-27K。
- PDF Conclusion: framework and dataset summary。

## 14. Draft Survey-Usable Sentences

Draft material: PRE-Mamba is a non-spiking but relevant event restoration paper, especially for noise and weather robustness.

Draft material: Its point-based 4D event cloud may be useful when discussing representations that preserve native event timing.
