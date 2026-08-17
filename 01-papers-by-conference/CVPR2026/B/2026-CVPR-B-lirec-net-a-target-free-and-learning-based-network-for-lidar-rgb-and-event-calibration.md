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
status: "official-abstract screening card"
---

## Official Abstract

Advanced autonomous systems rely on multi-sensor fusion for safer and more robust perception. To enable effective fusion, calibrating directly from natural driving scenes (i.e., target-free) with high accuracy is crucial for precise multi-sensor alignment. Existing learning-based calibration methods are typically designed for only a single pair of sensor modalities (i.e., a bi-modal setup). Unlike these methods, we propose LiREC-Net, a target-free, learning-based calibration network that jointly calibrates multiple sensor modality pairs, including LiDAR, RGB, and event data, within a unified framework. To reduce redundant computation and improve efficiency, we introduce a shared LiDAR representation that leverages features from both its 3D nature and projected depth map, ensuring better consistency across modalities. Trained and evaluated on established datasets, such as KITTI and DSEC, our LiREC-Net achieves competitive performance to bi-modal models and sets a new strong baseline for the tri-modal use case.

## Survey Role

LiREC-Net explicitly calibrates LiDAR, RGB, and event data in one target-free network. It provides non-spiking sensor-alignment and deployment background, not intersection-Core evidence.

## Advisor Role

Multi-sensor calibration may support future evaluation setups but does not contribute to SECNet representation, FFT, or SNN coupling.

## Verification Boundary

This card records official-title/abstract screening evidence. Verify the PDF before citing implementation details, formulas, tables, or numerical claims.
