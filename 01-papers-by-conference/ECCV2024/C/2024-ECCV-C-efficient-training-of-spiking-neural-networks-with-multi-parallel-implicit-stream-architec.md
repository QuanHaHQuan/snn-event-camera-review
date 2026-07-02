---
title: "Efficient Training of Spiking Neural Networks with Multi-Parallel Implicit Stream Architecture"
authors: ["Zhigao Cao", "Meng Li", "Xiashuang Wang", "Haoyu Wang", "Fan Wang", "Youjun Li", "Zigang Huang"]
conference: "ECCV"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05068.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1548"
tags: []
abstract: "Spiking neural networks (SNNs) are a novel type of bio-plausible neural network with energy efficiency. However, SNNs are non-differentiable and the training memory costs increase with the number of simulation steps. To address these challenges, this work introduces an implicit training method for SNNs inspired by equilibrium models. Our method relies on the multi-parallel implicit stream architecture (MPIS-SNNs). In the forward process, MPIS-SNNs drive multiple fused parallel implicit streams (ISs) to reach equilibrium state simultaneously. In the backward process, MPIS-SNNs solely rely on a single-time-step simulation of SNNs, avoiding the storage of a large number of activations. Extensive experiments on N-MNIST, Fashion-MNIST, CIFAR-10, and CIFAR-100 demonstrate that MPIS-SNNs exhibit excellent characteristics such as low latency, low memory cost, low firing rates, and fast convergence speed, and are competitive among latest efficient training methods for SNNs. Our code is available at an anonymized GitHub repository: https://anonymous.4open.science/r/MPIS-SNNs-3D32."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking neural networks (SNNs) are a novel type of bio-plausible neural network with energy
efficiency.

## Core Method

However, SNNs are non-differentiable and the training memory costs increase with the number
of simulation steps.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks。自动分类理由：Official abstract confirms efficient SNN training; no
clear event-camera/DVS evidence.。
