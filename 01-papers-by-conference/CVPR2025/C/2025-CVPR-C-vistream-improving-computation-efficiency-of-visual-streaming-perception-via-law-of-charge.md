---
title: "VISTREAM: Improving Computation Efficiency of Visual Streaming Perception via Law-of-Charge-Conservation Inspired Spiking Neural Network"
authors: ["Kang You", "Ziling Wei", "Jing Yan", "Boning Zhang", "Qinghai Guo", "Yaoyu Zhang", "Zhezhi He"]
conference: "CVPR"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/You_VISTREAM_Improving_Computation_Efficiency_of_Visual_Streaming_Perception_via_Law-of-Charge-Conservation_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/You_VISTREAM_Improving_Computation_Efficiency_of_Visual_Streaming_Perception_via_Law-of-Charge-Conservation_CVPR_2025_paper.html"
tags: []
abstract: "Visual streaming perception (VSP) involves online intelligent processing of sequential frames captured by vision sensors, enabling real-time decision-making in applications such as autonomous driving, UAVs, and AR/VR. However, the computational efficiency of VSP on edge devices remains a challenge due to power constraints and the underutilization of temporal dependencies between frames. While spiking neural networks (SNNs) offer biologically inspired event-driven processing with potential energy benefits, their practical advantage over artificial neural networks (ANNs) for VSP tasks remains unproven.In this work, we introduce a novel framework, VISTREAM, which leverages the Law of Charge Conservation (LoCC) property in ST-BIF neurons and a differential encoding (DiffEncode) scheme to optimize SNN inference for VSP. By encoding temporal differences between neighboring frames and eliminating frequent membrane resets, VISTREAM achieves significant computational efficiency while maintaining accuracy equivalent to its ANN counterpart. We provide theoretical proofs of equivalence and validate VISTREAM across diverse VSP tasks, including object detection, tracking, and segmentation, demonstrating substantial energy savings without compromising performance."
status: "auto-generated; brief scan note"
---
## Core Problem

Visual streaming perception (VSP) involves online intelligent processing of sequential
frames captured by vision sensors, enabling real-time decision-making in applications such
as autonomous driving, UAVs, and AR/VR.

## Core Method

However, the computational efficiency of VSP on edge devices remains a challenge due to
power constraints and the underutilization of temporal dependencies between frames.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural network; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：CVPR 2025
official CVF page inspected under broad high-recall title workflow.。
