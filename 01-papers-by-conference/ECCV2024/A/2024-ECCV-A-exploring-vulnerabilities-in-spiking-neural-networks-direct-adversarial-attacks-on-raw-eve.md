---
title: "Exploring Vulnerabilities in Spiking Neural Networks: Direct Adversarial Attacks on Raw Event Data"
authors: ["Yanmeng Yao", "Xiaohan Zhao", "Bin Gu"]
conference: "ECCV"
year: 2024
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09164.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1447"
tags: []
abstract: "In the field of computer vision, event-based Dynamic Vision Sensors (DVSs) have emerged as a significant complement to traditional pixel-based imaging due to their low power consumption and high temporal resolution. These sensors, particularly when combined with spiking neural networks (SNNs), offer a promising direction for energy-efficient and fast-reacting vision systems. Typically, DVS data are converted into grid-based formats for processing with SNNs, with this transformation process often being an opaque step in the pipeline. As a result, the grid representation becomes an intermediate yet inaccessible stage during the implementation of attacks, highlighting the importance of attacking raw event data. Existing attack methodologies predominantly target grid-based representations, hindered by the complexity of three-valued optimization and the broad optimization space associated with raw event data. Our study addresses this gap by introducing a novel adversarial attack approach that directly targets raw event data. We tackle the inherent challenges of three-valued optimization and the need to preserve data sparsity through a strategic amalgamation of methods: 1) Treating Discrete Event Values as Probabilistic Samples: This allows for continuous optimization by considering discrete event values as probabilistic space samples. 2) Focusing on Specific Event Positions: We prioritize specific event positions that merge original data with additional target label data, enhancing attack precision. 3) Employing a Sparsity Norm: To retain the original data's sparsity, a sparsity norm is utilized, ensuring the adversarial data's comparability. Our empirical findings demonstrate the effectiveness of our combined approach, achieving noteworthy success in targeted attacks and highlighting vulnerabilities in models based on raw event data."
status: "auto-generated; needs human review"
---
## Core Problem

In the field of computer vision, event-based Dynamic Vision Sensors (DVSs) have emerged as a
significant complement to traditional pixel-based imaging due to their low power consumption
and high temporal resolution.

## Core Method

These sensors, particularly when combined with spiking neural networks (SNNs), offer a
promising direction for energy-efficient and fast-reacting vision systems.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：DVS; event data; spiking neural network。自动分类理由：Official abstract/page confirms both
event-camera/DVS/event-stream evidence and SNN/spiking neural computation.。
该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

Typically, DVS data are converted into grid-based formats for processing with SNNs, with
this transformation process often being an opaque step in the pipeline. As a result, the
grid representation becomes an intermediate yet inaccessible stage during the implementation
of attacks, highlighting the importance of attacking raw event data. Existing attack
methodologies predominantly target grid-based representations, hindered by the complexity of
three-valued optimization and the broad optimization space associated with raw event data.
Our study addresses this gap by introducing a novel adversarial attack approach that
directly targets raw event data. We tackle the inherent challenges of three-valued
optimization and the need to preserve data sparsity through a strategic amalgamation of
methods: 1) Treating Discrete Event Values as Probabilistic Samples: This allows for
continuous optimization by considering discrete event values as probabilistic space samples.
2) Focusing on Specific Event Positions: We prioritize specific event positions that merge
original data with additional target label data, enhancing attack precision. 3) Employing a
Sparsity Norm: To retain the original data's sparsity, a sparsity norm is utilized, ensuring
the adversarial data's comparability. Our empirical findings demonstrate the effectiveness
of our combined approach, achieving noteworthy success in targeted attacks and highlighting
vulnerabilities in models based on raw event data.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
