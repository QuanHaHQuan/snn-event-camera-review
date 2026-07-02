---
title: "Adaptive Fission: Post-training Encoding for Low-latency Spike Neural Networks"
authors: ["Yizhou Jiang, Feng Chen, Yihan Li, Yuqian Liu, Haichuan Gao, Tianren Zhang, Ying Fang"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/e2e0a9004132490db1be58bffa419268-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/e2e0a9004132490db1be58bffa419268-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) often rely on rate coding, where high-precision inference depends on long time-steps, leading to significant latency and energy cost—especially for ANN-to-SNN conversions. To address this, we propose Adaptive Fission, a post-training encoding technique that selectively splits high-sensitivity neurons into groups with varying scales and weights. This enables neuron-specific, on-demand precision and threshold allocation while introducing minimal spatial overhead. As a generalized form of population coding, it seamlessly applies to a wide range of pretrained SNN architectures without requiring additional training or fine-tuning. Experiments on neuromorphic hardware demonstrate up to 80\\% reductions in latency and power consumption without degrading accuracy."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs) often rely on rate coding, where high-precision inference
depends on long time-steps, leading to significant latency and energy cost—especially for
ANN-to-SNN conversions.

## Core Method

To address this, we propose Adaptive Fission, a post-training encoding technique that
selectively splits high-sensitivity neurons into groups with varying scales and weights.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNN/spiking neural computation。自动分类理由：Official abstract confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence.。 备注：Track: Main Conference Track. Official
abstract/page inspected under broad high-recall title workflow.。
