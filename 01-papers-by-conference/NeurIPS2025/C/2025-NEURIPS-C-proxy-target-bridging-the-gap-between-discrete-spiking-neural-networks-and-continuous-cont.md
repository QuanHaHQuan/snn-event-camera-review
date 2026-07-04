---
title: "Proxy Target: Bridging the Gap Between Discrete Spiking Neural Networks and Continuous Control"
authors: ["Zijie Xu, Tong Bu, Zecheng Hao, Jianhao Ding, Zhaofei Yu"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/e95eb5206c867be843fbc14bbfe8c10e-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/e95eb5206c867be843fbc14bbfe8c10e-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) offer low-latency and energy-efficient decision making on neuromorphic hardware, making them attractive for Reinforcement Learning (RL) in resource-constrained edge devices. However, most RL algorithms for continuous control are designed for Artificial Neural Networks (ANNs), particularly the target network soft update mechanism, which conflicts with the discrete and non-differentiable dynamics of spiking neurons. We show that this mismatch destabilizes SNN training and degrades performance. To bridge the gap between discrete SNNs and continuous-control algorithms, we propose a novel proxy target framework. The proxy network introduces continuous and differentiable dynamics that enable smooth target updates, stabilizing the learning process. Since the proxy operates only during training, the deployed SNN remains fully energy-efficient with no additional inference overhead. Extensive experiments on continuous control benchmarks demonstrate that our framework consistently improves stability and achieves up to $32$% higher performance across various spiking neuron models. Notably, to the best of our knowledge, this is the first approach that enables SNNs with simple Leaky Integrate and Fire (LIF) neurons to surpass their ANN counterparts in continuous control. This work highlights the importance of SNN-tailored RL algorithms and paves the way for neuromorphic agents that combine high performance with low power consumption. Code is available at https://github.com/xuzijie32/Proxy-Target."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs) offer low-latency and energy-efficient decision making on
neuromorphic hardware, making them attractive for Reinforcement Learning (RL) in resource-
constrained edge devices.

## Core Method

However, most RL algorithms for continuous control are designed for Artificial Neural
Networks (ANNs), particularly the target network soft update mechanism, which conflicts with
the discrete and non-differentiable dynamics of spiking neurons.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; snns; spiking neurons; lif。自动分类理由：Official abstract/page
strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。
备注：strict two-stage rescan; official abstract/page inspected; needs human verification;
Track: Main Conference Track。
