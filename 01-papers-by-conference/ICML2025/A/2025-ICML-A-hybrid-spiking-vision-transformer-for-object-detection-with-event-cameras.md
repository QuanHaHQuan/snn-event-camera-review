---
title: "Hybrid Spiking Vision Transformer for Object Detection with Event Cameras"
authors: ["Qi Xu", "Jie Deng", "Jiangrong Shen", "Biwu Chen", "Huajin Tang", "Gang Pan"]
conference: "ICML"
year: 2025
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25e/xu25e.pdf"
official_page: "https://proceedings.mlr.press/v267/xu25e.html"
tags: []
abstract: "Event-based object detection has attracted increasing attention for its high temporal resolution, wide dynamic range, and asynchronous address-event representation. Leveraging these advantages, spiking neural networks (SNNs) have emerged as a promising approach, offering low energy consumption and rich spatiotemporal dynamics. To further enhance the performance of event-based object detection, this study proposes a novel hybrid spike vision Transformer (HsVT) model. The HsVT model integrates a spatial feature extraction module to capture local and global features, and a temporal feature extraction module to model time dependencies and long-term patterns in event sequences. This combination enables HsVT to capture spatiotemporal features, improving its capability in handling complex event-based object detection tasks. To support research in this area, we developed the Fall Detection dataset as a benchmark for event-based object detection tasks. The Fall DVS detection dataset protects facial privacy and reduces memory usage thanks to its event-based representation. Experimental results demonstrate that HsVT outperforms existing SNN methods and achieves competitive performance compared to ANN-based models, with fewer parameters and lower energy consumption."
status: "auto-generated; needs human review"
---

## Core Problem

Event-based object detection has attracted increasing attention for its high temporal resolution, wide dynamic range, and asynchronous address-event representation.

## Core Method

Leveraging these advantages, spiking neural networks (SNNs) have emerged as a promising approach, offering low energy consumption and rich spatiotemporal dynamics.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：event cameras; event; spiking。自动分类理由：Official abstract/page confirms both event-camera/DVS/visual-event-stream evidence and SNN/spiking neural computation.。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/视觉事件流与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
