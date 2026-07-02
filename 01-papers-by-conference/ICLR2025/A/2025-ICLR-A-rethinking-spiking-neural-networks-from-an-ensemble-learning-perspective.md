---
title: "Rethinking Spiking Neural Networks from an Ensemble Learning Perspective"
authors: ["Yongqi Ding", "Lin Zuo", "Mengmeng Jing", "Pei He", "Hanpu Deng"]
conference: "ICLR"
year: 2025
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2025/file/5543342b8c45c0cba04f832390cfb23c-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/5543342b8c45c0cba04f832390cfb23c-Abstract-Conference.html"
tags: []
abstract: "Spiking neural networks (SNNs) exhibit superior energy efficiency but suffer from limited performance. In this paper, we consider SNNs as ensembles of temporal subnetworks that share architectures and weights, and highlight a crucial issue that affects their performance: excessive differences in initial states (neuronal membrane potentials) across timesteps lead to unstable subnetwork outputs, resulting in degraded performance. To mitigate this, we promote the consistency of the initial membrane potential distribution and output through membrane potential smoothing and temporally adjacent subnetwork guidance, respectively, to improve overall stability and performance. Moreover, membrane potential smoothing facilitates forward propagation of information and backward propagation of gradients, mitigating the notorious temporal gradient vanishing problem. Our method requires only minimal modification of the spiking neurons without adapting the network structure, making our method generalizable and showing consistent performance gains in 1D speech, 2D object, and 3D point cloud recognition tasks. In particular, on the challenging CIFAR10-DVS dataset, we achieved 83.20\\% accuracy with only four timesteps. This provides valuable insights into unleashing the potential of SNNs."
status: "auto-generated; needs human review"
---

## Core Problem

Spiking neural networks (SNNs) exhibit superior energy efficiency but suffer from limited performance.

## Core Method

In this paper, we consider SNNs as ensembles of temporal subnetworks that share architectures and weights, and highlight a crucial issue that affects their performance: excessive differences in initial states (neuronal membrane potentials) across timesteps lead to unstable subnetwork outputs, resulting in degraded performance.

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
