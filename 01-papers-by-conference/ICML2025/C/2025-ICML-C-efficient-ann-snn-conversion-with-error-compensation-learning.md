---
title: "Efficient ANN-SNN Conversion with Error Compensation Learning"
authors: ["Chang Liu, Jiangrong Shen, Xuming Ran, Mingkun Xu, Qi Xu, Yi Xu, Gang Pan"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bl/liu25bl.pdf"
official_page: "https://proceedings.mlr.press/v267/liu25bl.html"
tags: []
abstract: "Artificial neural networks (ANNs) have demonstrated outstanding performance in numerous tasks, but deployment in resource-constrained environments remains a challenge due to their high computational and memory requirements. Spiking neural networks (SNNs) operate through discrete spike events and offer superior energy efficiency, providing a bio-inspired alternative. However, current ANN-to-SNN conversion often results in significant accuracy loss and increased inference time due to conversion errors such as clipping, quantization, and uneven activation. This paper proposes a novel ANN-to-SNN conversion framework based on error compensation learning. We introduce a learnable threshold clipping function, dual-threshold neurons, and an optimized membrane potential initialization strategy to mitigate the conversion error. Together, these techniques address the clipping error through adaptive thresholds, dynamically reduce the quantization error through dual-threshold neurons, and minimize the non-uniformity error by effectively managing the membrane potential. Experimental results on CIFAR-10, CIFAR-100, ImageNet datasets show that our method achieves high-precision and ultra-low latency among existing conversion methods. Using only two time steps, our method significantly reduces the inference time while maintains competitive accuracy of 94.75% on CIFAR-10 dataset under ResNet-18 structure. This research promotes the practical application of SNNs on low-power hardware, making efficient real-time processing possible."
status: "auto-generated; brief scan note"
---

## Core Problem

Artificial neural networks (ANNs) have demonstrated outstanding performance in numerous tasks, but deployment in resource-constrained environments remains a challenge due to their high computational and memory requirements.

## Core Method

Spiking neural networks (SNNs) operate through discrete spike events and offer superior energy efficiency, providing a bio-inspired alternative.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns; ann-to-snn`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
