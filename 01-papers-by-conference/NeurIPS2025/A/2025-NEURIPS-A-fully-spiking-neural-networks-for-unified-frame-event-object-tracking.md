---
title: "Fully Spiking Neural Networks for Unified Frame-Event Object Tracking"
authors: ["Jingjun Yang, Liangwei Fan, Jinpu Zhang, Xiangkai Lian, Hui Shen, Dewen Hu"]
conference: "NeurIPS"
year: 2025
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/af752cfbdcc6fd3e4cd0eea9f1ad0fab-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/af752cfbdcc6fd3e4cd0eea9f1ad0fab-Abstract-Conference.html"
tags: []
abstract: "The integration of image and event streams offers a promising approach for achieving robust visual object tracking in complex environments. However, current fusion methods achieve high performance at the cost of significant computational overhead and struggle to efficiently extract the sparse, asynchronous information from event streams, failing to leverage the energy-efficient advantages of event-driven spiking paradigms. To address this challenge, we propose the first fully Spiking Frame-Event Tracking framework called SpikeFET. This network achieves synergistic integration of convolutional local feature extraction and Transformer-based global modeling within the spiking paradigm, effectively fusing frame and event data. To overcome the degradation of translation invariance caused by convolutional padding, we introduce a Random Patchwork Module (RPM) that eliminates positional bias through randomized spatial reorganization and learnable type encoding while preserving residual structures. Furthermore, we propose a Spatial-Temporal Regularization (STR) strategy that overcomes similarity metric degradation from asymmetric features by enforcing spatio-temporal consistency among temporal template features in latent space. Extensive experiments across multiple benchmarks demonstrate that the proposed framework achieves superior tracking accuracy over existing methods while significantly reducing power consumption, attaining an optimal balance between performance and efficiency."
status: "auto-generated; needs human review"
---
## Core Problem

The integration of image and event streams offers a promising approach for achieving robust
visual object tracking in complex environments.

## Core Method

However, current fusion methods achieve high performance at the cost of significant
computational overhead and struggle to efficiently extract the sparse, asynchronous
information from event streams, failing to leverage the energy-efficient advantages of
event-driven spiking paradigms.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：frame-event visual-event context; event stream with event-camera context; spiking
neural networks。自动分类理由：Official abstract/page strictly confirms both event-
camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.。 备注：strict two-
stage rescan; official abstract/page inspected; needs human verification; Track: Main
Conference Track。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

To address this challenge, we propose the first fully Spiking Frame-Event Tracking framework
called SpikeFET. This network achieves synergistic integration of convolutional local
feature extraction and Transformer-based global modeling within the spiking paradigm,
effectively fusing frame and event data. To overcome the degradation of translation
invariance caused by convolutional padding, we introduce a Random Patchwork Module (RPM)
that eliminates positional bias through randomized spatial reorganization and learnable type
encoding while preserving residual structures. Furthermore, we propose a Spatial-Temporal
Regularization (STR) strategy that overcomes similarity metric degradation from asymmetric
features by enforcing spatio-temporal consistency among temporal template features in latent
space. Extensive experiments across multiple benchmarks demonstrate that the proposed
framework achieves superior tracking accuracy over existing methods while significantly
reducing power consumption, attaining an optimal balance between performance and efficiency.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
