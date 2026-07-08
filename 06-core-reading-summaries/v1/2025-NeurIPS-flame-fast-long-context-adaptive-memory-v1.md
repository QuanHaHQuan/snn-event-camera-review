---
title: "FLAME: Fast Long-context Adaptive Memory for Event-based Vision"
authors: ["Biswadeep Chakraborty", "Saibal Mukhopadhyay"]
year: 2025
venue: "NeurIPS"
level: "A"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/A/2025-NEURIPS-A-flame-fast-long-context-adaptive-memory-for-event-based-vision.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/1b71649968436c64a765e469ab6b615c-Abstract-Conference.html"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/1b71649968436c64a765e469ab6b615c-Paper-Conference.pdf"
local_pdf_status: "unavailable"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "LIF", "state space model", "HiPPO", "FLAME", "advisor-track"]
---

# Summary V1｜FLAME: Fast Long-context Adaptive Memory for Event-based Vision

## 1. One-sentence Summary

本文提出 FLAME，用 LIF-based Event Attention Layer 直接从 event stream 提取多时间尺度特征，再用 Event-Aware HiPPO/state-space memory 建模长程事件依赖。

## 2. Research Problem

event cameras 的 asynchronous sparse stream 难以被固定窗口 representation 和短时模型充分利用。长上下文事件任务需要同时保留 event-by-event 细节与高效 memory update。

## 3. Background and Motivation

SNN/LIF 可以自然处理事件式输入；State Space Model 和 HiPPO 适合长序列记忆。FLAME 的动机是把 neuromorphic feature extraction 与 structured sequence modeling 合并，处理跨时间尺度事件关系。

## 4. Method Overview

输入为 asynchronous event stream。Event Attention Layer 使用 LIF neuromorphic dynamics 捕获 multi-timescale features；随后 structured state-space model 通过 Event-Aware HiPPO 根据 inter-event intervals 动态调整 memory retention；NPLR decomposition 将 state update complexity 从 O(N^2) 降到 O(Nr)。输出用于 event-based vision tasks。

## 5. Technical Details

### 1. Event Representation

官方摘要强调 departure from conventional input encoding，倾向 event-by-event processing；PDF 未下载，具体 representation 需核验。
### 2. Spiking Module

Event Attention Layer 使用 Leaky Integrate-and-Fire (LIF) dynamics。
### 3. State Space Memory

EA-HiPPO 根据 inter-event intervals 调整 long-context memory。
### 4. Formula

O(N^2) 到 O(Nr) 表示 NPLR 用低秩结构近似/加速状态更新，其中 r 是低秩 rank 且 r << N。
### 5. Training / Experiments

官方摘要称在 complex event camera datasets 上达到 state-of-the-art accuracy，但数据集和数值需 PDF 深读。

## 6. Experiments

PDF 暂时无法本地下载；只能确认官方摘要声称 FLAME 在 event-by-event processing 的 complex event camera datasets 上达到 SOTA accuracy。具体 datasets、baselines、metrics、ablation、latency/energy 均为 Needs human verification。

## 7. Main Contributions

1. 提出 FLAME 作为 long-context event vision architecture。
2. 提出 LIF-based Event Attention Layer，直接处理 event streams。
3. 提出 Event-Aware HiPPO，根据 inter-event intervals 调整 memory retention。
4. 使用 NPLR decomposition 降低 state update 复杂度。

## 8. Limitations and Risks

- PDF 未能下载，实验结论和模块细节需要人工核验。
- 需要确认 LIF layer 是否真正产生 sparse spikes，以及是否有硬件能耗评估。
- SOTA claim 的 benchmark 范围未知。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper；advisor-track support。它连接 SNN/LIF 与 SSM，是 survey 中 long-context event modeling 的关键候选。

## 10. Relation to Survey Taxonomy

- SNN architectures for event cameras
- Event representations for SNNs
- Surrogate gradient and temporal credit assignment
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- FLAME：Fast Long-context Adaptive Memory for Event-based Vision。
- Event Attention Layer：LIF-based feature extractor。
- EA-HiPPO：Event-Aware HiPPO memory mechanism。
- NPLR：Normal Plus Low Rank decomposition。

## 12. Questions for Human Deep Reading

1. FLAME 具体评估了哪些 event datasets？
2. Event Attention Layer 是否端到端 surrogate gradient 训练？
3. EA-HiPPO 的 inter-event interval 如何进入状态更新？
4. NPLR 低秩近似对 accuracy 有何影响？
5. 是否报告 event-by-event latency 或 memory footprint？

## 13. Evidence Notes

- Source card / official abstract: FLAME、LIF Event Attention Layer、EA-HiPPO、NPLR。
- Local PDF: unavailable after repeated download attempts; no page/table evidence available.

## 14. Draft Survey-Usable Sentences

Draft material: FLAME is a promising example of combining LIF-based event feature extraction with state-space memory for long-context event streams.

Draft material: Its claims should be cited cautiously until the exact benchmarks and SOTA margins are verified from the PDF.
