---
title: "Complementing Event Streams and RGB Frames for Hand Mesh Reconstruction"
authors: ["Jianping Jiang", "Xinyu Zhou", "Bingxuan Wang", "Xiaoming Deng", "Chao Xu", "Boxin Shi"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Complementing_Event_Streams_and_RGB_Frames_for_Hand_Mesh_Reconstruction_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_Complementing_Event_Streams_and_RGB_Frames_for_Hand_Mesh_Reconstruction_CVPR_2024_paper.html"
tags: []
abstract: "Reliable hand mesh reconstruction (HMR) from commonly-used color and depth sensors is challenging especially under scenarios with varied illuminations and fast motions. Event camera is a highly promising alternative for its high dynamic range and dense temporal resolution properties but it lacks key texture appearance for hand mesh reconstruction. In this paper we propose EvRGBHand -- the first approach for 3D hand mesh reconstruction with an event camera and an RGB camera compensating for each other. By fusing two modalities of data across time space and information dimensionsEvRGBHand can tackle overexposure and motion blur issues in RGB-based HMR and foreground scarcity and background overflow issues in event-based HMR. We further propose EvRGBDegrader which allows our model to generalize effectively in challenging scenes even when trained solely on standard scenes thus reducing data acquisition costs. Experiments on real-world data demonstrate that EvRGBHand can effectively solve the challenging issues when using either type of camera alone via retaining the merits of both and shows the potential of generalization to outdoor scenes and another type of event camera. Our code models and dataset will be made public after acceptance."
status: "auto-generated; brief scan note"
---
## Core Problem

Reliable hand mesh reconstruction (HMR) from commonly-used color and depth sensors is
challenging especially under scenarios with varied illuminations and fast motions.

## Core Method

Event camera is a highly promising alternative for its high dynamic range and dense temporal
resolution properties but it lacks key texture appearance for hand mesh reconstruction.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event streams; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
