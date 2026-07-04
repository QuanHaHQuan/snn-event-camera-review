---
title: "Rethinking Scale-Aware Temporal Encoding for Event-based Object Detection"
authors: ["Lin Zhu, Tengyu Long, Xiao Wang, Lizhi Wang, Hua Huang"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/d450dceeacd6083d1d550247377f2320-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/d450dceeacd6083d1d550247377f2320-Abstract-Conference.html"
tags: []
abstract: "Event cameras provide asynchronous, low-latency, and high-dynamic-range visual signals, making them ideal for real-time perception tasks such as object detection. However, effectively modeling the temporal dynamics of event streams remains a core challenge. Most existing methods follow frame-based detection paradigms, applying temporal modules only at high-level features, which limits early-stage temporal modeling. Transformer-based approaches introduce global attention to capture long-range dependencies, but often add unnecessary complexity and overlook fine-grained temporal cues. In this paper, we propose a CNN-RNN hybrid framework that rethinks temporal modeling for event-based object detection. Our approach is based on two key insights: (1) introducing recurrent modules at lower spatial scales to preserve detailed temporal information where events are most dense, and (2) utilizing Decoupled Deformable-enhanced Recurrent Layers specifically designed according to the inherent motion characteristics of event cameras to extract multiple spatiotemporal features, and performing independent downsampling at multiple spatiotemporal scales to enable flexible, scale-aware representation learning. These multi-scale features are then fused via a feature pyramid network to produce robust detection outputs. Experiments on Gen1, 1 Mpx and eTram dataset demonstrate that our approach achieves superior accuracy over recent transformer-based models, highlighting the importance of precise temporal feature extraction in early stages. This work offers a new perspective on designing architectures for event-driven vision beyond attention-centric paradigms. Code: https://github.com/BIT-Vision/SATE."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras provide asynchronous, low-latency, and high-dynamic-range visual signals,
making them ideal for real-time perception tasks such as object detection.

## Core Method

However, effectively modeling the temporal dynamics of event streams remains a core
challenge.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event cameras; event camera visual-event context; event cameras visual-event
context; event-based object visual-event context; event stream with event-camera context;
event-based with event-camera context。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.。 备注：strict two-stage
rescan; official abstract/page inspected; needs human verification; Track: Main Conference
Track。
