---
title: "Scene Adaptive Sparse Transformer for Event-based Object Detection"
authors: ["Yansong Peng", "Hebei Li", "Yueyi Zhang", "Xiaoyan Sun", "Feng Wu"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Peng_Scene_Adaptive_Sparse_Transformer_for_Event-based_Object_Detection_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Peng_Scene_Adaptive_Sparse_Transformer_for_Event-based_Object_Detection_CVPR_2024_paper.html"
tags: []
abstract: "While recent Transformer-based approaches have shown impressive performances on event-based object detection tasks their high computational costs still diminish the low power consumption advantage of event cameras. Image-based works attempt to reduce these costs by introducing sparse Transformers. However they display inadequate sparsity and adaptability when applied to event-based object detection since these approaches cannot balance the fine granularity of token-level sparsification and the efficiency of window-based Transformers leading to reduced performance and efficiency. Furthermore they lack scene-specific sparsity optimization resulting in information loss and a lower recall rate. To overcome these limitations we propose the Scene Adaptive Sparse Transformer (SAST). SAST enables window-token co-sparsification significantly enhancing fault tolerance and reducing computational overhead. Leveraging the innovative scoring and selection modules along with the Masked Sparse Window Self-Attention SAST showcases remarkable scene-aware adaptability: It focuses only on important objects and dynamically optimizes sparsity level according to scene complexity maintaining a remarkable balance between performance and computational cost. The evaluation results show that SAST outperforms all other dense and sparse networks in both performance and efficiency on two large-scale event-based object detection datasets (1Mpx and Gen1). Code: https://github.com/Peterande/SAST"
status: "auto-generated; brief scan note"
---
## Core Problem

While recent Transformer-based approaches have shown impressive performances on event-based
object detection tasks their high computational costs still diminish the low power
consumption advantage of event cameras.

## Core Method

Image-based works attempt to reduce these costs by introducing sparse Transformers.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
