---
title: "FARSE-CNN: Fully Asynchronous, Recurrent and Sparse Event-Based CNN"
authors: ["Riccardo Santambrogio", "Marco Cannici", "Matteo Matteucci"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07037.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1742"
tags: []
abstract: "Event cameras are neuromorphic image sensors that respond to per-pixel brightness changes, producing a stream of asynchronous and spatially sparse events. Currently, the most successful algorithms for event cameras convert batches of events into dense image-like representations that are synchronously processed by deep learning models of frame-based computer vision. These methods discard the inherent properties of events, leading to high latency and computational costs. Following a recent line of works, we propose a model for efficient asynchronous event processing that exploits sparsity. We design the Fully Asynchronous, Recurrent and Sparse Event-Based CNN (FARSE-CNN), a novel multi-layered architecture which combines the mechanisms of recurrent and convolutional neural networks. To build efficient deep networks, we propose compression modules that allow to learn hierarchical features both in space and time. We theoretically derive the complexity of all components in our architecture, and experimentally validate our method on tasks for object recognition, object detection and gesture recognition. FARSE-CNN achieves similar or better performance than the state-of-the-art among asynchronous methods, with low computational complexity and without relying on a fixed-length history of events. Our code will be released on GitHub."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras are neuromorphic image sensors that respond to per-pixel brightness changes,
producing a stream of asynchronous and spatially sparse events.

## Core Method

Currently, the most successful algorithms for event cameras convert batches of events into
dense image-like representations that are synchronously processed by deep learning models of
frame-based computer vision.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
