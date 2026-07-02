---
title: "Sorbet: A Neuromorphic Hardware-Compatible Transformer-Based Spiking Language Model"
authors: ["Kaiwen Tang", "Zhanglu Yan", "Weng-Fai Wong"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25l/tang25l.pdf"
official_page: "https://proceedings.mlr.press/v267/tang25l.html"
tags: []
abstract: "For reasons such as privacy, there are use cases for language models at the edge. This has given rise to small language models targeted for deployment in resource-constrained devices where energy efficiency is critical. Spiking neural networks (SNNs) offer a promising solution due to their energy efficiency, and there are already works on realizing transformer-based models on SNNs. However, key operations like softmax and layer normalization (LN) are difficult to implement on neuromorphic hardware, and many of these early works sidestepped them. To address these challenges, we introduce Sorbet, a transformer-based spiking language model that is more neuromorphic hardware-compatible. Sorbet incorporates a novel shifting-based softmax called PTsoftmax and a BitShifting-based PowerNorm (BSPN), both designed to replace the respective energy-intensive operations. By leveraging knowledge distillation and model quantization, Sorbet achieved a highly compressed binary weight model that maintains competitive performance while achieving $27.16\\times$ energy savings compared to BERT. We validate Sorbet through extensive testing on the GLUE benchmark and a series of ablation studies, demonstrating its potential as an energy-efficient solution for language model inference. Our code is publicly available at https://github.com/Kaiwen-Tang/Sorbet"
status: "auto-generated; brief scan note"
---

## Core Problem

For reasons such as privacy, there are use cases for language models at the edge.

## Core Method

This has given rise to small language models targeted for deployment in resource-constrained devices where energy efficiency is critical.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：spiking。自动分类理由：Official abstract/page confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
