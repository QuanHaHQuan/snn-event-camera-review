---
title: "LMUFormer: Low Complexity Yet Powerful Spiking Model With Legendre Memory Units"
authors: ["Zeyu Liu, Gourav Datta, Anni Li, Peter Beerel"]
conference: "ICLR"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/3353b22e6b85a76d45d6b01aa4328be5-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/3353b22e6b85a76d45d6b01aa4328be5-Abstract-Conference.html"
tags: []
abstract: "Transformer models have demonstrated high accuracy in numerous applications but have high complexity and lack sequential processing capability making them ill-suited for many streaming applications at the edge where devices are heavily resource-constrained. Thus motivated, many researchers have proposed reformulating the transformer models as RNN modules which modify the self-attention computation with explicit states. However, these approaches often incur significant performance degradation.The ultimate goal is to develop a model that has the following properties: parallel training, streaming and low-cost inference, and state-of-the-art (SOTA) performance. In this paper, we propose a new direction to achieve this goal. We show how architectural modifications to a fully-sequential recurrent model can help push its performance toward Transformer models while retaining its sequential processing capability. Specifically, inspired by the recent success of Legendre Memory Units (LMU) in sequence learning tasks, we propose LMUFormer, which augments the LMU with convolutional patch embedding and convolutional channel mixer. Moreover, we present a spiking version of this architecture, which introduces the benefit of states within the patch embedding and channel mixer modules while simultaneously reducing the computing complexity. We evaluated our architectures on multiple sequence datasets. Of particular note is our performance on the Speech Commands V2 dataset (35 classes). In comparison to SOTA transformer-based models within the ANN domain, our LMUFormer demonstrates comparable performance while necessitating a remarkable $70\\times$ reduction in parameters and a substantial $140\\times$ decrement in FLOPs. Furthermore, when benchmarked against extant low-complexity SNN variants, our model establishes a new SOTA with an accuracy of 96.12\\%. Additionally, owing to our model's proficiency in real-time data processing, we are able to achieve a 32.03\\% reduction in sequence length, all while incurring an inconsequential decline in performance."
status: "auto-generated; brief scan note"
---
## Core Problem

Transformer models have demonstrated high accuracy in numerous applications but have high
complexity and lack sequential processing capability making them ill-suited for many
streaming applications at the edge where devices are heavily resource-constrained.

## Core Method

Thus motivated, many researchers have proposed reformulating the transformer models as RNN
modules which modify the self-attention computation with explicit states.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence found.。 备注：strict two-stage screening;
official abstract/page inspected; main conference; needs human verification。
