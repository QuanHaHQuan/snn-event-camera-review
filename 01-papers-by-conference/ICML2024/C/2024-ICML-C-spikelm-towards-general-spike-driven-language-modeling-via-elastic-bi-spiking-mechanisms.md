---
title: "SpikeLM: Towards General Spike-Driven Language Modeling via Elastic Bi-Spiking Mechanisms"
authors: ["Xingrun Xing, Zheng Zhang, Ziyi Ni, Shitao Xiao, Yiming Ju, Siqi Fan, Yequan Wang, Jiajun Zhang, Guoqi Li"]
conference: "ICML"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xing24d/xing24d.pdf"
official_page: "https://proceedings.mlr.press/v235/xing24d.html"
tags: []
abstract: "Towards energy-efficient artificial intelligence similar to the human brain, the bio-inspired spiking neural networks (SNNs) have advantages of biological plausibility, event-driven sparsity, and binary activation. Recently, large-scale language models exhibit promising generalization capability, making it a valuable issue to explore more general spike-driven models. However, the binary spikes in existing SNNs fail to encode adequate semantic information, placing technological challenges for generalization. This work proposes the first fully spiking mechanism for general language tasks, including both discriminative and generative ones. Different from previous spikes with 0,1 levels, we propose a more general spike formulation with bi-directional, elastic amplitude, and elastic frequency encoding, while still maintaining the addition nature of SNNs. In a single time step, the spike is enhanced by direction and amplitude information; in spike frequency, a strategy to control spike firing rate is well designed. We plug this elastic bi-spiking mechanism in language modeling, named SpikeLM. It is the first time to handle general language tasks with fully spike-driven models, which achieve much higher accuracy than previously possible. SpikeLM also greatly bridges the performance gap between SNNs and ANNs in language modeling. Our code is available at https://github.com/Xingrun-Xing/SpikeLM."
status: "auto-generated; brief scan note"
---
## Core Problem

Towards energy-efficient artificial intelligence similar to the human brain, the bio-
inspired spiking neural networks (SNNs) have advantages of biological plausibility, event-
driven sparsity, and binary activation.

## Core Method

Recently, large-scale language models exhibit promising generalization capability, making it
a valuable issue to explore more general spike-driven models.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spike; spiking。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence found.。 备注：strict two-stage screening;
official abstract/page inspected; main conference; needs human verification。
