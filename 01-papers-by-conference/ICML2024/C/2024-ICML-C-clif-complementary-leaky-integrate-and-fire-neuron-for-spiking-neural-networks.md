---
title: "CLIF: Complementary Leaky Integrate-and-Fire Neuron for Spiking Neural Networks"
authors: ["Yulong Huang, Xiaopeng Lin, Hongwei Ren, Haotian Fu, Yue Zhou, Zunchang Liu, Biao Pan, Bojun Cheng"]
conference: "ICML"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24n/huang24n.pdf"
official_page: "https://proceedings.mlr.press/v235/huang24n.html"
tags: []
abstract: "Spiking neural networks (SNNs) are promising brain-inspired energy-efficient models. Compared to conventional deep Artificial Neural Networks (ANNs), SNNs exhibit superior efficiency and capability to process temporal information. However, it remains a challenge to train SNNs due to their undifferentiable spiking mechanism. The surrogate gradients method is commonly used to train SNNs, but often comes with an accuracy disadvantage over ANNs counterpart. We link the degraded accuracy to the vanishing of gradient on the temporal dimension through the analytical and experimental study of the training process of Leaky Integrate-and-Fire (LIF) Neuron-based SNNs. Moreover, we propose the Complementary Leaky Integrate-and-Fire (CLIF) Neuron. CLIF creates extra paths to facilitate the backpropagation in computing temporal gradient while keeping binary output. CLIF is hyperparameter-free and features broad applicability. Extensive experiments on a variety of datasets demonstrate CLIF’s clear performance advantage over other neuron models. Furthermore, the CLIF’s performance even slightly surpasses superior ANNs with identical network structure and training conditions. The code is available at https://github.com/HuuYuLong/Complementary-LIF."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking neural networks (SNNs) are promising brain-inspired energy-efficient models.

## Core Method

Compared to conventional deep Artificial Neural Networks (ANNs), SNNs exhibit superior
efficiency and capability to process temporal information.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; leaky integrate-and-fire; integrate-and-fire;
spiking。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural computation; no
clear event-camera/DVS evidence found.。 备注：strict two-stage screening; official
abstract/page inspected; main conference; needs human verification。
