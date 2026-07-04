---
title: "SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition"
authors: ["Hongwei Ren, Yue ZHOU, Xiaopeng LIN, Yulong Huang, Haotian FU, Jie Song, Bojun Cheng"]
conference: "ICLR"
year: 2024
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/75f1a165c7561e028c41d42fa6286a76-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/75f1a165c7561e028c41d42fa6286a76-Abstract-Conference.html"
tags: []
abstract: "Event cameras are bio-inspired sensors that respond to local changes in light intensity and feature low latency, high energy efficiency, and high dynamic range. Meanwhile, Spiking Neural Networks (SNNs) have gained significant attention due to their remarkable efficiency and fault tolerance. By synergistically harnessing the energy efficiency inherent in event cameras and the spike-based processing capabilities of SNNs, their integration could enable ultra-low-power application scenarios, such as action recognition tasks. However, existing approaches often entail converting asynchronous events into conventional frames, leading to additional data mapping efforts and a loss of sparsity, contradicting the design concept of SNNs and event cameras. To address this challenge, we propose SpikePoint, a novel end-to-end point-based SNN architecture. SpikePoint excels at processing sparse event cloud data, effectively extracting both global and local features through a singular-stage structure. Leveraging the surrogate training method, SpikePoint achieves high accuracy with few parameters and maintains low power consumption, specifically employing the identity mapping feature extractor on diverse datasets. SpikePoint achieves state-of-the-art (SOTA) performance on four event-based action recognition datasets using only 16 timesteps, surpassing other SNN methods. Moreover, it also achieves SOTA performance across all methods on three datasets, utilizing approximately 0.3 % of the parameters and 0.5 % of power consumption employed by artificial neural networks (ANNs). These results emphasize the significance of Point Cloud and pave the way for many ultra-low-power event-based data processing applications."
status: "auto-generated; needs human review"
---
## Core Problem

Event cameras are bio-inspired sensors that respond to local changes in light intensity and
feature low latency, high energy efficiency, and high dynamic range.

## Core Method

Meanwhile, Spiking Neural Networks (SNNs) have gained significant attention due to their
remarkable efficiency and fault tolerance.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：event cameras; spiking neural network; event; spiking。自动分类理由：Official abstract/page
strictly confirms both event-camera/DVS/visual-event-stream evidence and SNN/spiking neural
computation.。 备注：strict two-stage screening; official abstract/page inspected; main
conference; needs human verification。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

By synergistically harnessing the energy efficiency inherent in event cameras and the spike-
based processing capabilities of SNNs, their integration could enable ultra-low-power
application scenarios, such as action recognition tasks. However, existing approaches often
entail converting asynchronous events into conventional frames, leading to additional data
mapping efforts and a loss of sparsity, contradicting the design concept of SNNs and event
cameras. To address this challenge, we propose SpikePoint, a novel end-to-end point-based
SNN architecture. SpikePoint excels at processing sparse event cloud data, effectively
extracting both global and local features through a singular-stage structure. Leveraging the
surrogate training method, SpikePoint achieves high accuracy with few parameters and
maintains low power consumption, specifically employing the identity mapping feature
extractor on diverse datasets. SpikePoint achieves state-of-the-art (SOTA) performance on
four event-based action recognition datasets using only 16 timesteps, surpassing other SNN
methods. Moreover, it also achieves SOTA performance across all methods on three datasets,
utilizing approximately 0.3 % of the parameters and 0.5 % of power consumption employed by
artificial neural networks (ANNs). These results emphasize the significance of Point Cloud
and pave the way for many ultra-low-power event-based data processing applications.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
