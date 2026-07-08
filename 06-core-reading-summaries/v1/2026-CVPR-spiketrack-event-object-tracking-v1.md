---
title: "SpikeTrack: High-performance and Energy-efficient Event-Based Object Tracking with Spiking Neural Network"
authors: ["Yang Wang", "Jiqing Zhang", "Chuanyu Sun", "Qianhui Liu", "Huilin Ge", "Ziqi Wei", "Xin Yang"]
year: 2026
venue: "CVPR"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2026/A/2026-CVPR-A-spiketrack-high-performance-and-energy-efficient-event-based-object-tracking-with-spiking-.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Wang_SpikeTrack_High-performance_and_Energy-efficient_Event-Based_Object_Tracking_with_Spiking_Neural_CVPR_2026_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_SpikeTrack_High-performance_and_Energy-efficient_Event-Based_Object_Tracking_with_Spiking_Neural_CVPR_2026_paper.pdf"
local_pdf_status: "unavailable"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "tracking", "SpikeTrack", "MSST", "DI-LIF"]
---

# Summary V1｜SpikeTrack: High-performance and Energy-efficient Event-Based Object Tracking with Spiking Neural Network

## 1. One-sentence Summary

本文提出 SpikeTrack，一个 purely spike-driven event-based single-object tracking framework，结合 MSST training paradigm 与 DI-LIF neuron 以兼顾 tracking performance 和 energy efficiency。

## 2. Research Problem

event-based tracking 在 fast motion 和 target appearance change 中有优势，但如何让 SNN 同时保持高精度和低能耗仍然困难。

## 3. Background and Motivation

event cameras 的 microsecond temporal resolution 与 wide dynamic range 适合 tracking；SNN 可以利用 sparse spike computation，但常规 LIF 或 ANN-SNN conversion 可能限制表征能力。

## 4. Method Overview

SpikeTrack 使用 purely spike-driven tracking framework。MSST (Multi-Search-sequence-and-Single-Template) training paradigm 让模型学习更丰富 temporal dependencies；DI-LIF (Dynamic Integer LIF) neuron 在训练时预测 integer-valued activations，并在推理时转换为 spikes。输出为 single-object tracking result。

## 5. Technical Details

### 1. Event Representation

面向 event-based object tracking，具体 event frame/voxel 需要 PDF 核验。
### 2. Spiking Neuron

DI-LIF 是核心，训练阶段用 dynamic integer activation，推理阶段转换为 spikes。
### 3. Training Strategy

MSST 使用 multiple search sequences 和 single template 捕获 temporal dependencies。
### 4. Experiments

官方摘要列出 FE108、FELT、VisEvent。
### 5. Efficiency

声称同时提升 accuracy 和 energy efficiency，具体计算边界需 PDF。

## 6. Experiments

PDF 未能下载。source card/official abstract 可确认评估数据集为 FE108、FELT、VisEvent，声称超过 state-of-the-art trackers，并通过 ablation 验证模块贡献。具体 success/precision、energy、latency 和 ablation 数值均需人工核验。

## 7. Main Contributions

1. 提出 purely spike-driven event-based object tracker SpikeTrack。
2. 提出 MSST training paradigm 建模 temporal dependencies。
3. 提出 DI-LIF neuron 连接 integer activations 与 inference spikes。
4. 在 FE108、FELT、VisEvent 上报告 accuracy/efficiency 优势。

## 8. Limitations and Risks

- PDF 不可用，无法确认 “purely spike-driven” 的边界。
- DI-LIF 训练时 integer activation 到推理 spike 的转换误差需要核验。
- VisEvent 包含 RGB-event 场景时，是否只用 event 或多模态需确认。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。它与 SDTrack/SpikeFET 一起构成 event-based tracking 的 SNN 方法簇。

## 10. Relation to Survey Taxonomy

- Event-based tracking
- SNN architectures for event cameras
- Efficiency, latency, and energy
- SNN training methods
- Open challenges

## 11. Key Terms and Concepts

- SpikeTrack：purely spike-driven event tracker。
- MSST：Multi-Search-sequence-and-Single-Template。
- DI-LIF：Dynamic Integer Leaky Integrate-and-Fire neuron。
- FE108/FELT/VisEvent：tracking benchmarks。

## 12. Questions for Human Deep Reading

1. DI-LIF 的数学形式是什么？
2. 训练时 integer-valued activations 是否需要 quantization loss？
3. MSST 如何采样 search sequences？
4. 是否在 neuromorphic hardware 上实测能耗？
5. FE108/FELT/VisEvent 的输入模态是否一致？

## 13. Evidence Notes

- Source card / official abstract: SpikeTrack、MSST、DI-LIF、FE108/FELT/VisEvent。
- Local PDF: unavailable after repeated download attempts.

## 14. Draft Survey-Usable Sentences

Draft material: SpikeTrack is a candidate purely spike-driven event tracker that introduces DI-LIF to bridge train-time integer activations and inference-time spikes.

Draft material: Its tracking and energy claims need table-level verification before survey citation.
