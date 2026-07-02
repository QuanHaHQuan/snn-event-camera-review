---
title: "Event-based Tiny Object Detection: A Benchmark Dataset and Baseline"
authors: ["Nuo Chen", "Chao Xiao", "Yimian Dai", "Shiman He", "Miao Li", "Wei An"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Event-based_Tiny_Object_Detection_A_Benchmark_Dataset_and_Baseline_ICCV_2025_paper.html"
tags: []
abstract: "Small object detection (SOD) in anti-UAV task is a challenging problem due to the small size of UAVs and complex backgrounds. Traditional frame-based cameras struggle to detect small objects in complex environments due to their low frame rates, limited dynamic range, and data redundancy. Event cameras, with microsecond temporal resolution and high dynamic range, provide a more effective solution for SOD. However, existing event-based object detection datasets are limited in scale, feature large targets size, and lack diverse backgrounds, making them unsuitable for SOD benchmarks. In this paper, we introduce a Event-based Small object detection (EVSOD) dataset (namely EV-UAV), the first large-scale, highly diverse benchmark for anti-UAV tasks. It includes 147 sequences with over 2.3 million event-level annotations, featuring extremely small targets (averaging 6.8 x 5.4 pixels) and diverse scenarios such as urban clutter and extreme lighting conditions. Furthermore, based on the observation that small moving targets form continuous curves in spatiotemporal event point clouds, we propose Event based Sparse Segmentation Network (EV-SpSegNet), a novel baseline for event segmentation in point cloud space, along with a Spatiotemporal Correlation (STC) loss that leverages motion continuity to guide the network in retaining target events. Extensive experiments on the EV-UAV dataset demonstrate the superiority of our method and provide a benchmark for future research in EVSOD."
status: "auto-generated; brief scan note"
---
## Core Problem

Small object detection (SOD) in anti-UAV task is a challenging problem due to the small size
of UAVs and complex backgrounds.

## Core Method

Traditional frame-based cameras struggle to detect small objects in complex environments due
to their low frame rates, limited dynamic range, and data redundancy.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
