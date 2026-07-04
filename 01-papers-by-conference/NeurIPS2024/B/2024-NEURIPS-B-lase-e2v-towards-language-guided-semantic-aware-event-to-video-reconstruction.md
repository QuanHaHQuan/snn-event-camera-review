---
title: "LaSe-E2V: Towards Language-guided Semantic-aware Event-to-Video Reconstruction"
authors: ["Kanghao Chen, Hangyu Li, Jiazhou Zhou, Zeyu Wang, Lin Wang"]
conference: "NeurIPS"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/823e43f5537d8c1894afd1f6ab00a927-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/823e43f5537d8c1894afd1f6ab00a927-Abstract-Conference.html"
tags: []
abstract: "Event cameras harness advantages such as low latency, high temporal resolution, and high dynamic range (HDR), compared to standard cameras. Due to the distinct imaging paradigm shift, a dominant line of research focuses on event-to-video (E2V) reconstruction to bridge event-based and standard computer vision. However, this task remains challenging due to its inherently ill-posed nature: event cameras only detect the edge and motion information locally. Consequently, the reconstructed videos are often plagued by artifacts and regional blur, primarily caused by the ambiguous semantics of event data. In this paper, we find language naturally conveys abundant semantic information, rendering it stunningly superior in ensuring semantic consistency for E2V reconstruction. Accordingly, we propose a novel framework, called LaSe-E2V, that can achieve semantic-aware high-quality E2V reconstruction from a language-guided perspective, buttressed by the text-conditional diffusion models. However, due to diffusion models' inherent diversity and randomness, it is hardly possible to directly apply them to achieve spatial and temporal consistency for E2V reconstruction. Thus, we first propose an Event-guided Spatiotemporal Attention (ESA) module to condition the event data to the denoising pipeline effectively. We then introduce an event-aware mask loss to ensure temporal coherence and a noise initialization strategy to enhance spatial consistency. Given the absence of event-text-video paired data, we aggregate existing E2V datasets and generate textual descriptions using the tagging models for training and evaluation. Extensive experiments on three datasets covering diverse challenging scenarios (e.g., fast motion, low light) demonstrate the superiority of our method. Demo videos for the results are attached to the project page."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras harness advantages such as low latency, high temporal resolution, and high
dynamic range (HDR), compared to standard cameras.

## Core Method

Due to the distinct imaging paradigm shift, a dominant line of research focuses on event-to-
video (E2V) reconstruction to bridge event-based and standard computer vision.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-
stream evidence; no clear SNN evidence found.。 备注：strict two-stage rescan; official
abstract/page inspected; Track: Main Conference Track; needs human verification.。
