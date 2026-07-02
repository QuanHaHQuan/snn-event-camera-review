---
title: "When Every Millisecond Counts: Real-Time Anomaly Detection via the Multimodal Asynchronous Hybrid Network"
authors: ["Dong Xiao", "Guangyao Chen", "Peixi Peng", "Yangru Huang", "Yifan Zhao", "Yongxing Dai", "Yonghong Tian"]
conference: "ICML"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25a/xiao25a.pdf"
official_page: "https://proceedings.mlr.press/v267/xiao25a.html"
tags: []
abstract: "Anomaly detection is essential for the safety and reliability of autonomous driving systems. Current methods often focus on detection accuracy but neglect response time, which is critical in time-sensitive driving scenarios. In this paper, we introduce real-time anomaly detection for autonomous driving, prioritizing both minimal response time and high accuracy. We propose a novel multimodal asynchronous hybrid network that combines event streams from event cameras with image data from RGB cameras. Our network utilizes the high temporal resolution of event cameras through an asynchronous Graph Neural Network and integrates it with spatial features extracted by a CNN from RGB images. This combination effectively captures both the temporal dynamics and spatial details of the driving environment, enabling swift and precise anomaly detection. Extensive experiments on benchmark datasets show that our approach outperforms existing methods in both accuracy and response time, achieving millisecond-level real-time performance."
status: "auto-generated; brief scan note"
---

## Core Problem

Anomaly detection is essential for the safety and reliability of autonomous driving systems.

## Core Method

Current methods often focus on detection accuracy but neglect response time, which is critical in time-sensitive driving scenarios.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：asynchronous。自动分类理由：Official abstract/page confirms event-camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
