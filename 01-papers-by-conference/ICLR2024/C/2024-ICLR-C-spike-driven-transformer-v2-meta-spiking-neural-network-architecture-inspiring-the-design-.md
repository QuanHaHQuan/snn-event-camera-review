---
title: "Spike-driven Transformer V2: Meta Spiking Neural Network Architecture Inspiring the Design of Next-generation Neuromorphic Chips"
authors: ["Man Yao, Jiakui Hu, Tianxiang Hu, Yifan Xu, Zhaokun Zhou, Yonghong Tian, Bo XU, Guoqi Li"]
conference: "ICLR"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/e9882f7f7c44a10acc01132302bac9d8-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9882f7f7c44a10acc01132302bac9d8-Abstract-Conference.html"
tags: []
abstract: "Neuromorphic computing, which exploits Spiking Neural Networks (SNNs) on neuromorphic chips, is a promising energy-efficient alternative to traditional AI. CNN-based SNNs are the current mainstream of neuromorphic computing. By contrast, no neuromorphic chips are designed especially for Transformer-based SNNs, which have just emerged, and their performance is only on par with CNN-based SNNs, offering no distinct advantage. In this work, we propose a general Transformer-based SNN architecture, termed as ``Meta-SpikeFormer\", whose goals are: (1) Lower-power , supports the spike-driven paradigm that there is only sparse addition in the network; (2) Versatility , handles various vision tasks; (3) High-performance , shows overwhelming performance advantages over CNN-based SNNs; (4) Meta-architecture , provides inspiration for future next-generation Transformer-based neuromorphic chip designs. Specifically, we extend the Spike-driven Transformer in \\citet{yao2023spike} into a meta architecture, and explore the impact of structure, spike-driven self-attention, and skip connection on its performance. On ImageNet-1K, Meta-SpikeFormer achieves 80.0\\% top-1 accuracy (55M), surpassing the current state-of-the-art (SOTA) SNN baselines (66M) by 3.7\\%. This is the first direct training SNN backbone that can simultaneously supports classification, detection, and segmentation, obtaining SOTA results in SNNs. Finally, we discuss the inspiration of the meta SNN architecture for neuromorphic chip design."
status: "auto-generated; brief scan note"
---
## Core Problem

Neuromorphic computing, which exploits Spiking Neural Networks (SNNs) on neuromorphic chips,
is a promising energy-efficient alternative to traditional AI.

## Core Method

CNN-based SNNs are the current mainstream of neuromorphic computing.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural network; spike; spiking。自动分类理由：Official abstract/page strictly
confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。
备注：strict two-stage screening; official abstract/page inspected; main conference; needs
human verification。
