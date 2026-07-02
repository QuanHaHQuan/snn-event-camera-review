---
title: "Event-Illumination Collaborative Low-light Image Enhancement with a High-resolution Real-world Dataset"
authors: ["Senyan Xu", "Zhijing Sun", "Kean Liu", "Xin Lu", "Ruixuan Jiang", "Xueyang Fu", "Zheng-Jun Zha"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Event-Illumination_Collaborative_Low-light_Image_Enhancement_with_a_High-resolution_Real-world_Dataset_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Event-Illumination_Collaborative_Low-light_Image_Enhancement_with_a_High-resolution_Real-world_Dataset_CVPR_2026_paper.html"
tags: []
abstract: "Event-based low-light image enhancement (LIE) methods mainly focus on incorporating high dynamic range (HDR) information from events while overlooking the essential global illumination in images and the inherent noise sensitivity of event signals in real-world scenarios. To address these issues, we propose EIC-LIE, an event-illumination collaborative LIE framework. Concretely, we first design an Event-Illumination Collaborative Interaction (EICI) module, which contains two key processes: forward gathering, which gathers HDR features across varying lighting conditions, and backward injection, which provides complementary content for illumination and event representations.Next, we introduce an Illumination-aware Event Filter (IAEF) that dynamically reduces event noise based on brightness statistics derived from images. Additionally, we build a beam-splitter-based hybrid imaging system to collect high-quality event-image pairs with temporal synchronization from dynamic scenes, providing the first high-resolution, real-world event-based LIE dataset.Extensive experiments show that our EIC-LIE outperforms state-of-the-art methods on five real-world and synthetic datasets, significantly surpassing previous methods with improvements of up to 1.24dB in PSNR and 0.069 in SSIM. The code and dataset are released at https://github.com/QUEAHREN/EIC-LIE."
status: "auto-generated; brief scan note"
---

## Core Problem

Event-based low-light image enhancement (LIE) methods mainly focus on incorporating high dynamic range (HDR) information from events while overlooking the essential global illumination in images and the inherent noise sensitivity of event signals in real-world scenarios.

## Core Method

To address these issues, we propose EIC-LIE, an event-illumination collaborative LIE framework.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event-image visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
