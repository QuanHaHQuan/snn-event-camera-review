---
title: "Event-assisted Low-Light Video Object Segmentation"
authors: ["Hebei Li", "Jin Wang", "Jiahui Yuan", "Yue Li", "Wenming Weng", "Yansong Peng", "Yueyi Zhang", "Zhiwei Xiong", "Xiaoyan Sun"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Li_Event-assisted_Low-Light_Video_Object_Segmentation_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Li_Event-assisted_Low-Light_Video_Object_Segmentation_CVPR_2024_paper.html"
tags: []
abstract: "In the realm of video object segmentation (VOS) the challenge of operating under low-light conditions persists resulting in notably degraded image quality and compromised accuracy when comparing query and memory frames for similarity computation. Event cameras characterized by their high dynamic range and ability to capture motion information of objects offer promise in enhancing object visibility and aiding VOS methods under such low-light conditions. This paper introduces a pioneering framework tailored for low-light VOS leveraging event camera data to elevate segmentation accuracy. Our approach hinges on two pivotal components: the Adaptive Cross-Modal Fusion (ACMF) module aimed at extracting pertinent features while fusing image and event modalities to mitigate noise interference and the Event-Guided Memory Matching (EGMM) module designed to rectify the issue of inaccurate matching prevalent in low-light settings. Additionally we present the creation of a synthetic LLE-DAVIS dataset and the curation of a real-world LLE-VOS dataset encompassing frames and events. Experimental evaluations corroborate the efficacy of our method across both datasets affirming its effectiveness in low-light scenarios. The datasets are available at https://github.com/HebeiFast/EventLowLightVOS."
status: "auto-generated; brief scan note"
---
## Core Problem

In the realm of video object segmentation (VOS) the challenge of operating under low-light
conditions persists resulting in notably degraded image quality and compromised accuracy
when comparing query and memory frames for similarity computation.

## Core Method

Event cameras characterized by their high dynamic range and ability to capture motion
information of objects offer promise in enhancing object visibility and aiding VOS methods
under such low-light conditions.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-
stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official CVF page inspected
under broad high-recall title workflow.。
