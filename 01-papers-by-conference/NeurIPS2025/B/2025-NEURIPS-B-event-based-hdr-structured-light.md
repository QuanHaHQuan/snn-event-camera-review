---
title: "Event-based HDR Structured Light"
authors: ["Jiacheng Fu, Yue Li, Xin Dong, Wenming Weng, Yueyi Zhang, Zhiwei Xiong"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/3056e3b2266c62ec11b110933db92284-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/3056e3b2266c62ec11b110933db92284-Abstract-Conference.html"
tags: []
abstract: "Event-based structured light (SL) systems have attracted increasing attention for their potential in high-performance 3D measurement. Despite the inherent HDR capability of event cameras, reflective and absorptive surfaces still cause event cluttering and absence, which produce overexposed and underexposed regions that degrade the reconstruction quality. In this work, we present the first HDR 3D measurement framework specifically designed for event-based SL systems. First, we introduce a multi-contrast HDR coding strategy that facilitates imaging of areas with different reflectance. Second, to alleviate inter-frame interference caused by overexposed and underexposed areas, we propose a universal confidence-driven stereo matching strategy. Specifically, we estimate a confidence map as the fusion weight for features via an energy-guided confidence estimation. Further, we propose the confidence propagation volume, an innovative cost volume that offers both effective suppression of inter-frame interference and strong representation capability. Third, we contribute an event-based SL simulator and propose the first event-based HDR SL dataset. We also collect a real-world benchmarking dataset with ground truth. We validate the effectiveness of our method with the proposed confidence-driven strategy on both synthetic and real-world datasets. Experimental results demonstrate that our proposed HDR framework enables accurate 3D measurement even under extreme conditions."
status: "auto-generated; brief scan note"
---

## Core Problem

Event-based structured light (SL) systems have attracted increasing attention for their potential in high-performance 3D measurement.

## Core Method

Despite the inherent HDR capability of event cameras, reflective and absorptive surfaces still cause event cluttering and absence, which produce overexposed and underexposed regions that degrade the reconstruction quality.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
