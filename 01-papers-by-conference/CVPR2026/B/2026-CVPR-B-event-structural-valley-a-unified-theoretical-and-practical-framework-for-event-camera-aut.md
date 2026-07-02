---
title: "Event Structural Valley: A Unified Theoretical and Practical Framework for Event Camera Autofocus"
authors: ["Xijie Xiang", "Lin Zhu", "Wei Zhang", "Yonghong Tian"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Xiang_Event_Structural_Valley_A_Unified_Theoretical_and_Practical_Framework_for_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_Event_Structural_Valley_A_Unified_Theoretical_and_Practical_Framework_for_CVPR_2026_paper.html"
tags: []
abstract: "Autofocus in dynamic environments remains challenging for conventional frame-based sensors, which often fail under fast motion, low light, or high dynamic range conditions. Event cameras, with microsecond temporal resolution and asynchronous brightness detection, offer a promising alternative. However, typical event-based autofocus methods assume that the sharpest focus corresponds to the maximum event rate. In this paper, we reveal a counterintuitive yet consistent phenomenon: the true focus actually corresponds to a local minimum in the event-rate curve. We theoretically derive this behavior from the physics of event generation and show that as defocus blur increases, the event rate first rises and then declines, forming a dual-peak-valley structure across focal distances. Based on this insight, we propose an Event Structural Valley-based Autofocus (ESVA) framework that identifies the valley between two dominant peaks as the true focal position. ESVA integrates structural smoothing, consistency filtering, and a dual-peak constraint to robustly recover the valley under noise and motion disturbances. Extensive experiments on multiple synthetic and real-world datasets demonstrate that ESVA delivers accurate and stable focus estimation, consistently outperforming existing event-only autofocus methods without requiring image reconstruction or supervision."
status: "auto-generated; brief scan note"
---
## Core Problem

Autofocus in dynamic environments remains challenging for conventional frame-based sensors,
which often fail under fast motion, low light, or high dynamic range conditions.

## Core Method

Event cameras, with microsecond temporal resolution and asynchronous brightness detection,
offer a promising alternative.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
