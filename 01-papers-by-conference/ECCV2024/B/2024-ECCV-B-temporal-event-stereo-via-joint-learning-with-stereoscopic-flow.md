---
title: "Temporal Event Stereo via Joint Learning with Stereoscopic Flow"
authors: ["Hoonhee Cho", "Jae-young Kang", "KUK-JIN YOON"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05185.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1741"
tags: []
abstract: "Event cameras are dynamic vision sensors inspired by the biological retina, characterized by their high dynamic range, high temporal resolution, and low power consumption. These features make them capable of perceiving 3D environments even in extreme conditions. Event data is continuous across the time dimension, which allows a detailed description of each pixel's movements. To fully utilize the temporally dense and continuous nature of event cameras, we propose a novel temporal event stereo, a framework that continuously uses information from previous time steps. This is accomplished through the simultaneous training of an event stereo matching network alongside stereoscopic flow, a new concept that captures all pixel movements from stereo cameras. Since obtaining ground truth for optical flow during training is challenging, we propose a method that uses only disparity maps to train the stereoscopic flow. Ultimately, we enhance the performance of event-based stereo matching by temporally aggregating information using the flows. We have achieved state-of-the-art performance on the MVSEC and the DSEC dataset. Our method is computationally efficient as it stacks previous information in a cascading manner."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras are dynamic vision sensors inspired by the biological retina, characterized by
their high dynamic range, high temporal resolution, and low power consumption.

## Core Method

These features make them capable of perceiving 3D environments even in extreme conditions.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; DVS; event data; event-based stereo。自动分类理由：Official abstract/page
confirms event-camera/DVS/event-stream evidence; no clear SNN evidence.。
