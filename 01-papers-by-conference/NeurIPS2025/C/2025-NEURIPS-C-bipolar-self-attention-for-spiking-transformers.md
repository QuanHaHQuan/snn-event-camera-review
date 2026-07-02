---
title: "Bipolar Self-attention for Spiking Transformers"
authors: ["Shuai Wang, Malu Zhang, Jingya Wang, Dehao Zhang, Yimeng Shan, Jieyuan Zhang, Yichen Xiao, Honglin Cao, Haonan Zhang, Zeyu Ma, Yang Yang, Haizhou Li"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/9316cfcb0a81e53a1f35b4353f115571-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/9316cfcb0a81e53a1f35b4353f115571-Abstract-Conference.html"
tags: []
abstract: "Harnessing the event-driven characteristic, Spiking Neural Networks (SNNs) present a promising avenue toward energy-efficient Transformer architectures. However, existing Spiking Transformers still suffer significant performance gaps compared to their Artificial Neural Network counterparts. Through comprehensive analysis, we attribute this gap to these two factors. First, the binary nature of spike trains limits Spiking Self-attention (SSA)’s capacity to capture negative–negative and positive–negative membrane potential interactions on Querys and Keys. Second, SSA typically omits Softmax functions to avoid energy-intensive multiply-accumulate operations, thereby failing to maintain row-stochasticity constraints on attention scores. To address these issues, we propose a Bipolar Self-attention (BSA) paradigm, effectively modeling multi-polar membrane potential interactions with a fully spike-driven characteristic. Specifically, we demonstrate that ternary matrix multiplication provides a closer approximation to real-valued computation on both distribution and local correlation, enabling clear differentiation between homopolar and heteropolar interactions. Moreover, we propose a shift-based Softmax approximation named Shiftmax, which efficiently achieves low-entropy activation and partly maintains row-stochasticity without non-linear operation, enabling precise attention allocation. Extensive experiments show that BSA achieves substantial performance improvements across various tasks, including image classification, semantic segmentation, and event-based tracking. These results establish its potential as a fundamental building block for energy-efficient Spiking Transformers."
status: "auto-generated; brief scan note"
---
## Core Problem

Harnessing the event-driven characteristic, Spiking Neural Networks (SNNs) present a
promising avenue toward energy-efficient Transformer architectures.

## Core Method

However, existing Spiking Transformers still suffer significant performance gaps compared to
their Artificial Neural Network counterparts.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNN/spiking neural computation。自动分类理由：Official abstract confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence.。 备注：Track: Main Conference Track. Official
abstract/page inspected under broad high-recall title workflow.。
