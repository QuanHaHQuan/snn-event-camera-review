---
title: "Towards Robust Event-based Networks for Nighttime via Unpaired Day-to-Night Event Translation"
authors: ["Yuhwan Jeong", "Hoonhee Cho", "KUK-JIN YOON"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08432.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/2482"
tags: []
abstract: "Event cameras with high dynamic range ensure scene capture even in low-light conditions. However, night events exhibit patterns different from those captured during the day. This difference causes performance degradation when applying night events to a model trained solely on day events. This limitation persists due to a lack of annotated night events. To overcome the limitation, we aim to alleviate data imbalance by translating annotated day data into night events. However, generating events from different modalities challenges reproducing their unique properties. Accordingly, we propose an unpaired event-to-event day-to-night translation model that effectively learns to map from one domain to another using Diffusion GAN. The proposed translation model analyzes events in spatio-temporal dimension with wavelet decomposition and disentangled convolution layers. We also propose a new temporal contrastive learning with a novel shuffling and sampling strategy to regularize temporal continuity. To validate the efficacy of the proposed methodology, we redesign metrics for evaluating events translated in an unpaired setting, aligning them with the event modality for the first time. Our framework shows the successful day-to-night event translation while preserving the characteristics of events. In addition, through our translation method, we facilitate event-based modes to learn about night events by translating annotated day events into night events. Our approach effectively mitigates the performance degradation of applying real night events to downstream tasks."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras with high dynamic range ensure scene capture even in low-light conditions.

## Core Method

However, night events exhibit patterns different from those captured during the day.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event-based official cross-check。自动分类理由：Official abstract confirms event cameras and
event-to-event day-to-night translation; no clear SNN evidence.。
