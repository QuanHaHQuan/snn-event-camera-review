---
title: "TTFSFormer: A TTFS-based Lossless Conversion of Spiking Transformer"
authors: ["Lusen Zhao, Zihan Huang, Jianhao Ding, Zhaofei Yu"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25n/zhao25n.pdf"
official_page: "https://proceedings.mlr.press/v267/zhao25n.html"
tags: []
abstract: "ANN-to-SNN conversion has emerged as a key approach to train Spiking Neural Networks (SNNs), particularly for Transformer architectures, as it maps pre-trained ANN parameters to SNN equivalents without requiring retraining, thereby preserving ANN accuracy while eliminating training costs. Among various coding methods used in ANN-to-SNN conversion, time-to-first-spike (TTFS) coding, which allows each neuron to at most one spike, offers significantly lower energy consumption. However, while previous TTFS-based SNNs have achieved comparable performance with convolutional ANNs, the attention mechanism and nonlinear layers in Transformer architectures remains a challenge by existing SNNs with TTFS coding. This paper proposes a new neuron structure for TTFS coding that expands its representational range and enhances the capability to process nonlinear functions, along with detailed designs of nonlinear neurons for different layers in Transformer. Experimental results on different models demonstrate that our proposed method can achieve high accuracy with significantly lower energy consumption. To the best of our knowledge, this is the first work to focus on converting Transformer to SNN with TTFS coding."
status: "auto-generated; brief scan note"
---

## Core Problem

ANN-to-SNN conversion has emerged as a key approach to train Spiking Neural Networks (SNNs), particularly for Transformer architectures, as it maps pre-trained ANN parameters to SNN equivalents without requiring retraining, thereby preserving ANN accuracy while eliminating training costs.

## Core Method

Among various coding methods used in ANN-to-SNN conversion, time-to-first-spike (TTFS) coding, which allows each neuron to at most one spike, offers significantly lower energy consumption.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns; ann-to-snn; spiking transformers`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
