---
title: "Event-based Tiny Object Detection: A Benchmark Dataset and Baseline"
authors: ["Nuo Chen", "Chao Xiao", "Yimian Dai", "Shiman He", "Miao Li", "Wei An"]
year: 2025
venue: "ICCV"
level: "B"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICCV2025/B/2025-ICCV-B-event-based-tiny-object-detection-a-benchmark-dataset-and-baseline.md"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Event-based_Tiny_Object_Detection_A_Benchmark_Dataset_and_Baseline_ICCV_2025_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Event-based_Tiny_Object_Detection_A_Benchmark_Dataset_and_Baseline_ICCV_2025_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "tiny object detection", "EV-UAV", "EVSOD", "EV-SpSegNet", "STC loss"]
---

# Summary V1｜Event-based Tiny Object Detection: A Benchmark Dataset and Baseline

## 1. One-sentence Summary

本文提出 EV-UAV/EVSOD benchmark 和 EV-SpSegNet baseline，用 event-level annotations 支持 anti-UAV tiny object detection。

## 2. Research Problem

anti-UAV small object detection 中目标极小、背景复杂，frame cameras 受低帧率、有限动态范围和冗余影响；现有 event detection datasets 又缺少 tiny target、多样场景和细粒度标注。

## 3. Background and Motivation

event cameras 对 fast tiny moving targets 有优势，因为目标在 spatiotemporal event point cloud 中形成连续轨迹。tiny object detection 对 benchmark 和 event-level annotations 的要求更高。

## 4. Method Overview

论文构建 EV-UAV，大规模、高多样 anti-UAV event tiny object dataset。baseline EV-SpSegNet 在 point cloud space 中做 event segmentation，并使用 Spatiotemporal Correlation (STC) loss 利用小目标运动连续性，保留 target events。

## 5. Technical Details

### 1. Dataset

147 sequences，over 2.3 million event-level annotations，平均目标尺寸 6.8 x 5.4 pixels。
### 2. Event Representation

支持 event-level fine-grained annotations 和 point-cloud-space processing。
### 3. Network Architecture

EV-SpSegNet 对 sparse event point clouds 做 target trajectory segmentation。
### 4. Loss

STC loss 利用 spatiotemporal local correlation 引导保留目标事件。
### 5. SNN Module

无 SNN，是 event tiny object detection benchmark/background。

## 6. Experiments

PDF Section 5 报告 EV-UAV 上的综合评估，比较本文方法与 13 state-of-the-art approaches。Conclusion 称 EV-SpSegNet 与 STC loss 在 proposed dataset 上表现优越。具体 detection/segmentation metrics、baseline 列表和数值需人工核验。

## 7. Main Contributions

1. 提出 EV-UAV，第一个面向 anti-UAV 的大规模 event-based small/tiny object detection benchmark。
2. 提供 event-level annotations 和极小目标场景。
3. 提出 EV-SpSegNet point-cloud baseline。
4. 提出 STC loss 利用小目标运动轨迹连续性。

## 8. Limitations and Risks

- 不是 SNN 方法，但可作为 SNN detector 的 challenging benchmark。
- dataset 只聚焦 anti-UAV，泛化到通用 tiny object detection 需谨慎。
- 需要核验 annotation quality、event-level labels 和 evaluation protocol。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background。它为 event-based small object detection 和 future SNN benchmark 提供重要数据集。

## 10. Relation to Survey Taxonomy

- Datasets and benchmarks
- Event-based object detection
- Event representations for SNNs
- Open challenges

## 11. Key Terms and Concepts

- EV-UAV：event-based anti-UAV tiny object dataset。
- EVSOD：Event-based Small Object Detection。
- EV-SpSegNet：point-cloud event segmentation baseline。
- STC loss：Spatiotemporal Correlation loss。

## 12. Questions for Human Deep Reading

1. EV-UAV 的 train/test split 和场景分布如何？
2. event-level annotation 如何生成和验证？
3. EV-SpSegNet 是检测、分割还是两者结合？
4. 13 个 baseline 包含哪些 event/SNN 方法？
5. tiny target metrics 是否与 COCO small object metric 对齐？

## 13. Evidence Notes

- PDF Abstract/Section 3: EV-UAV scale and annotations。
- PDF Section 4: EV-SpSegNet and STC loss。
- PDF Section 5: comparison with 13 approaches。
- PDF Conclusion: dataset and baseline claims。

## 14. Draft Survey-Usable Sentences

Draft material: EV-UAV provides a difficult event-camera benchmark where targets average only a few pixels, making it relevant for testing event representation robustness.

Draft material: It is not an SNN paper, but it can support future evaluation of spiking event detectors on tiny-object regimes.
