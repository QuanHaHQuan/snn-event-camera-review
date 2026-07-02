---
title: "Tracking through Severe Occlusion via Event-Derived Transient Cues"
authors: ["Hao Dong", "Yujin Liu", "Haoyue Liu", "Zhenyu Wang", "Shihan Peng", "Zhiwei Shi", "Yi Chang", "Luxin Yan"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_Tracking_through_Severe_Occlusion_via_Event-Derived_Transient_Cues_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Dong_Tracking_through_Severe_Occlusion_via_Event-Derived_Transient_Cues_CVPR_2026_paper.html"
tags: []
abstract: "Tracking targets with high-speed and nonlinear motion under occlusion remains challenging due to spatial appearance deprivation and temporal trajectory fragmentation caused by missing visual cues. Existing methods typically either dynamically update templates to maintain appearance similarity or employ autoregressive models to predict targets from historical trajectories. However, these methods are ineffective under severe occlusion owing to template contamination and limited frame rates for complex motion. In this work, we observe that occlusion inherently degrades the spatial matching mechanism, highlighting the importance of temporal cues. Meanwhile, event cameras with microsecond-level temporal resolution provide transient dynamic cues that facilitate modeling nonlinear motion. In light of this, we propose EvoTrack, an occlusion-robust tracking framework via event-derived transient evolution, which comprises event-based motion autoregression and target-aware appearance matching. Specifically, for motion autoregression, the fine-grained timestamps of events naturally encode the target's direction and speed, motivating a bidirectional motion consistency that constrains inter-frame displacement prediction under nonlinear motion. For appearance matching, we adopt a Gaussian masking strategy to simulate occlusion degradation, guiding the model to focus on target regions and learn invariant representations. Furthermore, we build a pixel-aligned Frame-Event tracking dataset with higher spatial resolution and explicit occlusion labels. Extensive experiments demonstrate the effectiveness of EvoTrack in challenging occlusion scenes."
status: "auto-generated; brief scan note"
---
## Core Problem

Tracking targets with high-speed and nonlinear motion under occlusion remains challenging
due to spatial appearance deprivation and temporal trajectory fragmentation caused by
missing visual cues.

## Core Method

Existing methods typically either dynamically update templates to maintain appearance
similarity or employ autoregressive models to predict targets from historical trajectories.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event-based motion; frame-event。自动分类理由：Official abstract/page confirms
event-camera/DVS/event-stream evidence; no clear SNN evidence.。
