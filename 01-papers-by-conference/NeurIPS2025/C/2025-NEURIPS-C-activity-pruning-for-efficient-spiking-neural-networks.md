---
title: "Activity Pruning for Efficient Spiking Neural Networks"
authors: ["Tong Bu, Xinyu Shi, Zhaofei Yu"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/fa12d67b5939c37ea8a4659c31a08d2c-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/fa12d67b5939c37ea8a4659c31a08d2c-Abstract-Conference.html"
tags: []
abstract: "While sparse coding plays an important role in promoting the efficiency of biological neural systems, it has not been fully utilized by artificial models as the activation sparsity is not well suited to the current structure of deep networks. Spiking Neural Networks (SNNs), with their event-driven characteristics, offer a more natural platform for leveraging activation sparsity. In this work, we specifically target the reduction of neuronal activity, which directly leads to lower computational cost and facilitates efficient SNN deployment on Neuromorphic hardware. We begin by analyzing the limitations of existing activity regularization methods and identifying critical challenges in training sparse SNNs. To address these issues, we propose a modified neuron model, AT-LIF, coupled with a threshold adaptation technique that stabilizes training and effectively suppresses spike activity. Through extensive experiments on multiple datasets, we demonstrate that our approach achieves significant reductions in average firing rates and synaptic operations without sacrificing much accuracy. Furthermore, we show that our method complements weight-based pruning techniques and successfully trains an SNN with only 0.06 average firing rate and 2.22M parameters on ImageNet, highlighting its potential for building highly efficient and scalable SNN models. Code is available at https://github.com/putshua/Activity-Pruning-SNN."
status: "auto-generated; brief scan note"
---

## Core Problem

While sparse coding plays an important role in promoting the efficiency of biological neural systems, it has not been fully utilized by artificial models as the activation sparsity is not well suited to the current structure of deep networks.

## Core Method

Spiking Neural Networks (SNNs), with their event-driven characteristics, offer a more natural platform for leveraging activation sparsity.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns; lif`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
