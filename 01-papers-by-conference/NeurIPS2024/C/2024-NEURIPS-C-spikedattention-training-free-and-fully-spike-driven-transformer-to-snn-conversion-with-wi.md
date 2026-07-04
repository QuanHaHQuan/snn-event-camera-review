---
title: "SpikedAttention: Training-Free and Fully Spike-Driven Transformer-to-SNN Conversion with Winner-Oriented Spike Shift for Softmax Operation"
authors: ["Sangwoo Hwang, Seunghyun Lee, Dahoon Park, Donghun Lee, Jaeha Kung"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/7c9341ad0263428b5057d92f4d88dfa0-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/7c9341ad0263428b5057d92f4d88dfa0-Abstract-Conference.html"
tags: []
abstract: "Event-driven spiking neural networks(SNNs) are promising neural networks that reduce the energy consumption of continuously growing AI models. Recently, keeping pace with the development of transformers, transformer-based SNNs were presented. Due to the incompatibility of self-attention with spikes, however, existing transformer-based SNNs limit themselves by either restructuring self-attention architecture or conforming to non-spike computations. In this work, we propose a novel transformer-to-SNN conversion method that outputs an end-to-end spike-based transformer, named SpikedAttention. Our method directly converts the well-trained transformer without modifying its attention architecture. For the vision task, the proposed method converts Swin Transformer into an SNN without post-training or conversion-aware training, achieving state-of-the-art SNN accuracy on ImageNet dataset, i.e., 80.0\\% with 28.7M parameters. Considering weight accumulation, neuron potential update, and on-chip data movement, SpikedAttention reduces energy consumption by 42\\% compared to the baseline ANN, i.e., Swin-T. Furthermore, for the first time, we demonstrate that SpikedAttention successfully converts a BERT model to an SNN with only 0.3\\% accuracy loss on average consuming 58\\% less energy on GLUE benchmark. Our code is available at Github ( https://github.com/sangwoohwang/SpikedAttention )."
status: "auto-generated; brief scan note"
---
## Core Problem

Event-driven spiking neural networks(SNNs) are promising neural networks that reduce the
energy consumption of continuously growing AI models.

## Core Method

Recently, keeping pace with the development of transformers, transformer-based SNNs were
presented.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNN; spike。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence found.。 备注：strict two-stage rescan; official
abstract/page inspected; Track: Main Conference Track; needs human verification.。
