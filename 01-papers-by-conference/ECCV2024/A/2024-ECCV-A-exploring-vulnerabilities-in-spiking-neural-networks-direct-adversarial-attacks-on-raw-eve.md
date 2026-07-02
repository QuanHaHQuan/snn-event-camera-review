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

In the field of computer vision, event-based Dynamic Vision Sensors (DVSs) have emerged as a significant complement to traditional pixel-based imaging due to their low power consumption and high temporal resolution.

## Core Method

These sensors, particularly when combined with spiking neural networks (SNNs), offer a promising direction for energy-efficient and fast-reacting vision systems.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `dynamic vision sensors; dvs; dynamic vision sensor visual-event context; dvs visual-event context; event-based with event-camera context; spiking neural networks; snns`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
