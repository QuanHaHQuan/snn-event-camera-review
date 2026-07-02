---
title: "AIMDepth: Asymmetric Image-Event Mamba for Monocular Depth Estimation"
authors: ["Luoxi Jing", "Dianxi Shi", "Yushe Cao", "Yuanze Wang", "Junze Zhang", "Yuning Cui", "Mengzhu Wang"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Jing_AIMDepth_Asymmetric_Image-Event_Mamba_for_Monocular_Depth_Estimation_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Jing_AIMDepth_Asymmetric_Image-Event_Mamba_for_Monocular_Depth_Estimation_CVPR_2026_paper.html"
tags: []
abstract: "Monocular depth estimation is essential for applications such as robotics. The complementary characteristics of event and image modalities have inspired fusion-based methods for robust depth estimation. However, existing methods rely on convolutional or attention-based architectures, which either have limited capacity for long-range modeling or incur high computational cost, making them less suitable for depth estimation over long sequences. Moreover, effective image-event fusion remains challenging, since most methods directly fuse features without addressing the domain gap and representational differences between raw events and images, resulting in semantic bias and degraded performance. In this work, we propose AIMDepth, an Asymmetric Image-Event Mamba framework for monocular depth estimation, built on state space models for linear complexity and accurate prediction. To alleviate input-domain misalignment, we introduce a Spectral Cross-modal Prior Guidance (SCPG) for bidirectional prior injection at the input level. To reduce the imbalance between sparse events and dense images, we design an asymmetric modal-aware Encoder (AME) with separate encoding paths and feature-level alignment. We further develop a Modality-interactive Local Refinement (ModiLocal) to enable hierarchical interaction and fine-grained alignment. Experiments on public datasets show that AIMDepth achieves state-of-the-art performance in complex environments."
status: "auto-generated; brief scan note"
---
## Core Problem

Monocular depth estimation is essential for applications such as robotics.

## Core Method

The complementary characteristics of event and image modalities have inspired fusion-based
methods for robust depth estimation.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera data; image-event; raw events。自动分类理由：Official abstract confirms image-
event fusion with raw events for monocular depth; no clear SNN evidence.。
