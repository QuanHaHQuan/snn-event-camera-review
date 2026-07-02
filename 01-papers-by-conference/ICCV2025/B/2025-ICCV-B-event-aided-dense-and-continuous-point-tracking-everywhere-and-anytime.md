---
title: "Event-aided Dense and Continuous Point Tracking: Everywhere and Anytime"
authors: ["Zhexiong Wan", "Jianqin Luo", "Yuchao Dai", "Gim Hee Lee"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Wan_Event-aided_Dense_and_Continuous_Point_Tracking_Everywhere_and_Anytime_ICCV_2025_paper.html"
tags: []
abstract: "Recent point tracking methods have made great strides in recovering the trajectories of any point (especially key points) in long video sequences associated with large motions. However, the spatial and temporal granularities of point trajectories remain constrained by limited motion estimation accuracy and video frame rate. Leveraging the high temporal resolution and motion sensitivity of event cameras, we introduce event data for the first time to recover spatially dense and temporally continuous trajectories of every point at any time. Specifically, we define the dense and continuous point trajectory representation as estimating multiple control points of curves for each pixel and model the movement of sparse events triggered along continuous point trajectories. Building on this, we propose a novel multi-frame iterative streaming framework that first estimates local inter-frame motion representations from two consecutive frames with inter-frame events, then aggregates them into a global long-term motion representation to utilize input full video and event data with an arbitrary number of frames. Extensive experiments on simulated and real data demonstrate the significant improvement of our framework over state-of-the-art methods and the crucial role of introducing events to model continuous point trajectories."
status: "auto-generated; brief scan note"
---

## Core Problem

Recent point tracking methods have made great strides in recovering the trajectories of any point (especially key points) in long video sequences associated with large motions.

## Core Method

However, the spatial and temporal granularities of point trajectories remain constrained by limited motion estimation accuracy and video frame rate.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
