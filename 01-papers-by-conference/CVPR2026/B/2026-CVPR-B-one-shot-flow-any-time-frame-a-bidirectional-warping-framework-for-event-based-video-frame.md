---
title: "One-Shot Flow, Any-Time Frame: A Bidirectional Warping Framework for Event-Based Video Frame Interpolation"
authors: ["Linghui Fu", "Yuhan Liu", "Hao Chen", "Zhen Yang", "Yongjian Deng"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Fu_One-Shot_Flow_Any-Time_Frame_A_Bidirectional_Warping_Framework_for_Event-Based_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Fu_One-Shot_Flow_Any-Time_Frame_A_Bidirectional_Warping_Framework_for_Event-Based_CVPR_2026_paper.html"
tags: []
abstract: "Video Frame Interpolation (VFI) is a crucial task in video processing. Flow-based methods, despite their success, are constrained by a fundamental dilemma: forward warping is efficient but prone to artifacts, while backward warping yields higher quality at a significant computational cost, especially for multi-frame interpolation. This trade-off is a major bottleneck. To overcome this, we introduce \"One-Shot Flow, Any-Time Frame,\" a novel framework for Event-based VFI (E-VFI) that achieves both high efficiency and superior quality for arbitrary-time interpolation. Our framework uniquely computes a comprehensive motion trajectory representation in a single pass using a Bidirectional Flow Estimation Block (BiFEB), leveraging the high temporal resolution of event data. Subsequently, our Flow Query (FQ) module can instantly retrieve the bidirectional optical flow for any timestamp, enabling the generation of any number of frames without repeated computation. Finally, a novel Bidirectional Warping (BiW) mechanism intelligently fuses the strengths of both warping directions, effectively mitigating artifacts and producing high-fidelity results. Extensive experiments show that our approach consistently surpasses state-of-the-art E-VFI methods in both reconstruction quality and inference efficiency, representing a substantial advance in efficient and high-quality event-based video interpolation. *The code will be released after acceptance.*"
status: "auto-generated; brief scan note"
---

## Core Problem

Video Frame Interpolation (VFI) is a crucial task in video processing.

## Core Method

Flow-based methods, despite their success, are constrained by a fundamental dilemma: forward warping is efficient but prone to artifacts, while backward warping yields higher quality at a significant computational cost, especially for multi-frame interpolation.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event-based video visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
