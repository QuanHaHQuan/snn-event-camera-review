---
title: 'EvRT-DETR: Latent Space Adaptation of Image Detectors for Event-based Vision'
authors: ['Dmitrii Torbunov', 'Yihui Ren', 'Animesh Ghose', 'Odera Dim', 'Yonggang Cui']
conference: 'ICCV'
year: 2025
level: 'B'
category: 'Event Camera'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Torbunov_EvRT-DETR_Latent_Space_Adaptation_of_Image_Detectors_for_Event-based_Vision_ICCV_2025_paper.html'
tags: []
abstract: 'Event-based cameras (EBCs) have emerged as a bio-inspired alternative to traditional cameras, offering advantages in power efficiency, temporal resolution, and high dynamic range. However, the development of image analysis methods for EBCs is challenging due to the sparse and asynchronous nature of the data. This work addresses the problem of object detection for EBC cameras. The current approaches to EBC object detection focus on constructing complex data representations and rely on specialized architectures. We introduce I2EvDet (Image-to-Event Detection), a novel adaptation framework that bridges mainstream object detection with temporal event data processing. First, we demonstrate that a Real-Time DEtection TRansformer, or RT-DETR, a state-of-the-art natural image detector, trained on a simple image-like representation of the EBC data achieves performance comparable to specialized EBC methods. Next, as part of our framework, we develop an efficient adaptation technique that transforms image-based detectors into event-based detection models by modifying their frozen latent representation space through minimal architectural additions. The resulting EvRT-DETR model reaches state-of-the-art performance on the standard benchmark datasets Gen1 (mAP +2.3) and 1Mpx/Gen4 (mAP +1.4). These results demonstrate a fundamentally new approach to EBC object detection through principled adaptation of mainstream architectures, offering an efficient alternative with potential applications to other temporal visual domains.'
status: 'auto-generated; brief scan note'
---

## Core Problem

事件相机目标检测通常依赖专门的数据表示和架构，限制了主流图像检测器迁移到 sparse/asynchronous EBC 数据的效率。

## Core Method

EvRT-DETR/I2EvDet 先验证 RT-DETR 在简单 image-like EBC 表示上可达到接近专门方法的效果，再通过少量结构改动在冻结 latent space 中适配图像检测器到事件数据。

## Key Metrics and Findings

摘要报告在 Gen1 上 mAP +2.3、1Mpx/Gen4 上 mAP +1.4，达到 SOTA；需核对 baseline 和训练设置。

## Personal Notes

B 类事件视觉检测论文，对“图像模型到事件相机任务迁移”这一背景方向很有用。
