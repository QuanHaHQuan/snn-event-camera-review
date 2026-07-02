---
title: "Unleashing the Temporal Potential of Stereo Event Cameras for Continuous-Time 3D Object Detection"
authors: ["Jae-Young Kang", "Hoonhee Cho", "Kuk-Jin Yoon"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Kang_Unleashing_the_Temporal_Potential_of_Stereo_Event_Cameras_for_Continuous-Time_ICCV_2025_paper.html"
tags: []
abstract: "3D object detection is essential for autonomous systems, enabling precise localization and dimension estimation. While LiDAR and RGB cameras are widely used, their fixed frame rates create perception gaps in high-speed scenarios. Event cameras, with their asynchronous nature and high temporal resolution, offer a solution by capturing motion continuously. The recent approach, which integrates event cameras with conventional sensors for continuous-time detection, struggles in fast-motion scenarios due to its dependency on synchronized sensors. We propose a novel stereo 3D object detection framework that relies solely on event cameras, eliminating the need for conventional 3D sensors. To compensate for the lack of semantic and geometric information in event data, we introduce a dual filter mechanism that extracts both. Additionally, we enhance regression by aligning bounding boxes with object-centric information. Experiments show that our method outperforms prior approaches in dynamic environments, demonstrating the potential of event cameras for robust, continuous-time 3D perception. The code is available at https://github.com/mickeykang16/Ev-Stereo3D."
status: "auto-generated; brief scan note"
---

## Core Problem

3D object detection is essential for autonomous systems, enabling precise localization and dimension estimation.

## Core Method

While LiDAR and RGB cameras are widely used, their fixed frame rates create perception gaps in high-speed scenarios.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
