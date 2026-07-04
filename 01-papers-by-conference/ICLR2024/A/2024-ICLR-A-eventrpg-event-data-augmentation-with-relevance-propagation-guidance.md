---
title: "EventRPG: Event Data Augmentation with Relevance Propagation Guidance"
authors: ["Mingyuan Sun, Donghao Zhang, Zongyuan Ge, Jiaxu Wang, Jia Li, Zheng Fang, Renjing Xu"]
conference: "ICLR"
year: 2024
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/19dbb86f771ddbf9986cf0c9b1c61c17-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/19dbb86f771ddbf9986cf0c9b1c61c17-Abstract-Conference.html"
tags: []
abstract: "Event camera, a novel bio-inspired vision sensor, has drawn a lot of attention for its low latency, low power consumption, and high dynamic range. Currently, overfitting remains a critical problem in event-based classification tasks for Spiking Neural Network (SNN) due to its relatively weak spatial representation capability. Data augmentation is a simple but efficient method to alleviate overfitting and improve the generalization ability of neural networks, and saliency-based augmentation methods are proven to be effective in the image processing field. However, there is no approach available for extracting saliency maps from SNNs. Therefore, for the first time, we present Spiking Layer-Time-wise Relevance Propagation rule (SLTRP) and Spiking Layer-wise Relevance Propagation rule (SLRP) in order for SNN to generate stable and accurate CAMs and saliency maps. Based on this, we propose EventRPG, which leverages relevance propagation on the spiking neural network for more efficient augmentation. Our proposed method has been evaluated on several SNN structures, achieving state-of-the-art performance in object recognition tasks including N-Caltech101, CIFAR10-DVS, with accuracies of 85.62% and 85.55%, as well as action recognition task SL-Animals with an accuracy of 91.59%. Our code is available at https://github.com/myuansun/EventRPG."
status: "auto-generated; needs human review"
---
## Core Problem

Event camera, a novel bio-inspired vision sensor, has drawn a lot of attention for its low
latency, low power consumption, and high dynamic range.

## Core Method

Currently, overfitting remains a critical problem in event-based classification tasks for
Spiking Neural Network (SNN) due to its relatively weak spatial representation capability.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：event; event data。自动分类理由：Official abstract/page strictly confirms both event-
camera/DVS/visual-event-stream evidence and SNN/spiking neural computation.。 备注：strict two-
stage screening; official abstract/page inspected; main conference; needs human
verification。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

Data augmentation is a simple but efficient method to alleviate overfitting and improve the
generalization ability of neural networks, and saliency-based augmentation methods are
proven to be effective in the image processing field. However, there is no approach
available for extracting saliency maps from SNNs. Therefore, for the first time, we present
Spiking Layer-Time-wise Relevance Propagation rule (SLTRP) and Spiking Layer-wise Relevance
Propagation rule (SLRP) in order for SNN to generate stable and accurate CAMs and saliency
maps. Based on this, we propose EventRPG, which leverages relevance propagation on the
spiking neural network for more efficient augmentation. Our proposed method has been
evaluated on several SNN structures, achieving state-of-the-art performance in object
recognition tasks including N-Caltech101, CIFAR10-DVS, with accuracies of 85.62% and 85.55%,
as well as action recognition task SL-Animals with an accuracy of 91.59%. Our code is
available at https://github.com/myuansun/EventRPG.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
