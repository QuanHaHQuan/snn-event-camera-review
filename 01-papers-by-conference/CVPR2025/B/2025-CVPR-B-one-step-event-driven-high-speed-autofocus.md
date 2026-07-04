---
title: "One-Step Event-Driven High-Speed Autofocus"
authors: ["Yuhan Bao", "Shaohua Gao", "Wenyong Li", "Kaiwei Wang"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Bao_One-Step_Event-Driven_High-Speed_Autofocus_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Bao_One-Step_Event-Driven_High-Speed_Autofocus_CVPR_2025_paper.html"
tags: []
abstract: "High-speed autofocus in extreme scenes remains a significant challenge. Traditional methods rely on repeated sampling around the focus position, resulting in \"focus hunting\". Event-driven methods have advanced focusing speed and improved performance in low-light conditions; however, current approaches still require at least one lengthy round of \"focus hunting\", involving the collection of a complete focus stack. We introduce the Event Laplacian Product (ELP) focus detection function, which combines event data with grayscale Laplacian information, redefining focus search as a detection task. This innovation enables the first one-step event-driven autofocus, cutting focusing time by up to two-thirds and reducing focusing error by 24 times on the DAVIS346 dataset and 22 times on the EVK4 dataset. Additionally, we present an autofocus pipeline tailored for event-only cameras, achieving accurate results across a range of challenging motion and lighting conditions. All datasets and code will be made publicly available."
status: "auto-generated; brief scan note"
---
## Core Problem

High-speed autofocus in extreme scenes remains a significant challenge.

## Core Method

Traditional methods rely on repeated sampling around the focus position, resulting in "focus
hunting".

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-driven。自动分类理由：Manual boundary check: official abstract confirms event
data, DAVIS346/EVK4 evaluation, and event-only cameras for high-speed autofocus.。 备注：CVPR
2025 official CVF page inspected under broad high-recall title workflow.。
