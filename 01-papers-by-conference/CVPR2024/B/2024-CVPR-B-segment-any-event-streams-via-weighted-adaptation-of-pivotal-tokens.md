---
title: "Segment Any Event Streams via Weighted Adaptation of Pivotal Tokens"
authors: ["Zhiwen Chen", "Zhiyu Zhu", "Yifan Zhang", "Junhui Hou", "Guangming Shi", "Jinjian Wu"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_Segment_Any_Event_Streams_via_Weighted_Adaptation_of_Pivotal_Tokens_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Segment_Any_Event_Streams_via_Weighted_Adaptation_of_Pivotal_Tokens_CVPR_2024_paper.html"
tags: []
abstract: "In this paper we delve into the nuanced challenge of tailoring the Segment Anything Models (SAMs) for integration with event data with the overarching objective of attaining robust and universal object segmentation within the event-centric domain. One pivotal issue at the heart of this endeavor is the precise alignment and calibration of embeddings derived from event-centric data such that they harmoniously coincide with those originating from RGB imagery. Capitalizing on the vast repositories of datasets with paired events and RGB images our proposition is to harness and extrapolate the profound knowledge encapsulated within the pre-trained SAM framework. As a cornerstone to achieving this we introduce a multi-scale feature distillation methodology. This methodology rigorously optimizes the alignment of token embeddings originating from event data with their RGB image counterparts thereby preserving and enhancing the robustness of the overall architecture. Considering the distinct significance that token embeddings from intermediate layers hold for higher-level embeddings our strategy is centered on accurately calibrating the pivotal token embeddings. This targeted calibration is aimed at effectively managing the discrepancies in high-level embeddings originating from both the event and image domains. Extensive experiments on different datasets demonstrate the effectiveness of the proposed distillation method. Code in https://github.com/happychenpipi/EventSAM."
status: "auto-generated; brief scan note"
---
## Core Problem

In this paper we delve into the nuanced challenge of tailoring the Segment Anything Models
(SAMs) for integration with event data with the overarching objective of attaining robust
and universal object segmentation within the event-centric domain.

## Core Method

One pivotal issue at the heart of this endeavor is the precise alignment and calibration of
embeddings derived from event-centric data such that they harmoniously coincide with those
originating from RGB imagery.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event streams; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow. Needs human verification for
event-stream wording.。
