---
title: "Diffusion-based Event Generation for High-Quality Image Deblurring"
authors: ["Xinan Xie", "Qing Zhang", "Wei-Shi Zheng"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Xie_Diffusion-based_Event_Generation_for_High-Quality_Image_Deblurring_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Xie_Diffusion-based_Event_Generation_for_High-Quality_Image_Deblurring_CVPR_2025_paper.html"
tags: []
abstract: "While event-based deblurring have demonstrated impressive results, they are impractical for consumer photos captured by cell phones and digital cameras that are not equipped with the event sensor. To address this problem, we in this paper propose a novel deblurring framework called Event Generation Deblurring (EGDeblurring), which allows to effectively deblur an image by generating event guidance describing the motion information using a diffusion model. Specifically, we design a motion prior generation diffusion model and a feature extractor to produce prior information beneficial for deblurring, rather than generating the raw event representation. In order to achieve effective fusion of motion prior information with blurry images and produce high-quality results, we develop a regression deblurring network embedded with a dual-attention channel fusion block. Experiments on multiple datasets demonstrate that our method outperforms state-of-the-art image deblurring methods. Our code is available at https://github.com/XinanXie/EGDeblurring https://github.com/XinanXie/EGDeblurring."
status: "auto-generated; brief scan note"
---
## Core Problem

While event-based deblurring have demonstrated impressive results, they are impractical for
consumer photos captured by cell phones and digital cameras that are not equipped with the
event sensor.

## Core Method

To address this problem, we in this paper propose a novel deblurring framework called Event
Generation Deblurring (EGDeblurring), which allows to effectively deblur an image by
generating event guidance describing the motion information using a diffusion model.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-
stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official CVF page inspected
under broad high-recall title workflow.。
