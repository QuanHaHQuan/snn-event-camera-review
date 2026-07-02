---
title: "Training High Performance Spiking Neural Network by Temporal Model Calibration"
authors: ["Jiaqi Yan", "Changping Wang", "De Ma", "Huajin Tang", "Qian Zheng", "Gang Pan"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25c/yan25c.pdf"
official_page: "https://proceedings.mlr.press/v267/yan25c.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) are considered promising energy-efficient models due to their dynamic capability to process spatial-temporal spike information. Existing work has demonstrated that SNNs exhibit temporal heterogeneity, which leads to diverse outputs of SNNs at different time steps and has the potential to enhance their performance. Although SNNs obtained by direct training methods achieve state-of-the-art performance, current methods introduce limited temporal heterogeneity through the dynamics of spiking neurons or network structures. They lack the improvement of temporal heterogeneity through the lens of the gradient. In this paper, we first conclude that the diversity of the temporal logit gradients in current methods is limited. This leads to insufficient temporal heterogeneity and results in temporally miscalibrated SNNs with degraded performance. Based on the above analysis, we propose a Temporal Model Calibration (TMC) method, which can be seen as a logit gradient rescaling mechanism across time steps. Experimental results show that our method can improve the temporal logit gradient diversity and generate temporally calibrated SNNs with enhanced performance. In particular, our method achieves state-of-the-art accuracy on ImageNet, DVSCIFAR10, and N-Caltech101. Codes are available at https://github.com/zju-bmi-lab/TMC."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks (SNNs) are considered promising energy-efficient models due to their dynamic capability to process spatial-temporal spike information.

## Core Method

Existing work has demonstrated that SNNs exhibit temporal heterogeneity, which leads to diverse outputs of SNNs at different time steps and has the potential to enhance their performance.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：spiking neural network; spiking。自动分类理由：Official abstract/page confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
