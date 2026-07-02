---
title: "ARES: Unifying Asymmetric RGB-Event Stereo for Probabilistic Scene Flow Estimation"
authors: ["Jie Long Lee", "Gim Hee Lee"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_ARES_Unifying_Asymmetric_RGB-Event_Stereo_for_Probabilistic_Scene_Flow_Estimation_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Lee_ARES_Unifying_Asymmetric_RGB-Event_Stereo_for_Probabilistic_Scene_Flow_Estimation_CVPR_2026_paper.html"
tags: []
abstract: "Estimating dense three dimensional motion in dynamic high speed scenes remains challenging due to motion blur, illumination variation, and the limited temporal resolution of conventional cameras. We introduce ARES, a unified framework for Asymmetric RGB-Event Stereo that addresses these issues through a hybrid setup where an event camera captures fine grained temporal dynamics and an RGB camera provides rich spatial structure. To integrate these heterogeneous modalities, we propose Multimodal Contextual Attention, a transformer based fusion mechanism that attends to spatial and temporal contexts under cross view constraints and forms a unified correspondence space for disparity and optical flow estimation. Building on this shared representation, we introduce Temporal Disparity Posterior Fusion, a probabilistic framework that models the evolution of disparity posteriors to infer disparity change and recover metrically coherent scene flow. Trained with sparse supervision and dense self consistency cues, our ARES achieves geometrically consistent and temporally stable three dimensional motion estimation across diverse driving scenarios. Experiments show that ARES attains state of the art performance in scene flow estimation among RGB-event stereo methods, establishing a principled path toward unified asymmetric multimodal stereo sensing. Code available at the project website."
status: "auto-generated; brief scan note"
---
## Core Problem

Estimating dense three dimensional motion in dynamic high speed scenes remains challenging
due to motion blur, illumination variation, and the limited temporal resolution of
conventional cameras.

## Core Method

We introduce ARES, a unified framework for Asymmetric RGB-Event Stereo that addresses these
issues through a hybrid setup where an event camera captures fine grained temporal dynamics
and an RGB camera provides rich spatial structure.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; rgb-event。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
