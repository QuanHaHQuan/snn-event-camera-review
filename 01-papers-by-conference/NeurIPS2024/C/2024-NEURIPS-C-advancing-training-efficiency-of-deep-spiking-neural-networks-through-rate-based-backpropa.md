---
title: "Advancing Training Efficiency of Deep Spiking Neural Networks through Rate-based Backpropagation"
authors: ["Chengting Yu, Lei Liu, Gaoang Wang, Erping Li, Aili Wang"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/d1bdc488ec18f64177b2275a03984683-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/d1bdc488ec18f64177b2275a03984683-Abstract-Conference.html"
tags: []
abstract: "Recent insights have revealed that rate-coding is a primary form of information representation captured by surrogate-gradient-based Backpropagation Through Time (BPTT) in training deep Spiking Neural Networks (SNNs). Motivated by these findings, we propose rate-based backpropagation, a training strategy specifically designed to exploit rate-based representations to reduce the complexity of BPTT. Our method minimizes reliance on detailed temporal derivatives by focusing on averaged dynamics, streamlining the computational graph to reduce memory and computational demands of SNNs training. We substantiate the rationality of the gradient approximation between BPTT and the proposed method through both theoretical analysis and empirical observations. Comprehensive experiments on CIFAR-10, CIFAR-100, ImageNet, and CIFAR10-DVS validate that our method achieves comparable performance to BPTT counterparts, and surpasses state-of-the-art efficient training techniques. By leveraging the inherent benefits of rate-coding, this work sets the stage for more scalable and efficient SNNs training within resource-constrained environments."
status: "auto-generated; brief scan note"
---
## Core Problem

Recent insights have revealed that rate-coding is a primary form of information
representation captured by surrogate-gradient-based Backpropagation Through Time (BPTT) in
training deep Spiking Neural Networks (SNNs).

## Core Method

Motivated by these findings, we propose rate-based backpropagation, a training strategy
specifically designed to exploit rate-based representations to reduce the complexity of
BPTT.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Manual boundary check: generic SNN training
method; event-camera evidence appears mainly as CIFAR10-DVS benchmark usage.。 备注：strict two-
stage rescan; official abstract/page inspected; Track: Main Conference Track; needs human
verification.。
