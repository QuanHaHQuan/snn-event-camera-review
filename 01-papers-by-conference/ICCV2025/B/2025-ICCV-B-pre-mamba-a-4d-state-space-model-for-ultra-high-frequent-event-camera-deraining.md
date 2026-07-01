---
title: 'PRE-Mamba: A 4D State Space Model for Ultra-High-Frequent Event Camera Deraining'
authors: ['Ciyu Ruan', 'Ruishan Guo', 'Zihang Gong', 'Jingao Xu', 'Wenhan Yang', 'Xinlei Chen']
conference: 'ICCV'
year: 2025
level: 'B'
category: 'Event Camera'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Ruan_PRE-Mamba_A_4D_State_Space_Model_for_Ultra-High-Frequent_Event_Camera_ICCV_2025_paper.html'
tags: []
abstract: 'Event cameras excel in high temporal resolution and dynamic range but suffer from dense noise in rainy conditions. Existing event deraining methods face trade-offs between temporal precision, deraining effectiveness, and computational efficiency. In this paper, we propose PRE-Mamba, a novel point-based event camera deraining framework that fully exploits the spatiotemporal characteristics of raw event and rain. Our framework introduces a 4D event cloud representation that integrates dual temporal scales to preserve high temporal precision, a Spatio-Temporal Decoupling and Fusion module (STDF) that enhances deraining capability by enabling shallow decoupling and interaction of temporal and spatial information, and a Multi-Scale State Space Model (MS3M) that captures deeper rain dynamics across dual-temporal and multi-spatial scales with linear computational complexity. Enhanced by frequency-domain regularization, PRE-Mamba achieves superior performance (0.95 SR, 0.91 NR, and 0.4s/M events) with only 0.26M parameters on EventRain-27K, a comprehensive dataset with labeled synthetic and real-world sequences. Moreover, our method generalizes well across varying rain intensities, viewpoints, and even snowy conditions. Code and dataset: https://github.com/softword-tt/PRE-Mamba.'
status: 'auto-generated; brief scan note'
---
## Core Problem

事件相机在该任务中的主要瓶颈是时序信息很强，但噪声、运动模糊或稀疏事件会让标准视觉方法失效。

## Core Method

方法围绕 event camera / event stream 输入，利用事件的异步变化特征完成任务建模。

## Key Metrics and Findings

需要结合官方论文页与正文核对具体指标；当前仅确认其属于事件相机侧工作。

## Personal Notes

可作为事件相机背景论文进入对应任务章节。
