---
title: "Towards efficient deep spiking neural networks construction with spiking activity based pruning"
authors: ["Yaxin Li, Qi Xu, Jiangrong Shen, Hongming Xu, Long Chen, Gang Pan"]
conference: "ICML"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bz/li24bz.pdf"
official_page: "https://proceedings.mlr.press/v235/li24bz.html"
tags: []
abstract: "The emergence of deep and large-scale spiking neural networks (SNNs) exhibiting high performance across diverse complex datasets has led to a need for compressing network models due to the presence of a significant number of redundant structural units, aiming to more effectively leverage their low-power consumption and biological interpretability advantages. Currently, most model compression techniques for SNNs are based on unstructured pruning of individual connections, which requires specific hardware support. Hence, we propose a structured pruning approach based on the activity levels of convolutional kernels named Spiking Channel Activity-based (SCA) network pruning framework. Inspired by synaptic plasticity mechanisms, our method dynamically adjusts the network’s structure by pruning and regenerating convolutional kernels during training, enhancing the model’s adaptation to the current target task. While maintaining model performance, this approach refines the network architecture, ultimately reducing computational load and accelerating the inference process. This indicates that structured dynamic sparse learning methods can better facilitate the application of deep SNNs in low-power and high-efficiency scenarios."
status: "auto-generated; brief scan note"
---
## Core Problem

The emergence of deep and large-scale spiking neural networks (SNNs) exhibiting high
performance across diverse complex datasets has led to a need for compressing network models
due to the presence of a significant number of redundant structural units, aiming to more
effectively leverage their low-power consumption and biological interpretability advantages.

## Core Method

Currently, most model compression techniques for SNNs are based on unstructured pruning of
individual connections, which requires specific hardware support.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage screening; official abstract/page inspected; main conference; needs human
verification。
