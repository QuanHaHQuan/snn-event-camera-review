---
title: "Depth Any Event Stream: Enhancing Event-based Monocular Depth Estimation via Dense-to-Sparse Distillation"
authors: ["Jinjing Zhu", "Tianbo Pan", "Zidong Cao", "Yexin Liu", "James T. Kwok", "Hui Xiong"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Depth_Any_Event_Stream_Enhancing_Event-based_Monocular_Depth_Estimation_via_ICCV_2025_paper.html"
tags: []
abstract: "With the superior sensitivity of event cameras to high-speed motion and extreme lighting conditions, event-based monocular depth estimation has gained popularity to predict structural information about surrounding scenes in challenging environments. However, the scarcity of labeled event data constrains prior supervised learning methods. Unleashing the promising potential of the existing RGB-based depth foundation model, DAM, we propose Depth Any Event stream (EventDAM) to achieve high-performance event based monocular depth estimation in an annotation-free manner. EventDAM effectively combines paired dense RGB images with sparse event data by incorporating three key cross-modality components: Sparsity-aware Feature Mixture (SFM), Sparsity-aware Feature Distillation (SFD), and Sparsity-invariant Consistency Module (SCM). With the proposed sparsity metric, SFM mixes features from RGB images and event data to generate auxiliary depth predictions, while SFD facilitates adaptive feature distillation. Furthermore, SCM ensures output consistency across varying sparsity levels in event data, thereby endowing EventDAM with zero shot capabilities across diverse scenes. Extensive experiments across a variety of benchmark datasets, compared to approaches using diverse input modalities, robustly substantiate the generalization and zero-shot capabilities of EventDAM."
status: "auto-generated; brief scan note"
---
## Core Problem

With the superior sensitivity of event cameras to high-speed motion and extreme lighting
conditions, event-based monocular depth estimation has gained popularity to predict
structural information about surrounding scenes in challenging environments.

## Core Method

However, the scarcity of labeled event data constrains prior supervised learning methods.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event stream; event data; event-based monocular。自动分类理由：Official
abstract/page confirms event-camera/DVS/event-stream evidence; no clear SNN evidence.。
