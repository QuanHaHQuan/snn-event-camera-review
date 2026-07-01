---
title: "EventGait: Towards Robust Gait Recognition with Event Streams"
authors: ["Senyan Xu", "Shuai Chen", "Chuanfu Shen", "Kean Liu", "Zhijing Sun", "Chengzhi Cao", "Xueyang Fu"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_EventGait_Towards_Robust_Gait_Recognition_with_Event_Streams_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Xu_EventGait_Towards_Robust_Gait_Recognition_with_Event_Streams_CVPR_2026_paper.html"
tags: []
abstract: "Gait recognition enables non-intrusive, privacy-preserving identification but suffers in uncontrolled environments due to illumination and motion sensitivity in conventional cameras. In this work, we explore gait recognition using event cameras, which offer microsecond temporal resolution and high dynamic range, naturally capturing robust dynamic cues and suppressing static noise. Existing event-based approaches typically aggregate event streams into event images over long time windows, thereby discarding fine-grained motion dynamics critical for gait recognition. Therefore, we propose EventGait, an end-to-end dual-stream framework that separately models motion and shape while preserving the advantages of events. Our dynamic stream leverages a Mixture of Spiking Experts (MoSE) with diverse neuron constants for robust dynamic perception across complex motion and illumination scenes, while the static stream learns dense shape representations via Cross-modal Structural Alignment (CroSA) with large vision foundation models. To address the absence of large-scale event-based gait datasets, we introduce a synthesis pipeline and release two new benchmarks: SUSTech1K-E and CCGR-Mini-E. Extensive experiments have shown that event-based gait recognition not only achieves results comparable to camera-based gait recognition under normal conditions but also significantly outperforms it in low-light scenarios. Our approach sets a new state of the art on both synthesized and real-world event-based gait benchmarks, highlighting the robustness and potential of event-driven gait analysis. The code and datasets are released at https://github.com/QUEAHREN/EventGait."
status: "auto-generated; brief scan note"
---

## Core Problem

步态识别在复杂光照和动态环境下容易退化，传统帧相机难以稳定提取动态线索。

## Core Method

提出双流框架，同时建模 motion 与 shape，并尽量保留事件流中的细粒度动作信息。

## Key Metrics and Findings

摘要指出长时间窗聚合会丢失关键动态，作者试图避免这一点。

## Personal Notes

适合放在事件相机任务应用章节。

