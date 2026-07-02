---
title: "Temporal Interaction in Spiking Transformers with Multi-Delay Mixer"
authors: ["Kexin Shi", "Hanwen Liu", "Zeyang Song", "Yang Liu", "Jieyuan Zhang", "Shuai Wang", "Jibin Wu", "Malu Zhang", "Yang Yang"]
conference: "CVPR"
year: 2026
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_Temporal_Interaction_in_Spiking_Transformers_with_Multi-Delay_Mixer_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Temporal_Interaction_in_Spiking_Transformers_with_Multi-Delay_Mixer_CVPR_2026_paper.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) have gained significant attention due to their event-driven computational paradigm, making them promising for neuromorphic computing. In recent years, the integration of SNNs and Transformer architectures has made remarkable progress in various tasks. However, existing spiking self-attention mechanisms predominantly focus on spatial information while neglecting explicit temporal modeling, leading to suboptimal performance. In this paper, we introduce the Temporal Interaction Coefficient (TIC) to analyze temporal dependency patterns in these spatial-only attention mechanisms, revealing their limited temporal interactions and restricted pattern diversity. To overcome this issue, we propose the Multi-Delay Mixer (MD-Mixer), drawing inspiration from time delay mechanisms in the nervous system. Specifically, MD-Mixer introduces multiple temporal delays to perform effective time mixing and facilitate temporally enriched spatial attention. In addition, it can be integrated seamlessly into existing Spiking Transformers as a drop-in replacement while maintaining computational efficiency. Extensive evaluations on static and neuromorphic benchmarks demonstrate that MD-Mixer substantially improves the performance of Spiking Transformers, outperforming existing state-of-the-art (SOTA) methods. This work establishes MD-Mixer as an effective and general solution for temporal modeling in event-driven architectures."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks (SNNs) have gained significant attention due to their event-driven computational paradigm, making them promising for neuromorphic computing.

## Core Method

In recent years, the integration of SNNs and Transformer architectures has made remarkable progress in various tasks.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns; spiking transformers`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
