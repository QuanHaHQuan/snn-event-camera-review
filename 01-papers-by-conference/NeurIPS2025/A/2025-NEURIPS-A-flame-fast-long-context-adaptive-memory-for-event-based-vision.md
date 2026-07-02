---
title: "FLAME: Fast Long-context Adaptive Memory for Event-based Vision"
authors: ["Biswadeep Chakraborty, Saibal Mukhopadhyay"]
conference: "NeurIPS"
year: 2025
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/1b71649968436c64a765e469ab6b615c-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/1b71649968436c64a765e469ab6b615c-Abstract-Conference.html"
tags: []
abstract: "We propose Fast Long-range Adaptive Memory for Event (FLAME), a novel scalable architecture that combines neuro-inspired feature extraction with robust structured sequence modeling to efficiently process asynchronous and sparse event camera data. As a departure from conventional input encoding methods, FLAME presents Event Attention Layer, a novel feature extractor that leverages neuromorphic dynamics (Leaky Integrate-and-Fire (LIF)) to directly capture multi-timescale features from event streams. The feature extractor is integrates with a structured state-space model with a novel Event-Aware HiPPO (EA-HiPPO) mechanism that dynamically adapts memory retention based on inter-event intervals to understand relationship across varying temporal scales and event sequences. A Normal Plus Low Rank (NPLR) decomposition reduces the computational complexity of state update from $\\mathcal{O}(N^2)$ to $\\mathcal{O}(Nr)$, where $N$ represents the dimension of the core state vector and $r$ is the rank of a low-rank component (with $r \\ll N$). FLAME demonstrates state-of-the-art accuracy for event-by-event processing on complex event camera datasets."
status: "auto-generated; needs human review"
---

## Core Problem

We propose Fast Long-range Adaptive Memory for Event (FLAME), a novel scalable architecture that combines neuro-inspired feature extraction with robust structured sequence modeling to efficiently process asynchronous and sparse event camera data.

## Core Method

As a departure from conventional input encoding methods, FLAME presents Event Attention Layer, a novel feature extractor that leverages neuromorphic dynamics (Leaky Integrate-and-Fire (LIF)) to directly capture multi-timescale features from event streams.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera data; event camera visual-event context; event stream with event-camera context; event-based vision with event-camera context; event-based with event-camera context; leaky integrate-and-fire; integrate-and-fire; lif`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
