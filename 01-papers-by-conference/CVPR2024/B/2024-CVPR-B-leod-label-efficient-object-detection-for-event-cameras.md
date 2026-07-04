---
title: "LEOD: Label-Efficient Object Detection for Event Cameras"
authors: ["Ziyi Wu", "Mathias Gehrig", "Qing Lyu", "Xudong Liu", "Igor Gilitschenski"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_LEOD_Label-Efficient_Object_Detection_for_Event_Cameras_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Wu_LEOD_Label-Efficient_Object_Detection_for_Event_Cameras_CVPR_2024_paper.html"
tags: []
abstract: "Object detection with event cameras benefits from the sensor's low latency and high dynamic range. However it is costly to fully label event streams for supervised training due to their high temporal resolution. To reduce this cost we present LEOD the first method for label-efficient event-based detection. Our approach unifies weakly- and semi-supervised object detection with a self-training mechanism. We first utilize a detector pre-trained on limited labels to produce pseudo ground truth on unlabeled events. Then the detector is re-trained with both real and generated labels. Leveraging the temporal consistency of events we run bi-directional inference and apply tracking-based post-processing to enhance the quality of pseudo labels. To stabilize training against label noise we further design a soft anchor assignment strategy. We introduce new experimental protocols to evaluate the task of label-efficient event-based detection on Gen1 and 1Mpx datasets. LEOD consistently outperforms supervised baselines across various labeling ratios. For example on Gen1 it improves mAP by 8.6% and 7.8% for RVT-S trained with 1% and 2% labels. On 1Mpx RVT-S with 10% labels even surpasses its fully-supervised counterpart using 100% labels. LEOD maintains its effectiveness even when all labeled data are available reaching new state-of-the-art results. Finally we show that our method readily scales to improve larger detectors as well. Code is released at https://github.com/Wuziyi616/LEOD."
status: "auto-generated; brief scan note"
---
## Core Problem

Object detection with event cameras benefits from the sensor's low latency and high dynamic
range.

## Core Method

However it is costly to fully label event streams for supervised training due to their high
temporal resolution.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event cameras; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
