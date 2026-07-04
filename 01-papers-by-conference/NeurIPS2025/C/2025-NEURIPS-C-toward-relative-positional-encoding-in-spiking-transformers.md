---
title: "Toward Relative Positional Encoding in Spiking Transformers"
authors: ["Changze Lv, Yansen Wang, Dongqi Han, Yifei Shen, Xiaoqing Zheng, Xuanjing Huang, Dongsheng Li"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/6fdbdaf19f4f3f8e2e08aa87987e459c-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/6fdbdaf19f4f3f8e2e08aa87987e459c-Abstract-Conference.html"
tags: []
abstract: "Spiking neural networks (SNNs) are bio-inspired networks that mimic how neurons in the brain communicate through discrete spikes, which have great potential in various tasks due to their energy efficiency and temporal processing capabilities. SNNs with self-attention mechanisms (spiking Transformers) have recently shown great advancements in various tasks, and inspired by traditional Transformers, several studies have demonstrated that spiking absolute positional encoding can help capture sequential relationships for input data, enhancing the capabilities of spiking Transformers for tasks such as sequential modeling and image classification. However, how to incorporate relative positional information into SNNs remains a challenge. In this paper, we introduce several strategies to approximate relative positional encoding (RPE) in spiking Transformers while preserving the binary nature of spikes. Firstly, we formally prove that encoding relative distances with Gray Code ensures that the binary representations of positional indices maintain a constant Hamming distance whenever their decimal values differ by a power of two, and we propose Gray-PE based on this property. In addition, we propose another RPE method called Log-PE , which combines the logarithmic form of the relative distance matrix directly into the spiking attention map. Furthermore, we extend our RPE methods to a two-dimensional form, making them suitable for processing image patches. We evaluate our RPE methods on various tasks, including time series forecasting, text classification, and patch-based image classification, and the experimental results demonstrate a satisfying performance gain by incorporating our RPE methods across many architectures. Our results provide fresh perspectives on designing spiking Transformers to advance their sequential modeling capability, thereby expanding their applicability across various domains. Our code is available at https://github.com/microsoft/SeqSNN."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking neural networks (SNNs) are bio-inspired networks that mimic how neurons in the brain
communicate through discrete spikes, which have great potential in various tasks due to
their energy efficiency and temporal processing capabilities.

## Core Method

SNNs with self-attention mechanisms (spiking Transformers) have recently shown great
advancements in various tasks, and inspired by traditional Transformers, several studies
have demonstrated that spiking absolute positional encoding can help capture sequential
relationships for input data, enhancing the capabilities of spiking Transformers for tasks
such as sequential modeling and image classification.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; snns; spiking transformers。自动分类理由：Official abstract/page
strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。
备注：strict two-stage rescan; official abstract/page inspected; needs human verification;
Track: Main Conference Track。
