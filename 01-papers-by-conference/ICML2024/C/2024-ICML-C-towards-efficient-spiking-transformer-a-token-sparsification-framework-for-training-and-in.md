---
title: "Towards Efficient Spiking Transformer: a Token Sparsification Framework for Training and Inference Acceleration"
authors: ["Zhengyang Zhuge, Peisong Wang, Xingting Yao, Jian Cheng"]
conference: "ICML"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhuge24b/zhuge24b.pdf"
official_page: "https://proceedings.mlr.press/v235/zhuge24b.html"
tags: []
abstract: "Nowadays Spiking Transformers have exhibited remarkable performance close to Artificial Neural Networks (ANNs), while enjoying the inherent energy-efficiency of Spiking Neural Networks (SNNs). However, training Spiking Transformers on GPUs is considerably more time-consuming compared to the ANN counterparts, despite the energy-efficient inference through neuromorphic computation. In this paper, we investigate the token sparsification technique for efficient training of Spiking Transformer and find conventional methods suffer from noticeable performance degradation. We analyze the issue and propose our Sparsification with Timestep-wise Anchor Token and dual Alignments (STATA). Timestep-wise Anchor Token enables precise identification of important tokens across timesteps based on standardized criteria. Additionally, dual Alignments incorporate both Intra and Inter Alignment of the attention maps, fostering the learning of inferior attention. Extensive experiments show the effectiveness of STATA thoroughly, which demonstrates up to $\\sim$1.53$\\times$ training speedup and $\\sim$48% energy reduction with comparable performance on various datasets and architectures."
status: "auto-generated; brief scan note"
---
## Core Problem

Nowadays Spiking Transformers have exhibited remarkable performance close to Artificial
Neural Networks (ANNs), while enjoying the inherent energy-efficiency of Spiking Neural
Networks (SNNs).

## Core Method

However, training Spiking Transformers on GPUs is considerably more time-consuming compared
to the ANN counterparts, despite the energy-efficient inference through neuromorphic
computation.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking transformer; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage screening; official abstract/page inspected; main conference; needs human
verification。
