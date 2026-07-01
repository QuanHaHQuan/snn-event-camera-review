---
title: "Rethinking SNN Online Training and Deployment: Gradient-Coherent Learning via Hybrid-Driven LIF Model"
authors: ["Zecheng Hao", "Yifan Huang", "Zijie Xu", "Wenxuan Liu", "Yuanhong Tang", "Zhaofei Yu", "Tiejun Huang"]
conference: "CVPR"
year: 2026
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Hao_Rethinking_SNN_Online_Training_and_Deployment_Gradient-Coherent_Learning_via_Hybrid-Driven_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Hao_Rethinking_SNN_Online_Training_and_Deployment_Gradient-Coherent_Learning_via_Hybrid-Driven_CVPR_2026_paper.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) are considered to have enormous potential in the future development of Artificial Intelligence due to their brain-inspired and energy-efficient properties. Compared to vanilla Spatial-Temporal Back-propagation (STBP) training methods, online training can effectively avoid the risk of GPU memory explosion. However, current online learning frameworks cannot tackle the gradient discrepancy problem between the forward and backward process, merely aiming to optimize the GPU memory, resulting in no performance advantages compared to the STBP-based models in the inference stage. To address the aforementioned challenges, we propose Hybrid-Driven Leaky Integrate-and-Fire (HD-LIF) model family for efficient online learning, which respectively adopt different spiking calculation mechanism in the upper-region and lower-region of the firing threshold. We theoretically point out that our learning framework can effectively separate temporal gradients and address the misalignment problem of surrogate gradients, as well as achieving full-stage optimization towards learning precision, memory footprint and power consumption. Experimental results have demonstrated that our scheme is enable to achieve state-of-the-art performance for multiple evaluation metrics, breaking through the traditional paradigm of SNN online training and deployment. Code is available at https://github.com/hzc1208/HD_LIF."
status: "auto-generated; brief scan note"
---

## Core Problem

在线训练虽然节省显存，但前向与反向过程的梯度不一致会让模型在部署端缺少优势。

## Core Method

提出 Gradient-Coherent Learning 与 Hybrid-Driven LIF 模型，试图协调训练与部署的梯度差异。

## Key Metrics and Findings

摘要指出其目标不是单纯优化显存，而是改善推理阶段性能。

## Personal Notes

适合放在 SNN 在线学习与部署章节。

