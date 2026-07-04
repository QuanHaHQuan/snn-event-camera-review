---
title: "TimeTracker: Event-based Continuous Point Tracking for Video Frame Interpolation with Non-linear Motion"
authors: ["Haoyue Liu", "Jinghan Xu", "Yi Chang", "Hanyu Zhou", "Haozhi Zhao", "Lin Wang", "Luxin Yan"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_TimeTracker_Event-based_Continuous_Point_Tracking_for_Video_Frame_Interpolation_with_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Liu_TimeTracker_Event-based_Continuous_Point_Tracking_for_Video_Frame_Interpolation_with_CVPR_2025_paper.html"
tags: []
abstract: "Video frame interpolation (VFI) that leverages the bio-inspired event cameras as guidance has recently shown better performance and memory efficiency than the frame-based methods, thanks to the event cameras' advantages, such as high temporal resolution. A hurdle for event-based VFI is how to effectively deal with non-linear motion, caused by the dynamic changes in motion direction and speed within the scene. Existing methods either use events to estimate sparse optical flow or fuse events with image features to estimate dense optical flow. Unfortunately, motion errors often degrade the VFI quality as the continuous motion cues from events do not align with the dense spatial information of images in the temporal dimension. In this paper, we find that object motion is continuous in space, tracking local regions over continuous time enables more accurate identification of spatiotemporal feature correlations. In light of this, we propose a novel continuous point tracking-based VFI framework, named TimeTracker. Specifically, we first design a Scene-Aware Region Segmentation (SARS) module to divide the scene into similar patches. Then, a Continuous Trajectory guided Motion Estimation (CTME) module is proposed to track the continuous motion trajectory of each patch through events. Finally, intermediate frames at any given time are generated through global motion optimization and frame refinement. Moreover, we collect a real-world dataset that features fast non-linear motion. Extensive experiments show that our method outperforms prior arts in both motion estimation and frame interpolation quality."
status: "auto-generated; brief scan note"
---
## Core Problem

Video frame interpolation (VFI) that leverages the bio-inspired event cameras as guidance
has recently shown better performance and memory efficiency than the frame-based methods,
thanks to the event cameras' advantages, such as high temporal resolution.

## Core Method

A hurdle for event-based VFI is how to effectively deal with non-linear motion, caused by
the dynamic changes in motion direction and speed within the scene.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official
CVF page inspected under broad high-recall title workflow.。
