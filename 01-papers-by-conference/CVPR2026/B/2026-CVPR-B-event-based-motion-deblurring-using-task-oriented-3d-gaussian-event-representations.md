---
title: "Event-Based Motion Deblurring Using Task-Oriented 3D Gaussian Event Representations"
authors: ["Shengdong Xue", "Haoxiang Ma", "Hao Chen", "Zhen Yang", "Yongjian Deng"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Xue_Event-Based_Motion_Deblurring_Using_Task-Oriented_3D_Gaussian_Event_Representations_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Event-Based_Motion_Deblurring_Using_Task-Oriented_3D_Gaussian_Event_Representations_CVPR_2026_paper.html"
tags: []
abstract: "Event-based motion deblurring has attracted increasing attention, as the high temporal resolution of event cameras provides motion cues unavailable to conventional RGB sensors, thereby enabling more effective deblurring. In real-world scenes, motion blur is often complex and nonlinear, with different regions exhibiting diverse motion speeds and directions. However, most existing approaches rely on handcrafted event representations that overlook such spatiotemporal motion heterogeneity, resulting in suboptimal deblurring performance. To address this limitation, we propose a learnable 3D Gaussian event representation module that adaptively selects key spatiotemporal coordinates for deblurring based on the blurred image content and the event density distribution. The event stream is then aggregated with 3D Gaussian weighting kernels to extract local motion features that are sensitive to motion direction and speed. Furthermore, to fully exploit the motion information encoded in the event representation, we adopt a two-stage fusion strategy. In the first stage, local motion features are used to enhance fine detail restoration. In the second stage, a bidirectional attention fusion module leverages one-dimensional Gaussian-weighted event frames to correct global spatial misalignment, leading to more accurate structural alignment. Extensive experiments on both synthetic and real-world datasets demonstrate the effectiveness of our method and show that it consistently outperforms state-of-the-art approaches."
status: "auto-generated; brief scan note"
---

## Core Problem

Event-based motion deblurring has attracted increasing attention, as the high temporal resolution of event cameras provides motion cues unavailable to conventional RGB sensors, thereby enabling more effective deblurring.

## Core Method

In real-world scenes, motion blur is often complex and nonlinear, with different regions exhibiting diverse motion speeds and directions.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-based motion visual-event context; event stream with event-camera context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
