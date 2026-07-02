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

Spiking Neural Networks (SNNs) are considered to have enormous potential in the future development of Artificial Intelligence due to their brain-inspired and energy-efficient properties.

## Core Method

Compared to vanilla Spatial-Temporal Back-propagation (STBP) training methods, online training can effectively avoid the risk of GPU memory explosion.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns; leaky integrate-and-fire; integrate-and-fire; lif; surrogate gradients`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
