---
title: "Take A Shortcut Back: Mitigating the Gradient Vanishing for Training Spiking Neural Networks"
authors: ["Yufei Guo, Yuanpei Chen, Zecheng Hao, Weihang Peng, Zhou Jie, Yuhan Zhang, Xiaode Liu, Zhe Ma"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/2c37c5bcef24b9541550261dcd63261b-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/2c37c5bcef24b9541550261dcd63261b-Abstract-Conference.html"
tags: []
abstract: "The Spiking Neural Network (SNN) is a biologically inspired neural network infrastructure that has recently garnered significant attention. It utilizes binary spike activations to transmit information, thereby replacing multiplications with additions and resulting in high energy efficiency. However, training an SNN directly poses a challenge due to the undefined gradient of the firing spike process. Although prior works have employed various surrogate gradient training methods that use an alternative function to replace the firing process during back-propagation, these approaches ignore an intrinsic problem: gradient vanishing. To address this issue, we propose a shortcut back-propagation method in the paper, which advocates for transmitting the gradient directly from the loss to the shallow layers. This enables us to present the gradient to the shallow layers directly, thereby significantly mitigating the gradient vanishing problem. Additionally, this method does not introduce any burden during the inference phase.To strike a balance between final accuracy and ease of training, we also propose an evolutionary training framework and implement it by inducing a balance coefficient that dynamically changes with the training epoch, which further improves the network's performance. Extensive experiments conducted over static and dynamic datasets using several popular network structures reveal that our method consistently outperforms state-of-the-art methods."
status: "auto-generated; brief scan note"
---
## Core Problem

The Spiking Neural Network (SNN) is a biologically inspired neural network infrastructure
that has recently garnered significant attention.

## Core Method

It utilizes binary spike activations to transmit information, thereby replacing
multiplications with additions and resulting in high energy efficiency.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage rescan; official abstract/page inspected; Track: Main Conference Track; needs human
verification.。
