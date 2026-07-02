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

However, events themselves are unlikely to trigger in the absence of motion or the presence
of large, untextured regions, making the correspondence problem much more challenging.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event-based stereo; lidar-event。自动分类理由：Official abstract/page confirms
event-camera/DVS/event-stream evidence; no clear SNN evidence.。
