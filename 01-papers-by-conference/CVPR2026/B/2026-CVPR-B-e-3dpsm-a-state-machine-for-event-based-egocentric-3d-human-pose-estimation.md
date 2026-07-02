---
title: "E-3DPSM: A State Machine for Event-based Egocentric 3D Human Pose Estimation"
authors: ["Mayur Deshmukh", "Hiroyasu Akada", "Helge Rhodin", "Christian Theobalt", "Vladislav Golyanik"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Deshmukh_E-3DPSM_A_State_Machine_for_Event-based_Egocentric_3D_Human_Pose_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Deshmukh_E-3DPSM_A_State_Machine_for_Event-based_Egocentric_3D_Human_Pose_CVPR_2026_paper.html"
tags: []
abstract: "Event cameras offer multiple advantages in monocular egocentric 3D human pose estimation from head-mounted devices, such as millisecond temporal resolution, high dynamic range, and negligible motion blur. Existing methods effectively leverage these properties, but suffer from low 3D estimation accuracy, insufficient in many applications (e.g., immersive VR/AR). This is due to the design not being fully tailored towards event streams (e.g., their asynchronous and continuous nature), leading to high sensitivity to self-occlusions and temporal jitter in the estimates. This paper rethinks the setting and introduces E-3DPSM, an event-driven continuous pose state machine for event-based egocentric 3D human pose estimation. E-3DPSM aligns continuous human motion with fine-grained event dynamics; it evolves latent states and predicts continuous changes in 3D joint positions associated with observed events, which are fused with direct 3D human pose predictions, leading to stable and drift-free final 3D pose reconstructions. E-3DPSM runs in real-time at 80 Hz on a single workstation and sets a new state of the art in experiments on two benchmarks, improving accuracy by up to 19% (MPJPE) and temporal stability by up to 2.7x."
status: "auto-generated; brief scan note"
---

## Core Problem

Event cameras offer multiple advantages in monocular egocentric 3D human pose estimation from head-mounted devices, such as millisecond temporal resolution, high dynamic range, and negligible motion blur.

## Core Method

Existing methods effectively leverage these properties, but suffer from low 3D estimation accuracy, insufficient in many applications (e.g., immersive VR/AR).

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event stream with event-camera context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
