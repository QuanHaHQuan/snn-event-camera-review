---
title: "Towards Energy Efficient Spiking Neural Networks: An Unstructured Pruning Framework"
authors: ["Xinyu Shi, Jianhao Ding, Zecheng Hao, Zhaofei Yu"]
conference: "ICLR"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/dd3c889922df2112a5b1769e3c19e28e-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/dd3c889922df2112a5b1769e3c19e28e-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) have emerged as energy-efficient alternatives to Artificial Neural Networks (ANNs) when deployed on neuromorphic chips. While recent studies have demonstrated the impressive performance of deep SNNs on challenging tasks, their energy efficiency advantage has been diminished. Existing methods targeting energy consumption reduction do not fully exploit sparsity, whereas powerful pruning methods can achieve high sparsity but are not directly targeted at energy efficiency, limiting their effectiveness in energy saving. Furthermore, none of these works fully exploit the sparsity of neurons or the potential for unstructured neuron pruning in SNNs. In this paper, we propose a novel pruning framework that combines unstructured weight pruning with unstructured neuron pruning to maximize the utilization of the sparsity of neuromorphic computing, thereby enhancing energy efficiency. To the best of our knowledge, this is the first application of unstructured neuron pruning to deep SNNs. Experimental results demonstrate that our method achieves impressive energy efficiency gains. The sparse network pruned by our method with only 0.63\\% remaining connections can achieve a remarkable 91 times increase in energy efficiency compared to the original dense network, requiring only 8.5M SOPs for inference, with merely 2.19\\% accuracy loss on the CIFAR-10 dataset. Our work suggests that deep and dense SNNs exhibit high redundancy in energy consumption, highlighting the potential for targeted SNN sparsification to save energy."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs) have emerged as energy-efficient alternatives to Artificial
Neural Networks (ANNs) when deployed on neuromorphic chips.

## Core Method

While recent studies have demonstrated the impressive performance of deep SNNs on
challenging tasks, their energy efficiency advantage has been diminished.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage screening; official abstract/page inspected; main conference; needs human
verification。
