---
title: "EvRT-DETR: Latent Space Adaptation of Image Detectors for Event-based Vision"
authors: ["Dmitrii Torbunov", "Yihui Ren", "Animesh Ghose", "Odera Dim", "Yonggang Cui"]
year: 2025
venue: "ICCV"
level: "B"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICCV2025/B/2025-ICCV-B-evrt-detr-latent-space-adaptation-of-image-detectors-for-event-based-vision.md"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Torbunov_EvRT-DETR_Latent_Space_Adaptation_of_Image_Detectors_for_Event-based_Vision_ICCV_2025_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/ICCV2025/papers/Torbunov_EvRT-DETR_Latent_Space_Adaptation_of_Image_Detectors_for_Event-based_Vision_ICCV_2025_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "object detection", "RT-DETR", "EvRT-DETR", "I2EvDet", "Gen1", "1Mpx"]
---

# Summary V1｜EvRT-DETR: Latent Space Adaptation of Image Detectors for Event-based Vision

## 1. One-sentence Summary

本文提出 I2EvDet/EvRT-DETR，通过在 frozen image detector latent space 中加入轻量 temporal adaptation，把 RT-DETR 转换为 event-based object detector。

## 2. Research Problem

event-based object detection 往往依赖专门 representation 和 architecture；这提高了方法复杂度，也限制了从成熟 image detectors 迁移能力。

## 3. Background and Motivation

EBC/event cameras 具有高动态范围和低功耗优势，但 sparse asynchronous data 不适合直接输入常规 image detector。RT-DETR 等 image detector 已有强大 latent representation，本文探索最小修改的 temporal adaptation。

## 4. Method Overview

I2EvDet 先证明 RT-DETR 在 simple image-like EBC representation 上可接近 specialized EBC methods；随后冻结 image detector parameters，在 latent representation space 加入 lightweight RNN/temporal modules，形成 EvRT-DETR。输出为 object detections。

## 5. Technical Details

### 1. Event Representation

使用 simple image-like representation of EBC data；具体 construction parameters 采用 RVT 风格，需核验。
### 2. Architecture

RT-DETR backbone/detector mostly frozen，插入 lightweight RNN modules 做 temporal event adaptation。
### 3. Training

adapter-style fine-tuning，目标是 minimal architectural additions。
### 4. Experiments

Gen1 与 1Mpx/Gen4 automotive detection。
### 5. SNN Module

无 SNN，是 event-camera object detection background。

## 6. Experiments

PDF key lines 显示 EvRT-DETR 在 Gen1 上达到 mAP +2.3，在 1Mpx/Gen4 上达到 mAP +1.4，相对 prior SOTA 提升，并保持 competitive inference efficiency。Table/figures 比较 COCO mAP、parameter size 和 performance。具体绝对 mAP、FPS 和 ablation 需人工复核。

## 7. Main Contributions

1. 提出 I2EvDet，把 image detector 适配到 event-based vision。
2. 展示 RT-DETR + simple event representation 已能接近 specialized methods。
3. 提出 latent space temporal adaptation 生成 EvRT-DETR。
4. 在 Gen1 和 1Mpx/Gen4 上报告 SOTA mAP gains。

## 8. Limitations and Risks

- 不是 SNN 方法，作为 event detection background 使用。
- 依赖 frozen image detector，可能牺牲 event-native/asynchronous 优势。
- 需要核验 temporal modules 的计算成本和延迟。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background。它为 event-based object detection 提供强 ANN baseline，对评估 SNN detectors 很重要。

## 10. Relation to Survey Taxonomy

- Event-based object detection
- Hybrid ANN-SNN models
- Event representations for SNNs
- Datasets and benchmarks
- Open challenges

## 11. Key Terms and Concepts

- I2EvDet：Image-to-Event Detection adaptation framework。
- EvRT-DETR：event-adapted RT-DETR。
- Latent space adaptation：在 frozen detector features 中插入时间模块。
- Gen1/1Mpx：automotive event detection benchmarks。

## 12. Questions for Human Deep Reading

1. simple image-like representation 的时间窗口和 polarity encoding 是什么？
2. RT-DETR 哪些参数被冻结？
3. RNN adapters 插入哪些层？
4. mAP +2.3/+1.4 的 reference baseline 是谁？
5. 与 SNN detector 的能耗和延迟如何比较？

## 13. Evidence Notes

- PDF Abstract/Section 3: I2EvDet/EvRT-DETR design。
- PDF Section 4: Gen1 and 1Mpx evaluation。
- PDF key lines: Gen1 mAP +2.3, 1Mpx/Gen4 mAP +1.4。

## 14. Draft Survey-Usable Sentences

Draft material: EvRT-DETR is an important non-spiking baseline showing that strong image detectors can be adapted to event detection with lightweight temporal modules.

Draft material: This makes SNN detector claims more meaningful only when compared against adapted mainstream detectors, not only older event-specific baselines.
