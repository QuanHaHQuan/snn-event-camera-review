---
title: "SpikePack: Enhanced Information Flow in Spiking Neural Networks with High Hardware Compatibility"
authors: ["Guobin Shen", "Jindong Li", "Tenglong Li", "Dongcheng Zhao", "Yi Zeng"]
conference: "ICCV"
year: 2025
level: "C"
category: "SNN"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Shen_SpikePack_Enhanced_Information_Flow_in_Spiking_Neural_Networks_with_High_ICCV_2025_paper.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) hold promise for energy-efficient, biologically inspired computing. We identify substantial information loss during spike transmission, linked to temporal dependencies in traditional Leaky Integrate-and-Fire (LIF) neurons--a key factor potentially limiting SNN performance. Existing SNN architectures also underutilize modern GPUs, constrained by single-bit spike storage and isolated weight-spike operations that restrict computational efficiency. We introduce SpikePack, a neuron model designed to reduce transmission loss while preserving essential features like membrane potential reset and leaky integration. SpikePack achieves constant \\mathcal O (1) time and space complexity, enabling efficient parallel processing on GPUs and also supporting serial inference on existing SNN hardware accelerators. Compatible with standard Artificial Neural Network (ANN) architectures, SpikePack facilitates near-lossless ANN-to-SNN conversion across various networks. Experimental results on tasks such as image classification, detection, and segmentation show SpikePack achieves significant gains in accuracy and efficiency for both directly trained and converted SNNs over state-of-the-art models. Tests on FPGA-based platforms further confirm cross-platform flexibility, delivering high performance and enhanced sparsity. By enhancing information flow and rethinking SNN-ANN integration, SpikePack advances efficient SNN deployment across diverse hardware platforms."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks (SNNs) hold promise for energy-efficient, biologically inspired computing.

## Core Method

We identify substantial information loss during spike transmission, linked to temporal dependencies in traditional Leaky Integrate-and-Fire (LIF) neurons--a key factor potentially limiting SNN performance.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns; leaky integrate-and-fire; integrate-and-fire; lif; ann-to-snn`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
