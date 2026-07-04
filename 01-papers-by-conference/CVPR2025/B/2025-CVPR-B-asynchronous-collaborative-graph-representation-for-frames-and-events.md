---
title: "Asynchronous Collaborative Graph Representation for Frames and Events"
authors: ["Dianze Li", "Jianing Li", "Xu Liu", "Xiaopeng Fan", "Yonghong Tian"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Asynchronous_Collaborative_Graph_Representation_for_Frames_and_Events_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Li_Asynchronous_Collaborative_Graph_Representation_for_Frames_and_Events_CVPR_2025_paper.html"
tags: []
abstract: "Integrating frames and events has become a widely accepted solution for various tasks in challenging scenarios. However, most multimodal methods directly convert events into image-like formats synchronized with frames and process each stream through separate two-branch backbones, making it difficult to fully exploit the spatiotemporal events while limiting inference frequency to the frame rate. To address these problems, we propose a novel asynchronous collaborative graph representation, namely ACGR, which is the first trial to explore a unified graph framework for asynchronously processing frames and events with high performance and low latency. Technically, we first construct unimodal graphs for frames and events to preserve their spatiotemporal properties and sparsity. Then, an asynchronous collaborative alignment module is designed to align and fuse frames and events into a unified graph and the ACGR is generated through graph convolutional networks. Finally, we innovatively introduce domain adaptation to enable cross-modal interactions between frames and events by aligning their feature spaces. Experimental results show that our approach outperforms state-of-the-art methods in both object detection and depth estimation tasks, while significantly reducing computational latency and achieving real-time inference up to 200 Hz. Our code can be available at https://github.com/dianzl/ACGR."
status: "auto-generated; brief scan note"
---
## Core Problem

Integrating frames and events has become a widely accepted solution for various tasks in
challenging scenarios.

## Core Method

However, most multimodal methods directly convert events into image-like formats
synchronized with frames and process each stream through separate two-branch backbones,
making it difficult to fully exploit the spatiotemporal events while limiting inference
frequency to the frame rate.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：asynchronous。自动分类理由：Manual boundary check: official abstract confirms frame-event
fusion for visual object detection and depth estimation.。 备注：CVPR 2025 official CVF page
inspected under broad high-recall title workflow. Needs human verification for event-stream
wording.。
