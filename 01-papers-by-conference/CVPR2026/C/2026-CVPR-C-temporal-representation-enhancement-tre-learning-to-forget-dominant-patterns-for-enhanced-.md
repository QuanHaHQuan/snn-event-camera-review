---
title: "Temporal Representation Enhancement (TRE): Learning to Forget Dominant Patterns for Enhanced Temporal Spiking Features"
authors: ["Wei Liu", "Li Yang", "Yufei Wang", "Han Xiao", "Boyu Cai", "Weiming Hu"]
conference: "CVPR"
year: 2026
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Temporal_Representation_Enhancement_TRE_Learning_to_Forget_Dominant_Patterns_for_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Temporal_Representation_Enhancement_TRE_Learning_to_Forget_Dominant_Patterns_for_CVPR_2026_paper.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) naturally process visual inputs across multiple timesteps, offering rich temporal dynamics and energy-efficient computation. However, the temporally invariant supervision commonly used in training tends to reinforce the same dominant response patterns across timesteps, leading to redundant representations and limiting temporal discriminability. To overcome this limitation, we introduce Temporal Representation Enhancement(TRE), a novel learning-to-forget paradigm that encourages more diverse and complementary temporal representations. TRE identifies high-contribution semantic patterns through class-specific contribution estimation and temporal accumulation, and selectively suppresses them using a dynamic modulation strategy. By redirecting the model's attention toward alternative yet informative semantic cues, TRE promotes the learning of complementary features across timesteps. This approach not only strengthens the temporal discriminative capacity of SNNs but also enables more effective multi-timestep learning by leveraging richer semantic information. Extensive experiments on both static image datasets and dynamic neuromorphic datasets demonstrate that TRE consistently improves classification accuracy and feature diversity across different SNN backbones."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks (SNNs) naturally process visual inputs across multiple timesteps, offering rich temporal dynamics and energy-efficient computation.

## Core Method

However, the temporally invariant supervision commonly used in training tends to reinforce the same dominant response patterns across timesteps, leading to redundant representations and limiting temporal discriminability.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
