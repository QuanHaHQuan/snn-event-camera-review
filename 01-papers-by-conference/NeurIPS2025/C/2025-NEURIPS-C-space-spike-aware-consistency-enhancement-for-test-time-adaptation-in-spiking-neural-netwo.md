---
title: "SPACE: SPike-Aware Consistency Enhancement for Test-Time Adaptation in Spiking Neural Networks"
authors: ["Xinyu Luo, Kecheng Chen, Pao-Sheng Sun, Chris Xing TIAN, Arindam Basu, Haoliang Li"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/3d9f111e9139bb008ffdfc6b466f3bf5-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/3d9f111e9139bb008ffdfc6b466f3bf5-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks (SNNs), as a biologically plausible alternative to Artificial Neural Networks (ANNs), have demonstrated advantages in terms of energy efficiency, temporal processing, and biological plausibility. However, SNNs are highly sensitive to distribution shifts, which can significantly degrade their performance in real-world scenarios. Traditional test-time adaptation (TTA) methods designed for ANNs often fail to address the unique computational dynamics of SNNs, such as sparsity and temporal spiking behavior. To address these challenges, we propose SPike-Aware Consistency Enhancement (SPACE), the first source-free and single-instance TTA method specifically designed for SNNs. SPACE leverages the inherent spike dynamics of SNNs to maximize the consistency of spike-behavior-based local feature maps across augmented versions of a single test sample, enabling robust adaptation without requiring source data. We evaluate SPACE on multiple datasets. Furthermore, SPACE exhibits robust generalization across diverse network architectures, consistently enhancing the performance of SNNs on CNNs, Transformer, and ConvLSTM architectures. Experimental results show that SPACE outperforms state-of-the-art ANN methods while maintaining lower computational cost, highlighting its effectiveness and robustness for SNNs in real-world settings. The code will be available at https://github.com/ethanxyluo/SPACE."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs), as a biologically plausible alternative to Artificial Neural
Networks (ANNs), have demonstrated advantages in terms of energy efficiency, temporal
processing, and biological plausibility.

## Core Method

However, SNNs are highly sensitive to distribution shifts, which can significantly degrade
their performance in real-world scenarios.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; snns。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage rescan; official abstract/page inspected; needs human verification; Track: Main
Conference Track。
