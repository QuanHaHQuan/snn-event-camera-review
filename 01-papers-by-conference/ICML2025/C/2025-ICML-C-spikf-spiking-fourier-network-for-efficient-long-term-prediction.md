---
title: "SpikF: Spiking Fourier Network for Efficient Long-term Prediction"
authors: ["Wenjie Wu, Dexuan Huo, Hong Chen"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25m/wu25m.pdf"
official_page: "https://proceedings.mlr.press/v267/wu25m.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) have demonstrated remarkable potential across many domains, including computer vision and natural language processing, owing to their energy efficiency and biological plausibility. However, their application in long-term prediction tasks remains underexplored, which is primarily due to two critical challenges: (1) current SNN encoding methods are unable to effectively encode long temporal information, leading to increased computational complexity and energy consumption; (2) though Transformer-based models have achieved state-of-the-art accuracy in temporal prediction tasks, the absence of proper positional encoding for spiking self-attention restricts Spiking Transformer from effectively utilizing positional information, resulting in performance degradation. To address these challenges, we introduce an attention-free framework, Spik ing F ourier Network ( SpikF ), that encodes input sequences in patches and employs an innovative frequency domain selection mechanism to effectively utilize the sequential properties of time-series data. Extensive evaluations on eight well-established long-term prediction datasets demonstrate that SpikF achieves an averaged $1.9\\%$ reduction in Mean Absolute Error (MAE) compared to state-of-the-art models, while lowering total energy consumption by $3.16\\times$. Our code is available at https://github.com/WWJ-creator/SpikF."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks (SNNs) have demonstrated remarkable potential across many domains, including computer vision and natural language processing, owing to their energy efficiency and biological plausibility.

## Core Method

However, their application in long-term prediction tasks remains underexplored, which is primarily due to two critical challenges: (1) current SNN encoding methods are unable to effectively encode long temporal information, leading to increased computational complexity and energy consumption; (2) though Transformer-based models have achieved state-of-the-art accuracy in temporal prediction tasks, the absence of proper positional encoding for spiking self-attention restricts Spiking Transformer from effectively utilizing positional information, resulting in performance degradation.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns; spiking transformers`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
