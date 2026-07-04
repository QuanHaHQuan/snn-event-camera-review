---
title: "STAA-SNN: Spatial-Temporal Attention Aggregator for Spiking Neural Networks"
authors: ["Tianqing Zhang", "Kairong Yu", "Xian Zhong", "Hongwei Wang", "Qi Xu", "Qiang Zhang"]
conference: "CVPR"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_STAA-SNN_Spatial-Temporal_Attention_Aggregator_for_Spiking_Neural_Networks_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_STAA-SNN_Spatial-Temporal_Attention_Aggregator_for_Spiking_Neural_Networks_CVPR_2025_paper.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) have gained significant attention due to their biological plausibility and energy efficiency, making them promising alternatives to Artificial Neural Networks (ANNs). However, the performance gap between SNNs and ANNs remains a substantial challenge hindering the widespread adoption of SNNs. In this paper, we propose a Spatial-Temporal Attention Aggregator SNN (STAA-SNN) framework, which dynamically focuses on and captures both spatial and temporal dependencies. First, we introduce a spike-driven self-attention mechanism specifically designed for SNNs. Additionally, we pioneeringly incorporate position encoding to integrate latent temporal relationships into the incoming features. For spatial-temporal information aggregation, we employ step attention to selectively amplify relevant features to variant steps. Finally, we implement a time-step random dropout strategy to avoid local optima. The framework demonstrates exceptional performance across diverse datasets and exhibits strong generalization capabilities. Notably, STAA-SNN achieves state-of-the-art results on neuromorphic datasets CIFAR10-DVS of 82.10% and with performances of 97.14%, 82.05% and 70.40% on the static datasets CIFAR-10, CIFAR-100 and ImageNet, respectively. Furthermore, this model exhibits improved performance ranging from 0.33% to 2.80% with fewer time steps."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs) have gained significant attention due to their biological
plausibility and energy efficiency, making them promising alternatives to Artificial Neural
Networks (ANNs).

## Core Method

However, the performance gap between SNNs and ANNs remains a substantial challenge hindering
the widespread adoption of SNNs.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; SNN; spiking。自动分类理由：Manual boundary check: generic SNN
framework; event-camera evidence is mainly neuromorphic benchmark usage, not an event-
camera-specific method.。 备注：CVPR 2025 official CVF page inspected under broad high-recall
title workflow.。
