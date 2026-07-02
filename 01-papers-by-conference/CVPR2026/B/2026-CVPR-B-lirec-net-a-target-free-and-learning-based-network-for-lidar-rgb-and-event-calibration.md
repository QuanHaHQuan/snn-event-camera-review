---
title: "LiREC-Net: A Target-Free and Learning-Based Network for LiDAR, RGB, and Event Calibration"
authors: ["Aditya Ranjan Dash", "Ramy Battrawy", "René Schuster", "Didier Stricker"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Dash_LiREC-Net_A_Target-Free_and_Learning-Based_Network_for_LiDAR_RGB_and_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Dash_LiREC-Net_A_Target-Free_and_Learning-Based_Network_for_LiDAR_RGB_and_CVPR_2026_paper.html"
tags: []
abstract: "Advanced autonomous systems rely on multi-sensor fusion for safer and more robust perception. To enable effective fusion, calibrating directly from natural driving scenes (i.e., target-free) with high accuracy is crucial for precise multi-sensor alignment. Existing learning-based calibration methods are typically designed for only a single pair of sensor modalities (i.e., a bi-modal setup). Unlike these methods, we propose LiREC-Net, a target-free, learning-based calibration network that jointly calibrates multiple sensor modality pairs, including LiDAR, RGB, and event data, within a unified framework. To reduce redundant computation and improve efficiency, we introduce a shared LiDAR representation that leverages features from both its 3D nature and projected depth map, ensuring better consistency across modalities. Trained and evaluated on established datasets, such as KITTI and DSEC, our LiREC-Net achieves competitive performance to bi-modal models and sets a new strong baseline for the tri-modal use case."
status: "auto-generated; brief scan note"
---
## Core Problem

Advanced autonomous systems rely on multi-sensor fusion for safer and more robust
perception.

## Core Method

To enable effective fusion, calibrating directly from natural driving scenes (i.e., target-
free) with high accuracy is crucial for precise multi-sensor alignment.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event data。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
