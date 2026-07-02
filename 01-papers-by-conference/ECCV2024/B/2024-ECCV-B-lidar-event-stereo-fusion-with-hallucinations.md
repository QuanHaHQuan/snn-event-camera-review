---
title: "LiDAR-Event Stereo Fusion with Hallucinations"
authors: ["Luca Bartolomei", "Matteo Poggi", "Andrea Conti", "Stefano Mattoccia"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00932.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/999"
tags: []
abstract: "Event stereo matching is an emerging technique to estimate depth with event cameras. However, events themselves are unlikely to trigger in the absence of motion or the presence of large, untextured regions, making the correspondence problem much more challenging. Purposely, we propose integrating a stereo event camera with a fixed-frequency active sensor -- e.g., a LiDAR -- collecting sparse depth measurements, overcoming previous limitations while still enjoying the microsecond resolution of event cameras. Such depth hints are used to hallucinate events in the stacks or along the raw streams, compensating for the lack of information in the absence of brightness changes. Our techniques are general, can be adapted to any structured representation to stack events proposed in the literature, and outperform state-of-the-art fusion methods applied to event-based stereo."
status: "auto-generated; brief scan note"
---

## Core Problem

Event stereo matching is an emerging technique to estimate depth with event cameras.

## Core Method

However, events themselves are unlikely to trigger in the absence of motion or the presence of large, untextured regions, making the correspondence problem much more challenging.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; brightness change visual-event context; event-based stereo visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
