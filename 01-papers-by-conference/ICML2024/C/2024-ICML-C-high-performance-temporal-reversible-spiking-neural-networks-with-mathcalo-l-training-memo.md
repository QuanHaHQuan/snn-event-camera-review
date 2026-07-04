---
title: "High-Performance Temporal Reversible Spiking Neural Networks with $\\mathcalO(L)$ Training Memory and $\\mathcalO(1)$ Inference Cost"
authors: ["Jiakui Hu, Man Yao, Xuerui Qiu, Yuhong Chou, Yuxuan Cai, Ning Qiao, Yonghong Tian, Bo Xu, Guoqi Li"]
conference: "ICML"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24q/hu24q.pdf"
official_page: "https://proceedings.mlr.press/v235/hu24q.html"
tags: []
abstract: "Multi-timestep simulation of brain-inspired Spiking Neural Networks (SNNs) boost memory requirements during training and increase inference energy cost. Current training methods cannot simultaneously solve both training and inference dilemmas. This work proposes a novel Temporal Reversible architecture for SNNs (T-RevSNN) to jointly address the training and inference challenges by altering the forward propagation of SNNs. We turn off the temporal dynamics of most spiking neurons and design multi-level temporal reversible interactions at temporal turn-on spiking neurons, resulting in a $\\mathcal{O}(L)$ training memory. Combined with the temporal reversible nature, we redesign the input encoding and network organization of SNNs to achieve $\\mathcal{O}(1)$ inference energy cost. Then, we finely adjust the internal units and residual connections of the basic SNN block to ensure the effectiveness of sparse temporal information interaction. T-RevSNN achieves excellent accuracy on ImageNet, while the memory efficiency, training time acceleration and inference energy efficiency can be significantly improved by $8.6 \\times$, $2.0 \\times$ and $1.6 \\times$, respectively. This work is expected to break the technical bottleneck of significantly increasing memory cost and training time for large-scale SNNs while maintaining both high performance and low inference energy cost."
status: "auto-generated; brief scan note"
---
## Core Problem

Multi-timestep simulation of brain-inspired Spiking Neural Networks (SNNs) boost memory
requirements during training and increase inference energy cost.

## Core Method

Current training methods cannot simultaneously solve both training and inference dilemmas.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage screening; official abstract/page inspected; main conference; needs human
verification。
