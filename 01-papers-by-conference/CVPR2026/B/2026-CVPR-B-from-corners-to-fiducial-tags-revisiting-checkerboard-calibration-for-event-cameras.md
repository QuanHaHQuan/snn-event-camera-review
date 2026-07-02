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

The conventional checkerboard-based calibration for standard cameras faces fundamental limitations when applied to bio-inspired event cameras.

## Core Method

Specifically, this stems from two challenges: (i) Events are triggered asynchronously at different timestamps along motion trajectories.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
