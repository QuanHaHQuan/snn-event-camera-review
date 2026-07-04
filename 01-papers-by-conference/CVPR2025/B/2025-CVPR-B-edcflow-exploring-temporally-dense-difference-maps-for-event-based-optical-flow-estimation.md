---
title: "EDCFlow: Exploring Temporally Dense Difference Maps for Event-based Optical Flow Estimation"
authors: ["Daikun Liu", "Lei Cheng", "Teng Wang", "Changyin Sun"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_EDCFlow_Exploring_Temporally_Dense_Difference_Maps_for_Event-based_Optical_Flow_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Liu_EDCFlow_Exploring_Temporally_Dense_Difference_Maps_for_Event-based_Optical_Flow_CVPR_2025_paper.html"
tags: []
abstract: "Recent learning-based methods for event-based optical flow estimation utilize cost volumes for pixel matching but suffer from redundant computations and limited scalability to higher resolutions for flow refinement. In this work, we take advantage of the complementarity between temporally dense feature differences of adjacent event frames and cost volume and present a lightweight event-based optical flow network (EDCFlow) to achieve high-quality flow estimation at a higher resolution. Specifically, an attention-based multi-scale temporal feature difference layer is developed to capture diverse motion patterns at high resolution in a computation-efficient manner. An adaptive fusion of high-resolution difference motion features and low-resolution correlation motion features is performed to enhance motion representation and model generalization. Notably, EDCFlow can serve as a plug-and-play refinement module for RAFT-like event-based methods to enhance flow details. Extensive experiments demonstrate that EDCFlow achieves better performance with lower complexity compared to existing methods, offering superior generalization. Codes and models will be available at here."
status: "auto-generated; brief scan note"
---
## Core Problem

Recent learning-based methods for event-based optical flow estimation utilize cost volumes
for pixel matching but suffer from redundant computations and limited scalability to higher
resolutions for flow refinement.

## Core Method

In this work, we take advantage of the complementarity between temporally dense feature
differences of adjacent event frames and cost volume and present a lightweight event-based
optical flow network (EDCFlow) to achieve high-quality flow estimation at a higher
resolution.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official
CVF page inspected under broad high-recall title workflow.。
