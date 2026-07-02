---
title: "ReverB-SNN: Reversing Bit of the Weight and Activation for Spiking Neural Networks"
authors: ["Yufei Guo", "Yuhan Zhang", "Zhou Jie", "Xiaode Liu", "Xin Tong", "Yuanpei Chen", "Weihang Peng", "Zhe Ma"]
conference: "ICML"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25t/guo25t.pdf"
official_page: "https://proceedings.mlr.press/v267/guo25t.html"
tags: []
abstract: "The Spiking Neural Network (SNN), a biologically inspired neural network infrastructure, has garnered significant attention recently. SNNs utilize binary spike activations for efficient information transmission, replacing multiplications with additions, thereby enhancing energy efficiency. However, binary spike activation maps often fail to capture sufficient data information, resulting in reduced accuracy. To address this challenge, we advocate reversing the bit of the weight and activation, called ReverB , inspired by recent findings that highlight greater accuracy degradation from quantizing activations compared to weights. Specifically, our method employs real-valued spike activations alongside binary weights in SNNs. This preserves the event-driven and multiplication-free advantages of standard SNNs while enhancing the information capacity of activations. Additionally, we introduce a trainable factor within binary weights to adaptively learn suitable weight amplitudes during training, thereby increasing network capacity. To maintain efficiency akin to vanilla ReverB , our trainable binary weight SNNs are converted back to standard form using a re-parameterization technique during inference. Extensive experiments across various network architectures and datasets, both static and dynamic, demonstrate that our approach consistently outperforms state-of-the-art methods."
status: "auto-generated; brief scan note"
---

## Core Problem

The Spiking Neural Network (SNN), a biologically inspired neural network infrastructure, has garnered significant attention recently.

## Core Method

SNNs utilize binary spike activations for efficient information transmission, replacing multiplications with additions, thereby enhancing energy efficiency.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; snn; spiking。自动分类理由：Official abstract/page confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
