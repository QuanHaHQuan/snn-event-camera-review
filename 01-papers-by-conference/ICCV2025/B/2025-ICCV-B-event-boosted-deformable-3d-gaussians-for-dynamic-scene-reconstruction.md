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

Deformable 3D Gaussian Splatting (3D-GS) is limited by missing intermediate motion
information due to the low temporal resolution of RGB cameras.

## Core Method

To address this, we introduce the first approach combining event cameras, which capture
high-temporal-resolution, continuous motion data, with deformable 3D-GS for dynamic scene
reconstruction.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
