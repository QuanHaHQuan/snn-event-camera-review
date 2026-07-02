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

Spiking Neural Networks (SNNs) based on Transformers have garnered significant attention due
to their superior performance and high energy efficiency.

## Core Method

However, the spiking attention modules of most existing Transformer-based SNNs are adapted
from those of analog Transformers, failing to fully address the issue of over-allocating
attention to irrelevant contexts.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：spiking neural network; spiking transformer; CIFAR10-DVS;
N-Caltech101。自动分类理由：Official abstract confirms a Spiking Transformer and reports event-
camera benchmarks CIFAR10-DVS and N-Caltech101.。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

To fix this fundamental yet overlooked issue, we propose a Lateral Inhibition-inspired
Spiking Transformer (SpiLiFormer). It emulates the brain's lateral inhibition mechanism,
guiding the model to enhance attention to relevant tokens while suppressing attention to
irrelevant ones. Our model achieves state-of-the-art (SOTA) performance across multiple
datasets, including CIFAR-10 (+0.45%), CIFAR-100 (+0.48%), CIFAR10-DVS (+2.70%),
N-Caltech101 (+1.94%), and ImageNet-1K (+1.6%). Notably, on the ImageNet-1K dataset,
SpiLiFormer (69.9M parameters, 4 time steps, 384 resolution) outperforms E-SpikeFormer
(173.0M parameters, 8 time steps, 384 resolution), a SOTA spiking Transformer, by 0.46%
using only 39% of the parameters and half the time steps. The code and model checkpoints are
publicly available at https://github.com/KirinZheng/SpiLiFormer.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
