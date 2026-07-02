---
title: "Efficient Learning of Event-based Dense Representation using Hierarchical Memories with Adaptive Update"
authors: ["Uday Kamal", "Saibal Mukhopadhyay"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10733.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/650"
tags: []
abstract: "Leveraging the high temporal resolution of an event-based camera requires highly efficient event-by-event processing. However, dense prediction tasks require explicit pixel-level association, which is challenging for event-based processing frameworks. Existing works aggregate the events into a static frame-like representation at the cost of a much slower processing rate and high compute cost. To address this challenge, this work introduces an event-based spatiotemporal representation learning framework for efficiently solving dense prediction tasks. We uniquely handle the sparse, asynchronous events using an unstructured, set-based approach and project them into a hierarchically organized multi-level latent memory space that preserves the pixel-level structure. Low-level event streams are dynamically encoded into these latent structures through an explicit attention-based spatial association. Unlike existing works that update these memory stacks at a fixed rate, we introduce a data-adaptive update rate that recurrently keeps track of the past memory states and learns to update the corresponding memory stacks only when it has substantial new information, thereby improving the overall compute latency. Our method consistently achieves competitive performance across different event-based dense prediction tasks while ensuring much lower latency compared to the existing methods."
status: "auto-generated; brief scan note"
---
## Core Problem

Leveraging the high temporal resolution of an event-based camera requires highly efficient
event-by-event processing.

## Core Method

However, dense prediction tasks require explicit pixel-level association, which is
challenging for event-based processing frameworks.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event-based official cross-check。自动分类理由：Official abstract confirms event-based
camera/event streams and dense event representation; no clear SNN evidence.。
