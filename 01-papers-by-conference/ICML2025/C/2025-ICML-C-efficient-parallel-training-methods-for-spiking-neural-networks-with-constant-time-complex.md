---
title: "Efficient Parallel Training Methods for Spiking Neural Networks with Constant Time Complexity"
authors: ["Wanjin Feng, Xingyu Gao, Wenqian Du, Hailong Shi, Peilin Zhao, Pengcheng Wu, Chunyan Miao"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25e/feng25e.pdf"
official_page: "https://proceedings.mlr.press/v267/feng25e.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) often suffer from high time complexity $O(T)$ due to the sequential processing of $T$ spikes, making training computationally expensive. In this paper, we propose a novel Fixed-point Parallel Training (FPT) method to accelerate SNN training without modifying the network architecture or introducing additional assumptions. FPT reduces the time complexity to $O(K)$, where $K$ is a small constant (usually $K=3$), by using a fixed-point iteration form of Leaky Integrate-and-Fire (LIF) neurons for all $T$ timesteps. We provide a theoretical convergence analysis of FPT and demonstrate that existing parallel spiking neurons can be viewed as special cases of our approach. Experimental results show that FPT effectively simulates the dynamics of original LIF neurons, significantly reducing computational time without sacrificing accuracy. This makes FPT a scalable and efficient solution for real-world applications, particularly for long-duration simulations."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks (SNNs) often suffer from high time complexity $O(T)$ due to the sequential processing of $T$ spikes, making training computationally expensive.

## Core Method

In this paper, we propose a novel Fixed-point Parallel Training (FPT) method to accelerate SNN training without modifying the network architecture or introducing additional assumptions.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns; spiking neurons; leaky integrate-and-fire; integrate-and-fire; lif`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
