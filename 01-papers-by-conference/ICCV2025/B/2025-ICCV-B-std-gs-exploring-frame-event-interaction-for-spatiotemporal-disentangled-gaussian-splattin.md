---
title: "STD-GS: Exploring Frame-Event Interaction for SpatioTemporal-Disentangled Gaussian Splatting to Reconstruct High-Dynamic Scene"
authors: ["Hanyu Zhou", "Haonan Wang", "Haoyue Liu", "Yuxing Duan", "Luxin Yan", "Gim Hee Lee"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_STD-GS_Exploring_Frame-Event_Interaction_for_SpatioTemporal-Disentangled_Gaussian_Splatting_to_Reconstruct_ICCV_2025_paper.html"
tags: []
abstract: "High-dynamic scene reconstruction aims to represent static background with rigid spatial features and dynamic objects with deformed continuous spatiotemporal features. Typically, existing methods adopt unified representation model (e.g., Gaussian) to directly match the spatiotemporal features of dynamic scene from frame camera. However, this unified paradigm fails in the potential discontinuous temporal features of objects due to frame imaging and the heterogeneous spatial features between background and objects. In this work, we introduce event camera to compensate for frame camera, and propose a spatiotemporal-disentangled Gaussian splatting framework for high-dynamic scene reconstruction. As for dynamic scene, we figure out that background and objects have appearance discrepancy in frame-based spatial features and motion discrepancy in event-based temporal features, which motivates us to distinguish the spatiotemporal features between background and objects via clustering. As for dynamic object, we discover that Gaussian representations and event data share the consistent spatiotemporal characteristic, which could serve as a prior to guide the spatiotemporal disentanglement of object Gaussians. Within Gaussian splatting framework, the cumulative scene-object disentanglement can improve the spatiotemporal discrimination between background and objects to render the time-continuous dynamic scene. Extensive experiments are performed to verify the superiority of our method."
status: "auto-generated; brief scan note"
---

## Core Problem

High-dynamic scene reconstruction aims to represent static background with rigid spatial features and dynamic objects with deformed continuous spatiotemporal features.

## Core Method

Typically, existing methods adopt unified representation model (e.g., Gaussian) to directly match the spatiotemporal features of dynamic scene from frame camera.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; frame-event visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
