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

Event-based motion deblurring has attracted increasing attention, as the high temporal
resolution of event cameras provides motion cues unavailable to conventional RGB sensors,
thereby enabling more effective deblurring.

## Core Method

In real-world scenes, motion blur is often complex and nonlinear, with different regions
exhibiting diverse motion speeds and directions.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event stream; event-based motion。自动分类理由：Official abstract/page
confirms event-camera/DVS/event-stream evidence; no clear SNN evidence.。
