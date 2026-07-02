---
title: "x^2-Fusion: Cross-Modality and Cross-Dimension Flow Estimation in Event Edge Space"
authors: ["Ruishan Guo", "Ciyu Ruan", "Haoyang Wang", "Zihang Gong", "Jingao Xu", "Xinlei Chen"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Guo_x2-Fusion_Cross-Modality_and_Cross-Dimension_Flow_Estimation_in_Event_Edge_Space_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Guo_x2-Fusion_Cross-Modality_and_Cross-Dimension_Flow_Estimation_in_Event_Edge_Space_CVPR_2026_paper.html"
tags: []
abstract: "Estimating dense 2D optical flow and 3D scene flow is essential for dynamic scene understanding. Recent work combines images, LiDAR, and event data to jointly predict 2D and 3D motion, yet most approaches operate in separate heterogeneous feature spaces. Without a shared latent space that all modalities can align to, these systems rely on multiple modality-specific blocks, leaving cross-sensor mismatches unresolved and making fusion unnecessarily complex. Event cameras naturally provide a spatiotemporal edge signal, which we can treat as an intrinsic edge field to anchor a unified latent representation, termed the Event Edge Space. Building on this idea, we introduce x^2-Fusion, which reframes multimodal fusion as representation unification: event-derived spatiotemporal edges define an edge-centric homogeneous space, and image and LiDAR features are explicitly aligned in this shared representation. Within this space, we perform reliability-aware adaptive fusion to estimate modality reliability and emphasize stable cues under degradation. We further employ cross-dimension contrast learning to tightly couple 2D optical flow with 3D scene flow. Extensive experiments on both synthetic and real benchmarks show that x^2-Fusion achieves state-of-the-art accuracy under standard conditions and delivers substantial improvements in challenging scenarios."
status: "auto-generated; brief scan note"
---
## Core Problem

Estimating dense 2D optical flow and 3D scene flow is essential for dynamic scene
understanding.

## Core Method

Recent work combines images, LiDAR, and event data to jointly predict 2D and 3D motion, yet
most approaches operate in separate heterogeneous feature spaces.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event data。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
