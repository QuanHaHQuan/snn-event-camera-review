---
title: "MI-TRQR: Mutual Information-Based Temporal Redundancy Quantification and Reduction for Energy-Efficient Spiking Neural Networks"
authors: ["Dengfeng Xue, Wenjuan Li, Yifan Lu, chunfeng yuan, Yufan Liu, Wei Liu, Man Yao, Li Yang, Guoqi Li, Bing Li, Stephen Maybank, Weiming Hu, Zhetao Li"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/dfb89b72be941eeeaeb5ee53bd3e7fc1-Paper-Conference.pdf"
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

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：dvs; cifar10-dvs; dvs visual-event context; spiking neural networks;
snns。自动分类理由：Official abstract/page strictly confirms both event-camera/DVS/visual-event-
sensor evidence and SNN/spiking neural computation.。 备注：strict two-stage rescan; official
abstract/page inspected; needs human verification; Track: Main Conference Track。
该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

This issue is further aggravated when processing static images due to the duplicated input.
To mitigate this problem, we propose a parameter-free and plug-and-play module named Mutual
Information-based Temporal Redundancy Quantification and Reduction (MI-TRQR), constructing
energy-efficient SNNs. Specifically, Mutual Information (MI) is properly introduced to
quantify redundancy between discrete spike features at different timesteps on two spatial
scales: pixel (local) and the entire spatial features (global). Based on the multi-scale
redundancy quantification, we apply a probabilistic masking strategy to remove redundant
spikes. The final representation is subsequently recalibrated to account for the spike
removal. Extensive experimental results demonstrate that our MI-TRQR achieves sparser
spiking firing, higher energy efficiency, and better performance concurrently with different
SNN architectures in tasks of neuromorphic data classification, static data classification,
and time-series forecasting. Notably, MI-TRQR increases accuracy by \textbf{1.7\%} on
CIFAR10-DVS with 4 timesteps while reducing energy cost by \textbf{37.5\%}. Our codes are
available at https://github.com/dfxue/MI-TRQR.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
