---
title: "A Progressive Training Framework for Spiking Neural Networks with Learnable Multi-hierarchical Model"
authors: ["Zecheng Hao, Xinyu Shi, Zihan Huang, Tong Bu, Zhaofei Yu, Tiejun Huang"]
conference: "ICLR"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/148865706acbd18627d3fc15cc3f3b93-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/148865706acbd18627d3fc15cc3f3b93-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) have garnered considerable attention due to their energy efficiency and unique biological characteristics. However, the widely adopted Leaky Integrate-and-Fire (LIF) model, as the mainstream neuron model in current SNN research, has been revealed to exhibit significant deficiencies in deep-layer gradient calculation and capturing global information on the time dimension. In this paper, we propose the Learnable Multi-hierarchical (LM-H) model to address these issues by dynamically regulating its membrane-related factors. We point out that the LM-H model fully encompasses the information representation range of the LIF model while offering the flexibility to adjust the extraction ratio between historical and current information. Additionally, we theoretically demonstrate the effectiveness of the LM-H model and the functionality of its internal parameters, and propose a progressive training algorithm tailored specifically for the LM-H model. Furthermore, we devise an efficient training framework for our novel advanced model, encompassing hybrid training and time-slicing online training. Through extensive experiments on various datasets, we validate the remarkable superiority of our model and training algorithm compared to previous state-of-the-art approaches. Code is available at https://github.com/hzc1208/STBP_LMH ."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs) have garnered considerable attention due to their energy
efficiency and unique biological characteristics.

## Core Method

However, the widely adopted Leaky Integrate-and-Fire (LIF) model, as the mainstream neuron
model in current SNN research, has been revealed to exhibit significant deficiencies in
deep-layer gradient calculation and capturing global information on the time dimension.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage screening; official abstract/page inspected; main conference; needs human
verification。
