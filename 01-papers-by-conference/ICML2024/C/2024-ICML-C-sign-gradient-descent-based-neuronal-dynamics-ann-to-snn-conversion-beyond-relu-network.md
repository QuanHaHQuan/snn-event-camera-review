---
title: "Sign Gradient Descent-based Neuronal Dynamics: ANN-to-SNN Conversion Beyond ReLU Network"
authors: ["Hyunseok Oh, Youngki Lee"]
conference: "ICML"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/oh24b/oh24b.pdf"
official_page: "https://proceedings.mlr.press/v235/oh24b.html"
tags: []
abstract: "Spiking neural network (SNN) is studied in multidisciplinary domains to (i) enable order-of-magnitudes energy-efficient AI inference, and (ii) computationally simulate neuroscientific mechanisms. The lack of discrete theory obstructs the practical application of SNN by limiting its performance and nonlinearity support. We present a new optimization-theoretic perspective of the discrete dynamics of spiking neuron. We prove that a discrete dynamical system of simple integrate-and-fire models approximates the subgradient method over unconstrained optimization problems. We practically extend our theory to introduce a novel sign gradient descent (signGD)-based neuronal dynamics that can (i) approximate diverse nonlinearities beyond ReLU, and (ii) advance ANN-to-SNN conversion performance in low time-steps. Experiments on large-scale datasets show that our technique achieve (i) state-of-the-art performance in ANN-to-SNN conversion, and (ii) is first to convert new DNN architectures, e.g., ConvNext, MLP-Mixer, and ResMLP. We publicly share our source code at www.github.com/snuhcs/snn_signgd ."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking neural network (SNN) is studied in multidisciplinary domains to (i) enable order-of-
magnitudes energy-efficient AI inference, and (ii) computationally simulate neuroscientific
mechanisms.

## Core Method

The lack of discrete theory obstructs the practical application of SNN by limiting its
performance and nonlinearity support.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNN; ANN-to-SNN。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence found.。 备注：strict two-stage screening;
official abstract/page inspected; main conference; needs human verification。
