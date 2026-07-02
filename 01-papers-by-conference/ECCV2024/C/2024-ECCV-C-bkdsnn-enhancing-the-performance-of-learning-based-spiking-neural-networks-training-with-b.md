---
title: "BKDSNN: Enhancing the Performance of Learning-based Spiking Neural Networks Training with Blurred Knowledge Distillation"
authors: ["Zekai Xu", "Kang You", "Qinghai Guo", "Xiang Wang", "Zhezhi He"]
conference: "ECCV"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06649.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/2655"
tags: []
abstract: "Spiking neural networks (SNNs), which mimic biological neural system to convey information via discrete spikes, are well known as brain-inspired models with excellent computing efficiency. By utilizing the surrogate gradient estimation for discrete spikes, learning-based SNN training methods that can achieve ultra-low inference latency (number of time-step) emerge recently. Nevertheless, due to the difficulty in deriving precise gradient estimation for discrete spikes using learning-based method, a distinct accuracy gap persists between SNN and its artificial neural networks (ANNs) counterpart. To address the aforementioned issue, we propose a blurred knowledge distillation (BKD) technique, which leverages random blurred SNN feature to restore and imitate the ANN feature. Note that, our BKD is applied upon the feature map right before the last layer of SNN, which can also mix with prior logits-based knowledge distillation for maximized accuracy boost. To our best knowledge, in the category of learning-based methods, our work achieves state-of-the-art performance for training SNNs on both static and neuromorphic datasets. On ImageNet dataset, BKDSNN outperforms prior best results by 4.51% and 0.93% with the network topology of CNN and Transformer respectively."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking neural networks (SNNs), which mimic biological neural system to convey information
via discrete spikes, are well known as brain-inspired models with excellent computing
efficiency.

## Core Method

By utilizing the surrogate gradient estimation for discrete spikes, learning-based SNN
training methods that can achieve ultra-low inference latency (number of time-step) emerge
recently.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks。自动分类理由：Official abstract confirms SNN training with
surrogate gradients/knowledge distillation; no clear event-camera/DVS evidence.。
