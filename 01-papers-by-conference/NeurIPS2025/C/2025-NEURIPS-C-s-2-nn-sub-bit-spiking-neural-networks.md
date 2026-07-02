---
title: "S$^2$NN: Sub-bit Spiking Neural Networks"
authors: ["Wenjie Wei, Malu Zhang, Jieyuan Zhang, Ammar Belatreche, Shuai Wang, Yimeng Shan, Hanwen Liu, Honglin Cao, Guoqing Wang, Yang Yang, Haizhou Li"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/40cba0984b4a2fa3b9f3e1231572e128-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/40cba0984b4a2fa3b9f3e1231572e128-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) offer an energy-efficient paradigm for machine intelligence, but their continued scaling poses challenges for resource-limited deployment. Despite recent advances in binary SNNs, the storage and computational demands remain substantial for large-scale networks. To further explore the compression and acceleration potential of SNNs, we propose Sub-bit Spiking Neural Networks (S$^2$NNs) that represent weights with less than one bit. Specifically, we first establish an S$^2$NN baseline by leveraging the clustering patterns of kernels in well-trained binary SNNs. This baseline is highly efficient but suffers from \\textit{outlier-induced codeword selection bias} during training. To mitigate this issue, we propose an \\textit{outlier-aware sub-bit weight quantization} (OS-Quant) method, which optimizes codeword selection by identifying and adaptively scaling outliers. Furthermore, we propose a \\textit{membrane potential-based feature distillation} (MPFD) method, improving the performance of highly compressed S$^2$NN via more precise guidance from a teacher model. Extensive results on vision reveal that S$^2$NN outperforms existing quantized SNNs in both performance and efficiency, making it promising for edge computing applications."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks (SNNs) offer an energy-efficient paradigm for machine intelligence, but their continued scaling poses challenges for resource-limited deployment.

## Core Method

Despite recent advances in binary SNNs, the storage and computational demands remain substantial for large-scale networks.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
