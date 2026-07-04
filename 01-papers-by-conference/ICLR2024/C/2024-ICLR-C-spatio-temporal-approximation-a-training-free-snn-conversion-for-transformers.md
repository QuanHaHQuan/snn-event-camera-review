---
title: "Spatio-Temporal Approximation: A Training-Free SNN Conversion for Transformers"
authors: ["Yizhou Jiang, Kunlin Hu, Tianren Zhang, Haichuan Gao, Yuqian Liu, Ying Fang, Feng Chen"]
conference: "ICLR"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/a875c5600e933e56aad7d63439b11b35-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/a875c5600e933e56aad7d63439b11b35-Abstract-Conference.html"
tags: []
abstract: "Spiking neural networks (SNNs) are energy-efficient and hold great potential for large-scale inference. Since training SNNs from scratch is costly and has limited performance, converting pretrained artificial neural networks (ANNs) to SNNs is an attractive approach that retains robust performance without additional training data and resources. However, while existing conversion methods work well on convolution networks, emerging Transformer models introduce unique mechanisms like self-attention and test-time normalization, leading to non-causal non-linear interactions unachievable by current SNNs. To address this, we approximate these operations in both temporal and spatial dimensions, thereby providing the first SNN conversion pipeline for Transformers. We propose \\textit{Universal Group Operators} to approximate non-linear operations spatially and a \\textit{Temporal-Corrective Self-Attention Layer} that approximates spike multiplications at inference through an estimation-correction approach. Our algorithm is implemented on a pretrained ViT-B/32 from CLIP, inheriting its zero-shot classification capabilities, while improving control over conversion losses. To our knowledge, this is the first direct training-free conversion of a pretrained Transformer to a purely event-driven SNN, promising for neuromorphic hardware deployment."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking neural networks (SNNs) are energy-efficient and hold great potential for large-scale
inference.

## Core Method

Since training SNNs from scratch is costly and has limited performance, converting
pretrained artificial neural networks (ANNs) to SNNs is an attractive approach that retains
robust performance without additional training data and resources.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNN。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural computation;
no clear event-camera/DVS evidence found.。 备注：strict two-stage screening; official
abstract/page inspected; main conference; needs human verification。
