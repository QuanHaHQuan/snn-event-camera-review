---
title: "Edge-Guided Fusion and Motion Augmentation for Event-Image Stereo"
authors: ["Fengan Zhao", "Qianang Zhou", "Junlin Xiong"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09268.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/2116"
tags: []
abstract: "Traditional frame-based cameras have achieved impressive performance in stereo matching, yet challenges remain due to sensor constraints, such as low dynamic range and motion blur. In contrast, event cameras capture per-pixel intensity changes asynchronously with high temporal resolution, making them less prone to motion blur and offering a high dynamic range. However, the event stream provides less spatial information compared to intensity images. Although existing state-of-the-art event-based stereo methods fuse features from both modalities, they still struggle to effectively capture and represent edge details in the scene. In this paper, we propose a novel edge-guided event-image stereo network, which utilizes extra edge cues to supplement edge information during disparity estimation. Firstly, we introduce an edge-guided event-image feature fusion approach to effectively supplement edge information in the fused features. Secondly, we incorporate edge cues into the disparity update process by introducing an edge-guided motion augmentation module, further augmenting the edge information during disparity estimation. Finally, we demonstrate the superiority of our method in stereo matching by conducting experiments on the real-world dataset using joint image and event data."
status: "auto-generated; brief scan note"
---
## Core Problem

Traditional frame-based cameras have achieved impressive performance in stereo matching, yet
challenges remain due to sensor constraints, such as low dynamic range and motion blur.

## Core Method

In contrast, event cameras capture per-pixel intensity changes asynchronously with high
temporal resolution, making them less prone to motion blur and offering a high dynamic
range.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event stream; event data; event-based stereo; event-
image。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream evidence; no
clear SNN evidence.。
