---
title: "E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction"
authors: ["Yunsoo Kim", "Changki Sung", "Dasol Hong", "Hyun Myung"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.html"
tags: []
abstract: "The emergence of neural radiance fields (NeRF) and 3D Gaussian splatting (3DGS) has advanced novel view synthesis (NVS). These methods, however, require high-quality RGB inputs and accurate corresponding poses, limiting robustness under real-world conditions such as fast camera motion or adverse lighting. Event cameras, which capture brightness changes at each pixel with high temporal resolution and wide dynamic range, enable precise sensing of dynamic scenes and offer a promising solution. However, existing event-based NVS methods either assume known poses or rely on depth estimation models that are bounded by their initial observations, failing to generalize as the camera traverses previously unseen regions. We present E2EGS, a pose-free framework operating solely on event streams. Our key insight is that edge information provides rich structural cues essential for accurate trajectory estimation and high-quality NVS. To extract edges from noisy event streams, we exploit the distinct spatio-temporal characteristics of edges and non-edge regions. The event camera's movement induces consistent events along edges, while non-edge regions produce sparse noise. We leverage this through a patch-based temporal coherence analysis that measures local variance to extract edges while robustly suppressing noise. The extracted edges guide structure-aware Gaussian initialization and enable edge-weighted losses throughout initialization, tracking, and bundle adjustment. Extensive experiments on both synthetic and real datasets demonstrate that E2EGS achieves superior reconstruction quality and trajectory accuracy, establishing a fully pose-free paradigm for event-based 3D reconstruction."
status: "auto-generated; brief scan note"
---

## Core Problem

The emergence of neural radiance fields (NeRF) and 3D Gaussian splatting (3DGS) has advanced novel view synthesis (NVS).

## Core Method

These methods, however, require high-quality RGB inputs and accurate corresponding poses, limiting robustness under real-world conditions such as fast camera motion or adverse lighting.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; brightness change visual-event context; event stream with event-camera context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
