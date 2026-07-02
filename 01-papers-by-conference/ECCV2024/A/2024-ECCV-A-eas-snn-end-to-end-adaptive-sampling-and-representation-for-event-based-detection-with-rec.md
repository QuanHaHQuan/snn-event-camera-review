---
title: "EAS-SNN: End-to-End Adaptive Sampling and Representation for Event-based Detection with Recurrent Spiking Neural Networks"
authors: ["Ziming Wang", "Ziling Wang", "Huaning Li", "Lang Qin", "Runhao Jiang", "De Ma", "Huajin Tang"]
conference: "ECCV"
year: 2024
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07766.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/711"
tags: []
abstract: "Event cameras, with their high dynamic range and temporal resolution, are ideally suited for object detection, especially under scenarios with motion blur and challenging lighting conditions. However, while most existing approaches prioritize optimizing spatiotemporal representations with advanced detection backbones and early aggregation functions, the crucial issue of adaptive event sampling remains largely unaddressed. Spiking Neural Networks (SNNs), which operate on an event-driven paradigm through sparse spike communication, emerge as a natural fit for addressing this challenge. In this study, we discover that the neural dynamics of spiking neurons align closely with the behavior of an ideal temporal event sampler. Motivated by this insight, we propose a novel adaptive sampling module that leverages recurrent convolutional SNNs enhanced with temporal memory, facilitating a fully end-to-end learnable framework for event-based detection. Additionally, we introduce Residual Potential Dropout (RPD) and Spike-Aware Training (SAT) to regulate potential distribution and address performance degradation encountered in spike-based sampling modules. Through rigorous testing on neuromorphic datasets for event-based detection, our approach demonstrably surpasses existing state-of-the-art spike-based methods, achieving superior performance with significantly fewer parameters and time steps. For instance, our method achieves a 4.4\\% mAP improvement on the Gen1 dataset, while requiring 38\\% fewer parameters and three time steps. Moreover, the applicability and effectiveness of our adaptive sampling methodology extend beyond SNNs, as demonstrated through further validation on conventional non-spiking detection models."
status: "auto-generated; needs human review"
---
## Core Problem

Event cameras, with their high dynamic range and temporal resolution, are ideally suited for
object detection, especially under scenarios with motion blur and challenging lighting
conditions.

## Core Method

However, while most existing approaches prioritize optimizing spatiotemporal representations
with advanced detection backbones and early aggregation functions, the crucial issue of
adaptive event sampling remains largely unaddressed.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：event camera; event-based detection; spiking neural network; spiking
neuron。自动分类理由：Official abstract/page confirms both event-camera/DVS/event-stream evidence
and SNN/spiking neural computation.。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

Spiking Neural Networks (SNNs), which operate on an event-driven paradigm through sparse
spike communication, emerge as a natural fit for addressing this challenge. In this study,
we discover that the neural dynamics of spiking neurons align closely with the behavior of
an ideal temporal event sampler. Motivated by this insight, we propose a novel adaptive
sampling module that leverages recurrent convolutional SNNs enhanced with temporal memory,
facilitating a fully end-to-end learnable framework for event-based detection. Additionally,
we introduce Residual Potential Dropout (RPD) and Spike-Aware Training (SAT) to regulate
potential distribution and address performance degradation encountered in spike-based
sampling modules. Through rigorous testing on neuromorphic datasets for event-based
detection, our approach demonstrably surpasses existing state-of-the-art spike-based
methods, achieving superior performance with significantly fewer parameters and time steps.
For instance, our method achieves a 4.4\% mAP improvement on the Gen1 dataset, while
requiring 38\% fewer parameters and three time steps. Moreover, the applicability and
effectiveness of our adaptive sampling methodology extend beyond SNNs, as demonstrated
through further validation on conventional non-spiking detection models.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
