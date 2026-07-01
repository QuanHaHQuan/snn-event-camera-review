---
title: "From Corners to Fiducial Tags: Revisiting Checkerboard Calibration for Event Cameras"
authors: ["Taehun Ryu", "Changwoo Kang", "Kyungdon Joo"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Ryu_From_Corners_to_Fiducial_Tags_Revisiting_Checkerboard_Calibration_for_Event_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Ryu_From_Corners_to_Fiducial_Tags_Revisiting_Checkerboard_Calibration_for_Event_CVPR_2026_paper.html"
tags: []
abstract: "The conventional checkerboard-based calibration for standard cameras faces fundamental limitations when applied to bio-inspired event cameras. Specifically, this stems from two challenges: (i) Events are triggered asynchronously at different timestamps along motion trajectories. If we accumulate them directly on the image plane, it causes temporal misalignment and produces blurred edges. (ii) Checkerboard corners on event cameras show near-zero event occurrence at the corner itself. This hinders reliable corner localization and makes calibration difficult. To address these issues, we present a novel calibration framework that directly detects checkerboard corners from event data without learning-based grayscale image reconstruction. We first mathematically analyze the absence of events at corner points. Based on this fact, we then leverage edge-driven event cues to initialize corner positions. Using the near-zero event occurrence at checkerboard corners, we gradually refine the estimated corner toward low event-density regions, achieving sub-pixel accuracy. Furthermore, we extend the corner detection to fiducial markers such as AprilTag, resulting in reliable detection even under partial visibility or occlusion. Evaluations on self-collected and public data demonstrate reliable checkerboard corner detection and stable camera calibration. Additional information is available at the following link: https://vision3d-lab.github.io/corner2tag/."
status: "auto-generated; brief scan note"
---

## Core Problem

传统棋盘格标定直接迁移到事件相机时会遇到时间错位和角点事件稀疏的问题。

## Core Method

提出直接从 event data 中检测棋盘角点的校准框架，改进事件相机标定流程。

## Key Metrics and Findings

摘要强调解决了角点附近事件稀疏与运动轨迹对齐困难。

## Personal Notes

可作为事件相机标定与传感器几何章节的背景论文。

