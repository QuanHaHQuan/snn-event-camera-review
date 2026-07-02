---
title: "Event-Adapted Video Super-Resolution"
authors: ["Zeyu Xiao", "Dachun Kai", "Yueyi Zhang", "Zheng-Jun Zha", "Xiaoyan Sun", "Zhiwei Xiong"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05857.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1743"
tags: []
abstract: "Introducing event cameras into video super-resolution (VSR) shows great promise. In practice, however, integrating event data as a new modality necessitates a laborious model architecture design. This not only consumes substantial time and effort but also disregards valuable insights from successful existing VSR models. Furthermore, the resource-intensive process of retraining these newly designed structures exacerbates the challenge. In this paper, inspired by recent success of parameter-efficient tuning in reducing the number of trainable parameters of a pre-trained model for downstream tasks, we introduce the Event AdapTER (EATER) for VSR. EATER efficiently utilizes pre-trained VSR model knowledge at the feature level through two lightweight and trainable components: the event-adapted alignment (EAA) unit and the event-adapted fusion (EAF) unit. The EAA unit aligns multiple frames based on the event stream in a coarse-to-fine manner, while the EAF unit efficiently fuses frames with the event stream through a multi-scaled design. Thanks to both units, EATER outperforms the full fine-tuning paradigm. Comprehensive experiments demonstrate the effectiveness of EATER, achieving superior results with parameter efficiency."
status: "auto-generated; brief scan note"
---

## Core Problem

Introducing event cameras into video super-resolution (VSR) shows great promise.

## Core Method

In practice, however, integrating event data as a new modality necessitates a laborious model architecture design.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event stream with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
