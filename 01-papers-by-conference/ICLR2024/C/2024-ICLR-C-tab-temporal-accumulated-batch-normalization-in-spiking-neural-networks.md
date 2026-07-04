---
title: "TAB: Temporal Accumulated Batch Normalization in Spiking Neural Networks"
authors: ["Haiyan Jiang, Vincent Zoonekynd, Giulia De Masi, Bin Gu, Huan Xiong"]
conference: "ICLR"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/1bd8cfc0e4c53869b7f1d0ed4b1e78e1-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/1bd8cfc0e4c53869b7f1d0ed4b1e78e1-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) are attracting growing interest for their energy-efficient computing when implemented on neuromorphic hardware. However, directly training SNNs, even adopting batch normalization (BN), is highly challenging due to their non-differentiable activation function and the temporally delayed accumulation of outputs over time. For SNN training, this temporal accumulation gives rise to Temporal Covariate Shifts (TCS) along the temporal dimension, a phenomenon that would become increasingly pronounced with layer-wise computations across multiple layers and multiple time-steps. In this paper, we introduce TAB (Temporal Accumulated Batch Normalization), a novel SNN batch normalization method that addresses the temporal covariate shift issue by aligning with neuron dynamics (specifically the accumulated membrane potential) and utilizing temporal accumulated statistics for data normalization. Within its framework, TAB effectively encapsulates the historical temporal dependencies that underlie the membrane potential accumulation process, thereby establishing a natural connection between neuron dynamics and TAB batch normalization. Experimental results on CIFAR-10, CIFAR-100, and DVS-CIFAR10 show that our TAB method outperforms other state-of-the-art methods."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs) are attracting growing interest for their energy-efficient
computing when implemented on neuromorphic hardware.

## Core Method

However, directly training SNNs, even adopting batch normalization (BN), is highly
challenging due to their non-differentiable activation function and the temporally delayed
accumulation of outputs over time.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Manual boundary check: generic SNN batch-
normalization/training method; event-camera evidence appears mainly as DVS benchmark usage.。
备注：strict two-stage screening; official abstract/page inspected; main conference; needs
human verification。
