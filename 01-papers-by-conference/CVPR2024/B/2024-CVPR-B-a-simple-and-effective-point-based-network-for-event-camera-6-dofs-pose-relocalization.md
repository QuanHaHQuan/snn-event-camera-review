---
title: "A Simple and Effective Point-based Network for Event Camera 6-DOFs Pose Relocalization"
authors: ["Hongwei Ren", "Jiadong Zhu", "Yue Zhou", "Haotian Fu", "Yulong Huang", "Bojun Cheng"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Ren_A_Simple_and_Effective_Point-based_Network_for_Event_Camera_6-DOFs_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Ren_A_Simple_and_Effective_Point-based_Network_for_Event_Camera_6-DOFs_CVPR_2024_paper.html"
tags: []
abstract: "Event cameras exhibit remarkable attributes such as high dynamic range asynchronicity and low latency making them highly suitable for vision tasks that involve high-speed motion in challenging lighting conditions. These cameras implicitly capture movement and depth information in events making them appealing sensors for Camera Pose Relocalization (CPR) tasks. Nevertheless existing CPR networks based on events neglect the pivotal fine-grained temporal information in events resulting in unsatisfactory performance. Moreover the energy-efficient features are further compromised by the use of excessively complex models hindering efficient deployment on edge devices. In this paper we introduce PEPNet a simple and effective point-based network designed to regress six degrees of freedom (6-DOFs) event camera poses. We rethink the relationship between the event camera and CPR tasks leveraging the raw Point Cloud directly as network input to harness the high-temporal resolution and inherent sparsity of events. PEPNet is adept at abstracting the spatial and implicit temporal features through hierarchical structure and explicit temporal features by Attentive Bi-directional Long Short-Term Memory (A-Bi-LSTM). By employing a carefully crafted lightweight design PEPNet delivers state-of-the-art (SOTA) performance on both indoor and outdoor datasets with meager computational resources. Specifically PEPNet attains a significant 38% and 33% performance improvement on the random split IJRR and M3ED datasets respectively. Moreover the lightweight design version PEPNet_ tiny accomplishes results comparable to the SOTA while employing a mere 0.5% of the parameters."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras exhibit remarkable attributes such as high dynamic range asynchronicity and
low latency making them highly suitable for vision tasks that involve high-speed motion in
challenging lighting conditions.

## Core Method

These cameras implicitly capture movement and depth information in events making them
appealing sensors for Camera Pose Relocalization (CPR) tasks.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
