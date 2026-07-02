---
title: "Physical-Based Event Camera Simulator"
authors: ["Haiqian Han", "Jiacheng Lyu", "Jianing Li", "Henglu Wei", "Cheng Li", "Yajing Wei", "SHU CHEN", "Xiangyang Ji"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06110.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/2117"
tags: []
abstract: "Existing event camera simulators primarily focus on the process of generating video events and often overlook the entire optical path in real-world camera systems. To address this limitation, we propose a novel Physical-based Event Camera Simulator (PECS), which is able to generate a high-fidelity realistic event stream by directly interfacing with the 3D scene. Our PECS features a lens simulation block for accurate light-to-sensor chip replication and a multispectral rendering module for precise photocurrent generation. We present two spatiotemporal event metrics to assess the similarity between simulated and actual camera events. Experimental results demonstrate that our PECS outperforms four state-of-the-art simulators by a large margin in terms of event-based signal fidelity. We integrate our PECS into the UE platform to generate extensive multi-task synthetic datasets and evaluate its effectiveness in downstream vision tasks (e.g., video reconstruction). Our open-source code can be available in the supplementary material."
status: "auto-generated; brief scan note"
---

## Core Problem

Existing event camera simulators primarily focus on the process of generating video events and often overlook the entire optical path in real-world camera systems.

## Core Method

To address this limitation, we propose a novel Physical-based Event Camera Simulator (PECS), which is able to generate a high-fidelity realistic event stream by directly interfacing with the 3D scene.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event stream with event-camera context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
