---
title: "MI-TRQR: Mutual Information-Based Temporal Redundancy Quantification and Reduction for Energy-Efficient Spiking Neural Networks"
authors: ["Dengfeng Xue, Wenjuan Li, Yifan Lu, chunfeng yuan, Yufan Liu, Wei Liu, Man Yao, Li Yang, Guoqi Li, Bing Li, Stephen Maybank, Weiming Hu, Zhetao Li"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/dfb89b72be941eeeaeb5ee53bd3e7fc1-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/dfb89b72be941eeeaeb5ee53bd3e7fc1-Abstract-Conference.html"
tags: []
abstract: "Brain-inspired spiking neural networks (SNNs) provide energy-efficient computation through event-driven processing. However, the shared weights across multiple timesteps lead to serious temporal feature redundancy, limiting both efficiency and performance. This issue is further aggravated when processing static images due to the duplicated input. To mitigate this problem, we propose a parameter-free and plug-and-play module named Mutual Information-based Temporal Redundancy Quantification and Reduction (MI-TRQR), constructing energy-efficient SNNs. Specifically, Mutual Information (MI) is properly introduced to quantify redundancy between discrete spike features at different timesteps on two spatial scales: pixel (local) and the entire spatial features (global). Based on the multi-scale redundancy quantification, we apply a probabilistic masking strategy to remove redundant spikes. The final representation is subsequently recalibrated to account for the spike removal. Extensive experimental results demonstrate that our MI-TRQR achieves sparser spiking firing, higher energy efficiency, and better performance concurrently with different SNN architectures in tasks of neuromorphic data classification, static data classification, and time-series forecasting. Notably, MI-TRQR increases accuracy by \\textbf{1.7\\%} on CIFAR10-DVS with 4 timesteps while reducing energy cost by \\textbf{37.5\\%}. Our codes are available at https://github.com/dfxue/MI-TRQR."
status: "auto-generated; brief scan note"
---
## Core Problem

Brain-inspired spiking neural networks (SNNs) provide energy-efficient computation through
event-driven processing.

## Core Method

However, the shared weights across multiple timesteps lead to serious temporal feature
redundancy, limiting both efficiency and performance.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNN/spiking neural computation。自动分类理由：Official abstract confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence.。 备注：Track: Main Conference Track. Official
abstract/page inspected under broad high-recall title workflow.。
