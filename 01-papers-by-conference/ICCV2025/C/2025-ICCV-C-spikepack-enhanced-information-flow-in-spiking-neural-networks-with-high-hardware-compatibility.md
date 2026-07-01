---
title: 'SpikePack: Enhanced Information Flow in Spiking Neural Networks with High Hardware Compatibility'
authors: ['Guobin Shen', 'Jindong Li', 'Tenglong Li', 'Dongcheng Zhao', 'Yi Zeng']
conference: 'ICCV'
year: 2025
level: 'C'
category: 'SNN'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Shen_SpikePack_Enhanced_Information_Flow_in_Spiking_Neural_Networks_with_High_ICCV_2025_paper.html'
tags: []
abstract: 'Spiking Neural Networks (SNNs) hold promise for energy-efficient, biologically inspired computing. We identify substantial information loss during spike transmission, linked to temporal dependencies in traditional Leaky Integrate-and-Fire (LIF) neurons--a key factor potentially limiting SNN performance. Existing SNN architectures also underutilize modern GPUs, constrained by single-bit spike storage and isolated weight-spike operations that restrict computational efficiency. We introduce SpikePack, a neuron model designed to reduce transmission loss while preserving essential features like membrane potential reset and leaky integration. SpikePack achieves constant \\mathcal O (1) time and space complexity, enabling efficient parallel processing on GPUs and also supporting serial inference on existing SNN hardware accelerators. Compatible with standard Artificial Neural Network (ANN) architectures, SpikePack facilitates near-lossless ANN-to-SNN conversion across various networks. Experimental results on tasks such as image classification, detection, and segmentation show SpikePack achieves significant gains in accuracy and efficiency for both directly trained and converted SNNs over state-of-the-art models. Tests on FPGA-based platforms further confirm cross-platform flexibility, delivering high performance and enhanced sparsity. By enhancing information flow and rethinking SNN-ANN integration, SpikePack advances efficient SNN deployment across diverse hardware platforms.'
status: 'auto-generated; brief scan note'
---
## Core Problem

SNN 方向的核心问题通常是脉冲表示的稳定性、效率或结构设计。

## Core Method

论文围绕 spiking neural networks / spiking transformers 展开，并针对其结构或训练做改进。

## Key Metrics and Findings

需要结合正文核对定量结果；当前仅确认其属于 SNN 背景论文。

## Personal Notes

可作为 SNN 侧背景论文进入对应方法章节。
