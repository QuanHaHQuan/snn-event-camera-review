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

现有脉冲 Transformer 的自注意力多偏重空间信息，时间建模不足。

## Core Method

提出 Multi-Delay Mixer，并用 Temporal Interaction Coefficient 分析时间依赖模式与交互强度。

## Key Metrics and Findings

摘要指出该方法改善了有限时间交互和模式多样性不足的问题。

## Personal Notes

和事件相机没有直接数据联系，但能补充 SNN 结构设计部分。

