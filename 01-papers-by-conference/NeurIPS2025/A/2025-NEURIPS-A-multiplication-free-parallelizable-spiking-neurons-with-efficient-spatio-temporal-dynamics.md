---
title: "Multiplication-Free Parallelizable Spiking Neurons with Efficient Spatio-Temporal Dynamics"
authors: ["Peng Xue, Wei Fang, Zhengyu Ma, Zihan Huang, Zhaokun Zhou, Yonghong Tian, Timothée Masquelier, Huihui Zhou"]
conference: "NeurIPS"
year: 2025
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/5f40a99efedc1148a061d80201949c84-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/5f40a99efedc1148a061d80201949c84-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) are distinguished from Artificial Neural Networks (ANNs) for their complex neuronal dynamics and sparse binary activations (spikes) inspired by the biological neural system. Traditional neuron models use iterative step-by-step dynamics, resulting in serial computation and slow training speed of SNNs. Recently, parallelizable spiking neuron models have been proposed to fully utilize the massive parallel computing ability of graphics processing units to accelerate the training of SNNs. However, existing parallelizable spiking neuron models involve dense floating operations and can only achieve high long-term dependencies learning ability with a large order at the cost of huge computational and memory costs. To solve the dilemma of performance and costs, we propose the mul-free channel-wise Parallel Spiking Neuron, which is hardware-friendly and suitable for SNNs’ resource-restricted application scenarios. The proposed neuron imports the channel-wise convolution to enhance the learning ability, induces the sawtooth dilations to reduce the neuron order, and employs the bit-shift operation to avoid multiplications. The algorithm for the design and implementation of acceleration methods is discussed extensively. Our methods are validated in neuromorphic Spiking Heidelberg Digits voices, sequential CIFAR images, and neuromorphic DVS-Lip vision datasets, achieving superior performance over SOTA spiking neurons. Training speed results demonstrate the effectiveness of our acceleration methods, providing a practical reference for future research. Our code is available at Github."
status: "auto-generated; needs human review"
---

## Core Problem

Spiking Neural Networks (SNNs) are distinguished from Artificial Neural Networks (ANNs) for their complex neuronal dynamics and sparse binary activations (spikes) inspired by the biological neural system.

## Core Method

Traditional neuron models use iterative step-by-step dynamics, resulting in serial computation and slow training speed of SNNs.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `dvs; dvs visual-event context; spiking neural networks; snns; spiking neurons`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
