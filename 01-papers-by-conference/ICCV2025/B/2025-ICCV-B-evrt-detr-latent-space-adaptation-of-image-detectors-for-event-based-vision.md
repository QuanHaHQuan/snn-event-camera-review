---
title: "EvRT-DETR: Latent Space Adaptation of Image Detectors for Event-based Vision"
authors: ["Dmitrii Torbunov", "Yihui Ren", "Animesh Ghose", "Odera Dim", "Yonggang Cui"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Torbunov_EvRT-DETR_Latent_Space_Adaptation_of_Image_Detectors_for_Event-based_Vision_ICCV_2025_paper.html"
tags: []
abstract: "Event-based cameras (EBCs) have emerged as a bio-inspired alternative to traditional cameras, offering advantages in power efficiency, temporal resolution, and high dynamic range. However, the development of image analysis methods for EBCs is challenging due to the sparse and asynchronous nature of the data. This work addresses the problem of object detection for EBC cameras. The current approaches to EBC object detection focus on constructing complex data representations and rely on specialized architectures. We introduce I2EvDet (Image-to-Event Detection), a novel adaptation framework that bridges mainstream object detection with temporal event data processing. First, we demonstrate that a Real-Time DEtection TRansformer, or RT-DETR, a state-of-the-art natural image detector, trained on a simple image-like representation of the EBC data achieves performance comparable to specialized EBC methods. Next, as part of our framework, we develop an efficient adaptation technique that transforms image-based detectors into event-based detection models by modifying their frozen latent representation space through minimal architectural additions. The resulting EvRT-DETR model reaches state-of-the-art performance on the standard benchmark datasets Gen1 (mAP +2.3) and 1Mpx/Gen4 (mAP +1.4). These results demonstrate a fundamentally new approach to EBC object detection through principled adaptation of mainstream architectures, offering an efficient alternative with potential applications to other temporal visual domains."
status: "auto-generated; brief scan note"
---
## Core Problem

Event-based cameras (EBCs) have emerged as a bio-inspired alternative to traditional
cameras, offering advantages in power efficiency, temporal resolution, and high dynamic
range.

## Core Method

However, the development of image analysis methods for EBCs is challenging due to the sparse
and asynchronous nature of the data.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event data; event-based vision; event-based camera; event-based
detection。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream evidence; no
clear SNN evidence.。
