---
title: 'FlashCap: Millisecond-Accurate Human Motion Capture via Flashing LEDs and Event-Based Vision'
authors: ['Zekai Wu', 'Shuqi Fan', 'Mengyin Liu', 'Yuhua Luo', 'Xincheng Lin', 'Ming Yan', 'Junhao Wu', 'Xiuhong Lin', 'Yuexin Ma', 'Chenglu Wen', 'Lan Xu', 'Siqi Shen', 'Cheng Wang']
conference: 'CVPR'
year: 2026
level: 'B'
category: 'Event Camera'
pdf_link: 'https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_FlashCap_Millisecond-Accurate_Human_Motion_Capture_via_Flashing_LEDs_and_Event-Based_CVPR_2026_paper.pdf'
official_page: 'https://openaccess.thecvf.com/content/CVPR2026/html/Wu_FlashCap_Millisecond-Accurate_Human_Motion_Capture_via_Flashing_LEDs_and_Event-Based_CVPR_2026_paper.html'
tags: []
abstract: 'Precise motion timing (PMT) is crucial for swift motion analysis. A millisecond difference may determine victory or defeat in sports competitions. Despite substantial progress in human pose estimation (HPE), PMT remains largely overlooked by the HPE community due to the limited availability of high-temporal-resolution labeled datasets. Today, PMT is achieved using high-speed RGB cameras in specialized scenarios such as the Olympic Games; however, their high costs, light sensitivity, bandwidth, and computational complexity limit their feasibility for daily use. We developed FlashCap, the first flashing LED-based MoCap system for PMT. With FlashCap, we collect a millisecond-resolution human motion dataset, FlashMotion, comprising the event, RGB, LiDAR, and IMU modalities, and demonstrate its high quality through rigorous validation. To evaluate the merits of FlashMotion, we perform two tasks: precise motion timing and high-temporal-resolution HPE. For these tasks, we propose ResPose, a simple yet effective baseline that learns residual poses based on events and RGBs. Experimental results show that ResPose reduces pose estimation errors by  40% and achieves millisecond-level timing accuracy, enabling new research opportunities. The dataset and code will be shared with the community.'
status: 'auto-generated; brief scan note'
---

## Core Problem

高时间精度人体动作捕捉依赖昂贵高速 RGB 设备，而普通 HPE 数据和方法难以提供毫秒级运动时序标注。

## Core Method

FlashCap 使用 flashing LEDs 与 event-based vision 构建毫秒级 MoCap 系统，并发布包含 event、RGB、LiDAR、IMU 的 FlashMotion 数据；ResPose 基线结合事件与 RGB 学习 residual poses。

## Key Metrics and Findings

摘要报告 ResPose 将姿态估计误差降低 40%，并达到毫秒级 timing accuracy；实验设置和指标需人工核对。

## Personal Notes

B 类事件相机应用/数据集论文，对“事件相机的高时间分辨率优势”和人体运动捕捉案例很有用。
