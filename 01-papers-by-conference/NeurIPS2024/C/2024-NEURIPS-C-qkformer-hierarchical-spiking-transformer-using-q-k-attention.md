---
title: "QKFormer: Hierarchical Spiking Transformer using Q-K Attention"
authors: ["Chenlin Zhou, Han Zhang, Zhaokun Zhou, Liutao Yu, Liwei Huang, Xiaopeng Fan, Li Yuan, Zhengyu Ma, Huihui Zhou, Yonghong Tian"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/179f5dcdeedc149443ebd3ba70811dbd-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/179f5dcdeedc149443ebd3ba70811dbd-Abstract-Conference.html"
tags: []
abstract: "Spiking Transformers, which integrate Spiking Neural Networks (SNNs) with Transformer architectures, have attracted significant attention due to their potential for low energy consumption and high performance. However, there remains a substantial gap in performance between SNNs and Artificial Neural Networks (ANNs). To narrow this gap, we have developed QKFormer, a direct training spiking transformer with the following features: i) Linear complexity and high energy efficiency , the novel spike-form Q-K attention module efficiently models the token or channel attention through binary vectors and enables the construction of larger models. ii) Multi-scale spiking representation , achieved by a hierarchical structure with the different numbers of tokens across blocks. iii) Spiking Patch Embedding with Deformed Shortcut (SPEDS) , enhances spiking information transmission and integration, thus improving overall performance. It is shown that QKFormer achieves significantly superior performance over existing state-of-the-art SNN models on various mainstream datasets. Notably, with comparable size to Spikformer (66.34 M, 74.81\\%), QKFormer (64.96 M) achieves a groundbreaking top-1 accuracy of 85.65\\% on ImageNet-1k, substantially outperforming Spikformer by 10.84\\% . To our best knowledge, this is the first time that directly training SNNs have exceeded 85\\% accuracy on ImageNet-1K."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Transformers, which integrate Spiking Neural Networks (SNNs) with Transformer
architectures, have attracted significant attention due to their potential for low energy
consumption and high performance.

## Core Method

However, there remains a substantial gap in performance between SNNs and Artificial Neural
Networks (ANNs).

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking transformer; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage rescan; official abstract/page inspected; Track: Main Conference Track; needs human
verification.。
