---
title: "EMoTive: Event-guided Trajectory Modeling for 3D Motion Estimation"
authors: ["Zengyu Wan", "Wei Zhai", "Yang Cao", "Zhengjun Zha"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Wan_EMoTive_Event-guided_Trajectory_Modeling_for_3D_Motion_Estimation_ICCV_2025_paper.html"
tags: []
abstract: "Visual 3D motion estimation aims to infer the motion of 2D pixels in 3D space based on visual cues. The key challenge arises from depth variation induced spatio-temporal motion inconsistencies, disrupting the assumptions of local spatial or temporal motion smoothness in previous motion estimation frameworks. In contrast, event cameras offer new possibilities for 3D motion estimation through continuous adaptive pixel-level responses to scene changes. This paper presents EMoTive, a novel event-based framework that models spatio-temporal trajectories via event-guided non-uniform parametric curves, effectively characterizing locally heterogeneous spatio-temporal motion. Specifically, we first introduce Event Kymograph - an event projection method that leverages a continuous temporal projection kernel and decouples spatial observations to encode fine-grained temporal evolution explicitly. For motion representation, we introduce a density-aware adaptation mechanism to fuse spatial and temporal features under event guidance, coupled with a non-uniform rational curve parameterization framework to adaptively model heterogeneous trajectories. The final 3D motion estimation is achieved through multi-temporal sampling of parametric trajectories, yielding optical flow and depth motion fields. To facilitate evaluation, we introduce CarlaEvent3D, a multi-dynamic synthetic dataset for comprehensive validation. Extensive experiments on both this dataset and a real-world benchmark demonstrate the effectiveness of the proposed method."
status: "auto-generated; brief scan note"
---
## Core Problem

Visual 3D motion estimation aims to infer the motion of 2D pixels in 3D space based on
visual cues.

## Core Method

The key challenge arises from depth variation induced spatio-temporal motion
inconsistencies, disrupting the assumptions of local spatial or temporal motion smoothness
in previous motion estimation frameworks.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
