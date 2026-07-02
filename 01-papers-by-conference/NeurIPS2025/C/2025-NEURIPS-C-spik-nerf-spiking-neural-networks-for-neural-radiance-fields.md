---
title: "Spik-NeRF: Spiking Neural Networks for Neural Radiance Fields"
authors: ["Gang Wan, Qinlong Lan, Zihan Li, Huimin Wang, Wu Yitian, wang zhen, Wanhua Li, Yufei Guo"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/43a69d143273bd8215578bde887bb552-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/43a69d143273bd8215578bde887bb552-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks (SNNs), as a biologically inspired neural network architecture, have garnered significant attention due to their exceptional energy efficiency and increasing potential for various applications. In this work, we extend the use of SNNs to neural rendering tasks and introduce Spik-NeRF (Spiking Neural Radiance Fields). We observe that the binary spike activation map of traditional SNNs lacks sufficient information capacity, leading to information loss and a subsequent decline in the performance of spiking neural rendering models. To address this limitation, we propose the use of ternary spike neurons, which enhance the information-carrying capacity in the spiking neural rendering model. With ternary spike neurons, Spik-NeRF achieves performance that is on par with, or nearly identical to, traditional ANN-based rendering models. Additionally, we present a re-parameterization technique for inference that allows Spik-NeRF with ternary spike neurons to retain the event-driven, multiplication-free advantages typical of binary spike neurons. Furthermore, to further boost the performance of Spik-NeRF, we employ a distillation method, using an ANN-based NeRF to guide the training of our Spik-NeRF model, which is more compatible with the ternary neurons compared to the standard binary neurons. We evaluate Spik-NeRF on both realistic and synthetic scenes, and the experimental results demonstrate that Spik-NeRF achieves rendering performance comparable to ANN-based NeRF models."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks (SNNs), as a biologically inspired neural network architecture, have garnered significant attention due to their exceptional energy efficiency and increasing potential for various applications.

## Core Method

In this work, we extend the use of SNNs to neural rendering tasks and introduce Spik-NeRF (Spiking Neural Radiance Fields).

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
