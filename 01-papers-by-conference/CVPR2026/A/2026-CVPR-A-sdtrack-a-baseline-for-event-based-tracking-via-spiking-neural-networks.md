---
title: "SDTrack: A Baseline for Event-based Tracking via Spiking Neural Networks"
authors: ["Yimeng Shan", "Zhenbang Ren", "Haodi Wu", "Wenjie Wei", "Rui-Jie Zhu", "Shuai Wang", "Dehao Zhang", "Yichen Xiao", "Jieyuan Zhang", "Kexin Shi", "Jingzhinan Wang", "Jason K. Eshraghian", "Haicheng Qu", "Malu Zhang"]
conference: "CVPR"
year: 2026
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Shan_SDTrack_A_Baseline_for_Event-based_Tracking_via_Spiking_Neural_Networks_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Shan_SDTrack_A_Baseline_for_Event-based_Tracking_via_Spiking_Neural_Networks_CVPR_2026_paper.html"
tags: []
abstract: "Event cameras provide superior temporal resolution, dynamic range, energy efficiency, and pixel bandwidth. Spiking Neural Networks (SNNs) naturally complement event data through discrete spike signals, making them ideal for event-based tracking. However, current approaches combining Artificial Neural Networks (ANNs) and SNNs suffer from suboptimal architectures that compromise energy efficiency and limit tracking performance. To address these limitations, we propose the first Transformer-based Spike-Driven Tracking (SDTrack) pipeline. It incorporates a novel event frame aggregation method called Global Trajectory Prompt (GTP) and a Transformer-based tracker. The GTP method effectively captures global trajectory information and aggregates it with event streams into event frames to enhance spatiotemporal representation. The Transformer-based tracker comprises a fully spike-driven SNN backbone and a simple tracking head. The SDTrack pipeline operates end-to-end without data augmentation or post-processing. Extensive experiments demonstrate that our SDTrack-Tiny pipeline achieves competitive accuracy with only 19.61M parameters and 8.16mJ energy consumption, while our Base version achieves state-of-the-art accuracy across three datasets. Our work establishes a solid foundation for future neuromorphic vision research."
status: "auto-generated; needs human review"
---

## Core Problem

事件相机跟踪需要兼顾高时间分辨率与能效，但现有 ANN/SNN 混合方案架构并不理想。

## Core Method

提出 Transformer-based Spike-Driven Tracking (SDTrack)，并用 GTP 事件帧聚合与跟踪器协同建模。

## Key Metrics and Findings

摘要声称该基线在性能和能效上都优于现有方案。

## Personal Notes

这是事件相机与 SNN 交叉方向的另一篇核心候选。

## Method Details

GTP 用于事件帧聚合，Transformer tracker 用于表征时序轨迹。

## Experimental Analysis

需要核对跟踪基准、能耗度量和对照模型。

## Related Work Connections

可与 SpikeTrack 组成 A 类核心跟踪组。

## Survey-Usable Points

适合放在事件相机 + SNN 跟踪章节的主线。

