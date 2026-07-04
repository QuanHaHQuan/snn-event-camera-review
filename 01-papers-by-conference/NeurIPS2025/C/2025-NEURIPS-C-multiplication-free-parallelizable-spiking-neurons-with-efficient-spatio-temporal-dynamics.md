---
title: "Multiplication-Free Parallelizable Spiking Neurons with Efficient Spatio-Temporal Dynamics"
authors: ["Peng Xue, Wei Fang, Zhengyu Ma, Zihan Huang, Zhaokun Zhou, Yonghong Tian, Timothée Masquelier, Huihui Zhou"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/5f40a99efedc1148a061d80201949c84-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/5f40a99efedc1148a061d80201949c84-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) are distinguished from Artificial Neural Networks (ANNs) for their complex neuronal dynamics and sparse binary activations (spikes) inspired by the biological neural system. Traditional neuron models use iterative step-by-step dynamics, resulting in serial computation and slow training speed of SNNs. Recently, parallelizable spiking neuron models have been proposed to fully utilize the massive parallel computing ability of graphics processing units to accelerate the training of SNNs. However, existing parallelizable spiking neuron models involve dense floating operations and can only achieve high long-term dependencies learning ability with a large order at the cost of huge computational and memory costs. To solve the dilemma of performance and costs, we propose the mul-free channel-wise Parallel Spiking Neuron, which is hardware-friendly and suitable for SNNs’ resource-restricted application scenarios. The proposed neuron imports the channel-wise convolution to enhance the learning ability, induces the sawtooth dilations to reduce the neuron order, and employs the bit-shift operation to avoid multiplications. The algorithm for the design and implementation of acceleration methods is discussed extensively. Our methods are validated in neuromorphic Spiking Heidelberg Digits voices, sequential CIFAR images, and neuromorphic DVS-Lip vision datasets, achieving superior performance over SOTA spiking neurons. Training speed results demonstrate the effectiveness of our acceleration methods, providing a practical reference for future research. Our code is available at Github."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs) are distinguished from Artificial Neural Networks (ANNs) for
their complex neuronal dynamics and sparse binary activations (spikes) inspired by the
biological neural system.

## Core Method

Traditional neuron models use iterative step-by-step dynamics, resulting in serial
computation and slow training speed of SNNs.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：dvs; dvs visual-event context; spiking neural networks; snns; spiking
neurons。自动分类理由：Official abstract/page strictly confirms both event-camera/DVS/visual-event-
sensor evidence and SNN/spiking neural computation.。 备注：strict two-stage rescan; official
abstract/page inspected; needs human verification; Track: Main Conference Track。
该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

Recently, parallelizable spiking neuron models have been proposed to fully utilize the
massive parallel computing ability of graphics processing units to accelerate the training
of SNNs. However, existing parallelizable spiking neuron models involve dense floating
operations and can only achieve high long-term dependencies learning ability with a large
order at the cost of huge computational and memory costs. To solve the dilemma of
performance and costs, we propose the mul-free channel-wise Parallel Spiking Neuron, which
is hardware-friendly and suitable for SNNs’ resource-restricted application scenarios. The
proposed neuron imports the channel-wise convolution to enhance the learning ability,
induces the sawtooth dilations to reduce the neuron order, and employs the bit-shift
operation to avoid multiplications. The algorithm for the design and implementation of
acceleration methods is discussed extensively. Our methods are validated in neuromorphic
Spiking Heidelberg Digits voices, sequential CIFAR images, and neuromorphic DVS-Lip vision
datasets, achieving superior performance over SOTA spiking neurons. Training speed results
demonstrate the effectiveness of our acceleration methods, providing a practical reference
for future research. Our code is available at Github.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
