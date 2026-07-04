---
title: "Temporal Misalignment in ANN-SNN Conversion and its Mitigation via Probabilistic Spiking Neurons"
authors: ["Velibor Bojkovic, Xiaofeng Wu, Bin Gu"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/bojkovic25a/bojkovic25a.pdf"
official_page: "https://proceedings.mlr.press/v267/bojkovic25a.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) offer a more energy-efficient alternative to Artificial Neural Networks (ANNs) by mimicking biological neural principles, establishing them as a promising approach to mitigate the increasing energy demands of large-scale neural models. However, fully harnessing the capabilities of SNNs remains challenging due to their discrete signal processing and temporal dynamics. ANN-SNN conversion has emerged as a practical approach, enabling SNNs to achieve competitive performance on complex machine learning tasks. In this work, we identify a phenomenon in the ANN-SNN conversion framework, termed temporal misalignment , in which random spike rearrangement across SNN layers leads to performance improvements. Based on this observation, we introduce biologically plausible two-phase probabilistic (TPP) spiking neurons, further enhancing the conversion process. We demonstrate the advantages of our proposed method both theoretically and empirically through comprehensive experiments on CIFAR-10/100, CIFAR10-DVS, and ImageNet across a variety of architectures, achieving state-of-the-art results."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks (SNNs) offer a more energy-efficient alternative to Artificial Neural Networks (ANNs) by mimicking biological neural principles, establishing them as a promising approach to mitigate the increasing energy demands of large-scale neural models.

## Core Method

However, fully harnessing the capabilities of SNNs remains challenging due to their discrete signal processing and temporal dynamics.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `dvs; cifar10-dvs; dvs visual-event context; spiking neural networks; snns; spiking neurons`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
