---
title: "Revisiting motion information for RGB-Event tracking with MOT philosophy"
authors: ["Tianlu Zhang, Kurt Debattista, Qiang Zhang, Guiguang Ding, Jungong Han"]
conference: "NeurIPS"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/a29f0fc2127c9d8cb1c9d86e423241af-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/a29f0fc2127c9d8cb1c9d86e423241af-Abstract-Conference.html"
tags: []
abstract: "RGB-Event single object tracking (SOT) aims to leverage the merits of RGB and event data to achieve higher performance. However, existing frameworks focus on exploring complementary appearance information within multi-modal data, and struggle to address the association problem of targets and distractors in the temporal domain using motion information from the event stream. In this paper, we introduce the Multi-Object Tracking (MOT) philosophy into RGB-E SOT to keep track of targets as well as distractors by using both RGB and event data, thereby improving the robustness of the tracker. Specifically, an appearance model is employed to predict the initial candidates. Subsequently, the initially predicted tracking results, in combination with the RGB-E features, are encoded into appearance and motion embeddings, respectively. Furthermore, a Spatial-Temporal Transformer Encoder is proposed to model the spatial-temporal relationships and learn discriminative features for each candidate through guidance of the appearance-motion embeddings. Simultaneously, a Dual-Branch Transformer Decoder is designed to adopt such motion and appearance information for candidate matching, thus distinguishing between targets and distractors. The proposed method is evaluated on multiple benchmark datasets and achieves state-of-the-art performance on all the datasets tested."
status: "auto-generated; brief scan note"
---
## Core Problem

RGB-Event single object tracking (SOT) aims to leverage the merits of RGB and event data to
achieve higher performance.

## Core Method

However, existing frameworks focus on exploring complementary appearance information within
multi-modal data, and struggle to address the association problem of targets and distractors
in the temporal domain using motion information from the event stream.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-
stream evidence; no clear SNN evidence found.。 备注：strict two-stage rescan; official
abstract/page inspected; Track: Main Conference Track; needs human verification. Needs human
verification for broad event wording.。
