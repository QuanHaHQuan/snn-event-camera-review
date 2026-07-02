---
title: "Differential Coding for Training-Free ANN-to-SNN Conversion"
authors: ["Zihan Huang", "Wei Fang", "Tong Bu", "Peng Xue", "Zecheng Hao", "Wenxuan Liu", "Yuanhong Tang", "Zhaofei Yu", "Tiejun Huang"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25i/huang25i.pdf"
official_page: "https://proceedings.mlr.press/v267/huang25i.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) exhibit significant potential due to their low energy consumption. Converting Artificial Neural Networks (ANNs) to SNNs is an efficient way to achieve high-performance SNNs. However, many conversion methods are based on rate coding, which requires numerous spikes and longer time-steps compared to directly trained SNNs, leading to increased energy consumption and latency. This article introduces differential coding for ANN-to-SNN conversion, a novel coding scheme that reduces spike counts and energy consumption by transmitting changes in rate information rather than rates directly, and explores its application across various layers. Additionally, the threshold iteration method is proposed to optimize thresholds based on activation distribution when converting Rectified Linear Units (ReLUs) to spiking neurons. Experimental results on various Convolutional Neural Networks (CNNs) and Transformers demonstrate that the proposed differential coding significantly improves accuracy while reducing energy consumption, particularly when combined with the threshold iteration method, achieving state-of-the-art performance. The source codes of the proposed method are available at https://github.com/h-z-h-cell/ANN-to-SNN-DCGS."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks (SNNs) exhibit significant potential due to their low energy consumption.

## Core Method

Converting Artificial Neural Networks (ANNs) to SNNs is an efficient way to achieve high-performance SNNs.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：snn; ann-to-snn。自动分类理由：Official abstract/page confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
