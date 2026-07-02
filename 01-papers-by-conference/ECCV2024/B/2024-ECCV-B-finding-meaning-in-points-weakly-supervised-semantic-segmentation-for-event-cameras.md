---
title: "Finding Meaning in Points: Weakly Supervised Semantic Segmentation for Event Cameras"
authors: ["Hoonhee Cho", "Sung-Hoon Yoon", "Hyeokjun Kweon", "KUK-JIN YOON"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05674.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/391"
tags: []
abstract: "Event cameras excel in capturing high-contrast scenes and dynamic objects, offering a significant advantage over traditional frame-based cameras. Despite active research into leveraging event cameras for semantic segmentation, generating pixel-wise dense semantic maps for such challenging scenarios remains labor-intensive. As a remedy, we present EV-WSSS: a novel weakly supervised approach for event-based semantic segmentation that utilizes sparse point annotations. To fully leverage the temporal characteristics of event data, the proposed framework performs asymmetric dual-student learning between 1) the original forward event data and 2) the longer reversed event data, which contain complementary information from the past and the future, respectively. Besides, to mitigate the challenges posed by sparse supervision, we propose feature-level contrastive learning based on class-wise prototypes, carefully aggregated at both spatial region and sample levels. Additionally, we further excavate the potential of our dual-student learning model by exchanging prototypes between the two learning paths, thereby harnessing their complementary strengths. With extensive experiments on various datasets, including DSEC Night-Point with sparse point annotations newly provided by this paper, the proposed method achieves substantial segmentation results even without relying on pixel-level dense ground truths. The code and dataset will be published soon."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras excel in capturing high-contrast scenes and dynamic objects, offering a
significant advantage over traditional frame-based cameras.

## Core Method

Despite active research into leveraging event cameras for semantic segmentation, generating
pixel-wise dense semantic maps for such challenging scenarios remains labor-intensive.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event cameras。自动分类理由：Official abstract confirms event cameras for weakly supervised
semantic segmentation; no clear SNN evidence.。
