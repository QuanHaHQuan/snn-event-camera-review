---
title: "Event-based Motion Deblurring with Unpaired Data"
authors: ["Hoonhee Cho", "Yuhwan Jeong", "Kuk-Jin Yoon"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Cho_Event-based_Motion_Deblurring_with_Unpaired_Data_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Cho_Event-based_Motion_Deblurring_with_Unpaired_Data_CVPR_2026_paper.html"
tags: []
abstract: "Event cameras provide high-temporal-resolution, motion-centric measurements that remain reliable under fast motion and challenging illumination, making them a promising sensing modality for motion deblurring. However, existing deblurring methods typically require large-scale paired blur--sharp datasets, which are extremely difficult to obtain in real-world settings, especially when an additional modality such as events is involved. In this work, we introduce EMP, an event-based motion deblurring framework that operates entirely in an unpaired setting, removing the need for aligned blur--sharp supervision. EMP bridges the disjoint blur and sharp domains through event information and leverages two complementary training mechanisms tailored to the unpaired regime: (1) an event-based physical prior with confidence masking that provides reliable self-supervisory signals for blurry inputs, and (2) a generative blur modeling process that extracts blur-related frequency-domain cues from blur--event pairs and transfers them to sharp images to synthesize realistic blur. Together, these mechanisms enable stable and effective deblurring without paired labels. Extensive experiments on various real event datasets, including REBlur, EventAid, and HighREV, show that EMP outperforms existing unpaired baselines and achieves performance competitive with paired methods."
status: "auto-generated; brief scan note"
---

## Core Problem

Event cameras provide high-temporal-resolution, motion-centric measurements that remain reliable under fast motion and challenging illumination, making them a promising sensing modality for motion deblurring.

## Core Method

However, existing deblurring methods typically require large-scale paired blur--sharp datasets, which are extremely difficult to obtain in real-world settings, especially when an additional modality such as events is involved.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-based motion visual-event context; event dataset visual-event context; event datasets visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
