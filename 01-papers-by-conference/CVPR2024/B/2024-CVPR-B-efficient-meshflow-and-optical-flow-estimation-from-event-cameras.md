---
title: "Efficient Meshflow and Optical Flow Estimation from Event Cameras"
authors: ["Xinglong Luo", "Ao Luo", "Zhengning Wang", "Chunyu Lin", "Bing Zeng", "Shuaicheng Liu"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Luo_Efficient_Meshflow_and_Optical_Flow_Estimation_from_Event_Cameras_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Luo_Efficient_Meshflow_and_Optical_Flow_Estimation_from_Event_Cameras_CVPR_2024_paper.html"
tags: []
abstract: "In this paper we explore the problem of event-based meshflow estimation a novel task that involves predicting a spatially smooth sparse motion field from event cameras. To start we generate a large-scale High-Resolution Event Meshflow (HREM) dataset which showcases its superiority by encompassing the merits of high resolution at 1280x720 handling dynamic objects and complex motion patterns and offering both optical flow and meshflow labels. These aspects have not been fully explored in previous works. Besides we propose Efficient Event-based MeshFlow (EEMFlow) network a lightweight model featuring a specially crafted encoder-decoder architecture to facilitate swift and accurate meshflow estimation. Furthermore we upgrade EEMFlow network to support dense event optical flow in which a Confidence-induced Detail Completion (CDC) module is proposed to preserve sharp motion boundaries. We conduct comprehensive experiments to show the exceptional performance and runtime efficiency (39x faster) of our EEMFlow model compared to recent state-of-the-art flow methods. Our code is available at https://github.com/boomluo02/EEMFlow."
status: "auto-generated; brief scan note"
---
## Core Problem

In this paper we explore the problem of event-based meshflow estimation a novel task that
involves predicting a spatially smooth sparse motion field from event cameras.

## Core Method

To start we generate a large-scale High-Resolution Event Meshflow (HREM) dataset which
showcases its superiority by encompassing the merits of high resolution at 1280x720 handling
dynamic objects and complex motion patterns and offering both optical flow and meshflow
labels.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event cameras; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
