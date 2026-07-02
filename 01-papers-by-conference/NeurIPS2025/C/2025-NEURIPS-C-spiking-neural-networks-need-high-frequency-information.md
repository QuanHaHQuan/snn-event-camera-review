---
title: "Spiking Neural Networks Need High-Frequency Information"
authors: ["Yuetong Fang, Deming Zhou, Ziqing Wang, Hongwei Ren, zeng zecui, Lusong Li, shibo zhou, Renjing Xu"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/956834836f36dd07df7064ff42ca69f2-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/956834836f36dd07df7064ff42ca69f2-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks promise brain-inspired and energy-efficient computation by transmitting information through binary (0/1) spikes. Yet, their performance still lags behind that of artificial neural networks, often assumed to result from information loss caused by sparse and binary activations. In this work, we challenge this long-standing assumption and reveal a previously overlooked frequency bias: spiking neurons inherently suppress high-frequency components and preferentially propagate low-frequency information. This frequency-domain imbalance, we argue, is the root cause of degraded feature representation in SNNs. Empirically, on Spiking Transformers, adopting Avg-Pooling (low-pass) for token mixing lowers performance to 76.73% on Cifar-100, whereas replacing it with Max-Pool (high-pass) pushes the top-1 accuracy to 79.12%. Accordingly, we introduce Max-Former that restores high-frequency signals through two frequency-enhancing operators: (1) extra Max-Pool in patch embedding, and (2) Depth-Wise Convolution in place of self-attention. Notably, Max-Former attains 82.39% top-1 accuracy on ImageNet using only 63.99M parameters, surpassing Spikformer (74.81%, 66.34M) by +7.58%. Extending our insight beyond transformers, our Max-ResNet-18 achieves state-of-the-art performance on convolution-based benchmarks: 97.17% on CIFAR-10 and 83.06% on CIFAR-100. We hope this simple yet effective solution inspires future research to explore the distinctive nature of spiking neural networks. Code is available: https://github.com/bic-L/MaxFormer."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks promise brain-inspired and energy-efficient computation by transmitting information through binary (0/1) spikes.

## Core Method

Yet, their performance still lags behind that of artificial neural networks, often assumed to result from information loss caused by sparse and binary activations.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns; spiking neurons; spiking transformers`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
