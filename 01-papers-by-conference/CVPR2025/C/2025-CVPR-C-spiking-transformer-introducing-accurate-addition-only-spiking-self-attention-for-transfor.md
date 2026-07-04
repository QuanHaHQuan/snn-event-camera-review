---
title: "Spiking Transformer: Introducing Accurate Addition-Only Spiking Self-Attention for Transformer"
authors: ["Yufei Guo", "Xiaode Liu", "Yuanpei Chen", "Weihang Peng", "Yuhan Zhang", "Zhe Ma"]
conference: "CVPR"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Guo_Spiking_Transformer_Introducing_Accurate_Addition-Only_Spiking_Self-Attention_for_Transformer_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Guo_Spiking_Transformer_Introducing_Accurate_Addition-Only_Spiking_Self-Attention_for_Transformer_CVPR_2025_paper.html"
tags: []
abstract: "Transformers have demonstrated outstanding performance across a wide range of tasks, owing to their self-attention mechanism, but they are highly energy-consuming. Spiking Neural Networks have emerged as a promising energy-efficient alternative to traditional Artificial Neural Networks, leveraging event-driven computation and binary spikes for information transfer. The combination of Transformers' capabilities with the energy efficiency of SNNs offers a compelling opportunity. This paper addresses the challenge of adapting the self-attention mechanism of Transformers to the spiking paradigm by introducing a novel approach: Accurate Addition-Only Spiking Self-Attention (A^2OS^2A). Unlike existing methods that rely solely on binary spiking neurons for all components of the self-attention mechanism, our approach integrates binary, ReLU, and ternary spiking neurons. This hybrid strategy significantly improves accuracy while preserving non-multiplicative computations. Moreover, our method eliminates the need for softmax and scaling operations. Extensive experiments show that the A^2OS^2A-based Spiking Transformer outperforms existing SNN-based Transformers on several datasets, even achieving an accuracy of 78.66% on ImageNet-1K. Our work represents a significant advancement in SNN-based Transformer models, offering a more accurate and efficient solution for real-world applications."
status: "auto-generated; brief scan note"
---
## Core Problem

Transformers have demonstrated outstanding performance across a wide range of tasks, owing
to their self-attention mechanism, but they are highly energy-consuming.

## Core Method

Spiking Neural Networks have emerged as a promising energy-efficient alternative to
traditional Artificial Neural Networks, leveraging event-driven computation and binary
spikes for information transfer.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking transformer; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：CVPR 2025
official CVF page inspected under broad high-recall title workflow.。
