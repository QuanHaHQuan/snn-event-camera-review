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

Event cameras provide superior temporal resolution, dynamic range, energy efficiency, and
pixel bandwidth.

## Core Method

Spiking Neural Networks (SNNs) naturally complement event data through discrete spike
signals, making them ideal for event-based tracking.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：event camera; event stream; event data; spiking neural network; spike-
driven。自动分类理由：Official abstract/page confirms both event-camera/DVS/event-stream evidence
and SNN/spiking neural computation.。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

However, current approaches combining Artificial Neural Networks (ANNs) and SNNs suffer from
suboptimal architectures that compromise energy efficiency and limit tracking performance.
To address these limitations, we propose the first Transformer-based Spike-Driven Tracking
(SDTrack) pipeline. It incorporates a novel event frame aggregation method called Global
Trajectory Prompt (GTP) and a Transformer-based tracker. The GTP method effectively captures
global trajectory information and aggregates it with event streams into event frames to
enhance spatiotemporal representation. The Transformer-based tracker comprises a fully
spike-driven SNN backbone and a simple tracking head. The SDTrack pipeline operates end-to-
end without data augmentation or post-processing. Extensive experiments demonstrate that our
SDTrack-Tiny pipeline achieves competitive accuracy with only 19.61M parameters and 8.16mJ
energy consumption, while our Base version achieves state-of-the-art accuracy across three
datasets. Our work establishes a solid foundation for future neuromorphic vision research.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
