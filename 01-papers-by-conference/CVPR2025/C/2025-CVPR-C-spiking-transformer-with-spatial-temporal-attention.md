---
title: "Spiking Transformer with Spatial-Temporal Attention"
authors: ["Donghyun Lee", "Yuhang Li", "Youngeun Kim", "Shiting Xiao", "Priyadarshini Panda"]
conference: "CVPR"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_Spiking_Transformer_with_Spatial-Temporal_Attention_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Spiking_Transformer_with_Spatial-Temporal_Attention_CVPR_2025_paper.html"
tags: []
abstract: "Spike-based Transformer presents a compelling and energy-efficient alternative to traditional Artificial Neural Network (ANN)-based Transformers, achieving impressive results through sparse binary computations. However, existing spike-based transformers predominantly focus on spatial attention while neglecting crucial temporal dependencies inherent in spike-based processing, leading to suboptimal feature representation and limited performance. To address this limitation, we propose Spiking Transformer with Spatial-Temporal Attention (STAtten), a simple and straightforward architecture that efficiently integrates both spatial and temporal information in the self-attention mechanism. STAtten introduces a block-wise computation strategy that processes information in spatial-temporal chunks, enabling comprehensive feature capture while maintaining the same computational complexity as previous spatial-only approaches. Our method can be seamlessly integrated into existing spike-based transformers without architectural overhaul. Extensive experiments demonstrate that STAtten significantly improves the performance of existing spike-based transformers across both static and neuromorphic datasets, including CIFAR10/100, ImageNet, CIFAR10-DVS, and N-Caltech101."
status: "auto-generated; brief scan note"
---
## Core Problem

Spike-based Transformer presents a compelling and energy-efficient alternative to
traditional Artificial Neural Network (ANN)-based Transformers, achieving impressive results
through sparse binary computations.

## Core Method

However, existing spike-based transformers predominantly focus on spatial attention while
neglecting crucial temporal dependencies inherent in spike-based processing, leading to
suboptimal feature representation and limited performance.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking transformer; spiking。自动分类理由：Manual boundary check: generic spiking
Transformer method; neuromorphic/event-camera datasets appear as benchmarks rather than an
event-camera-specific method.。 备注：CVPR 2025 official CVF page inspected under broad high-
recall title workflow.。
