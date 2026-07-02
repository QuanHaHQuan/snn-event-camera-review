---
title: "Faster and Stronger: When ANN-SNN Conversion Meets Parallel Spiking Calculation"
authors: ["Zecheng Hao", "Qichao Ma", "Kang Chen", "Yi Zhang", "Zhaofei Yu", "Tiejun Huang"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/hao25c/hao25c.pdf"
official_page: "https://proceedings.mlr.press/v267/hao25c.html"
tags: []
abstract: "Spiking Neural Network (SNN), as a brain-inspired and energy-efficient network, is currently facing the pivotal challenge of exploring a suitable and efficient learning framework. The predominant training methodologies, namely Spatial-Temporal Back-propagation (STBP) and ANN-SNN Conversion, are encumbered by substantial training overhead or pronounced inference latency, which impedes the advancement of SNNs in scaling to larger networks and navigating intricate application domains. In this work, we propose a novel parallel conversion learning framework, which establishes a mathematical mapping relationship between each time-step of the parallel spiking neurons and the cumulative spike firing rate. We theoretically validate the lossless and sorting properties of the conversion process, as well as pointing out the optimal shifting distance for each step. Furthermore, by integrating the above framework with the distribution-aware error calibration technique, we can achieve efficient conversion towards more general activation functions or training-free circumstance. Extensive experiments have confirmed the significant performance advantages of our method for various conversion cases under ultra-low time latency. To our best knowledge, this is the first work which jointly utilizes parallel spiking calculation and ANN-SNN Conversion, providing a highly promising approach for SNN supervised training. Code is available at https://github.com/hzc1208/Parallel_Conversion."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Network (SNN), as a brain-inspired and energy-efficient network, is currently facing the pivotal challenge of exploring a suitable and efficient learning framework.

## Core Method

The predominant training methodologies, namely Spatial-Temporal Back-propagation (STBP) and ANN-SNN Conversion, are encumbered by substantial training overhead or pronounced inference latency, which impedes the advancement of SNNs in scaling to larger networks and navigating intricate application domains.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：snn; spiking。自动分类理由：Official abstract/page confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
