---
title: "Unsupervised 3d Motion Estimation Using Event Camera"
authors: ["Han Han", "Wei Zhai", "Tiesong Zhao", "Bin Li", "Yang Cao", "Zheng-jun Zha"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Han_Unsupervised_3d_Motion_Estimation_Using_Event_Camera_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Han_Unsupervised_3d_Motion_Estimation_Using_Event_Camera_CVPR_2026_paper.html"
tags: []
abstract: "Estimating the 3D motion of scene points from 2D observations, typically parameterized by optical flow and motion in depth, is a fundamental problem in computer vision. Existing learning-based methods usually rely on supervised regression from densely labeled data, but their dependence on annotations and limited use of geometric constraints restricts generalization, motivating unsupervised solutions. Unsupervised 3D motion estimation is challenging because motion along the viewing direction is unobservable, and optical flow and motion in depth are geometrically coupled, making their separation ambiguous. Event cameras capture per-pixel brightness changes asynchronously with microsecond latency, providing high temporal resolution and motion continuity. Projecting event streams along different axes reveals spatiotemporal expansion and contraction patterns that encode depth variation and geometric structure, offering rich cues for unsupervised estimation. Leveraging these properties, we propose an unsupervised event-based 3D motion estimation framework that jointly models optical flow and motion in depth. We first derive an analytical relationship to infer initial motion in depth from estimated flow and further refine it using a directional expansion modulation module that captures horizontal and vertical expansion-contraction patterns in event projections. Finally, motion in depth is incorporated into optical flow warping under a contrast maximization objective. Experiments on the CarlaEvent3D dataset show that our method achieves competitive accuracy and strong generalization, advancing unsupervised 3D motion estimation in the event domain."
status: "auto-generated; brief scan note"
---

## Core Problem

Estimating the 3D motion of scene points from 2D observations, typically parameterized by optical flow and motion in depth, is a fundamental problem in computer vision.

## Core Method

Existing learning-based methods usually rely on supervised regression from densely labeled data, but their dependence on annotations and limited use of geometric constraints restricts generalization, motivating unsupervised solutions.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; brightness change visual-event context; event stream with event-camera context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
