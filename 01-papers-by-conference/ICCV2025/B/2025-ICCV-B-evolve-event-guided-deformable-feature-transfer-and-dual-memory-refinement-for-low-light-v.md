---
title: "EVOLVE: Event-Guided Deformable Feature Transfer and Dual-Memory Refinement for Low-Light Video Object Segmentation"
authors: ["Jong-Hyeon Baek", "Jiwon Oh", "Yeong Jun Koh"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Baek_EVOLVE_Event-Guided_Deformable_Feature_Transfer_and_Dual-Memory_Refinement_for_Low-Light_ICCV_2025_paper.html"
tags: []
abstract: "Video Object Segmentation (VOS) in low-light scenarios remains highly challenging due to significant texture loss and severe noise, which often lead to unreliable image feature generation and degraded segmentation performance. To address this issue, we propose EVOLVE, a novel event-guided deformable feature transfer and dual-memory refinement framework for low-light VOS. EVOLVE addresses spatial misalignment between frames and improves object representation by utilizing event-driven cues. The event-guided deformable feature transfer (EDFT) module enhances feature alignment through event-driven deformable convolutions, where offsets derived from event features enable motion-aware spatial adjustments, leading to more precise propagation of object features in reference frames. Furthermore, the dual-memory object transformer (DMOT) iteratively refines object representations by maintaining and updating both image-based and event-based memory representations. Through its memory refinement module (MRM), DMOT selectively enhances relevant object features while suppressing background noise, resulting in stable and temporally coherent segmentation results. Extensive experiments on low-light VOS benchmarks demonstrate that EVOLVE achieves state-of-the-art segmentation performance, surpassing both event-based and image-based VOS methods in accuracy and computational efficiency."
status: "auto-generated; brief scan note"
---
## Core Problem

Video Object Segmentation (VOS) in low-light scenarios remains highly challenging due to
significant texture loss and severe noise, which often lead to unreliable image feature
generation and degraded segmentation performance.

## Core Method

To address this issue, we propose EVOLVE, a novel event-guided deformable feature transfer
and dual-memory refinement framework for low-light VOS.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event features; event-based memory; event-guided low-light VOS。自动分类理由：Official
abstract confirms event features and event-based memory for low-light video object
segmentation; no clear SNN evidence.。
