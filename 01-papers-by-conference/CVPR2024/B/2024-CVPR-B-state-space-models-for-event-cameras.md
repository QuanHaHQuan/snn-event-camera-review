---
title: "State Space Models for Event Cameras"
authors: ["Nikola Zubic", "Mathias Gehrig", "Davide Scaramuzza"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Zubic_State_Space_Models_for_Event_Cameras_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Zubic_State_Space_Models_for_Event_Cameras_CVPR_2024_paper.html"
tags: []
abstract: "Today state-of-the-art deep neural networks that process event-camera data first convert a temporal window of events into dense grid-like input representations. As such they exhibit poor generalizability when deployed at higher inference frequencies (i.e. smaller temporal windows) than the ones they were trained on. We address this challenge by introducing state-space models (SSMs) with learnable timescale parameters to event-based vision. This design adapts to varying frequencies without the need to retrain the network at different frequencies. Additionally we investigate two strategies to counteract aliasing effects when deploying the model at higher frequencies. We comprehensively evaluate our approach against existing methods based on RNN and Transformer architectures across various benchmarks including Gen1 and 1 Mpx event camera datasets. Our results demonstrate that SSM-based models train 33% faster and also exhibit minimal performance degradation when tested at higher frequencies than the training input. Traditional RNN and Transformer models exhibit performance drops of more than 20 mAP with SSMs having a drop of 3.31 mAP highlighting the effectiveness of SSMs in event-based vision tasks."
status: "auto-generated; brief scan note"
---
## Core Problem

Today state-of-the-art deep neural networks that process event-camera data first convert a
temporal window of events into dense grid-like input representations.

## Core Method

As such they exhibit poor generalizability when deployed at higher inference frequencies
(i.e.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event cameras; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
