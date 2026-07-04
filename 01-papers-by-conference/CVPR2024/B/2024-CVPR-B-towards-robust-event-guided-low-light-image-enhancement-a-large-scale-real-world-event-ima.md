---
title: "Towards Robust Event-guided Low-Light Image Enhancement: A Large-Scale Real-World Event-Image Dataset and Novel Approach"
authors: ["Guoqiang Liang", "Kanghao Chen", "Hangyu Li", "Yunfan Lu", "Lin Wang"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Liang_Towards_Robust_Event-guided_Low-Light_Image_Enhancement_A_Large-Scale_Real-World_Event-Image_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Liang_Towards_Robust_Event-guided_Low-Light_Image_Enhancement_A_Large-Scale_Real-World_Event-Image_CVPR_2024_paper.html"
tags: []
abstract: "Event camera has recently received much attention for low-light image enhancement (LIE) thanks to their distinct advantages such as high dynamic range. However current research is prohibitively restricted by the lack of large-scale real-world and spatial-temporally aligned event-image datasets. To this end we propose a real-world (indoor and outdoor) dataset comprising over 30K pairs of images and events under both low and normal illumination conditions. To achieve this we utilize a robotic arm that traces a consistent non-linear trajectory to curate the dataset with spatial alignment precision under 0.03mm. We then introduce a matching alignment strategy rendering 90% of our dataset with errors less than 0.01s. Based on the dataset we propose a novel event-guided LIE approach called EvLight towards robust performance in real-world low-light scenes. Specifically we first design the multi-scale holistic fusion branch to extract holistic structural and textural information from both events and images. To ensure robustness against variations in the regional illumination and noise we then introduce a Signal-to-Noise-Ratio (SNR)-guided regional feature selection to selectively fuse features of images from regions with high SNR and enhance those with low SNR by extracting regional structural information from events. our EvLight significantly surpasses the frame-based methods e.g. Retinexformer by 1.14 dB and 2.62 dB respectively. Code and datasets are available at https://vlislab22.github.io/eg-lowlight/."
status: "auto-generated; brief scan note"
---
## Core Problem

Event camera has recently received much attention for low-light image enhancement (LIE)
thanks to their distinct advantages such as high dynamic range.

## Core Method

However current research is prohibitively restricted by the lack of large-scale real-world
and spatial-temporally aligned event-image datasets.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-
stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official CVF page inspected
under broad high-recall title workflow.。
