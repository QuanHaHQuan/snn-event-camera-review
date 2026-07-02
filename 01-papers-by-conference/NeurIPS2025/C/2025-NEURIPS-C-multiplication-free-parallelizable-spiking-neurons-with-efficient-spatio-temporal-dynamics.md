---
title: "Multiplication-Free Parallelizable Spiking Neurons with Efficient Spatio-Temporal Dynamics"
authors: ["Peng Xue, Wei Fang, Zhengyu Ma, Zihan Huang, Zhaokun Zhou, Yonghong Tian, Timothée Masquelier, Huihui Zhou"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/5f40a99efedc1148a061d80201949c84-Paper-Conference.pdf"
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

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNN/spiking neural computation。自动分类理由：Official abstract confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence.。 备注：Track: Main Conference Track. Official
abstract/page inspected under broad high-recall title workflow.。
