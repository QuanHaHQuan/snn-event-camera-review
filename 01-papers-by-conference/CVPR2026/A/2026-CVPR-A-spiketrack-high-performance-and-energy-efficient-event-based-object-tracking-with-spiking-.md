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

Event cameras have attracted considerable attention for object tracking due to their
microsecond-level temporal resolution and wide dynamic range, yet effectively harnessing
spiking neural networks (SNNs) in this domain remains challenging.

## Core Method

In this paper, we introduce SpikeTrack, a purely spike-driven framework for single-object
tracking that addresses the shortcomings of RGB-based approaches in fast-motion or target
appearance change.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：event camera; event data; spiking neural network; LIF; spike-driven。自动分类理由：Official
abstract/page confirms both event-camera/DVS/event-stream evidence and SNN/spiking neural
computation.。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

Central to SpikeTrack is the Multi-Search-sequence-and-Single-Template (MSST) training
paradigm, which captures rich temporal dependencies, alongside a Dynamic Integer Leaky
Integrate-and-Fire (DI-LIF) neuron that adaptively predicts integer-valued activations based
on the input features during training and converts them into spikes during inference. Our
design preserves the intrinsic sparsity and fine-grained spatiotemporal acuity of event
data, resulting in efficient energy consumption without sacrificing performance. Extensive
evaluations on FE108, FELT, and VisEvent demonstrate that SpikeTrack exceeds the performance
of state-of-the-art trackers in both accuracy and efficiency. Furthermore, ablation studies
validate each module's contribution, highlighting the practical potential of spike-driven
architectures for future vision applications.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
