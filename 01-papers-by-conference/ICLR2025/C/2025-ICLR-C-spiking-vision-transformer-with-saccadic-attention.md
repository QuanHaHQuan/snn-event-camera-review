---
title: "Spiking Vision Transformer with Saccadic Attention"
authors: ["Shuai Wang", "Malu Zhang", "Dehao Zhang", "Ammar Belatreche", "Yichen Xiao", "Yu Liang", "Yimeng Shan", "Qian Sun", "Enqi Zhang", "Yang Yang"]
conference: "ICLR"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2025/file/3c85f70d3fd83f4fba47e117e5429f35-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/3c85f70d3fd83f4fba47e117e5429f35-Abstract-Conference.html"
tags: []
abstract: "The combination of Spiking Neural Networks (SNNs) and Vision Transformers (ViTs) holds potential for achieving both energy efficiency and high performance, particularly suitable for edge vision applications. However, a significant performance gap still exists between SNN-based ViTs and their ANN counterparts. Here, we first analyze why SNN-based ViTs suffer from limited performance and identify a mismatch between the vanilla self-attention mechanism and spatio-temporal spike trains. This mismatch results in degraded spatial relevance and limited temporal interactions. To address these issues, we draw inspiration from biological saccadic attention mechanisms and introduce an innovative Saccadic Spike Self-Attention (SSSA) method. Specifically, in the spatial domain, SSSA employs a novel spike distribution-based method to effectively assess the relevance between Query and Key pairs in SNN-based ViTs. Temporally, SSSA employs a saccadic interaction module that dynamically focuses on selected visual areas at each timestep and significantly enhances whole scene understanding through temporal interactions.Building on the SSSA mechanism, we develop a SNN-based Vision Transformer (SNN-ViT). Extensive experiments across various visual tasks demonstrate that SNN-ViT achieves state-of-the-art performance with linear computational complexity. The effectiveness and efficiency of the SNN-ViT highlight its potential for power-critical edge vision applications."
status: "auto-generated; brief scan note"
---

## Core Problem

The combination of Spiking Neural Networks (SNNs) and Vision Transformers (ViTs) holds potential for achieving both energy efficiency and high performance, particularly suitable for edge vision applications.

## Core Method

However, a significant performance gap still exists between SNN-based ViTs and their ANN counterparts.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：spiking。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
