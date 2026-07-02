---
title: "Efficient Training of Spiking Neural Networks with Multi-Parallel Implicit Stream Architecture"
authors: ["Zhigao Cao", "Meng Li", "Xiashuang Wang", "Haoyu Wang", "Fan Wang", "Youjun Li", "Zigang Huang"]
conference: "ECCV"
year: 2024
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05068.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1548"
tags: []
abstract: "Spiking neural networks (SNNs) are a novel type of bio-plausible neural network with energy efficiency. However, SNNs are non-differentiable and the training memory costs increase with the number of simulation steps. To address these challenges, this work introduces an implicit training method for SNNs inspired by equilibrium models. Our method relies on the multi-parallel implicit stream architecture (MPIS-SNNs). In the forward process, MPIS-SNNs drive multiple fused parallel implicit streams (ISs) to reach equilibrium state simultaneously. In the backward process, MPIS-SNNs solely rely on a single-time-step simulation of SNNs, avoiding the storage of a large number of activations. Extensive experiments on N-MNIST, Fashion-MNIST, CIFAR-10, and CIFAR-100 demonstrate that MPIS-SNNs exhibit excellent characteristics such as low latency, low memory cost, low firing rates, and fast convergence speed, and are competitive among latest efficient training methods for SNNs. Our code is available at an anonymized GitHub repository: https://anonymous.4open.science/r/MPIS-SNNs-3D32."
status: "auto-generated; needs human review"
---

## Core Problem

Spiking neural networks (SNNs) are a novel type of bio-plausible neural network with energy efficiency.

## Core Method

However, SNNs are non-differentiable and the training memory costs increase with the number of simulation steps.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `n-mnist; spiking neural networks; snns`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
