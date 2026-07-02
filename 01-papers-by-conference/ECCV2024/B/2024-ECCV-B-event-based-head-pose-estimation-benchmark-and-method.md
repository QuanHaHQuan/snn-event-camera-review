---
title: "Event-based Head Pose Estimation: Benchmark and Method"
authors: ["jiahui yuan", "Hebei Li", "Yansong Peng", "Jin Wang", "Yuheng Jiang", "Yueyi Zhang", "Xiaoyan Sun"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02323.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/227"
tags: []
abstract: "Head pose estimation (HPE) is crucial for various applications, including human-computer interaction, augmented reality, and driver monitoring. However, traditional RGB-based methods struggle in challenging conditions like sudden movement and extreme lighting. Event cameras, as a neuromorphic sensor, have the advantages of high temporal resolution and high dynamic range, offering a promising solution for HPE. However, the lack of paired event and head pose data hinders the full potential of event-based HPE. To address this, we introduce two large-scale, diverse event-based head pose datasets encompassing 282 sequences across different resolutions and scenarios. Furthermore, we propose the event-based HPE network, featuring two novel modules: the Event Spatial-Temporal Fusion (ESTF) module and the Event Motion Perceptual Attention (EMPA) module. The ESTF module effectively combines spatial and temporal information from the event streams, while the EMPA module captures crucial motion details across the scene using a large receptive field. We also propose a unified loss function to optimize the network using both angle and rotation matrix information. Extensive experiments demonstrate the superior performance of our network on both datasets, showcasing its effectiveness in handling HPE across various challenging scenarios. The datasets and code are available at https://github.com/Jiahui-Yuan-1/EVHPE"
status: "auto-generated; brief scan note"
---

## Core Problem

Head pose estimation (HPE) is crucial for various applications, including human-computer interaction, augmented reality, and driver monitoring.

## Core Method

However, traditional RGB-based methods struggle in challenging conditions like sudden movement and extreme lighting.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event stream with event-camera context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
