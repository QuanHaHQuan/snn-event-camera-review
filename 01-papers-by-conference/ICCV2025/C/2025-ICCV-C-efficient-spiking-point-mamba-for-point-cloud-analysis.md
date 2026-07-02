---
title: "Efficient Spiking Point Mamba for Point Cloud Analysis"
authors: ["Peixi Wu", "Bosong Chai", "Menghua Zheng", "Wei Li", "Zhangchi Hu", "Jie Chen", "Zheyu Zhang", "Hebei Li", "Xiaoyan Sun"]
conference: "ICCV"
year: 2025
level: "C"
category: "SNN"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Wu_Efficient_Spiking_Point_Mamba_for_Point_Cloud_Analysis_ICCV_2025_paper.html"
tags: []
abstract: "Bio-inspired Spiking Neural Networks (SNNs) provide an energy-efficient way to extract 3D spatio-temporal features. However, existing 3D SNNs have struggled with long-range dependencies until the recent emergence of Mamba, which offers superior computational efficiency and sequence modeling capability. In this work, we propose Spiking Point Mamba (SPM), the first Mamba-based SNN in the 3D domain. Naively adapting Mamba to 3D SNNs, though, is hindered by temporal dynamics mismatch and spike-induced information loss. Thus, we first introduce Hierarchical Dynamic Encoding (HDE), an improved direct encoding method that effectively introduces dynamic temporal mechanism. Then, we propose Spiking Mamba Block (SMB), which builds upon Mamba while learning inter-time-step features and minimizing information loss caused by spikes. Finally, to further boost performance, we adopt an asymmetric SNN-ANN architecture for spike-based pre-training and finetune. Compared with the previous state-of-the-art SNN models, SPM improves overall accuracy by +6.2%, +6.1%, and +7.4% on three variants of ScanObjectNN, and boosts instance mIOU by +1.9% on ShapeNetPart. Meanwhile, its energy consumption is at most 12.6x lower than that of its ANN counterpart. Code: https://github.com/PeppaWu/SPM."
status: "auto-generated; brief scan note"
---

## Core Problem

Bio-inspired Spiking Neural Networks (SNNs) provide an energy-efficient way to extract 3D spatio-temporal features.

## Core Method

However, existing 3D SNNs have struggled with long-range dependencies until the recent emergence of Mamba, which offers superior computational efficiency and sequence modeling capability.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
