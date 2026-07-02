---
title: "AE2VID: Event-based Video Reconstruction via Aperture Modulation"
authors: ["Chenxu Bai", "Boyu Li", "Peiqi Duan", "Xinyu Zhou", "Hanyue Lou", "Boxin Shi"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Bai_AE2VID_Event-based_Video_Reconstruction_via_Aperture_Modulation_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Bai_AE2VID_Event-based_Video_Reconstruction_via_Aperture_Modulation_CVPR_2026_paper.html"
tags: []
abstract: "Event-based video reconstruction seeks to recover high-speed, high-dynamic-range videos from event streams. While existing approaches rely exclusively on motion-triggered events, these events are inherently sparse and primarily capture dynamic regions. Therefore, they often suffer from error accumulation and degraded quality in regions with few events. In this work, we introduce aperture-modulation-triggered events as a complementary mechanism to enrich the captured scene information. Specifically, we periodically modulate the aperture to actively generate dense event signals, thereby encoding intensity cues even in static or low-motion regions. Building upon this idea, we design an AE2VID framework that jointly leverages aperture-modulation-triggered and motion-triggered events to enhance the fidelity of predictions. The proposed framework consists of two subnetworks for the dedicated processing of both event types. We further collect a real dataset and validate the effectiveness of our method. Extensive experiments show our superiority over state-of-the-art methods. Code and data will be available at https://github.com/a1henu/AE2VID/."
status: "auto-generated; brief scan note"
---

## Core Problem

Event-based video reconstruction seeks to recover high-speed, high-dynamic-range videos from event streams.

## Core Method

While existing approaches rely exclusively on motion-triggered events, these events are inherently sparse and primarily capture dynamic regions.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event-based video visual-event context; event stream with event-camera context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
