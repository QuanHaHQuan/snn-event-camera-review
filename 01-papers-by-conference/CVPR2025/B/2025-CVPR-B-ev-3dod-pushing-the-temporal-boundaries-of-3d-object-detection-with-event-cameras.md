---
title: "Ev-3DOD: Pushing the Temporal Boundaries of 3D Object Detection with Event Cameras"
authors: ["Hoonhee Cho", "Jae-Young Kang", "Youngho Kim", "Kuk-Jin Yoon"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Cho_Ev-3DOD_Pushing_the_Temporal_Boundaries_of_3D_Object_Detection_with_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Cho_Ev-3DOD_Pushing_the_Temporal_Boundaries_of_3D_Object_Detection_with_CVPR_2025_paper.html"
tags: []
abstract: "Detecting 3D objects in point clouds plays a crucial role in autonomous driving systems. Recently, advanced multi-modal methods incorporating camera information have achieved notable performance. For a safe and effective autonomous driving system, algorithms that excel not only in accuracy but also in speed and low latency are essential. However, existing algorithms fail to meet these requirements due to the latency and bandwidth limitations of fixed frame rate sensors, e.g., LiDAR and camera. To address this limitation, we introduce asynchronous event cameras into 3D object detection for the first time. We leverage their high temporal resolution and low bandwidth to enable high-speed 3D object detection. Our method enables detection even during inter-frame intervals when synchronized data is unavailable, by retrieving previous 3D information through the event camera. Furthermore, we introduce the first event-based 3D object detection datasets, Ev-Waymo and DSEC-3DOD, both of which include ground truth 3D bounding boxes at 100 FPS, establishing the first benchmarks for event-based 3D detectors. The code and dataset are available at https://github.com/mickeykang16/Ev3DOD."
status: "auto-generated; brief scan note"
---
## Core Problem

Detecting 3D objects in point clouds plays a crucial role in autonomous driving systems.

## Core Method

Recently, advanced multi-modal methods incorporating camera information have achieved
notable performance.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event cameras; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official
CVF page inspected under broad high-recall title workflow.。
