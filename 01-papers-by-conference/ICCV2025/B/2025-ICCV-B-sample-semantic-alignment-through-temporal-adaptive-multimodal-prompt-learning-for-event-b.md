---
title: "SAMPLE: Semantic Alignment through Temporal-Adaptive Multimodal Prompt Learning for Event-Based Open-Vocabulary Action Recognition"
authors: ["Jing Wang", "Rui Zhao", "Ruiqin Xiong", "Xingtao Wang", "Xiaopeng Fan", "Tiejun Huang"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Wang_SAMPLE_Semantic_Alignment_through_Temporal-Adaptive_Multimodal_Prompt_Learning_for_Event-Based_ICCV_2025_paper.html"
tags: []
abstract: "Open-vocabulary action recognition (OVAR) extends recognition systems to identify unseen action categories. While large-scale vision-language models (VLMs) like CLIP have enabled OVAR in image domains, their adaptation to event data remains underexplored. Event cameras offer high temporal resolution and inherent privacy preservation, making them suitable for capturing fine-grained motion dynamics. However, leveraging event data for OVAR presents challenges: 1) bridging the domain gap between static image-based models and event streams, and 2) preserving the generalization capabilities of pretrained VLMs in open-vocabulary settings. In this paper, we propose SAMPLE, a lightweight adaptation of VLMs for event-based action recognition, balancing supervised and open-vocabulary performance. We introduce a Temporal-Adaptive Multimodal Prompt Learning strategy that can be divided into: 1) Unimodal prompt on both the event and text branches to learn the data distribution 2) Event-Text cross-modal prompt for representation space alignment 3) Temporal-Adaptive prompt to model temporal dependencies across event data. Extensive evaluations demonstrate that SAMPLE outperforms prior methods across fully supervised, few-shot, base-to-novel and zero-shot settings. Notably, in zero-shot scenarios, SAMPLE achieves gains of +15.46%, +29.76%, and +23.79% on SeAct, DVS128Gesture, and PAF respectively with less commute cost. Our codes are released at https://github.com/JingWang-self/SAMPLE."
status: "auto-generated; brief scan note"
---
## Core Problem

Open-vocabulary action recognition (OVAR) extends recognition systems to identify unseen
action categories.

## Core Method

While large-scale vision-language models (VLMs) like CLIP have enabled OVAR in image
domains, their adaptation to event data remains underexplored.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event stream; event data; event-based action
recognition。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream evidence;
no clear SNN evidence.。
