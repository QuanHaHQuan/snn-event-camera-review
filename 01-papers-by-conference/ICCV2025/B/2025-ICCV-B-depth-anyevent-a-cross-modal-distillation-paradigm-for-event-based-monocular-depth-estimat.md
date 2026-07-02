---
title: "Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation"
authors: ["Luca Bartolomei", "Enrico Mannocci", "Fabio Tosi", "Matteo Poggi", "Stefano Mattoccia"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Bartolomei_Depth_AnyEvent_A_Cross-Modal_Distillation_Paradigm_for_Event-Based_Monocular_Depth_ICCV_2025_paper.html"
tags: []
abstract: "Event cameras capture sparse, high-temporal-resolution visual information, making them particularly suitable for challenging environments with high-speed motion and strongly varying lighting conditions. However, the lack of large datasets with dense ground-truth depth annotations hinders learning-based monocular depth estimation from event data. To address this limitation, we propose a cross-modal distillation paradigm to generate dense proxy labels leveraging a Vision Foundation Model (VFM). Our strategy requires an event stream spatially aligned with RGB frames, a simple setup even available off-the-shelf, and exploits the robustness of large-scale VFMs.Additionally, we propose to adapt VFMs, either a vanilla one like Depth Anything v2 (DAv2), or deriving from it a novel recurrent architecture to infer depth from monocular event cameras. We evaluate our approach using synthetic and real-world datasets, demonstrating that i) our cross-modal paradigm achieves competitive performance compared to fully supervised methods without requiring expensive depth annotations, and ii) our VFM-based models achieve state-of-the-art performance"
status: "auto-generated; brief scan note"
---

## Core Problem

Event cameras capture sparse, high-temporal-resolution visual information, making them particularly suitable for challenging environments with high-speed motion and strongly varying lighting conditions.

## Core Method

However, the lack of large datasets with dense ground-truth depth annotations hinders learning-based monocular depth estimation from event data.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event stream with event-camera context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
