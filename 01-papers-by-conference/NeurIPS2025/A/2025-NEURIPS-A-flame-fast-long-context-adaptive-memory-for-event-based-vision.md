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

We propose Fast Long-range Adaptive Memory for Event (FLAME), a novel scalable architecture
that combines neuro-inspired feature extraction with robust structured sequence modeling to
efficiently process asynchronous and sparse event camera data.

## Core Method

As a departure from conventional input encoding methods, FLAME presents Event Attention
Layer, a novel feature extractor that leverages neuromorphic dynamics (Leaky Integrate-and-
Fire (LIF)) to directly capture multi-timescale features from event streams.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：event cameras; event camera data; event camera visual-event context; event stream
with event-camera context; event-based vision with event-camera context; event-based with
event-camera context; leaky integrate-and-fire; integrate-and-fire; lif。自动分类理由：Official
abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and
SNN/spiking neural computation.。 备注：strict two-stage rescan; official abstract/page
inspected; needs human verification; Track: Main Conference Track。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

The feature extractor is integrates with a structured state-space model with a novel Event-
Aware HiPPO (EA-HiPPO) mechanism that dynamically adapts memory retention based on inter-
event intervals to understand relationship across varying temporal scales and event
sequences. A Normal Plus Low Rank (NPLR) decomposition reduces the computational complexity
of state update from $\mathcal{O}(N^2)$ to $\mathcal{O}(Nr)$, where $N$ represents the
dimension of the core state vector and $r$ is the rank of a low-rank component (with $r \ll
N$). FLAME demonstrates state-of-the-art accuracy for event-by-event processing on complex
event camera datasets.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
