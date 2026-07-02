---
title: "EMatch: A Unified Framework for Event-based Optical Flow and Stereo Matching"
authors: ["Pengjie Zhang", "Lin Zhu", "Xiao Wang", "Lizhi Wang", "Hua Huang"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_EMatch_A_Unified_Framework_for_Event-based_Optical_Flow_and_Stereo_ICCV_2025_paper.html"
tags: []
abstract: "Event cameras have shown promise in vision applications like optical flow estimation and stereo matching with many specialized architectures. However, existing works only focus event data within the confines of task-specific domains, overlooking the correlations between tasks across the temporal and spatial domains. In this paper, we propose a novel matching-based framework for event cameras to estimate flow and disparity simultaneously in a shared representation space, reformulating them as a unified pixel-wise correspondence matching problem. Specifically, our method utilizes a Temporal Recurrent Network to aggregate asynchronous event features across temporal or spatial domains, and a Spatial Contextual Attention to enhance knowledge transfer across event flows via temporal or spatial interactions. By utilizing a shared pixel-wise feature similarities module, our network performs optical flow estimation from temporal event segments and stereo matching from spatial event segments simultaneously. Our unified model inherently supports multi-task unification and cross-task transfer, which facilitate training and streamline deployment. Without the need for retraining on specific tasks, our model can effectively handle both event-based flow and stereo estimation, achieving state-of-the-art performance on both tasks. Our code will be released upon acceptance."
status: "auto-generated; brief scan note"
---

## Core Problem

Event cameras have shown promise in vision applications like optical flow estimation and stereo matching with many specialized architectures.

## Core Method

However, existing works only focus event data within the confines of task-specific domains, overlooking the correlations between tasks across the temporal and spatial domains.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event flow visual-event context; event-based optical visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
