---
title: "Hebbian Learning based Orthogonal Projection for Continual Learning of Spiking Neural Networks"
authors: ["Mingqing Xiao, Qingyan Meng, Zongpeng Zhang, Di He, Zhouchen Lin"]
conference: "ICLR"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/46b1be2b90c6addc84efdf5d7e90eebc-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/46b1be2b90c6addc84efdf5d7e90eebc-Abstract-Conference.html"
tags: []
abstract: "Neuromorphic computing with spiking neural networks is promising for energy-efficient artificial intelligence (AI) applications. However, different from humans who continually learn different tasks in a lifetime, neural network models suffer from catastrophic forgetting. How could neuronal operations solve this problem is an important question for AI and neuroscience. Many previous studies draw inspiration from observed neuroscience phenomena and propose episodic replay or synaptic metaplasticity, but they are not guaranteed to explicitly preserve knowledge for neuron populations. Other works focus on machine learning methods with more mathematical grounding, e.g., orthogonal projection on high dimensional spaces, but there is no neural correspondence for neuromorphic computing. In this work, we develop a new method with neuronal operations based on lateral connections and Hebbian learning, which can protect knowledge by projecting activity traces of neurons into an orthogonal subspace so that synaptic weight update will not interfere with old tasks. We show that Hebbian and anti-Hebbian learning on recurrent lateral connections can effectively extract the principal subspace of neural activities and enable orthogonal projection. This provides new insights into how neural circuits and Hebbian learning can help continual learning, and also how the concept of orthogonal projection can be realized in neuronal systems. Our method is also flexible to utilize arbitrary training methods based on presynaptic activities/traces. Experiments show that our method consistently solves forgetting for spiking neural networks with nearly zero forgetting under various supervised training methods with different error propagation approaches, and outperforms previous approaches under various settings. Our method can pave a solid path for building continual neuromorphic computing systems. The code is available at https://github.com/pkuxmq/HLOP-SNN."
status: "auto-generated; brief scan note"
---
## Core Problem

Neuromorphic computing with spiking neural networks is promising for energy-efficient
artificial intelligence (AI) applications.

## Core Method

However, different from humans who continually learn different tasks in a lifetime, neural
network models suffer from catastrophic forgetting.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage screening; official abstract/page inspected; main conference; needs human
verification。
