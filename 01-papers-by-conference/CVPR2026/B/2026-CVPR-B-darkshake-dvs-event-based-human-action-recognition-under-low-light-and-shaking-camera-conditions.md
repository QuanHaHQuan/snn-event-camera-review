---
title: "DarkShake-DVS: Event-based Human Action Recognition under Low-light and Shaking Camera Conditions"
authors: ["Jiaqi Chen", "Qinfu Xu", "Liyuan Pan"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_DarkShake-DVS_Event-based_Human_Action_Recognition_under_Low-light_and_Shaking_Camera_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Chen_DarkShake-DVS_Event-based_Human_Action_Recognition_under_Low-light_and_Shaking_Camera_CVPR_2026_paper.html"
tags: []
abstract: "Human Action Recognition (HAR) is a fundamental computer vision task with diverse real-world applications. Practical deployments often involve low-light environments and unconstrained 6-DoF camera motion, conditions that degrade visual quality, disrupt temporal coherence, and compromise reliability of existing methods. Event cameras, with high low-light sensitivity and microsecond-level temporal resolution, paired with an inertial measurement unit (IMU), present a promising solution. However, current research faces two key challenges: absence of a benchmark integrating low-light conditions, 6-DoF motion, and synchronized IMU data; and lack of effective motion compensation techniques. To address these, we propose Event-IMU Stabilized HAR (EIS-HAR), with two modules. The first is an EIS module that reduces motion blur via a non-linear warping function to reconstruct a motion-compensated input. The second is a HAR module with a four-stage hybrid architecture to efficiently extract spatiotemporal features for accurate action recognition. To alleviate data scarcity, we introduce DarkShake-DVS, the first large-scale event-based HAR benchmark that includes 18,041 real-world clips captured in low light and intense 6-DoF motion, supplemented by synchronized IMU data. Extensive experiments on three datasets demonstrate consistent superiority of EIS-HAR over state-of-the-art methods."
status: "auto-generated; brief scan note"
---

## Core Problem

低照度和抖动摄像条件会破坏传统动作识别的视觉质量与时序一致性。

## Core Method

提出事件相机 + IMU 的动作识别框架，并补充低照度、6DoF 运动与同步 IMU 的基准。

## Key Metrics and Findings

摘要强调数据集与运动补偿机制是主要贡献。

## Personal Notes

适合放在事件相机动作识别与多传感器章节。

