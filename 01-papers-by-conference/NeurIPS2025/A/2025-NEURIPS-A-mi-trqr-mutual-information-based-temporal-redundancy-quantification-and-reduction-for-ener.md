---
title: "MI-TRQR: Mutual Information-Based Temporal Redundancy Quantification and Reduction for Energy-Efficient Spiking Neural Networks"
authors: ["Dengfeng Xue, Wenjuan Li, Yifan Lu, chunfeng yuan, Yufan Liu, Wei Liu, Man Yao, Li Yang, Guoqi Li, Bing Li, Stephen Maybank, Weiming Hu, Zhetao Li"]
conference: "NeurIPS"
year: 2025
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/dfb89b72be941eeeaeb5ee53bd3e7fc1-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/dfb89b72be941eeeaeb5ee53bd3e7fc1-Abstract-Conference.html"
tags: []
abstract: "Brain-inspired spiking neural networks (SNNs) provide energy-efficient computation through event-driven processing. However, the shared weights across multiple timesteps lead to serious temporal feature redundancy, limiting both efficiency and performance. This issue is further aggravated when processing static images due to the duplicated input. To mitigate this problem, we propose a parameter-free and plug-and-play module named Mutual Information-based Temporal Redundancy Quantification and Reduction (MI-TRQR), constructing energy-efficient SNNs. Specifically, Mutual Information (MI) is properly introduced to quantify redundancy between discrete spike features at different timesteps on two spatial scales: pixel (local) and the entire spatial features (global). Based on the multi-scale redundancy quantification, we apply a probabilistic masking strategy to remove redundant spikes. The final representation is subsequently recalibrated to account for the spike removal. Extensive experimental results demonstrate that our MI-TRQR achieves sparser spiking firing, higher energy efficiency, and better performance concurrently with different SNN architectures in tasks of neuromorphic data classification, static data classification, and time-series forecasting. Notably, MI-TRQR increases accuracy by \\textbf{1.7\\%} on CIFAR10-DVS with 4 timesteps while reducing energy cost by \\textbf{37.5\\%}. Our codes are available at https://github.com/dfxue/MI-TRQR."
status: "auto-generated; needs human review"
---

## Core Problem

Brain-inspired spiking neural networks (SNNs) provide energy-efficient computation through event-driven processing.

## Core Method

However, the shared weights across multiple timesteps lead to serious temporal feature redundancy, limiting both efficiency and performance.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `dvs; cifar10-dvs; dvs visual-event context; spiking neural networks; snns`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
