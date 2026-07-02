---
title: "BSO: Binary Spiking Online Optimization Algorithm"
authors: ["Yu Liang, Yu Yang, Wenjie Wei, Ammar Belatreche, Shuai Wang, Malu Zhang, Yang Yang"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/liang25r/liang25r.pdf"
official_page: "https://proceedings.mlr.press/v267/liang25r.html"
tags: []
abstract: "Binary Spiking Neural Networks (BSNNs) offer promising efficiency advantages for resource-constrained computing. However, their training algorithms often require substantial memory overhead due to latent weights storage and temporal processing requirements. To address this issue, we propose Binary Spiking Online (BSO) optimization algorithm, a novel online training algorithm that significantly reduces training memory. BSO directly updates weights through flip signals under the online training framework. These signals are triggered when the product of gradient momentum and weights exceeds a threshold, eliminating the need for latent weights during training. To enhance performance, we propose T-BSO, a temporal-aware variant that leverages the inherent temporal dynamics of BSNNs by capturing gradient information across time steps for adaptive threshold adjustment. Theoretical analysis establishes convergence guarantees for both BSO and T-BSO, with formal regret bounds characterizing their convergence rates. Extensive experiments demonstrate that both BSO and T-BSO achieve superior optimization performance compared to existing training methods for BSNNs. The codes are available at https://github.com/hamingsi/BSO."
status: "auto-generated; brief scan note"
---

## Core Problem

Binary Spiking Neural Networks (BSNNs) offer promising efficiency advantages for resource-constrained computing.

## Core Method

However, their training algorithms often require substantial memory overhead due to latent weights storage and temporal processing requirements.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
