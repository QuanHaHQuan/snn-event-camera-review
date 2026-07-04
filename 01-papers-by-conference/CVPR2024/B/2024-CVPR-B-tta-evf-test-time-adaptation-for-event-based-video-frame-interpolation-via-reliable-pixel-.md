---
title: "TTA-EVF: Test-Time Adaptation for Event-based Video Frame Interpolation via Reliable Pixel and Sample Estimation"
authors: ["Hoonhee Cho", "Taewoo Kim", "Yuhwan Jeong", "Kuk-Jin Yoon"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Cho_TTA-EVF_Test-Time_Adaptation_for_Event-based_Video_Frame_Interpolation_via_Reliable_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Cho_TTA-EVF_Test-Time_Adaptation_for_Event-based_Video_Frame_Interpolation_via_Reliable_CVPR_2024_paper.html"
tags: []
abstract: "Video Frame Interpolation (VFI) which aims at generating high-frame-rate videos from low-frame-rate inputs is a highly challenging task. The emergence of bio-inspired sensors known as event cameras which boast microsecond-level temporal resolution has ushered in a transformative era for VFI. Nonetheless the application of event-based VFI techniques in domains with distinct environments from the training data can be problematic. This is mainly because event camera data distribution can undergo substantial variations based on camera settings and scene conditions presenting challenges for effective adaptation. In this paper we propose a test-time adaptation method for event-based VFI to address the gap between the source and target domains. Our approach enables sequential learning in an online manner on the target domain which only provides low-frame-rate videos. We present an approach that leverages confident pixels as pseudo ground-truths enabling stable and accurate online learning from low-frame-rate videos. Furthermore to prevent overfitting during the continuous online process where the same scene is encountered repeatedly we propose a method of blending historical samples with current scenes. Extensive experiments validate the effectiveness of our method both in cross-domain and continuous domain shifting setups. The code is available at https://github.com/Chohoonhee/TTA-EVF."
status: "auto-generated; brief scan note"
---
## Core Problem

Video Frame Interpolation (VFI) which aims at generating high-frame-rate videos from low-
frame-rate inputs is a highly challenging task.

## Core Method

The emergence of bio-inspired sensors known as event cameras which boast microsecond-level
temporal resolution has ushered in a transformative era for VFI.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
