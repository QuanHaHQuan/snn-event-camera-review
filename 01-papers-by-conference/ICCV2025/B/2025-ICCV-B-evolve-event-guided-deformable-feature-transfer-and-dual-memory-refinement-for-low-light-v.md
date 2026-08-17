---
title: "EVOLVE: Event-Guided Deformable Feature Transfer and Dual-Memory Refinement for Low-Light Video Object Segmentation"
authors: ["Jong-Hyeon Baek", "Jiwon Oh", "Yeong Jun Koh"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: ""
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Baek_EVOLVE_Event-Guided_Deformable_Feature_Transfer_and_Dual-Memory_Refinement_for_Low-Light_ICCV_2025_paper.html"
tags: []
abstract: "Video Object Segmentation (VOS) in low-light scenarios remains highly challenging due to significant texture loss and severe noise, which often lead to unreliable image feature generation and degraded segmentation performance. To address this issue, we propose EVOLVE, a novel event-guided deformable feature transfer and dual-memory refinement framework for low-light VOS. EVOLVE addresses spatial misalignment between frames and improves object representation by utilizing event-driven cues. The event-guided deformable feature transfer (EDFT) module enhances feature alignment through event-driven deformable convolutions, where offsets derived from event features enable motion-aware spatial adjustments, leading to more precise propagation of object features in reference frames. Furthermore, the dual-memory object transformer (DMOT) iteratively refines object representations by maintaining and updating both image-based and event-based memory representations. Through its memory refinement module (MRM), DMOT selectively enhances relevant object features while suppressing background noise, resulting in stable and temporally coherent segmentation results. Extensive experiments on low-light VOS benchmarks demonstrate that EVOLVE achieves state-of-the-art segmentation performance, surpassing both event-based and image-based VOS methods in accuracy and computational efficiency."
status: "official-abstract screening card"
---

## Official Abstract

Video Object Segmentation (VOS) in low-light scenarios remains highly challenging due to significant texture loss and severe noise, which often lead to unreliable image feature generation and degraded segmentation performance. To address this issue, we propose EVOLVE, a novel event-guided deformable feature transfer and dual-memory refinement framework for low-light VOS. EVOLVE addresses spatial misalignment between frames and improves object representation by utilizing event-driven cues. The event-guided deformable feature transfer (EDFT) module enhances feature alignment through event-driven deformable convolutions, where offsets derived from event features enable motion-aware spatial adjustments, leading to more precise propagation of object features in reference frames. Furthermore, the dual-memory object transformer (DMOT) iteratively refines object representations by maintaining and updating both image-based and event-based memory representations. Through its memory refinement module (MRM), DMOT selectively enhances relevant object features while suppressing background noise, resulting in stable and temporally coherent segmentation results. Extensive experiments on low-light VOS benchmarks demonstrate that EVOLVE achieves state-of-the-art segmentation performance, surpassing both event-based and image-based VOS methods in accuracy and computational efficiency.

## Survey Role

EVOLVE uses event features and event memory for low-light video object segmentation. It is a non-spiking event-guided temporal baseline and does not enter the strict intersection Core.

## Advisor Role

Event-guided memory and low-light segmentation are distant task comparators without Event Cloud, FFT, or SNN coupling.

## Verification Boundary

This card records official-title/abstract screening evidence. Verify the PDF before citing implementation details, formulas, tables, or numerical claims.
