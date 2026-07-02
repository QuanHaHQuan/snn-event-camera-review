---
title: "Distil-E2D: Distilling Image-to-Depth Priors for Event-Based Monocular Depth Estimation"
authors: ["Jie Long Lee, Gim Hee Lee"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/b6fa3ed9624c184bd73e435123bd576a-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/b6fa3ed9624c184bd73e435123bd576a-Abstract-Conference.html"
tags: []
abstract: "Event cameras are neuromorphic vision sensors that asynchronously capture pixel-level intensity changes with high temporal resolution and dynamic range. These make them well suited for monocular depth estimation under challenging lighting conditions. However, progress in event-based monocular depth estimation remains constrained by the quality of supervision: LiDAR-based depth labels are inherently sparse, spatially incomplete, and prone to artifacts. Consequently, these signals are suboptimal for learning dense depth from sparse events. To address this problem, we propose Distil-E2D, a framework that distills depth priors from the image domain into the event domain by generating dense synthetic pseudolabels from co-recorded APS or RGB frames using foundational depth models. These pseudolabels complement sparse LiDAR depths with dense semantically rich supervision informed by large-scale image-depth datasets. To reconcile discrepancies between synthetic and real depths, we introduce a Confidence-Guided Calibrated Depth Loss that learns nonlinear depth alignment and adaptively weights supervision by alignment confidence. Additionally, our architecture integrates past predictions via a Context Transformer and employs a Dual-Decoder Training scheme that enhances encoder representations by jointly learning metric and relative depth abstractions. Experiments on benchmark datasets show that Distil-E2D achieves state-of-the-art performance in event-based monocular depth estimation across both event-only and event+APS settings."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras are neuromorphic vision sensors that asynchronously capture pixel-level
intensity changes with high temporal resolution and dynamic range.

## Core Method

These make them well suited for monocular depth estimation under challenging lighting
conditions.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event-camera/DVS/visual event stream evidence。自动分类理由：Official abstract/page confirms
event-camera/DVS/visual-event-stream data; no clear SNN evidence.。 备注：Track: Main Conference
Track. Official abstract/page inspected under broad high-recall title workflow.。
