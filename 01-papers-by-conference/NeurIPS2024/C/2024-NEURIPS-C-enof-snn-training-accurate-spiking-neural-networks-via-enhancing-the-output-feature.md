---
title: "EnOF-SNN: Training Accurate Spiking Neural Networks via Enhancing the Output Feature"
authors: ["Yufei Guo, Weihang Peng, Xiaode Liu, Yuanpei Chen, Yuhan Zhang, Xin Tong, Zhou Jie, Zhe Ma"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/5c6f928e3fc5f32ee29a1d916b68e6f5-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/5c6f928e3fc5f32ee29a1d916b68e6f5-Abstract-Conference.html"
tags: []
abstract: "Spiking neural networks (SNNs) have gained more and more interest as one of the energy-efficient alternatives of conventional artificial neural networks (ANNs). They exchange 0/1 spikes for processing information, thus most of the multiplications in networks can be replaced by additions. However, binary spike feature maps will limit the expressiveness of the SNN and result in unsatisfactory performance compared with ANNs. It is shown that a rich output feature representation, i.e., the feature vector before classifier) is beneficial to training an accurate model in ANNs for classification. We wonder if it also does for SNNs and how to improve the feature representation of the SNN.To this end, we materialize this idea in two special designed methods for SNNs.First, inspired by some ANN-SNN methods that directly copy-paste the weight parameters from trained ANN with light modification to homogeneous SNN can obtain a well-performed SNN, we use rich information of the weight parameters from the trained ANN counterpart to guide the feature representation learning of the SNN. In particular, we present the SNN's and ANN's feature representation from the same input to ANN's classifier to product SNN's and ANN's outputs respectively and then align the feature with the KL-divergence loss as in knowledge distillation methods, called L_ AF loss.It can be seen as a novel and effective knowledge distillation method specially designed for the SNN that comes from both the knowledge distillation and ANN-SNN methods. Various ablation study shows that the L_AF loss is more powerful than the vanilla knowledge distillation method.Second, we replace the last Leaky Integrate-and-Fire (LIF) activation layer as the ReLU activation layer to generate the output feature, thus a more powerful SNN with full-precision feature representation can be achieved but with only a little extra computation.Experimental results show that our method consistently outperforms the current state-of-the-art algorithms on both popular non-spiking static and neuromorphic datasets. We provide an extremely simple but effective way to train high-accuracy spiking neural networks."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking neural networks (SNNs) have gained more and more interest as one of the energy-
efficient alternatives of conventional artificial neural networks (ANNs).

## Core Method

They exchange 0/1 spikes for processing information, thus most of the multiplications in
networks can be replaced by additions.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; SNN; spiking。自动分类理由：Official abstract/page strictly
confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。
备注：strict two-stage rescan; official abstract/page inspected; Track: Main Conference Track;
needs human verification.。
