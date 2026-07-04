---
title: "3D Feature Tracking via Event Camera"
authors: ["Siqi Li", "Zhikuan Zhou", "Zhou Xue", "Yipeng Li", "Shaoyi Du", "Yue Gao"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Li_3D_Feature_Tracking_via_Event_Camera_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Li_3D_Feature_Tracking_via_Event_Camera_CVPR_2024_paper.html"
tags: []
abstract: "This paper presents the first 3D feature tracking method with the corresponding dataset. Our proposed method takes event streams from stereo event cameras as input to predict 3D trajectories of the target features with high-speed motion. To achieve this our method leverages a joint framework to predict the 2D feature motion offsets and the 3D feature spatial position simultaneously. A motion compensation module is leveraged to overcome the feature deformation. A patch matching module based on bi-polarity hypergraph modeling is proposed to robustly estimate the feature spatial position. Meanwhile we collect the first 3D feature tracking dataset with high-speed moving objects and ground truth 3D feature trajectories at 250 FPS named E-3DTrack which can be used as the first high-speed 3D feature tracking benchmark. Our code and dataset could be found at: https://github.com/lisiqi19971013/E-3DTrack."
status: "auto-generated; brief scan note"
---
## Core Problem

This paper presents the first 3D feature tracking method with the corresponding dataset.

## Core Method

Our proposed method takes event streams from stereo event cameras as input to predict 3D
trajectories of the target features with high-speed motion.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
