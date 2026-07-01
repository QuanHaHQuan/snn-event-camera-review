---
title: 'SpiLiFormer: Enhancing Spiking Transformers with Lateral Inhibition'
authors: ['Zeqi Zheng', 'Yanchen Huang', 'Yingchao Yu', 'Zizheng Zhu', 'Junfeng Tang', 'Zhaofei Yu', 'Yaochu Jin']
conference: 'ICCV'
year: 2025
level: 'A'
category: 'SNN + Event Camera'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Zheng_SpiLiFormer_Enhancing_Spiking_Transformers_with_Lateral_Inhibition_ICCV_2025_paper.html'
tags: []
abstract: "Spiking Neural Networks (SNNs) based on Transformers have garnered significant attention due to their superior performance and high energy efficiency. However, the spiking attention modules of most existing Transformer-based SNNs are adapted from those of analog Transformers, failing to fully address the issue of over-allocating attention to irrelevant contexts. To fix this fundamental yet overlooked issue, we propose a Lateral Inhibition-inspired Spiking Transformer (SpiLiFormer). It emulates the brain's lateral inhibition mechanism, guiding the model to enhance attention to relevant tokens while suppressing attention to irrelevant ones. Our model achieves state-of-the-art (SOTA) performance across multiple datasets, including CIFAR-10 (+0.45%), CIFAR-100 (+0.48%), CIFAR10-DVS (+2.70%), N-Caltech101 (+1.94%), and ImageNet-1K (+1.6%). Notably, on the ImageNet-1K dataset, SpiLiFormer (69.9M parameters, 4 time steps, 384 resolution) outperforms E-SpikeFormer (173.0M parameters, 8 time steps, 384 resolution), a SOTA spiking Transformer, by 0.46% using only 39% of the parameters and half the time steps. The code and model checkpoints are publicly available at https://github.com/KirinZheng/SpiLiFormer."
status: 'auto-generated; needs human review'
---

## Core Problem

Spiking Transformer 已用于高效视觉识别，但现有 spiking attention 多从 analog Transformer 改造而来，容易把注意力分配给无关上下文；同时该工作在 CIFAR10-DVS、N-Caltech101 等事件相机数据集上报告结果，因此进入 SNN + event-camera 交叉候选。

## Core Method

提出 Lateral Inhibition-inspired Spiking Transformer (SpiLiFormer)，用类脑侧抑制机制增强相关 token、抑制无关 token，从而改进 spiking attention 的选择性。

## Key Metrics and Findings

摘要报告 CIFAR-10 +0.45%、CIFAR-100 +0.48%、CIFAR10-DVS +2.70%、N-Caltech101 +1.94%、ImageNet-1K +1.6%；并称在 ImageNet-1K 上用 39% 参数和一半 time steps 超过 E-SpikeFormer 0.46%。

## Personal Notes

A 类边界需要人工复核：方法核心是 SNN/Spiking Transformer，事件相机侧证据主要来自 CIFAR10-DVS 和 N-Caltech101 benchmark，而不是专门为事件相机设计的输入表示。

## Method Details

当前卡片仅基于官方摘要；需要阅读全文确认 lateral inhibition 模块的具体实现、spiking attention 形式、time steps、神经元模型和训练设置。

## Experimental Analysis

需要核对事件数据集实验是否与主论文核心贡献一致，以及是否有能耗、延迟、参数量、time step 的公平比较。

## Related Work Connections

应与 C 类 Spiking Transformer / SNN 训练论文联读，也可与 A 类事件跟踪 SNN 工作区分：本论文更偏通用 SNN 架构，事件相机只是评测轴之一。

## Survey-Usable Points

可作为“通用 SNN 架构在事件相机数据集上的验证”案例；综述中不宜过度表述为事件相机专用方法。
