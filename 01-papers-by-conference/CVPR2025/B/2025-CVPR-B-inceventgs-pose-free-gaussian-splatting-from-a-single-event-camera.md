---
title: "IncEventGS: Pose-Free Gaussian Splatting from a Single Event Camera"
authors: ["Jian Huang", "Chengrui Dong", "Xuanhua Chen", "Peidong Liu"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_IncEventGS_Pose-Free_Gaussian_Splatting_from_a_Single_Event_Camera_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Huang_IncEventGS_Pose-Free_Gaussian_Splatting_from_a_Single_Event_Camera_CVPR_2025_paper.html"
tags: []
abstract: "Implicit neural representation and explicit 3D Gaussian Splatting (3D-GS) for novel view synthesis have achieved remarkable progress with frame-based camera (e.g. RGB and RGB-D cameras) recently. Compared to frame-based camera, a novel type of bio-inspired visual sensor, i.e. event camera, has demonstrated advantages in high temporal resolution, high dynamic range, low power consumption and low latency, which make it being favored for many robotic applications. In this work, we present IncEventGS, an incremental 3D Gaussian Splatting reconstruction algorithm with a single event camera, without the assumption of known camera poses. To recover the 3D scene representation incrementally, we exploit the tracking and mapping paradigm of conventional SLAM pipelines for IncEventGS. Given the incoming event stream, the tracker first estimates an initial camera motion based on prior reconstructed 3D-GS scene representation. The mapper then jointly refines both the 3D scene representation and camera motion based on the previously estimated motion trajectory from the tracker. The experimental results demonstrate that IncEventGS delivers superior performance compared to prior NeRF-based methods and other related baselines, even we do not have the ground-truth camera poses. Furthermore, our method can also deliver better performance compared to state-of-the-art event visual odometry methods in terms of camera motion estimation."
status: "auto-generated; brief scan note"
---
## Core Problem

Implicit neural representation and explicit 3D Gaussian Splatting (3D-GS) for novel view
synthesis have achieved remarkable progress with frame-based camera (e.g.

## Core Method

RGB and RGB-D cameras) recently.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official
CVF page inspected under broad high-recall title workflow.。
