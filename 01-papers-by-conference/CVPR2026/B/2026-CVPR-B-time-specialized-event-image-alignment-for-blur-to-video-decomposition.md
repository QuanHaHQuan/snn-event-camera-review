---
title: "Time-Specialized Event-Image Alignment for Blur-to-Video Decomposition"
authors: ["Zhijing Sun", "Senyan Xu", "Ruixuan Jiang", "Kean Liu", "Runze Tian", "Xueyang Fu", "Zheng-Jun Zha"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Time-Specialized_Event-Image_Alignment_for_Blur-to-Video_Decomposition_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Time-Specialized_Event-Image_Alignment_for_Blur-to-Video_Decomposition_CVPR_2026_paper.html"
tags: []
abstract: "Motion blur is a common degradation in dynamic imaging. Recent studies have moved beyond restoring a single sharp image from a blurred input and instead target blur decomposition: recovering a temporally continuous sharp video sequence from one motion-blurred image. Event cameras, with their microsecond temporal resolution, can effectively alleviate motion ambiguity. However, existing event-based methods often fail to explicitly model time-aligned event-image features. How to accurately exploit event data to reconstruct frames at different time instants remains largely underexplored. In this paper, we propose TSANet, an event-based blur-to-video decomposition method that time-specializes both event features and image features for alignment. Specifically, we introduce a Relative Time-Encoded Attention module that steers event features toward motion information relevant to a given target time, and a Timesurface Dynamic Warping module that warps image features into the spatial configuration corresponding to that time. With time-specialized motion and image features explicitly aligned at arbitrary query times, our framework can decompose a single blurred image into a high-frame-rate sharp video sequence. In addition, we collect a new dataset containing real events and high-quality color videos, and synthesize blurred inputs by averaging sharp frames to evaluate our method. Experiments on multiple datasets with both synthetic and real events demonstrate that our approach consistently outperforms previous state-of-the-art methods on the blur decomposition task."
status: "auto-generated; brief scan note"
---

## Core Problem

Motion blur is a common degradation in dynamic imaging.

## Core Method

Recent studies have moved beyond restoring a single sharp image from a blurred input and instead target blur decomposition: recovering a temporally continuous sharp video sequence from one motion-blurred image.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-image visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
