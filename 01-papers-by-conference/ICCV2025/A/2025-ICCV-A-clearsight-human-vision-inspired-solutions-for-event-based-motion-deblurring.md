---
title: "ClearSight: Human Vision-Inspired Solutions for Event-Based Motion Deblurring"
authors: ["Xiaopeng Lin", "Yulong Huang", "Hongwei Ren", "Zunchang Liu", "Hongxiang Huang", "Yue Zhou", "Haotian Fu", "Bojun Cheng"]
conference: "ICCV"
year: 2025
level: "A"
category: "SNN + Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Lin_ClearSight_Human_Vision-Inspired_Solutions_for_Event-Based_Motion_Deblurring_ICCV_2025_paper.html"
tags: []
abstract: "Motion deblurring addresses the challenge of image blur caused by camera or scene movement. Event cameras provide motion information that is encoded in the asynchronous event streams. To efficiently leverage the temporal information of event streams, we employ Spiking Neural Networks (SNNs) for motion feature extraction and Artificial Neural Networks (ANNs) for color information processing. Due to the non-uniform distribution and inherent redundancy of event data, existing cross-modal feature fusion methods exhibit certain limitations. Inspired by the visual attention mechanism in the human visual system, this study introduces a bioinspired dual-drive hybrid network (BDHNet). Specifically, the Neuron Configurator Module (NCM) is designed to dynamically adjust neuron configurations based on cross-modal features, thereby focusing the spikes in blurry regions and adapting to varying blurry scenarios dynamically. Additionally, the Region of Blurry Attention Module (RBAM) is introduced to generate a blurry mask in an unsupervised manner, effectively extracting motion clues from the event features and guiding more accurate cross-modal feature fusion. Extensive subjective and objective evaluations demonstrate that our method outperforms current state-of-the-art methods on both synthetic and real-world datasets."
status: "auto-generated; needs human review"
---
## Core Problem

Motion deblurring addresses the challenge of image blur caused by camera or scene movement.

## Core Method

Event cameras provide motion information that is encoded in the asynchronous event streams.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：event camera; event stream; event data; event-based motion; spiking neural
network。自动分类理由：Official abstract/page confirms both event-camera/DVS/event-stream evidence
and SNN/spiking neural computation.。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

To efficiently leverage the temporal information of event streams, we employ Spiking Neural
Networks (SNNs) for motion feature extraction and Artificial Neural Networks (ANNs) for
color information processing. Due to the non-uniform distribution and inherent redundancy of
event data, existing cross-modal feature fusion methods exhibit certain limitations.
Inspired by the visual attention mechanism in the human visual system, this study introduces
a bioinspired dual-drive hybrid network (BDHNet). Specifically, the Neuron Configurator
Module (NCM) is designed to dynamically adjust neuron configurations based on cross-modal
features, thereby focusing the spikes in blurry regions and adapting to varying blurry
scenarios dynamically. Additionally, the Region of Blurry Attention Module (RBAM) is
introduced to generate a blurry mask in an unsupervised manner, effectively extracting
motion clues from the event features and guiding more accurate cross-modal feature fusion.
Extensive subjective and objective evaluations demonstrate that our method outperforms
current state-of-the-art methods on both synthetic and real-world datasets.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
