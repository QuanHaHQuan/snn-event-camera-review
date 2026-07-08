---
title: "EventMG: Efficient Multilevel Mamba-Graph Learning for Spatiotemporal Event Representation"
authors: ["Sheng Wu", "Lin Jin", "Hui Feng", "Bo Hu"]
year: 2025
venue: "NeurIPS"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/B/2025-NEURIPS-B-eventmg-efficient-multilevel-mamba-graph-learning-for-spatiotemporal-event-representation.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/73d829353fdd9749f9b6cf26c5387f2e-Abstract-Conference.html"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/73d829353fdd9749f9b6cf26c5387f2e-Paper-Conference.pdf"
local_pdf_status: "unavailable"
status: "auto-generated; needs human review"
tags: ["event camera", "Mamba", "graph learning", "EventMG", "SEST", "advisor-track"]
---

# Summary V1｜EventMG: Efficient Multilevel Mamba-Graph Learning for Spatiotemporal Event Representation

## 1. One-sentence Summary

本文提出 EventMG，将 micro-level Mamba event-node modeling 与 macro-level Component Graphs 结合，以高效学习多尺度 spatiotemporal event representation。

## 2. Research Problem

event data 的 asynchronous sparse nature 使全局时空上下文、salient dynamic regions 和可变事件密度建模都很困难。

## 3. Background and Motivation

Mamba/SSM 擅长长程依赖，graph learning 擅长局部拓扑和事件簇结构。event representation 需要同时处理单个 event 的细节和 event cluster 的宏观语义。

## 4. Method Overview

EventMG 使用 multilevel Mamba-Graph architecture。micro-level 用 SSM-based Mamba 捕获 numerous event nodes 的 long-range dependencies；macro-level 引入 Component Graphs 编码 dense event regions 的 local semantics 和 global topology；SEST 结合 Adaptive Perturbation Network (APN) 和 Multidirectional Scanning Module (MSM)，增强对关键时空模式的感知。

## 5. Technical Details

### 1. Event Representation

micro single-event level + macro event-cluster level。
### 2. Mamba Module

用于 event nodes 的 long-range dependency modeling。
### 3. Graph Module

Component Graphs 处理局部语义和全局拓扑。
### 4. SEST

Spatiotemporal-aware Event Scanning Technology，包括 APN 与 MSM。
### 5. SNN Module

无 SNN，是 event representation background。

## 6. Experiments

PDF 未能下载。官方摘要称 EventMG 具有 low parameter count 和 linear computational complexity，并可学习 high-quality spatiotemporal event representations。具体 datasets、metrics、baselines 和 ablations 为 Needs human verification。

## 7. Main Contributions

1. 提出 multilevel Mamba-Graph event representation architecture。
2. 同时建模 single event micro details 与 event cluster macro semantics。
3. 提出 Component Graphs、SEST、APN、MSM 等模块。
4. 强调 linear complexity 和 lightweight design。

## 8. Limitations and Risks

- PDF 不可用，实验任务和数值无法确认。
- 不是 SNN 方法；与 spike-based event processing 的关系需要人工总结。
- 模块较多，需确认哪部分真正贡献主要性能。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background; advisor-track support。它适合在 survey 中作为 non-spiking event representation/SSM-graph baseline。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs
- Efficiency, latency, and energy
- Datasets and benchmarks
- Open challenges

## 11. Key Terms and Concepts

- EventMG：Multilevel Mamba-Graph event representation model。
- Component Graphs：事件簇级图结构。
- SEST：Spatiotemporal-aware Event Scanning Technology。
- APN/MSM：Adaptive Perturbation Network / Multidirectional Scanning Module。

## 12. Questions for Human Deep Reading

1. EventMG 评估了哪些任务和数据集？
2. micro event nodes 如何采样或排序？
3. Component Graphs 如何构建边？
4. linear complexity 的变量定义是什么？
5. 与 SNN event representation 的互补关系是什么？

## 13. Evidence Notes

- Source card / official abstract: EventMG, micro/macro levels, Mamba, Component Graphs, SEST/APN/MSM。
- Local PDF: unavailable after repeated download attempts.

## 14. Draft Survey-Usable Sentences

Draft material: EventMG is a non-spiking Mamba-Graph representation model that emphasizes multi-level event structure.

Draft material: It can serve as a strong background comparator for future SNN event representation methods.
