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

极暗环境下 RGB 传感器难以保留足够结构与颜色信息。

## Core Method

结合 event streams、低照度帧和 3D Gaussian Splatting 做场景级增强与重建。

## Key Metrics and Findings

摘要强调多视角几何与光度一致性。

## Personal Notes

可作为 event stream + 3DGS 的背景论文。

