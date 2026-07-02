---
title: "SpiLiFormer: Enhancing Spiking Transformers with Lateral Inhibition"
authors: ["Zeqi Zheng", "Yanchen Huang", "Yingchao Yu", "Zizheng Zhu", "Junfeng Tang", "Zhaofei Yu", "Yaochu Jin"]
conference: "ICCV"
year: 2025
level: "A"
category: "SNN + Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Zheng_SpiLiFormer_Enhancing_Spiking_Transformers_with_Lateral_Inhibition_ICCV_2025_paper.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) based on Transformers have garnered significant attention due to their superior performance and high energy efficiency. However, the spiking attention modules of most existing Transformer-based SNNs are adapted from those of analog Transformers, failing to fully address the issue of over-allocating attention to irrelevant contexts. To fix this fundamental yet overlooked issue, we propose a Lateral Inhibition-inspired Spiking Transformer (SpiLiFormer). It emulates the brain's lateral inhibition mechanism, guiding the model to enhance attention to relevant tokens while suppressing attention to irrelevant ones. Our model achieves state-of-the-art (SOTA) performance across multiple datasets, including CIFAR-10 (+0.45%), CIFAR-100 (+0.48%), CIFAR10-DVS (+2.70%), N-Caltech101 (+1.94%), and ImageNet-1K (+1.6%). Notably, on the ImageNet-1K dataset, SpiLiFormer (69.9M parameters, 4 time steps, 384 resolution) outperforms E-SpikeFormer (173.0M parameters, 8 time steps, 384 resolution), a SOTA spiking Transformer, by 0.46% using only 39% of the parameters and half the time steps. The code and model checkpoints are publicly available at https://github.com/KirinZheng/SpiLiFormer."
status: "auto-generated; needs human review"
---

## Core Problem

Spiking Neural Networks (SNNs) based on Transformers have garnered significant attention due to their superior performance and high energy efficiency.

## Core Method

However, the spiking attention modules of most existing Transformer-based SNNs are adapted from those of analog Transformers, failing to fully address the issue of over-allocating attention to irrelevant contexts.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `dvs; cifar10-dvs; dvs visual-event context; spiking neural networks; snns; spiking transformers`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
