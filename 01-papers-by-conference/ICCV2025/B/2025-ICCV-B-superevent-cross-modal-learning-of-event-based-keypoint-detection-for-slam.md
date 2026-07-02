---
title: "SuperEvent: Cross-Modal Learning of Event-based Keypoint Detection for SLAM"
authors: ["Yannick Burkhardt", "Simon Schaefer", "Stefan Leutenegger"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Burkhardt_SuperEvent_Cross-Modal_Learning_of_Event-based_Keypoint_Detection_for_SLAM_ICCV_2025_paper.html"
tags: []
abstract: "Event-based keypoint detection and matching holds significant potential, enabling the integration of event sensors into highly optimized Visual SLAM systems developed for frame cameras over decades of research. Unfortunately, existing approaches struggle with the motion-dependent appearance of keypoints and the complex noise prevalent in event streams, resulting in severely limited feature matching capabilities and poor performance on downstream tasks. To mitigate this problem, we propose SuperEvent, a data-driven approach to predict stable keypoints with expressive descriptors. Due to the absence of event datasets with ground truth keypoint labels, we leverage existing frame-based keypoint detectors on readily available event-aligned and synchronized gray-scale frames for self-supervision: we generate temporally sparse keypoint pseudo-labels considering that events are a product of both scene appearance and camera motion. Combined with our novel, information-rich event representation, we enable SuperEvent to effectively learn robust keypoint detection and description in event streams. Finally, we demonstrate the usefulness of SuperEvent by its integration into a modern sparse keypoint and descriptor-based SLAM framework originally developed for traditional cameras, surpassing the state-of-the-art in event-based SLAM by a wide margin. Source code is available at https://ethz-mrl.github.io/SuperEvent/."
status: "auto-generated; brief scan note"
---
## Core Problem

Event-based keypoint detection and matching holds significant potential, enabling the
integration of event sensors into highly optimized Visual SLAM systems developed for frame
cameras over decades of research.

## Core Method

Unfortunately, existing approaches struggle with the motion-dependent appearance of
keypoints and the complex noise prevalent in event streams, resulting in severely limited
feature matching capabilities and poor performance on downstream tasks.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event stream; event data。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
