---
title: "Synergy Between the Strong and the Weak: Spiking Neural Networks are Inherently Self-Distillers"
authors: ["Yongqi Ding, Lin Zuo, Mengmeng Jing, Kunshan Yang, Pei He, Tonglan Xie"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/a1a923ac3eb5c02b34423a0b343a24cb-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/a1a923ac3eb5c02b34423a0b343a24cb-Abstract-Conference.html"
tags: []
abstract: "Brain-inspired spiking neural networks (SNNs) promise to be a low-power alternative to computationally intensive artificial neural networks (ANNs), although performance gaps persist. Recent studies have improved the performance of SNNs through knowledge distillation, but rely on large teacher models or introduce additional training overhead. In this paper, we show that SNNs can be naturally deconstructed into multiple submodels for efficient self-distillation. We treat each timestep instance of the SNN as a submodel and evaluate its output confidence, thus efficiently identifying the strong and the weak. Based on this strong and weak relationship, we propose two efficient self-distillation schemes: (1) Strong2Weak: During training, the stronger \"teacher\" guides the weaker \"student\", effectively improving overall performance. (2) Weak2Strong: The weak serve as the \"teacher\", distilling the strong in reverse with underlying dark knowledge, again yielding significant performance gains. For both distillation schemes, we offer flexible implementations such as ensemble, simultaneous, and cascade distillation. Experiments show that our method effectively improves the discriminability and overall performance of the SNN, while its adversarial robustness is also enhanced, benefiting from the stability brought by self-distillation. This ingeniously exploits the temporal properties of SNNs and provides insight into how to efficiently train high-performance SNNs."
status: "auto-generated; brief scan note"
---

## Core Problem

Brain-inspired spiking neural networks (SNNs) promise to be a low-power alternative to computationally intensive artificial neural networks (ANNs), although performance gaps persist.

## Core Method

Recent studies have improved the performance of SNNs through knowledge distillation, but rely on large teacher models or introduce additional training overhead.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
