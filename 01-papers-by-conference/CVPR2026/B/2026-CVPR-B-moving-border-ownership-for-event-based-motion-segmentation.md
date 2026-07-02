---
title: "Moving Border Ownership for Event-based Motion Segmentation"
authors: ["Zhiyuan Hua", "Cornelia Fermüller", "Yiannis Aloimonos"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Hua_Moving_Border_Ownership_for_Event-based_Motion_Segmentation_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Hua_Moving_Border_Ownership_for_Event-based_Motion_Segmentation_CVPR_2026_paper.html"
tags: []
abstract: "Event cameras provide accurate information at motion boundaries--exactly where disentangling ego-motion, object motion, and border ownership determines segmentation quality. We argue that the missing ingredient in dynamic scene interpretation is moving border ownership: detecting motion boundaries and assigning which side is foreground so occlusions are resolved by design. Traditional geometric motion segmentation pipelines (e.g., flow clustering, simple motion models) remain assumption-heavy and slow, while deep models often fail to generalize across sensors or datasets. We introduce a lightweight, ownership-aware predictor trained solely on synthetic events with perfect supervision for boundaries, ownership, and motion, generated via a Blender pipeline. Its key targets--a signed-distance ownership field and a motion mask--focus learning where events occur and yield stable gradients. The model runs in real time and generalizes without tuning: trained on synthetic events, it achieves zero-shot transfer on EED, EVIMO1, EVIMO2, and EMSMC, delivering state-of-the-art performance. By casting motion segmentation as ownership-aware edge understanding, we combine the robustness of model-based reasoning with the scalability of learning."
status: "auto-generated; brief scan note"
---

## Core Problem

Event cameras provide accurate information at motion boundaries--exactly where disentangling ego-motion, object motion, and border ownership determines segmentation quality.

## Core Method

We argue that the missing ingredient in dynamic scene interpretation is moving border ownership: detecting motion boundaries and assigning which side is foreground so occlusions are resolved by design.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-based motion visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
