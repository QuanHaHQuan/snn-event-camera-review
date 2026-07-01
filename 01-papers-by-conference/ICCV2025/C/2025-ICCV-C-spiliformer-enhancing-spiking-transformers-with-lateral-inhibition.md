---
title: 'SpiLiFormer: Enhancing Spiking Transformers with Lateral Inhibition'
authors: ['Zeqi Zheng', 'Yanchen Huang', 'Yingchao Yu', 'Zizheng Zhu', 'Junfeng Tang', 'Zhaofei Yu', 'Yaochu Jin']
conference: 'ICCV'
year: 2025
level: 'C'
category: 'SNN'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Zheng_SpiLiFormer_Enhancing_Spiking_Transformers_with_Lateral_Inhibition_ICCV_2025_paper.html'
tags: []
abstract: "Spiking Neural Networks (SNNs) based on Transformers have garnered significant attention due to their superior performance and high energy efficiency. However, the spiking attention modules of most existing Transformer-based SNNs are adapted from those of analog Transformers, failing to fully address the issue of over-allocating attention to irrelevant contexts. To fix this fundamental yet overlooked issue, we propose a Lateral Inhibition-inspired Spiking Transformer (SpiLiFormer). It emulates the brain's lateral inhibition mechanism, guiding the model to enhance attention to relevant tokens while suppressing attention to irrelevant ones. Our model achieves state-of-the-art (SOTA) performance across multiple datasets, including CIFAR-10 (+0.45%), CIFAR-100 (+0.48%), CIFAR10-DVS (+2.70%), N-Caltech101 (+1.94%), and ImageNet-1K (+1.6%). Notably, on the ImageNet-1K dataset, SpiLiFormer (69.9M parameters, 4 time steps, 384 resolution) outperforms E-SpikeFormer (173.0M parameters, 8 time steps, 384 resolution), a SOTA spiking Transformer, by 0.46% using only 39% of the parameters and half the time steps. The code and model checkpoints are publicly available at https://github.com/KirinZheng/SpiLiFormer."
status: 'auto-generated; brief scan note'
---
## Core Problem

SNN 方向的核心问题通常是脉冲表示的稳定性、效率或结构设计。

## Core Method

论文围绕 spiking neural networks / spiking transformers 展开，并针对其结构或训练做改进。

## Key Metrics and Findings

需要结合正文核对定量结果；当前仅确认其属于 SNN 背景论文。

## Personal Notes

可作为 SNN 侧背景论文进入对应方法章节。
