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

Event cameras provide superior temporal resolution, dynamic range, energy efficiency, and pixel bandwidth.

## Core Method

Spiking Neural Networks (SNNs) naturally complement event data through discrete spike signals, making them ideal for event-based tracking.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event stream with event-camera context; event-based with event-camera context; spiking neural networks; snns; spike-driven`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
