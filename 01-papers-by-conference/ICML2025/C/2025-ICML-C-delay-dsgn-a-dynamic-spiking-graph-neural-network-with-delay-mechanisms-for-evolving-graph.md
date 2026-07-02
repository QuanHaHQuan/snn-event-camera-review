---
title: "Delay-DSGN: A Dynamic Spiking Graph Neural Network with Delay Mechanisms for Evolving Graph"
authors: ["Zhiqiang Wang", "Jianghao Wen", "Jianqing Liang"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dm/wang25dm.pdf"
official_page: "https://proceedings.mlr.press/v267/wang25dm.html"
tags: []
abstract: "Dynamic graph representation learning using Spiking Neural Networks (SNNs) exploits the temporal spiking behavior of neurons, offering advantages in capturing the temporal evolution and sparsity of dynamic graphs. However, existing SNN-based methods often fail to effectively capture the impact of latency in information propagation on node representations. To address this, we propose Delay-DSGN, a dynamic spiking graph neural network incorporating a learnable delay mechanism. By leveraging synaptic plasticity, the model dynamically adjusts connection weights and propagation speeds, enhancing temporal correlations and enabling historical data to influence future representations. Specifically, we introduce a Gaussian delay kernel into the neighborhood aggregation process at each time step, adaptively delaying historical information to future time steps and mitigating information forgetting. Experiments on three large-scale dynamic graph datasets demonstrate that Delay-DSGN outperforms eight state-of-the-art methods, achieving the best results in node classification tasks. We also theoretically derive the constraint conditions between the Gaussian kernel’s standard deviation and size, ensuring stable training and preventing gradient explosion and vanishing issues."
status: "auto-generated; brief scan note"
---

## Core Problem

Dynamic graph representation learning using Spiking Neural Networks (SNNs) exploits the temporal spiking behavior of neurons, offering advantages in capturing the temporal evolution and sparsity of dynamic graphs.

## Core Method

However, existing SNN-based methods often fail to effectively capture the impact of latency in information propagation on node representations.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：spiking。自动分类理由：Official abstract/page confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
