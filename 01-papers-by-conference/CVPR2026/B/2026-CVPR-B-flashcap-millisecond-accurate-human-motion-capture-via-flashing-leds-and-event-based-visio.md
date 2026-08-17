---
title: "FlashCap: Millisecond-Accurate Human Motion Capture via Flashing LEDs and Event-Based Vision"
authors: ["Zekai Wu", "Shuqi Fan", "Mengyin Liu", "Yuhua Luo", "Xincheng Lin", "Ming Yan", "Junhao Wu", "Xiuhong Lin", "Yuexin Ma", "Chenglu Wen", "Lan Xu", "Siqi Shen", "Cheng Wang"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_FlashCap_Millisecond-Accurate_Human_Motion_Capture_via_Flashing_LEDs_and_Event-Based_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Wu_FlashCap_Millisecond-Accurate_Human_Motion_Capture_via_Flashing_LEDs_and_Event-Based_CVPR_2026_paper.html"
tags: []
abstract: "Precise motion timing (PMT) is crucial for swift motion analysis. A millisecond difference may determine victory or defeat in sports competitions. Despite substantial progress in human pose estimation (HPE), PMT remains largely overlooked by the HPE community due to the limited availability of high-temporal-resolution labeled datasets. Today, PMT is achieved using high-speed RGB cameras in specialized scenarios such as the Olympic Games; however, their high costs, light sensitivity, bandwidth, and computational complexity limit their feasibility for daily use. We developed FlashCap, the first flashing LED-based MoCap system for PMT. With FlashCap, we collect a millisecond-resolution human motion dataset, FlashMotion, comprising the event, RGB, LiDAR, and IMU modalities, and demonstrate its high quality through rigorous validation. To evaluate the merits of FlashMotion, we perform two tasks: precise motion timing and high-temporal-resolution HPE. For these tasks, we propose ResPose, a simple yet effective baseline that learns residual poses based on events and RGBs. Experimental results show that ResPose reduces pose estimation errors by 40% and achieves millisecond-level timing accuracy, enabling new research opportunities. The dataset and code will be shared with the community."
status: "official-abstract screening card"
---

## Official Abstract

Precise motion timing (PMT) is crucial for swift motion analysis. A millisecond difference may determine victory or defeat in sports competitions. Despite substantial progress in human pose estimation (HPE), PMT remains largely overlooked by the HPE community due to the limited availability of high-temporal-resolution labeled datasets. Today, PMT is achieved using high-speed RGB cameras in specialized scenarios such as the Olympic Games; however, their high costs, light sensitivity, bandwidth, and computational complexity limit their feasibility for daily use. We developed FlashCap, the first flashing LED-based MoCap system for PMT. With FlashCap, we collect a millisecond-resolution human motion dataset, FlashMotion, comprising the event, RGB, LiDAR, and IMU modalities, and demonstrate its high quality through rigorous validation. To evaluate the merits of FlashMotion, we perform two tasks: precise motion timing and high-temporal-resolution HPE. For these tasks, we propose ResPose, a simple yet effective baseline that learns residual poses based on events and RGBs. Experimental results show that ResPose reduces pose estimation errors by 40% and achieves millisecond-level timing accuracy, enabling new research opportunities. The dataset and code will be shared with the community.

## Survey Role

FlashCap supplies millisecond-resolution event/RGB/LiDAR/IMU motion capture and an event-RGB pose baseline. It is task and dataset background without an SNN.

## Advisor Role

Its high-temporal-resolution benchmark is adjacent evaluation evidence, not a direct Event Cloud, frequency, or SNN mechanism.

## Verification Boundary

This card records official-title/abstract screening evidence. Verify the PDF before citing implementation details, formulas, tables, or numerical claims.
