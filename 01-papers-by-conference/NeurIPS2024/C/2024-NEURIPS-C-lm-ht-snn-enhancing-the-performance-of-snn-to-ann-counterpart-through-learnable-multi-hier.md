---
title: "LM-HT SNN: Enhancing the Performance of SNN to ANN Counterpart through Learnable Multi-hierarchical Threshold Model"
authors: ["Zecheng Hao, Xinyu Shi, Yujia Liu, Zhaofei Yu, Tiejun Huang"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/b8bf2c0dd0b48511889b7d3b2c5fc8f5-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/b8bf2c0dd0b48511889b7d3b2c5fc8f5-Abstract-Conference.html"
tags: []
abstract: "Compared to traditional Artificial Neural Network (ANN), Spiking Neural Network (SNN) has garnered widespread academic interest for its intrinsic ability to transmit information in a more energy-efficient manner. However, despite previous efforts to optimize the learning algorithm of SNNs through various methods, SNNs still lag behind ANNs in terms of performance. The recently proposed multi-threshold model provides more possibilities for further enhancing the learning capability of SNNs. In this paper, we rigorously analyze the relationship among the multi-threshold model, vanilla spiking model and quantized ANNs from a mathematical perspective, then propose a novel LM-HT model, which is an equidistant multi-threshold model that can dynamically regulate the global input current and membrane potential leakage on the time dimension. The LM-HT model can also be transformed into a vanilla single threshold model through reparameterization, thereby achieving more flexible hardware deployment. In addition, we note that the LM-HT model can seamlessly integrate with ANN-SNN Conversion framework under special initialization. This novel hybrid learning framework can effectively improve the relatively poor performance of converted SNNs under low time latency. Extensive experimental results have demonstrated that our model can outperform previous state-of-the-art works on various types of datasets, which promote SNNs to achieve a brand-new level of performance comparable to quantized ANNs. Code is available at https://github.com/hzc1208/LMHT_SNN."
status: "auto-generated; brief scan note"
---
## Core Problem

Compared to traditional Artificial Neural Network (ANN), Spiking Neural Network (SNN) has
garnered widespread academic interest for its intrinsic ability to transmit information in a
more energy-efficient manner.

## Core Method

However, despite previous efforts to optimize the learning algorithm of SNNs through various
methods, SNNs still lag behind ANNs in terms of performance.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNN。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural computation;
no clear event-camera/DVS evidence found.。 备注：strict two-stage rescan; official
abstract/page inspected; Track: Main Conference Track; needs human verification.。
