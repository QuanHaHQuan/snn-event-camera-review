---
title: "V2V: Scaling Event-Based Vision through Efficient Video-to-Voxel Simulation"
authors: ["Hanyue Lou, Jinxiu Liang, Minggui Teng, Yi Wang, Boxin Shi"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/b14cf0a01f7a8b9cd3e365e40f910272-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/b14cf0a01f7a8b9cd3e365e40f910272-Abstract-Conference.html"
tags: []
abstract: "Event-based cameras offer unique advantages such as high temporal resolution, high dynamic range, and low power consumption. However, the massive storage requirements and I/O burdens of existing synthetic data generation pipelines and the scarcity of real data prevent event-based training datasets from scaling up, limiting the development and generalization capabilities of event vision models. To address this challenge, we introduce Video-to-Voxel (V2V), an approach that directly converts conventional video frames into event-based voxel grid representations, bypassing the storage-intensive event stream generation entirely. V2V enables a 150× reduction in storage requirements while supporting on-the-fly parameter randomization for enhanced model robustness. Leveraging this efficiency, we train several video reconstruction and optical flow estimation model architectures on 10,000 diverse videos totaling 52 hours—an order of magnitude larger than existing event datasets, yielding substantial improvements."
status: "auto-generated; brief scan note"
---
## Core Problem

Event-based cameras offer unique advantages such as high temporal resolution, high dynamic
range, and low power consumption.

## Core Method

However, the massive storage requirements and I/O burdens of existing synthetic data
generation pipelines and the scarcity of real data prevent event-based training datasets
from scaling up, limiting the development and generalization capabilities of event vision
models.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event-based cameras; event dataset visual-event context; event datasets visual-event
context; event stream with event-camera context; event-based vision with event-camera
context; event-based with event-camera context。自动分类理由：Official abstract/page strictly
confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.。
备注：strict two-stage rescan; official abstract/page inspected; needs human verification;
Track: Main Conference Track。
