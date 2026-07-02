---
title: "Event6D: Event-based Novel Object 6D Pose Tracking"
authors: ["Jae-Young Kang", "Hoonhee Cho", "Taeyeop Lee", "Minjun Kang", "Bowen Wen", "Youngho Kim", "Kuk-Jin Yoon"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_Event6D_Event-based_Novel_Object_6D_Pose_Tracking_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Kang_Event6D_Event-based_Novel_Object_6D_Pose_Tracking_CVPR_2026_paper.html"
tags: []
abstract: "Event cameras provide microsecond latency, making them suitable for 6D object pose tracking in fast, dynamic scenes where conventional RGB and depth pipelines suffer from motion blur and large pixel displacements. We introduce EventTrack6D, an event-depth tracking framework that generalizes to novel objects without object-specific training by reconstructing both intensity and depth at arbitrary timestamps between depth frames. Conditioned on the most recent depth measurement, our dual reconstruction recovers dense photometric and geometric cues from sparse event streams. Our EventTrack6D operates at over 120 FPS and maintains temporal consistency under rapid motion. To support training and evaluation, we introduce a comprehensive benchmark suite: a large-scale synthetic dataset for training and two complementary evaluation sets, including real and simulated event datasets. Trained exclusively on synthetic data, EventTrack6D generalizes effectively to real-world scenarios without fine-tuning, maintaining accurate tracking across diverse objects and motion patterns. Our method and datasets validate the effectiveness of event cameras for event-based 6D pose tracking of novel objects. Code and datasets are publicly available at https://chohoonhee.github.io/Event6D."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras provide microsecond latency, making them suitable for 6D object pose tracking
in fast, dynamic scenes where conventional RGB and depth pipelines suffer from motion blur
and large pixel displacements.

## Core Method

We introduce EventTrack6D, an event-depth tracking framework that generalizes to novel
objects without object-specific training by reconstructing both intensity and depth at
arbitrary timestamps between depth frames.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event stream; event data。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
