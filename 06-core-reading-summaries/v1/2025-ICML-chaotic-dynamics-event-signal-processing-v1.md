---
title: "A Chaotic Dynamics Framework Inspired by Dorsal Stream for Event Signal Processing"
authors: ["Yu Chen", "Jing Lian", "Zhaofei Yu", "Jizhao Liu", "Jisheng Dang", "Gang Wang"]
year: 2025
venue: "ICML"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICML2025/B/2025-ICML-B-a-chaotic-dynamics-framework-inspired-by-dorsal-stream-for-event-signal-processing.md"
official_page: "https://proceedings.mlr.press/v267/chen25am.html"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25am/chen25am.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "bio-inspired", "chaotic dynamics", "CCNN", "wavelet transform", "N-Caltech101", "N-CARS", "advisor-track"]
---

# Summary V1｜A Chaotic Dynamics Framework Inspired by Dorsal Stream for Event Signal Processing

## 1. One-sentence Summary

本文提出 dorsal-stream-inspired chaotic dynamics framework，用 CCNN 将 event sequences 编码为 periodic/chaotic signals，并用 continuous wavelet transform 构建稳定的 event representation。

## 2. Research Problem

现有 event stream processing 多依赖端到端深度学习和特定数据结构，可能降低跨任务稳定性和泛化能力。

## 3. Background and Motivation

event cameras 是 bio-inspired sensors；dorsal visual pathway 与运动处理相关。作者借用 chaotic dynamics 和 wavelet analysis，希望得到更稳定、可解释的 event signal representation。

## 4. Method Overview

框架使用 Continuous-coupled Neural Network (CCNN) 编码 event stream：polarity-invariant event sequences 被编码为 periodic signals，polarity-changing sequences 被编码为 chaotic signals。随后用 continuous wavelet transforms 分析 CCNN neurons 的 dynamical states，建立 event stream 的 high-order mappings，再接入 conventional classification networks。

## 5. Technical Details

### 1. Event Representation

从 raw event stream 生成 dynamical signal representation。
### 2. CCNN

Continuous-coupled Neural Network，非传统 SNN，但神经动力学/生物启发明显。
### 3. Wavelet Analysis

通过 scale/translation parameters 分析周期/混沌状态。
### 4. Tasks

event-based object classification。
### 5. Efficiency

PDF conclusion 报告 472 samples per second inference processing。

## 6. Experiments

PDF Section 4 使用 N-MNIST、N-Caltech101、N-CARS、ASL-DVS。abstract 报告 N-Caltech101 accuracy 84.3%，N-CARS accuracy 99.9%。Conclusion 报告 472 samples/s。具体其它数据集、baseline 和 ablation 需人工核验。

## 7. Main Contributions

1. 提出 chaotic dynamics event signal processing framework。
2. 使用 CCNN 区分 polarity-invariant 与 polarity-changing event sequences。
3. 用 continuous wavelet transform 构建 high-order event mappings。
4. 在多个 classification datasets 上展示 accuracy 与 inference efficiency。

## 8. Limitations and Risks

- 不是标准 SNN 方法，需避免把 CCNN 等同于 spiking neural network。
- 主要验证 classification，复杂 dense/event tracking task 尚不明确。
- bio-inspired explanation 与实际性能贡献需要看 ablation。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background; advisor-track support。它可作为 bio-inspired event representation 的辅助材料，不是 SNN core。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs
- Datasets and benchmarks
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- CCNN：Continuous-coupled Neural Network。
- Chaotic signal：polarity-changing sequences 对应的动态编码。
- Continuous wavelet transform：分析动态状态的时频工具。
- N-Caltech101/N-CARS：event classification datasets。

## 12. Questions for Human Deep Reading

1. CCNN 与 SNN/LIF 的关系是什么？
2. periodic/chaotic 分类如何从事件极性序列得到？
3. wavelet scale parameter 如何选择？
4. 与深度 SNN baselines 的比较是否充分？
5. 472 samples/s 的硬件和 batch setting 是什么？

## 13. Evidence Notes

- PDF Abstract: CCNN, wavelet transform, 84.3% N-Caltech101, 99.9% N-CARS。
- PDF Section 3: Methods。
- PDF Section 4: datasets N-MNIST/N-Caltech101/N-CARS/ASL-DVS。
- PDF Conclusion: 472 samples per second。

## 14. Draft Survey-Usable Sentences

Draft material: This paper is best used as bio-inspired event representation background rather than as an SNN method.

Draft material: Its CCNN/wavelet pipeline offers a contrasting non-deep-learning route for stable event signal encoding.
