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

SNN 的鲁棒性与其时间动态之间的关系尚不清楚。

## Core Method

从信息论视角分析时间维度上的输入与潜表示互信息，并据此构建鲁棒性解释。

## Key Metrics and Findings

摘要称该方法建立了鲁棒误差与时间互信息的理论联系。

## Personal Notes

适合放在 SNN 鲁棒性与理论分析小节。

