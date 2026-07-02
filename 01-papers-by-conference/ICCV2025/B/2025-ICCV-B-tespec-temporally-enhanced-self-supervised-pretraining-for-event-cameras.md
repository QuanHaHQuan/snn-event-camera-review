---
title: "TESPEC: Temporally-Enhanced Self-Supervised Pretraining for Event Cameras"
authors: ["Mohammad Mohammadi", "Ziyi Wu", "Igor Gilitschenski"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Mohammadi_TESPEC_Temporally-Enhanced_Self-Supervised_Pretraining_for_Event_Cameras_ICCV_2025_paper.html"
tags: []
abstract: "Long-term temporal information is crucial for event-based perception tasks, as raw events only encode pixel brightness changes. Recent works show that when trained from scratch, recurrent models achieve better results than feedforward models in these tasks. However, when leveraging self-supervised pre-trained weights, feedforward models can outperform their recurrent counterparts. Current self-supervised learning (SSL) methods for event-based pre-training largely mimic RGB image-based approaches. They pre-train feedforward models on raw events within a short time interval, ignoring the temporal information of events. In this work, we introduce TESPEC, a self-supervised pre-training framework tailored for learning spatio-temporal information. TESPEC is well-suited for recurrent models, as it is the first framework to leverage long event sequences during pre-training. TESPEC employs the masked image modeling paradigm with a new reconstruction target. We design a novel method to accumulate events into pseudo grayscale videos containing high-level semantic information about the underlying scene, which is robust to sensor noise and reduces motion blur. Reconstructing this target thus requires the model to reason about long-term history of events. Extensive experiments demonstrate our state-of-the-art results in downstream tasks, including object detection, semantic segmentation, and monocular depth estimation. Project webpage: https://mhdmohammadi.github.io/TESPEC_webpage."
status: "auto-generated; brief scan note"
---
## Core Problem

Long-term temporal information is crucial for event-based perception tasks, as raw events
only encode pixel brightness changes.

## Core Method

Recent works show that when trained from scratch, recurrent models achieve better results
than feedforward models in these tasks.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
