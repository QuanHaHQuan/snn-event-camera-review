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

Recent point tracking methods have made great strides in recovering the trajectories of any
point (especially key points) in long video sequences associated with large motions.

## Core Method

However, the spatial and temporal granularities of point trajectories remain constrained by
limited motion estimation accuracy and video frame rate.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event data; event-aided。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
