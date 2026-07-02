---
title: "eRetinexGS: Retinex Modeling for Low-Light Scene Enhancement via Event Streams and 3D Gaussian Splatting"
authors: ["Haojie Yan", "Zehao Chen", "Yan Liu", "Shi Gu", "Peng Lin", "De Ma", "Huajin Tang", "Qian Zheng", "Gang Pan"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Yan_eRetinexGS_Retinex_Modeling_for_Low-Light_Scene_Enhancement_via_Event_Streams_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Yan_eRetinexGS_Retinex_Modeling_for_Low-Light_Scene_Enhancement_via_Event_Streams_CVPR_2026_paper.html"
tags: []
abstract: "Perception under low illumination remains a major challenge for computer vision systems, as RGB sensors often fail to capture sufficient structural and color information in extremely dark environments. Event cameras, with their high dynamic range and temporal resolution, provide complementary cues that are well suited for such conditions. In this work, we present eRetinexGS, a novel framework that jointly leverages event streams and low-light frames through 3D Gaussian Splatting for scene-level enhancement and reconstruction. Unlike previous approaches that operate on individual frames, eRetinexGS enforces geometric and photometric consistency across multiple views, bridging the gap between degraded images and noisy event signals. By introducing an event-assisted Retinex decomposition and a reflectance-illumination representation within the 3DGS pipeline, our method reconstructs normal-light radiance fields with fine-grained details and accurate color. Extensive experiments on both synthetic and real datasets demonstrate that eRetinexGS achieves state-of-the-art performance in low-light scene enhancement while maintaining real-time rendering capability."
status: "auto-generated; brief scan note"
---
## Core Problem

Perception under low illumination remains a major challenge for computer vision systems, as
RGB sensors often fail to capture sufficient structural and color information in extremely
dark environments.

## Core Method

Event cameras, with their high dynamic range and temporal resolution, provide complementary
cues that are well suited for such conditions.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event stream。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
