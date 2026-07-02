---
title: "DeepTAGE: Deep Temporal-Aligned Gradient Enhancement for Optimizing Spiking Neural Networks"
authors: ["Wei Liu", "Li Yang", "Mingxuan Zhao", "Shuxun Wang", "Jin Gao", "Wenjuan Li", "Bing Li", "Weiming Hu"]
conference: "ICLR"
year: 2025
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2025/file/6b6492cd06db22bac024506e9ed0925e-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/6b6492cd06db22bac024506e9ed0925e-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks (SNNs), with their biologically inspired spatio-temporal dynamics and spike-driven processing, are emerging as a promising low-power alternative to traditional Artificial Neural Networks (ANNs). However, the complex neuronal dynamics and non-differentiable spike communication mechanisms in SNNs present substantial challenges for efficient training. By analyzing the membrane potentials in spiking neurons, we found that their distributions can increasingly deviate from the firing threshold as time progresses, which tends to cause diminished backpropagation gradients and unbalanced optimization. To address these challenges, we propose Deep Temporal-Aligned Gradient Enhancement (DeepTAGE), a novel approach that improves optimization gradients in SNNs from both internal surrogate gradient functions and external supervision methods. Our DeepTAGE dynamically adjusts surrogate gradients in accordance with the membrane potential distribution across different time steps, enhancing their respective gradients in a temporal-aligned manner that promotes balanced training. Moreover, to mitigate issues of gradient vanishing or deviating during backpropagation, DeepTAGE incorporates deep supervision at both spatial (network stages) and temporal (time steps) levels to ensure more effective and robust network optimization. Importantly, our method can be seamlessly integrated into existing SNN architectures without imposing additional inference costs or requiring extra control modules. We validate the efficacy of DeepTAGE through extensive experiments on static benchmarks (CIFAR10, CIFAR100, and ImageNet-1k) and a neuromorphic dataset (DVS-CIFAR10), demonstrating significant performance improvements."
status: "auto-generated; needs human review"
---

## Core Problem

Spiking Neural Networks (SNNs), with their biologically inspired spatio-temporal dynamics and spike-driven processing, are emerging as a promising low-power alternative to traditional Artificial Neural Networks (ANNs).

## Core Method

However, the complex neuronal dynamics and non-differentiable spike communication mechanisms in SNNs present substantial challenges for efficient training.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Official abstract/page strictly confirms both event-camera/DVS/visual-event-stream evidence and SNN/spiking neural computation.。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/视觉事件流与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
