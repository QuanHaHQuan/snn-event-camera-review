---
title: "NDOT: Neuronal Dynamics-based Online Training for Spiking Neural Networks"
authors: ["Haiyan Jiang, Giulia De Masi, Huan Xiong, Bin Gu"]
conference: "ICML"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jiang24a/jiang24a.pdf"
official_page: "https://proceedings.mlr.press/v235/jiang24a.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) are attracting great attention for their energy-efficient and fast-inference properties in neuromorphic computing. However, the efficient training of deep SNNs poses challenges in gradient calculation due to the non-differentiability of their binary spike-generating activation functions. The widely used surrogate gradient (SG) method, combined with the back-propagation through time (BPTT), has shown considerable effectiveness. Yet, BPTT’s process of unfolding and back-propagating along the computation graph requires storing intermediate information at all time-steps, resulting in huge memory consumption and failing to meet online requirements. In this work, we propose Neuronal Dynamics-based Online Training (NDOT) for SNNs, which uses the neuronal dynamics-based temporal dependency/sensitivity in gradient computation. NDOT enables forward-in-time learning by decomposing the full gradient into temporal and spatial gradients. To illustrate the intuition behind NDOT, we employ the Follow-the-Regularized-Leader (FTRL) algorithm. FTRL explicitly utilizes historical information and addresses limitations in instantaneous loss. Our proposed NDOT method accurately captures temporal dependencies through neuronal dynamics, functioning similarly to FTRL’s explicit utilizing historical information. Experiments on CIFAR-10, CIFAR-100, and CIFAR10-DVS demonstrate the superior performance of our NDOT method on large-scale static and neuromorphic datasets within a small number of time steps. The codes are available at https://github.com/HaiyanJiang/SNN-NDOT."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs) are attracting great attention for their energy-efficient and
fast-inference properties in neuromorphic computing.

## Core Method

However, the efficient training of deep SNNs poses challenges in gradient calculation due to
the non-differentiability of their binary spike-generating activation functions.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Manual boundary check: generic SNN online-
training method; event-camera evidence appears mainly as CIFAR10-DVS benchmark usage.。
备注：strict two-stage screening; official abstract/page inspected; main conference; needs
human verification。
