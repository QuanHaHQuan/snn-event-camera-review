---
title: "Event Camera Data Dense Pre-training"
authors: ["Yan Yang", "Liyuan Pan", "Liu liu"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05986.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1466"
tags: []
abstract: "This paper introduces a self-supervised learning framework designed for pre-training neural networks tailored to dense prediction tasks using event camera data. Our approach utilizes solely event data for training. Transferring achievements from dense RGB pre-training directly to event camera data yields subpar performance. This is attributed to the spatial sparsity inherent in an event image (converted from event data), where many pixels do not contain information. To mitigate this sparsity issue, we encode an event image into event patch features, automatically mine contextual similarity relationships among patches, group the patch features into distinctive contexts, and enforce context-to-context similarities to learn discriminative event features. For training our framework, we curate a synthetic event camera dataset featuring diverse scene and motion patterns. Transfer learning performance on downstream dense prediction tasks illustrates the superiority of our method over state-of-the-art approaches."
status: "auto-generated; brief scan note"
---

## Core Problem

This paper introduces a self-supervised learning framework designed for pre-training neural networks tailored to dense prediction tasks using event camera data.

## Core Method

Our approach utilizes solely event data for training.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera data; event camera visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
