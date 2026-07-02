---
title: "Event-boosted Deformable 3D Gaussians for Dynamic Scene Reconstruction"
authors: ["Wenhao Xu", "Wenming Weng", "Yueyi Zhang", "Ruikang Xu", "Zhiwei Xiong"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Xu_Event-boosted_Deformable_3D_Gaussians_for_Dynamic_Scene_Reconstruction_ICCV_2025_paper.html"
tags: []
abstract: "Deformable 3D Gaussian Splatting (3D-GS) is limited by missing intermediate motion information due to the low temporal resolution of RGB cameras. To address this, we introduce the first approach combining event cameras, which capture high-temporal-resolution, continuous motion data, with deformable 3D-GS for dynamic scene reconstruction. We observe that threshold modeling for events plays a crucial role in achieving high-quality reconstruction. Therefore, we propose a GS-Threshold Joint Modeling strategy, creating a mutually reinforcing process that greatly improves both 3D reconstruction and threshold modeling. Moreover, we introduce a Dynamic-Static Decomposition strategy that first identifies dynamic areas by exploiting the inability of static Gaussians to represent motions, then applies a buffer-based soft decomposition to separate dynamic and static areas. This strategy accelerates rendering by avoiding unnecessary deformation in static areas, and focuses on dynamic areas to enhance fidelity. Additionally, we contribute the first event-inclusive 4D benchmark with synthetic and real-world dynamic scenes, on which our method achieves state-of-the-art performance."
status: "auto-generated; brief scan note"
---

## Core Problem

Deformable 3D Gaussian Splatting (3D-GS) is limited by missing intermediate motion information due to the low temporal resolution of RGB cameras.

## Core Method

To address this, we introduce the first approach combining event cameras, which capture high-temporal-resolution, continuous motion data, with deformable 3D-GS for dynamic scene reconstruction.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
