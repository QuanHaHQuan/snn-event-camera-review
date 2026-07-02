---
title: "Efficient Event Camera Data Pretraining with Adaptive Prompt Fusion"
authors: ["Quanmin Liang", "Qiang Li", "Shuai Liu", "Xinzi Cao", "Jinyi Lu", "Feidiao Yang", "Wei Zhang", "Kai Huang", "Yonghong Tian"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Liang_Efficient_Event_Camera_Data_Pretraining_with_Adaptive_Prompt_Fusion_ICCV_2025_paper.html"
tags: []
abstract: "Applying pretraining-finetuning paradigm to event cameras presents significant challenges due to the scarcity of large-scale event datasets and the inherently sparse nature of event data, which increases the risk of overfitting during extensive pretraining.In this paper, we explore the transfer of pretrained image knowledge to the domain of event cameras to address this challenge. The key to our approach lies in adapting event data representations to align with image pretrained models while simultaneously integrating spatiotemporal information and mitigating data sparsity. To achieve this, we propose a lightweight SpatioTemporal information fusion Prompting (STP) method, which progressively fuses the spatiotemporal characteristics of event data through a dynamic perception module with multi-scale spatiotemporal receptive fields, enabling compatibility with image pretrained models.STP enhances event data representation by capturing local information within a large receptive field and performing global information exchange along the temporal dimension. This strategy effectively reduces sparse regions in event data while refining fine-grained details, all while preserving its inherent spatiotemporal structure. Our method significantly outperforms previous state-of-the-art approaches across classification, semantic segmentation, and optical flow estimation tasks. For instance, it achieves a top-1 accuracy of 68.87% (+4.04%) on N-ImageNet with only 1/10 of the pretraining parameters and 1/3 of the training epochs."
status: "auto-generated; brief scan note"
---
## Core Problem

Applying pretraining-finetuning paradigm to event cameras presents significant challenges
due to the scarcity of large-scale event datasets and the inherently sparse nature of event
data, which increases the risk of overfitting during extensive pretraining.In this paper, we
explore the transfer of pretrained image knowledge to the domain of event cameras to address
this challenge.

## Core Method

The key to our approach lies in adapting event data representations to align with image
pretrained models while simultaneously integrating spatiotemporal information and mitigating
data sparsity.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event data。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
