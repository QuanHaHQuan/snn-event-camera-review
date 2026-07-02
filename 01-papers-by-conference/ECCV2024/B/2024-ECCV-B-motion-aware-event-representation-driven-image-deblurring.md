---
title: "Motion Aware Event Representation-driven Image Deblurring"
authors: ["Zhijing Sun", "Xueyang Fu", "Longzhuo Huang", "Aiping Liu", "Zheng-Jun Zha"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06299.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1001"
tags: []
abstract: "Traditional image deblurring struggles with high-quality reconstruction due to limited motion data from single blurred images. Excitingly, the high-temporal resolution of event cameras records motion more precisely in a different modality, transforming image deblurring. However, many event camera-based methods, which only care about the final value of the polarity accumulation, ignore the influence of the absolute intensity change where events generate so fall short in perceiving motion patterns and effectively aiding image reconstruction. To overcome this, in this work, we propose a new event preprocessing technique that accumulates the deviation from the initial moment each time the event is updated. This process can distinguish the order of events to improve the perception of object motion patterns. To complement our proposed event representation, we create a recurrent module designed to meticulously extract motion features across local and global time scales. To further facilitate the event feature and image feature integration, which assists in image reconstruction, we develop a bi-directional feature alignment and fusion module. This module works to lessen inter-modal inconsistencies. Our approach has been thoroughly tested through rigorous experiments carried out on several datasets with different distributions. These trials have delivered promising results, with our method achieving top-tier performance in both quantitative and qualitative assessments."
status: "auto-generated; brief scan note"
---
## Core Problem

Traditional image deblurring struggles with high-quality reconstruction due to limited
motion data from single blurred images.

## Core Method

Excitingly, the high-temporal resolution of event cameras records motion more precisely in a
different modality, transforming image deblurring.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event representation。自动分类理由：Auxiliary title hit; official abstract confirms event
cameras for image deblurring; no clear SNN evidence.。
