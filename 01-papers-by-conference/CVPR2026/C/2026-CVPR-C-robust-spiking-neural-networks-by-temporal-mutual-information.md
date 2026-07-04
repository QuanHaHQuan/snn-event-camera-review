---
title: "Robust Spiking Neural Networks by Temporal Mutual Information"
authors: ["Mengting Xu", "Shi Gu", "Peng Lin", "De Ma", "Huajin Tang", "Qian Zheng", "Gang Pan"]
conference: "CVPR"
year: 2026
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Robust_Spiking_Neural_Networks_by_Temporal_Mutual_Information_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Robust_Spiking_Neural_Networks_by_Temporal_Mutual_Information_CVPR_2026_paper.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) have attracted increasing attention for their biologically inspired temporal dynamics. As their applications expand, understanding their robustness has become an important research focus. However, little is known about how the intrinsic temporal properties of SNNs affect robustness. In this work, we revisit SNN robustness from an information-theoretic perspective and reveal the pivotal role of temporal dynamics. We establish a theoretical link between robustness error and the mutual information (MI) between inputs and latent representations along the temporal dimension, grounded in the information bottleneck principle. Through an analysis of spike-based information transmission, we show that temporal dynamics inherently compress MI, thereby tightening the robustness error bound. Building on this insight, we propose a Temporal Mutual Information (TMI) regularizer that explicitly exploits temporal characteristics to enhance robustness. Extensive experiments on CIFAR-10, CIFAR-100, DVS-CIFAR10, Tiny-ImageNet, and ImageNet demonstrate that our method consistently improves SNN robustness across various architectures and attack settings."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks (SNNs) have attracted increasing attention for their biologically inspired temporal dynamics.

## Core Method

As their applications expand, understanding their robustness has become an important research focus.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `dvs; dvs visual-event context; spiking neural networks; snns`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
