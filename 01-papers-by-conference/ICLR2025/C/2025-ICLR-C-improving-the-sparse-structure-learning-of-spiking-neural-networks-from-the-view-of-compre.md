---
title: "Improving the Sparse Structure Learning of Spiking Neural Networks from the View of Compression Efficiency"
authors: ["Jiangrong Shen", "Qi Xu", "Gang Pan", "Badong Chen"]
conference: "ICLR"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2025/file/e7fd2c0a1a6f956c94024e955b34cc43-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/e7fd2c0a1a6f956c94024e955b34cc43-Abstract-Conference.html"
tags: []
abstract: "The human brain utilizes spikes for information transmission and dynamically reorganizes its network structure to boost energy efficiency and cognitive capabilities throughout its lifespan. Drawing inspiration from this spike-based computation, Spiking Neural Networks (SNNs) have been developed to construct event-driven models that emulate this efficiency. Despite these advances, deep SNNs continue to suffer from over-parameterization during training and inference, a stark contrast to the brain’s ability to self-organize. Furthermore, existing sparse SNNs are challenged by maintaining optimal pruning levels due to a static pruning ratio, resulting in either under or over-pruning.In this paper, we propose a novel two-stage dynamic structure learning approach for deep SNNs, aimed at maintaining effective sparse training from scratch while optimizing compression efficiency. The first stage evaluates the compressibility of existing sparse subnetworks within SNNs using the PQ index, which facilitates an adaptive determination of the rewiring ratio for synaptic connections based on data compression insights. In the second stage, this rewiring ratio critically informs the dynamic synaptic connection rewiring process, including both pruning and regrowth. This approach significantly improves the exploration of sparse structures training in deep SNNs, adapting sparsity dynamically from the point view of compression efficiency.Our experiments demonstrate that this sparse training approach not only aligns with the performance of current deep SNNs models but also significantly improves the efficiency of compressing sparse SNNs. Crucially, it preserves the advantages of initiating training with sparse models and offers a promising solution for implementing Edge AI on neuromorphic hardware."
status: "auto-generated; brief scan note"
---

## Core Problem

The human brain utilizes spikes for information transmission and dynamically reorganizes its network structure to boost energy efficiency and cognitive capabilities throughout its lifespan.

## Core Method

Drawing inspiration from this spike-based computation, Spiking Neural Networks (SNNs) have been developed to construct event-driven models that emulate this efficiency.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
