---
title: "Online Stabilization of Spiking Neural Networks"
authors: ["Yaoyu Zhu, Jianhao Ding, Tiejun Huang, Xiaodong Xie, Zhaofei Yu"]
conference: "ICLR"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/eb261df4322a8bd0a73093c4d8a0d02d-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/eb261df4322a8bd0a73093c4d8a0d02d-Abstract-Conference.html"
tags: []
abstract: "Spiking neural networks (SNNs), attributed to the binary, event-driven nature of spikes, possess heightened biological plausibility and enhanced energy efficiency on neuromorphic hardware compared to analog neural networks (ANNs). Mainstream SNN training schemes apply backpropagation-through-time (BPTT) with surrogate gradients to replace the non-differentiable spike emitting process during backpropagation. While achieving competitive performance, the requirement for storing intermediate information at all time-steps incurs higher memory consumption and fails to fulfill the online property crucial to biological brains. Our work focuses on online training techniques, aiming for memory efficiency while preserving biological plausibility. The limitation of not having access to future information in early time steps in online training has constrained previous efforts to incorporate advantageous modules such as batch normalization. To address this problem, we propose Online Spiking Renormalization (OSR) to ensure consistent parameters between testing and training, and Online Threshold Stabilizer (OTS) to stabilize neuron firing rates across time steps. Furthermore, we design a novel online approach to compute the sample mean and variance over time for OSR. Experiments conducted on various datasets demonstrate the proposed method's superior performance among SNN online training algorithms.Our code is available at https://github.com/zhuyaoyu/SNN-online-normalization."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking neural networks (SNNs), attributed to the binary, event-driven nature of spikes,
possess heightened biological plausibility and enhanced energy efficiency on neuromorphic
hardware compared to analog neural networks (ANNs).

## Core Method

Mainstream SNN training schemes apply backpropagation-through-time (BPTT) with surrogate
gradients to replace the non-differentiable spike emitting process during backpropagation.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage screening; official abstract/page inspected; main conference; needs human
verification。
