---
title: "Asynchronous Bioplausible Neuron for Spiking Neural Networks for Event-Based Vision"
authors: ["Hussain Sajwani", "Dimitrios Makris", "Yahya Zweiri", "Fariborz Baghaei Naeini", "Sanket Mr Kachole"]
conference: "ECCV"
year: 2024
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08133.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1172"
tags: []
abstract: "Spiking Neural Networks (SNNs) offer a biologically inspired approach to computer vision that can lead to more efficient processing of visual data with reduced energy consumption. However, maintaining homeostasis within SNNs is challenging, as it requires continuous adjustment of neural responses to preserve equilibrium and optimal processing efficiency amidst diverse and often unpredictable input signals. In response to these challenges, we propose the Asynchronous Bioplausible Neuron (ABN), a dynamic spike firing mechanism that offers a simple yet potent auto-adjustment to variations in input signals. Its parameters, Membrane Gradient (MG), Threshold Retrospective Gradient (TRG), and Spike Efficiency (SE), make it stand out for its easy implementation, significant effectiveness, and proven reduction in power consumption, a key innovation demonstrated in our experiments. Comprehensive evaluation across various datasets demonstrates ABN's enhanced performance in image classification and segmentation, maintenance of neural equilibrium, and energy efficiency. The code will be publicly available on the GitHub Project Page."
status: "auto-generated; needs human review"
---
## Core Problem

Spiking Neural Networks (SNNs) offer a biologically inspired approach to computer vision
that can lead to more efficient processing of visual data with reduced energy consumption.

## Core Method

However, maintaining homeostasis within SNNs is challenging, as it requires continuous
adjustment of neural responses to preserve equilibrium and optimal processing efficiency
amidst diverse and often unpredictable input signals.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：spiking neural network; event-camera datasets。自动分类理由：Official abstract/page and
targeted PDF check confirm SNN computation evaluated for event-based vision/event-camera
dataset context.。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

In response to these challenges, we propose the Asynchronous Bioplausible Neuron (ABN), a
dynamic spike firing mechanism that offers a simple yet potent auto-adjustment to variations
in input signals. Its parameters, Membrane Gradient (MG), Threshold Retrospective Gradient
(TRG), and Spike Efficiency (SE), make it stand out for its easy implementation, significant
effectiveness, and proven reduction in power consumption, a key innovation demonstrated in
our experiments. Comprehensive evaluation across various datasets demonstrates ABN's
enhanced performance in image classification and segmentation, maintenance of neural
equilibrium, and energy efficiency. The code will be publicly available on the GitHub
Project Page.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
