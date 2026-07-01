---
title: "SpikeTrack: High-performance and Energy-efficient Event-Based Object Tracking with Spiking Neural Network"
authors: ["Yang Wang", "Jiqing Zhang", "Chuanyu Sun", "Qianhui Liu", "Huilin Ge", "Ziqi Wei", "Xin Yang"]
conference: "CVPR"
year: 2026
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_SpikeTrack_High-performance_and_Energy-efficient_Event-Based_Object_Tracking_with_Spiking_Neural_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Wang_SpikeTrack_High-performance_and_Energy-efficient_Event-Based_Object_Tracking_with_Spiking_Neural_CVPR_2026_paper.html"
tags: []
abstract: "Event cameras have attracted considerable attention for object tracking due to their microsecond-level temporal resolution and wide dynamic range, yet effectively harnessing spiking neural networks (SNNs) in this domain remains challenging. In this paper, we introduce SpikeTrack, a purely spike-driven framework for single-object tracking that addresses the shortcomings of RGB-based approaches in fast-motion or target appearance change. Central to SpikeTrack is the Multi-Search-sequence-and-Single-Template (MSST) training paradigm, which captures rich temporal dependencies, alongside a Dynamic Integer Leaky Integrate-and-Fire (DI-LIF) neuron that adaptively predicts integer-valued activations based on the input features during training and converts them into spikes during inference. Our design preserves the intrinsic sparsity and fine-grained spatiotemporal acuity of event data, resulting in efficient energy consumption without sacrificing performance. Extensive evaluations on FE108, FELT, and VisEvent demonstrate that SpikeTrack exceeds the performance of state-of-the-art trackers in both accuracy and efficiency. Furthermore, ablation studies validate each module's contribution, highlighting the practical potential of spike-driven architectures for future vision applications."
status: "auto-generated; needs human review"
---

## Core Problem

事件相机跟踪在高速运动和外观变化下仍然困难，而纯 ANN 方法难以充分利用脉冲表示。

## Core Method

提出纯 spike-driven 的 SpikeTrack，并结合 MSST 训练范式与 DI-LIF 神经元实现更强时序建模。

## Key Metrics and Findings

摘要声称该框架兼顾跟踪性能与能效，但具体提升幅度需查表核对。

## Personal Notes

这是事件相机与 SNN 交叉方向的核心候选之一。

## Method Details

MSST 用于丰富时序依赖，DI-LIF 用于整数化脉冲表示和动态预测。

## Experimental Analysis

需要核对所用跟踪基准、能耗口径、与 ANN/SNN 对照。

## Related Work Connections

可与 SDTrack 组成事件跟踪的 A 类主线。

## Survey-Usable Points

适合放在事件相机 + SNN 跟踪章节的核心位置。

