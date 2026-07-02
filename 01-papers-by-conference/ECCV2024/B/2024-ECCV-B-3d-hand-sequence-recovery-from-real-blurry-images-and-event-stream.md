---
title: "3D Hand Sequence Recovery from Real Blurry Images and Event Stream"
authors: ["Joonkyu Park", "Gyeongsik Moon", "Weipeng Xu", "Evan Kaseman", "Takaaki Shiratori", "Kyoung Mu Lee"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07674.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/620"
tags: []
abstract: "Although hands frequently exhibit motion blur due to their dynamic nature, existing approaches for 3D hand recovery often disregard the impact of motion blur in hand images. Blurry hand images contain hands from multiple time steps, lacking precise hand location at a specific time step and introducing temporal ambiguity, leading to multiple possible hand trajectories. To address this issue and in the absence of datasets with real blur, we introduce the EBH dataset, which provides 1) hand images with real motion blur and 2) event data for authentic representation of fast hand movements. In conjunction with our new dataset, we present EBHNet, a novel network capable of recovering 3D hands from diverse input combinations, including blurry hand images, events, or both. Here, the event stream enhances motion understanding in blurry hands, addressing temporal ambiguity. Recognizing that blurry hand images include not only single 3D hands at a time step but also multiple hands along their motion trajectories, we design EBHNet to generate 3D hand sequences in motion. Moreover, to enable our EBHNet to predict 3D hands at novel, unsupervised time steps using a single shared module, we employ a Transformer-based module, temporal splitter, into EBHNet. Our experiments show the superior performance of EBH and EBHNet, especially in handling blurry hand images, making them valuable in real-world applications. The code and dataset will be released."
status: "auto-generated; brief scan note"
---
## Core Problem

Although hands frequently exhibit motion blur due to their dynamic nature, existing
approaches for 3D hand recovery often disregard the impact of motion blur in hand images.

## Core Method

Blurry hand images contain hands from multiple time steps, lacking precise hand location at
a specific time step and introducing temporal ambiguity, leading to multiple possible hand
trajectories.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event stream; event data。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
