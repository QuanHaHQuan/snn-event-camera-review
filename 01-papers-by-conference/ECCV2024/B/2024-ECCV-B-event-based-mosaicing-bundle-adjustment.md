---
title: "Event-based Mosaicing Bundle Adjustment"
authors: ["Shuang Guo", "Guillermo Gallego"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02142.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1388"
tags: []
abstract: "We tackle the problem of mosaicing bundle adjustment (i.e., simultaneous refinement of camera orientations and scene map) for a purely rotating event camera. We formulate the problem as a regularized non-linear least squares optimization. The objective function is defined using the linearized event generation model in the camera orientations and the panoramic gradient maps of the scene. We show that this BA optimization has an exploitable block-diagonal sparsity structure, so that the problem can be solved efficiently. To the best of our knowledge, this is the first work to leverage such sparsity to speed up the optimization in the context of event-based cameras, without the need to convert events into image-like representations. We evaluate EMBA on both synthetic and real-world datasets to show its effectiveness (50% photometric error decrease), yielding results of unprecedented quality. In addition, we demonstrate EMBA using high spatial resolution event cameras, yielding delicate panoramas in the wild, even without an initial map. We make the source code publicly available."
status: "auto-generated; brief scan note"
---
## Core Problem

We tackle the problem of mosaicing bundle adjustment (i.e., simultaneous refinement of
camera orientations and scene map) for a purely rotating event camera.

## Core Method

We formulate the problem as a regularized non-linear least squares optimization.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event-based official cross-check。自动分类理由：Official abstract confirms purely rotating
event camera and event-based mosaicing bundle adjustment; no clear SNN evidence.。
