---
title: "Latency Correction for Event-guided Deblurring and Frame Interpolation"
authors: ["Yixin Yang", "Jinxiu Liang", "Bohan Yu", "Yan Chen", "Jimmy S. Ren", "Boxin Shi"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Latency_Correction_for_Event-guided_Deblurring_and_Frame_Interpolation_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Latency_Correction_for_Event-guided_Deblurring_and_Frame_Interpolation_CVPR_2024_paper.html"
tags: []
abstract: "Event cameras with their high temporal resolution dynamic range and low power consumption are particularly good at time-sensitive applications like deblurring and frame interpolation. However their performance is hindered by latency variability especially under low-light conditions and with fast-moving objects. This paper addresses the challenge of latency in event cameras -- the temporal discrepancy between the actual occurrence of changes in the corresponding timestamp assigned by the sensor. Focusing on event-guided deblurring and frame interpolation tasks we propose a latency correction method based on a parameterized latency model. To enable data-driven learning we develop an event-based temporal fidelity to describe the sharpness of latent images reconstructed from events and the corresponding blurry images and reformulate the event-based double integral model differentiable to latency. The proposed method is validated using synthetic and real-world datasets demonstrating the benefits of latency correction for deblurring and interpolation across different lighting conditions."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras with their high temporal resolution dynamic range and low power consumption
are particularly good at time-sensitive applications like deblurring and frame
interpolation.

## Core Method

However their performance is hindered by latency variability especially under low-light
conditions and with fast-moving objects.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-
stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official CVF page inspected
under broad high-recall title workflow.。
