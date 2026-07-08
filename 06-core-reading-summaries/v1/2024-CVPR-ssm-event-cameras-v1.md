---
title: "State Space Models for Event Cameras"
authors: ["Nikola Zubic", "Mathias Gehrig", "Davide Scaramuzza"]
year: 2024
venue: "CVPR"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2024/B/2024-CVPR-B-state-space-models-for-event-cameras.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Zubic_State_Space_Models_for_Event_Cameras_CVPR_2024_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Zubic_State_Space_Models_for_Event_Cameras_CVPR_2024_paper.pdf"
local_pdf_status: "unavailable"
status: "auto-generated; needs human review"
tags: ["event camera", "state space model", "SSM", "frequency adaptation", "Gen1", "1Mpx", "advisor-track"]
---

# Summary V1｜State Space Models for Event Cameras

## 1. One-sentence Summary

本文将 learnable-timescale State Space Models 引入 event-based vision，用于缓解模型在训练频率和更高推理频率之间的 generalization degradation。

## 2. Research Problem

许多 event-camera networks 先把固定时间窗口的 events 转成 dense grid representation；当推理频率升高、时间窗口变短时，输入分布改变，性能容易下降。

## 3. Background and Motivation

event cameras 可在高频率下输出信息，但深度模型常被固定 representation frequency 绑定。SSM 具有连续/序列建模能力，learnable timescale 可帮助模型跨 temporal resolution 适配。

## 4. Method Overview

方法把 state-space models 用于 event camera processing，并学习 timescale parameters，使模型在不同 inference frequencies 下无需重训。论文还研究两种 counteract aliasing effects 的策略。输入为 event-camera data 的 dense/grid-like representation 或序列化特征，输出用于 detection 等 event vision tasks。

## 5. Technical Details

### 1. Event Representation

官方摘要指出 baseline 通常把 temporal window events 转成 dense grid-like input。
### 2. SSM Module

learnable timescale parameters 是核心，用于适配 smaller temporal windows。
### 3. Aliasing Handling

论文研究两个策略缓解高频部署时 aliasing；具体机制需 PDF。
### 4. Experiments

覆盖 Gen1 和 1Mpx event camera datasets，并与 RNN/Transformer architectures 比较。
### 5. Efficiency

官方摘要称 SSM-based models train 33% faster，且高频测试时性能退化更小。

## 6. Experiments

PDF 未能下载。source card/official abstract 可确认 benchmark 包括 Gen1 与 1Mpx，比较对象包括 RNN 和 Transformer architectures；主要结论是训练快 33%，高 inference frequency 下 degradation 较小。具体 mAP、频率设置和 aliasing ablation 需要人工核验。

## 7. Main Contributions

1. 将 SSM 与 learnable timescale 引入 event camera tasks。
2. 明确研究 train/test inference frequency mismatch。
3. 提出/比较 anti-aliasing strategies。
4. 在 Gen1/1Mpx 上与 RNN/Transformer event models 做系统比较。

## 8. Limitations and Risks

- PDF 不可用，无法确认模型架构和表格数值。
- 该论文不是 SNN 方法，属于 event-camera background。
- SSM 频率适配和 SNN temporal dynamics 的关系需要 survey 中谨慎类比。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background; advisor-track support。它不属于 SNN core，但对 event temporal modeling 与高频推理很重要。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs
- Event-based object detection
- Efficiency, latency, and energy
- Datasets and benchmarks
- Open challenges

## 11. Key Terms and Concepts

- SSM：State Space Model。
- Learnable timescale：模型学习适配不同时间尺度的参数。
- Aliasing：高频/短窗口输入导致时序采样伪影。
- Gen1/1Mpx：event-based automotive detection benchmarks。

## 12. Questions for Human Deep Reading

1. SSM block 是如何嵌入 detector backbone 的？
2. 两种 anti-aliasing strategy 分别是什么？
3. 33% faster 的训练设置和硬件是什么？
4. 高频推理频率范围是多少？
5. 是否有直接适配 SNN representation 的启发？

## 13. Evidence Notes

- Source card / official abstract: learnable timescale SSM、Gen1/1Mpx、33% faster。
- Local PDF: unavailable after repeated download attempts.

## 14. Draft Survey-Usable Sentences

Draft material: This paper is useful background for temporal-frequency robustness in event-camera models rather than an SNN method.

Draft material: Its learnable-timescale SSM framing may help motivate why fixed event aggregation windows are brittle for high-frequency inference.
