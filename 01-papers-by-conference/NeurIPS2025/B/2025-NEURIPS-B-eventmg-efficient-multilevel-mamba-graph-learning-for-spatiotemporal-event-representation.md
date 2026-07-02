---
title: "EventMG: Efficient Multilevel Mamba-Graph Learning for Spatiotemporal Event Representation"
authors: ["Sheng Wu, Lin Jin, Hui Feng, Bo Hu"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/73d829353fdd9749f9b6cf26c5387f2e-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/73d829353fdd9749f9b6cf26c5387f2e-Abstract-Conference.html"
tags: []
abstract: "Event cameras offer unique advantages in scenarios involving high speed, low light, and high dynamic range, yet their asynchronous and sparse nature poses significant challenges to efficient spatiotemporal representation learning. Specifically, despite notable progress in the field, effectively modeling the full spatiotemporal context, selectively attending to salient dynamic regions, and robustly adapting to the variable density and dynamic nature of event data remain key challenges. Motivated by these challenges, this paper proposes EventMG, a lightweight, efficient, multilevel Mamba-Graph architecture designed for learning high-quality spatiotemporal event representations. EventMG employs a multilevel approach, jointly modeling information at the micro (single event) and macro (event cluster) levels to comprehensively capture the multi-scale characteristics of event data. At the micro-level, it focuses on spatiotemporal details, employing State Space Model (SSM) based Mamba, to precisely capture long-range dependencies among numerous event nodes. Concurrently, at the macro-level, Component Graphs are introduced to efficiently encode the local semantics and global topology of dense event regions. Furthermore, to better accommodate the dynamic and sparse characteristics of data, we propose the Spatiotemporal-aware Event Scanning Technology (SEST), integrating the Adaptive Perturbation Network (APN) and Multidirectional Scanning Module (MSM), which substantially enhances the model's ability to perceive and focus on key spatiotemporal patterns. By employing this novel collaborative paradigm, EventMG demonstrates the ability to effectively capture multi-level spatiotemporal characteristics of event data while maintaining a low parameter count and linear computational complexity, suggesting a promising direction for event representation learning."
status: "auto-generated; brief scan note"
---

## Core Problem

Event cameras offer unique advantages in scenarios involving high speed, low light, and high dynamic range, yet their asynchronous and sparse nature poses significant challenges to efficient spatiotemporal representation learning.

## Core Method

Specifically, despite notable progress in the field, effectively modeling the full spatiotemporal context, selectively attending to salient dynamic regions, and robustly adapting to the variable density and dynamic nature of event data remain key challenges.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
