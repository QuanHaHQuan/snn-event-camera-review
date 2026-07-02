---
title: "Depth Hypothesis Guided Iterative Refinement for Event-Image Monocular Depth Estimation"
authors: ["Daikun Liu", "Teng Wang", "Changyin Sun"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Depth_Hypothesis_Guided_Iterative_Refinement_for_Event-Image_Monocular_Depth_Estimation_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Depth_Hypothesis_Guided_Iterative_Refinement_for_Event-Image_Monocular_Depth_Estimation_CVPR_2026_paper.html"
tags: []
abstract: "Event cameras hold excellent dynamic properties, showing great potential for monocular depth estimation (MDE). However, existing methods mainly improve performance by optimizing contextual features, but still struggle with the ill-posed and nonlinear nature of direct full-depth regression. In this paper, we propose HypoDepth, the first event-image monocular depth iterative refinement framework. By introducing a discrete Depth Hypothesis Volume (DHV), we transform the depth regression problem into a constrained depth search task. Specifically, we construct a 3D cost volume between the DHV features and contextual features and perform a multi-scale correlation search to guide stable residual optimization. This lightweight cost volume enables efficient global-to-local refinement across multi-resolution. Our method outperforms existing approaches on DSEC and MVSEC with state-of-the-art results and strong zero-shot generalization. Meanwhile, our tiny model achieves an excellent balance between accuracy and efficiency, enabling real-time performance on resource-limited devices."
status: "auto-generated; brief scan note"
---

## Core Problem

Event cameras hold excellent dynamic properties, showing great potential for monocular depth estimation (MDE).

## Core Method

However, existing methods mainly improve performance by optimizing contextual features, but still struggle with the ill-posed and nonlinear nature of direct full-depth regression.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-image visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
