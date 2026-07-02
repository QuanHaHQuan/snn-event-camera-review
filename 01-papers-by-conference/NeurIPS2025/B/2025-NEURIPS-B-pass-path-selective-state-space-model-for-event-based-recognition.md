---
title: "PASS: Path-selective State Space Model for Event-based Recognition"
authors: ["Jiazhou Zhou, Kanghao Chen, Lei Zhang, Lin Wang"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/f5dbd98d426772945099ccace06418ba-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/f5dbd98d426772945099ccace06418ba-Abstract-Conference.html"
tags: []
abstract: "Event cameras are bio-inspired sensors that capture intensity changes asynchronously with distinct advantages, such as high temporal resolution. Existing methods for event-based object/action recognition predominantly sample and convert event representation at every fixed temporal interval (or frequency). However, they are constrained to processing a limited number of event lengths and show poor frequency generalization, thus not fully leveraging the event's high temporal resolution. In this paper, we present our PASS framework, exhibiting superior capacity for spatiotemporal event modeling towards a larger number of event lengths and generalization across varying inference temporal frequencies. Our key insight is to learn adaptively encoded event features via the state space models (SSMs), whose linear complexity and generalization on input frequency make them ideal for processing high temporal resolution events. Specifically, we propose a Path-selective Event Aggregation and Scan (PEAS) module to encode events into features with fixed dimensions by adaptively scanning and selecting aggregated event presentation. On top of it, we introduce a novel Multi-faceted Selection Guiding (MSG) loss to minimize the randomness and redundancy of the encoded features during the PEAS selection process. Our method outperforms prior methods on five public datasets and shows strong generalization across varying inference frequencies with less accuracy drop (ours -8.62% v.s. -20.69% for the baseline). Moreover, our model exhibits strong long spatiotemporal modeling for a broader distribution of event length (1-10^9), precise temporal perception, and effective generalization for real-world scenarios. Code and checkpoints will be released upon acceptance."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras are bio-inspired sensors that capture intensity changes asynchronously with
distinct advantages, such as high temporal resolution.

## Core Method

Existing methods for event-based object/action recognition predominantly sample and convert
event representation at every fixed temporal interval (or frequency).

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event-camera/DVS/visual event stream evidence。自动分类理由：Official abstract/page confirms
event-camera/DVS/visual-event-stream data; no clear SNN evidence.。 备注：Track: Main Conference
Track. Official abstract/page inspected under broad high-recall title workflow.。
