---
title: "Beyond Duality: A Hybrid Framework of Leveraging Shared and Private Features for RGB-Event Object Detection"
authors: ["Keyao Wang", "Shuai Liu", "Hengda Shi", "Lukui Shi", "Haiyong Chen"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Beyond_Duality_A_Hybrid_Framework_of_Leveraging_Shared_and_Private_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Beyond_Duality_A_Hybrid_Framework_of_Leveraging_Shared_and_Private_CVPR_2026_paper.html"
tags: []
abstract: "RGB-Event object detection is able to capture clear and detailed features of the target while maintaining high-speed information collection. It is suitable for high dynamic or harsh environments and has become a research hotspot in recent years. The existing RGB-Event object detectors all struggle to fully utilize the fusion features of two modalities, but do not explicitly disentangle shared vs. private features to dedicated branches. To fully tap into the potential of single features, we propose a frequency-domain coherence-based Shared and Private Features Decoupling method for RGB-Event object detection, SPFD network. First, we design a FCFS module to separate shared and private features by exploring the spectral energy distribution differences between dual modalities. Then, we design a TriAdapt Encoder to process the shared and private features, selectively emphasizing texture-rich RGB features in static regions and motion-sensitive event features in dynamic regions, thereby achieving a robust balance between spatial detail and temporal awareness. Finally, a TriInject Decoder is proposed to emphasize the most discriminative modality features dynamically. Experimental results on the DSEC-Det and PKU-DAVIS-SOD datasets demonstrate that our model achieves competitive performance with state-of-the-art methods."
status: "auto-generated; brief scan note"
---

## Core Problem

RGB-Event object detection is able to capture clear and detailed features of the target while maintaining high-speed information collection.

## Core Method

It is suitable for high dynamic or harsh environments and has become a research hotspot in recent years.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `rgb-event visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
