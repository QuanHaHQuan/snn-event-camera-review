---
title: "MATE: Motion-Augmented Temporal Consistency for Event-based Point Tracking"
authors: ["Han Han", "Wei Zhai", "Yang Cao", "Bin Li", "Zheng-jun Zha"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Han_MATE_Motion-Augmented_Temporal_Consistency_for_Event-based_Point_Tracking_ICCV_2025_paper.html"
tags: []
abstract: "Tracking Any Point (TAP) plays a crucial role in motion analysis. Video-based approaches rely on iterative local matching for tracking, but they assume linear motion during the blind time between frames, which leads to point loss under large displacements or nonlinear motion. The high temporal resolution and motion blur-free characteristics of event cameras provide continuous, fine-grained motion information, capturing subtle variations with microsecond precision. This paper presents an event-based framework for tracking any point, which tackles the challenges posed by spatial sparsity and motion sensitivity in events through two tailored modules. Specifically, to resolve ambiguities caused by event sparsity, a motion-guidance module incorporates kinematic vectors into the local matching process. Additionally, a variable motion aware module is integrated to ensure temporally consistent responses that are insensitive to varying velocities, thereby enhancing matching precision.To validate the effectiveness of the approach, two event dataset for tracking any point is constructed by simulation. The method improves the Survival_ 50 metric by 17.9% over event-only tracking of any point baseline. Moreover, on standard feature tracking benchmarks, it outperforms all existing methods, even those that combine events and video frames."
status: "auto-generated; brief scan note"
---
## Core Problem

Tracking Any Point (TAP) plays a crucial role in motion analysis.

## Core Method

Video-based approaches rely on iterative local matching for tracking, but they assume linear
motion during the blind time between frames, which leads to point loss under large
displacements or nonlinear motion.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event data。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
