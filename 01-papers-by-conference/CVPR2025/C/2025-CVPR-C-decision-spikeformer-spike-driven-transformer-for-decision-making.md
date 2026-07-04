---
title: "Decision SpikeFormer: Spike-Driven Transformer for Decision Making"
authors: ["Wei Huang", "Qinying Gu", "Nanyang Ye"]
conference: "CVPR"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_Decision_SpikeFormer_Spike-Driven_Transformer_for_Decision_Making_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Huang_Decision_SpikeFormer_Spike-Driven_Transformer_for_Decision_Making_CVPR_2025_paper.html"
tags: []
abstract: "Offline reinforcement learning (RL) enables policy training solely on pre-collected data, avoiding direct environment interaction--a crucial benefit for energy-constrained embodied AI applications. Although Artificial Neural Networks (ANN)-based methods perform well in offline RL, their high computational and energy demands motivate exploration of more efficient alternatives. Spiking Neural Networks (SNNs) show promise for such tasks, given their low power consumption. In this work, we introduce DSFormer, the first spike-driven transformer model designed to tackle offline RL via sequence modeling. Unlike existing SNN transformers focused on spatial dimensions for vision tasks, we develop Temporal Spiking Self-Attention (TSSA) and Positional Spiking Self-Attention (PSSA) in DSFormer to capture the temporal and positional dependencies essential for sequence modeling in RL. Additionally, we propose Progressive Threshold-dependent Batch Normalization (PTBN), which combines the benefits of LayerNorm and BatchNorm to preserve temporal dependencies while maintaining the spiking nature of SNNs. Comprehensive results in the D4RL benchmark show DSFormer's superiority over both SNN and ANN counterparts, achieving 78.4% energy savings, highlighting DSFormer's advantages not only in energy efficiency but also in competitive performance. Code and models are public at \\href https://wei-nijuan.github.io/DecisionSpikeFormer/ project page ."
status: "auto-generated; brief scan note"
---
## Core Problem

Offline reinforcement learning (RL) enables policy training solely on pre-collected data,
avoiding direct environment interaction--a crucial benefit for energy-constrained embodied
AI applications.

## Core Method

Although Artificial Neural Networks (ANN)-based methods perform well in offline RL, their
high computational and energy demands motivate exploration of more efficient alternatives.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spike。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence found.。 备注：CVPR 2025 official CVF page
inspected under broad high-recall title workflow.。
