---
title: "Hybrid Spiking Vision Transformer for Object Detection with Event Cameras"
authors: ["Qi Xu", "Jie Deng", "Jiangrong Shen", "Biwu Chen", "Huajin Tang", "Gang Pan"]
year: 2025
venue: "ICML"
level: "A"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICML2025/A/2025-ICML-A-hybrid-spiking-vision-transformer-for-object-detection-with-event-cameras.md"
official_page: "https://proceedings.mlr.press/v267/xu25e.html"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25e/xu25e.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "Vision Transformer", "event camera", "object detection", "HsVT", "Fall DVS", "advisor-track"]
---

# Summary V1｜Hybrid Spiking Vision Transformer for Object Detection with Event Cameras

## 1. One-sentence Summary

本文提出 HsVT，将 spatial feature extraction 与 temporal spiking/Transformer modeling 结合，用于 event-based object detection，并构建 Fall DVS detection benchmark。

## 2. Research Problem

event-based object detection 需要同时利用 event stream 的高时间分辨率和低功耗潜力。现有 SNN detector 在 global context、long-term temporal dependency 或 detector accuracy 上受限；ANN detector 又可能参数量和能耗较高。

## 3. Background and Motivation

event cameras 输出 asynchronous address-event representation，适合 low latency detection。SNN 与事件形式相容，但传统卷积 SNN 对长程依赖建模不足。Vision Transformer 擅长全局关系建模，本文尝试把 Transformer 思路和 spiking dynamics 结合。

## 4. Method Overview

HsVT 包含 spatial feature extraction module 和 temporal feature extraction module。输入为 event representation，模型捕获 local/global spatial features 与 event sequence time dependencies，输出 object bounding boxes。论文还构建 Fall DVS detection dataset，用于 privacy-preserving fall detection。

## 5. Technical Details

### 1. Event Representation

PDF 描述 event-based object detection datasets，包括 Gen1、Fall DVS、Aircraft Detection Dataset；具体 event tensor 构造需复核。
### 2. Spiking / Transformer Module

HsVT 使用 hybrid spike vision Transformer，通过 temporal module 建模 long-term patterns。
### 3. Network Architecture

Tiny/Small/Base 规模用于比较 parameter efficiency；模型意图在 SNN efficiency 与 Transformer context 间折中。
### 4. Training Strategy

在 Gen1、Fall Detection、Aircraft Detection Dataset 上评估；训练细节需 V2 复核。
### 5. Loss / Inference

object detection head 的具体 loss 需要人工核验；输出为 detection boxes。

## 6. Experiments

PDF Section 5 在 Gen1、Fall Detection 和 Aircraft Detection Dataset 上实验。Conclusion 指出 Gen1 上 HsVT 与 pure SNN model mAP 接近但参数更少；在 Fall/AIR 上 HsVT 相对 RVT 更稳健，但 Base/Small/Tiny 不总按规模单调提升，作者将其归因于 dataset size limitation 和 overfitting。精确 mAP、参数和能耗表格需人工核验。

## 7. Main Contributions

1. 提出 Hybrid Spiking Vision Transformer (HsVT) 用于 event camera object detection。
2. 结合 spatial feature extraction 与 temporal dependency modeling。
3. 发布/构建 Fall DVS detection dataset，强调隐私和事件表示的存储优势。
4. 展示相对 SNN/ANN baseline 的参数效率和竞争性性能。

## 8. Limitations and Risks

- Fall/AIR 数据集上模型规模和性能不单调，说明数据规模可能限制结论。
- “competitive with ANN” 的范围需要按具体 baseline 和指标解释。
- energy consumption 的计算边界需要确认是否为理论估算或硬件测量。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper；同时是 advisor-track support，因为 reading plan 标记为 yes。它适合讨论 spiking Transformer 在 event detection 中的作用。

## 10. Relation to Survey Taxonomy

- SNN architectures for event cameras
- Hybrid ANN-SNN models
- Event-based object detection
- Efficiency, latency, and energy
- Datasets and benchmarks

## 11. Key Terms and Concepts

- HsVT：Hybrid Spiking Vision Transformer。
- Fall DVS：本文构建的 event-based fall detection benchmark。
- RVT：常见 recurrent vision transformer event baseline。
- mAP：object detection 主要指标。

## 12. Questions for Human Deep Reading

1. HsVT 的 spike operation 出现在全部层还是部分 temporal module？
2. Fall DVS 的采集设备、类别和标注频率是什么？
3. energy consumption 是硬件实测还是 operation-count 估算？
4. Gen1 上与 pure SNN 的 mAP/parameter trade-off 精确是多少？
5. Transformer attention 是否保留 spike sparsity？
6. Fall/AIR 上 overfitting 结论是否由 validation curve 支持？

## 13. Evidence Notes

- PDF Section 3: Event-based Fall Detection Benchmark。
- PDF Section 4: Methodology。
- PDF Section 5: Experiments。
- PDF Discussion and Conclusion: Gen1/FALL/AIR 结论。

## 14. Draft Survey-Usable Sentences

Draft material: HsVT represents a spiking Transformer direction for event-based detection, aiming to combine SNN efficiency with longer-range temporal modeling.

Draft material: The accompanying Fall DVS benchmark is relevant for privacy-sensitive event-camera detection settings.
