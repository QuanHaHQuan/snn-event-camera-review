---
title: "Training High Performance Spiking Neural Network by Temporal Model Calibration"
authors: ["Jiaqi Yan, Changping Wang, De Ma, Huajin Tang, Qian Zheng, Gang Pan"]
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

严格两阶段复扫：标题宽召回命中 `dvs visual-event context; spiking neural networks; snns; spiking neurons`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
