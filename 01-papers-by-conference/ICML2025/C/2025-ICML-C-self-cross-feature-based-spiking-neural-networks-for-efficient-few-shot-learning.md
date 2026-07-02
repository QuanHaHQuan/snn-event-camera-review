---
title: "Self-cross Feature based Spiking Neural Networks for Efficient Few-shot Learning"
authors: ["Qi Xu, Junyang Zhu, Dongdong Zhou, Hao Chen, Yang Liu, Jiangrong Shen, Qiang Zhang"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25aq/xu25aq.pdf"
official_page: "https://proceedings.mlr.press/v267/xu25aq.html"
tags: []
abstract: "Deep neural networks (DNNs) excel in computer vision tasks, especially, few-shot learning (FSL), which is increasingly important for generalizing from limited examples. However, DNNs are computationally expensive with scalability issues in real world. Spiking Neural Networks (SNNs), with their event-driven nature and low energy consumption, are particularly efficient in processing sparse and dynamic data, though they still encounter difficulties in capturing complex spatiotemporal features and performing accurate cross-class comparisons. To further enhance the performance and efficiency of SNNs in few-shot learning, we propose a few-shot learning framework based on SNNs, which combines a self-feature extractor module and a cross-feature contrastive module to refine feature representation and reduce power consumption. We apply the combination of temporal efficient training loss and InfoNCE loss to optimize the temporal dynamics of spike trains and enhance the discriminative power. Experimental results show that the proposed FSL-SNN significantly improves the classification performance on the neuromorphic dataset N-Omniglot, and also achieves competitive performance to ANNs on static datasets such as CUB and miniImageNet with low power consumption."
status: "auto-generated; brief scan note"
---

## Core Problem

Deep neural networks (DNNs) excel in computer vision tasks, especially, few-shot learning (FSL), which is increasingly important for generalizing from limited examples.

## Core Method

However, DNNs are computationally expensive with scalability issues in real world.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns; spike trains`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
