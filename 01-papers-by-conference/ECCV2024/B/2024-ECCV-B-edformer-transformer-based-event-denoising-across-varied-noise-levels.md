---
title: "EDformer: Transformer-Based Event Denoising Across Varied Noise Levels"
authors: ["Bin Jiang", "Bo Xiong", "Bohan Qu", "M. Salman Asif", "You Zhou", "Zhan Ma"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03905.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1120"
tags: []
abstract: "Currently, there is relatively limited research on the non-informative background activity noise of event cameras in different brightness conditions, and the relevant real-world datasets is extremely scarce. This limitation contributes to the lack of robustness in existing event denoising algorithms when applied in practical scenarios. This paper addresses this gap by collecting and analyzing background activity noise from the DAVIS346 event camera under different illumination conditions. We introduce the first real-world event denoising dataset, ED24, encompassing 21 noise levels and noise annotations. Furthermore, we propose EDformer, an innovative event-by-event denoising model based on transformer. This model excels in event denoising by learning the spatiotemporal correlations among events across varied noise levels. In comparison to existing denoising algorithms, the proposed EDformer achieves state-of-the-art performance in denoising accuracy, including open-source datasets and datasets captured in practical scenarios with low-light intensity requirements such as zebrafish blood vessels imaging."
status: "auto-generated; brief scan note"
---

## Core Problem

Currently, there is relatively limited research on the non-informative background activity noise of event cameras in different brightness conditions, and the relevant real-world datasets is extremely scarce.

## Core Method

This limitation contributes to the lack of robustness in existing event denoising algorithms when applied in practical scenarios.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
