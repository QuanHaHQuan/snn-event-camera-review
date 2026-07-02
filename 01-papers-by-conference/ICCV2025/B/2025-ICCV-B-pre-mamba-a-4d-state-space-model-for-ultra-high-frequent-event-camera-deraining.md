---
title: "PRE-Mamba: A 4D State Space Model for Ultra-High-Frequent Event Camera Deraining"
authors: ["Ciyu Ruan", "Ruishan Guo", "Zihang Gong", "Jingao Xu", "Wenhan Yang", "Xinlei Chen"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Ruan_PRE-Mamba_A_4D_State_Space_Model_for_Ultra-High-Frequent_Event_Camera_ICCV_2025_paper.html"
tags: []
abstract: "Event cameras excel in high temporal resolution and dynamic range but suffer from dense noise in rainy conditions. Existing event deraining methods face trade-offs between temporal precision, deraining effectiveness, and computational efficiency. In this paper, we propose PRE-Mamba, a novel point-based event camera deraining framework that fully exploits the spatiotemporal characteristics of raw event and rain. Our framework introduces a 4D event cloud representation that integrates dual temporal scales to preserve high temporal precision, a Spatio-Temporal Decoupling and Fusion module (STDF) that enhances deraining capability by enabling shallow decoupling and interaction of temporal and spatial information, and a Multi-Scale State Space Model (MS3M) that captures deeper rain dynamics across dual-temporal and multi-spatial scales with linear computational complexity. Enhanced by frequency-domain regularization, PRE-Mamba achieves superior performance (0.95 SR, 0.91 NR, and 0.4s/M events) with only 0.26M parameters on EventRain-27K, a comprehensive dataset with labeled synthetic and real-world sequences. Moreover, our method generalizes well across varying rain intensities, viewpoints, and even snowy conditions. Code and dataset: https://github.com/softword-tt/PRE-Mamba."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras excel in high temporal resolution and dynamic range but suffer from dense
noise in rainy conditions.

## Core Method

Existing event deraining methods face trade-offs between temporal precision, deraining
effectiveness, and computational efficiency.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
