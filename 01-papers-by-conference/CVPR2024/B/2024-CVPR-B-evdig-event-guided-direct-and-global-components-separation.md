---
title: "EvDiG: Event-guided Direct and Global Components Separation"
authors: ["Xinyu Zhou", "Peiqi Duan", "Boyu Li", "Chu Zhou", "Chao Xu", "Boxin Shi"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Zhou_EvDiG_Event-guided_Direct_and_Global_Components_Separation_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_EvDiG_Event-guided_Direct_and_Global_Components_Separation_CVPR_2024_paper.html"
tags: []
abstract: "Separating the direct and global components of a scene aids in shape recovery and basic material understanding. Conventional methods capture multiple frames under high frequency illumination patterns or shadows requiring the scene to keep stationary during the image acquisition process. Single-frame methods simplify the capture procedure but yield lower-quality separation results. In this paper we leverage the event camera to facilitate the separation of direct and global components enabling video-rate separation of high quality. In detail we adopt an event camera to record rapid illumination changes caused by the shadow of a line occluder sweeping over the scene and reconstruct the coarse separation results through event accumulation. We then design a network to resolve the noise in the coarse separation results and restore color information. A real-world dataset is collected using a hybrid camera system for network training and evaluation. Experimental results show superior performance over state-of-the-art methods."
status: "auto-generated; brief scan note"
---
## Core Problem

Separating the direct and global components of a scene aids in shape recovery and basic
material understanding.

## Core Method

Conventional methods capture multiple frames under high frequency illumination patterns or
shadows requiring the scene to keep stationary during the image acquisition process.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-
stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official CVF page inspected
under broad high-recall title workflow.。
