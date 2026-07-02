---
title: "Event-Aided Time-To-Collision Estimation for Autonomous Driving"
authors: ["Jinghang Li", "Bangyan Liao", "Xiuyuan LU", "Peidong Liu", "Shaojie Shen", "Yi Zhou"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07043.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1387"
tags: []
abstract: "Predicting a potential collision with leading vehicles is a fundamentally essential functionality of any autonomous/assisted driving system. One bottleneck of existing vision-based solutions is that their updating rate is limited to the frame rate of standard cameras used. In this paper, we present a novel method that estimates the time to collision using a neuromorphic event-based camera, a biologically inspired visual sensor that can sense at exactly the same rate as scene dynamics. The core of the proposed algorithm consists of a two-step approach for efficient and accurate geometric model fitting on event data in a coarse-to-fine manner. The first step is a robust linear solver based on a novel geometric measurement that overcomes the partial observability of event-based normal flow. The second step further refines the resulting model via a spatio-temporal registration process which is formulated as a nonlinear optimization problem. Experiments demonstrate the effectiveness of the proposed method, outperforming other counterparts in terms of efficiency and accuracy."
status: "auto-generated; brief scan note"
---
## Core Problem

Predicting a potential collision with leading vehicles is a fundamentally essential
functionality of any autonomous/assisted driving system.

## Core Method

One bottleneck of existing vision-based solutions is that their updating rate is limited to
the frame rate of standard cameras used.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event data; event-based camera; neuromorphic event; event-aided。自动分类理由：Official
abstract/page confirms event-camera/DVS/event-stream evidence; no clear SNN evidence.。
