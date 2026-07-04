---
title: "Rethinking the Membrane Dynamics and Optimization Objectives of Spiking Neural Networks"
authors: ["Hangchi Shen, Qian Zheng, Huamin Wang, Gang Pan"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/a867a94a427bacbe3f4de16c7ac10ba8-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/a867a94a427bacbe3f4de16c7ac10ba8-Abstract-Conference.html"
tags: []
abstract: "Despite spiking neural networks (SNNs) have demonstrated notable energy efficiency across various fields, the limited firing patterns of spiking neurons within fixed time steps restrict the expression of information, which impedes further improvement of SNN performance. In addition, current implementations of SNNs typically consider the firing rate or average membrane potential of the last layer as the output, lacking exploration of other possibilities. In this paper, we identify that the limited spike patterns of spiking neurons stem from the initial membrane potential (IMP), which is set to 0. By adjusting the IMP, the spiking neurons can generate additional firing patterns and pattern mappings. Furthermore, we find that in static tasks, the accuracy of SNNs at each time step increases as the membrane potential evolves from zero. This observation inspires us to propose a learnable IMP, which can accelerate the evolution of membrane potential and enables higher performance within a limited number of time steps. Additionally, we introduce the last time step (LTS) approach to accelerate convergence in static tasks, and we propose a label smooth temporal efficient training (TET) loss to mitigate the conflicts between optimization objective and regularization term in the vanilla TET. Our methods improve the accuracy by 4.05\\% on ImageNet compared to baseline and achieve state-of-the-art performance of 87.80\\% on CIFAR10-DVS and 87.86\\% on N-Caltech101."
status: "auto-generated; brief scan note"
---
## Core Problem

Despite spiking neural networks (SNNs) have demonstrated notable energy efficiency across
various fields, the limited firing patterns of spiking neurons within fixed time steps
restrict the expression of information, which impedes further improvement of SNN
performance.

## Core Method

In addition, current implementations of SNNs typically consider the firing rate or average
membrane potential of the last layer as the output, lacking exploration of other
possibilities.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Manual boundary check: generic SNN method;
event-camera evidence appears mainly as CIFAR10-DVS/N-Caltech101 benchmark usage.。 备注：strict
two-stage rescan; official abstract/page inspected; Track: Main Conference Track; needs
human verification.。
