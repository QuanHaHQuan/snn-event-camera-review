---
title: "Robust Stable Spiking Neural Networks"
authors: ["Jianhao Ding, Zhiyu Pan, Yujia Liu, Zhaofei Yu, Tiejun Huang"]
conference: "ICML"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ding24e/ding24e.pdf"
official_page: "https://proceedings.mlr.press/v235/ding24e.html"
tags: []
abstract: "Spiking neural networks (SNNs) are gaining popularity in deep learning due to their low energy budget on neuromorphic hardware. However, they still face challenges in lacking sufficient robustness to guard safety-critical applications such as autonomous driving. Many studies have been conducted to defend SNNs from the threat of adversarial attacks. This paper aims to uncover the robustness of SNN through the lens of the stability of nonlinear systems. We are inspired by the fact that searching for parameters altering the leaky integrate-and-fire dynamics can enhance their robustness. Thus, we dive into the dynamics of membrane potential perturbation and simplify the formulation of the dynamics. We present that membrane potential perturbation dynamics can reliably convey the intensity of perturbation. Our theoretical analyses imply that the simplified perturbation dynamics satisfy input-output stability. Thus, we propose a training framework with modified SNN neurons and to reduce the mean square of membrane potential perturbation aiming at enhancing the robustness of SNN. Finally, we experimentally verify the effectiveness of the framework in the setting of Gaussian noise training and adversarial training on the image classification task. Please refer to https://github.com/DingJianhao/stable-snn for our code implementation."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking neural networks (SNNs) are gaining popularity in deep learning due to their low
energy budget on neuromorphic hardware.

## Core Method

However, they still face challenges in lacking sufficient robustness to guard safety-
critical applications such as autonomous driving.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage screening; official abstract/page inspected; main conference; needs human
verification。
