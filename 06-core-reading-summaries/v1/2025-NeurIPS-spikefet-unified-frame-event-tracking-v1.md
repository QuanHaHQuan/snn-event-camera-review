---
title: "Fully Spiking Neural Networks for Unified Frame-Event Object Tracking"
authors: ["Jingjun Yang", "Liangwei Fan", "Jinpu Zhang", "Xiangkai Lian", "Hui Shen", "Dewen Hu"]
year: 2025
venue: "NeurIPS"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/A/2025-NEURIPS-A-fully-spiking-neural-networks-for-unified-frame-event-object-tracking.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/af752cfbdcc6fd3e4cd0eea9f1ad0fab-Abstract-Conference.html"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/af752cfbdcc6fd3e4cd0eea9f1ad0fab-Paper-Conference.pdf"
local_pdf_status: "unavailable"
status: "auto-generated; needs human review"
tags: ["SNN", "fully spiking", "event camera", "frame-event tracking", "SpikeFET", "RPM", "STR"]
---

# Summary V1｜Fully Spiking Neural Networks for Unified Frame-Event Object Tracking

## 1. One-sentence Summary

本文提出 SpikeFET，一个 fully Spiking Frame-Event Tracking framework，用 spiking convolution/Transformer 式建模融合 frame 与 event streams，并以 RPM 和 STR 改善 tracking 表征。

## 2. Research Problem

frame-event tracking 能提升复杂环境下的 robustness，但现有 fusion methods 计算开销大，且未充分利用 event-driven spiking paradigm 的能效优势。

## 3. Background and Motivation

event streams 提供 fast motion clues，frames 提供 appearance/context。tracking 需要 template-search matching 和 temporal consistency。fully spiking 设计如果可行，可把融合和全局建模都放入 spike domain。

## 4. Method Overview

SpikeFET 输入 image/frame stream 与 event stream，使用 fully spiking framework 融合 local convolutional feature extraction 和 Transformer-based global modeling。Random Patchwork Module (RPM) 缓解 convolutional padding 导致的 translation invariance degradation；Spatial-Temporal Regularization (STR) 在 latent space 约束 temporal template features 的一致性。输出为 object tracking result。

## 5. Technical Details

### 1. Event Representation

官方摘要确认 frame-event inputs；具体 event frame/voxel construction 需 PDF 核验。
### 2. Spiking Module

网络声称 fully spiking，卷积局部特征与 Transformer global modeling 均在 spiking paradigm 中协同。
### 3. RPM

随机空间重组与 learnable type encoding，用于减轻 positional bias，同时保留 residual structure。
### 4. STR

对 temporal template features 施加 spatio-temporal consistency，缓解 asymmetric features 的 similarity metric degradation。
### 5. Training / Inference

具体 loss、datasets 和能耗测量需人工核验。

## 6. Experiments

PDF 未能下载。官方摘要称在 multiple benchmarks 上取得 superior tracking accuracy 并显著降低 power consumption，但数据集、success/precision/EAO 等指标、baseline 和能耗计算边界均需人工核验。

## 7. Main Contributions

1. 提出 first fully Spiking Frame-Event Tracking framework SpikeFET。
2. 在 spiking paradigm 中结合 convolutional local feature extraction 与 Transformer global modeling。
3. 提出 RPM 处理 padding positional bias。
4. 提出 STR 加强 temporal template consistency。

## 8. Limitations and Risks

- PDF 不可用，所有实验数字都不能在本轮确认。
- “fully spiking” 需要检查是否包括 head、fusion、normalization 和 similarity computation。
- power consumption claim 需要确认是理论估算、GPU proxy 还是 neuromorphic hardware 实测。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。它是 survey 中 event-based tracking 和 fully spiking architecture 的重要候选。

## 10. Relation to Survey Taxonomy

- SNN architectures for event cameras
- Event-based tracking
- Efficiency, latency, and energy
- Hybrid ANN-SNN models
- Open challenges

## 11. Key Terms and Concepts

- SpikeFET：Fully Spiking Frame-Event Tracking framework。
- RPM：Random Patchwork Module。
- STR：Spatial-Temporal Regularization。
- Template/Search：tracking 中用于目标匹配的两类输入区域。

## 12. Questions for Human Deep Reading

1. SpikeFET 的全部模块是否都使用 spike activations？
2. RPM 的 randomization 在训练/推理是否一致？
3. STR 的 loss 形式和权重是多少？
4. 比较的 frame-event trackers 包含哪些强 baseline？
5. power reduction 的硬件假设是什么？

## 13. Evidence Notes

- Source card / official abstract: SpikeFET、RPM、STR、fully spiking claim。
- Local PDF: unavailable after repeated download attempts; no page/table evidence available.

## 14. Draft Survey-Usable Sentences

Draft material: SpikeFET should be treated as a candidate fully spiking frame-event tracker, but the exact spiking boundary needs PDF verification.

Draft material: Its RPM and STR modules may be useful when discussing tracking-specific inductive biases for spiking event models.
