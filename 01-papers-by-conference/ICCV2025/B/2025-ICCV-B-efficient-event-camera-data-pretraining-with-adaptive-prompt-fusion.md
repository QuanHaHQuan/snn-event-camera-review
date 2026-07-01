---
title: 'Efficient Event Camera Data Pretraining with Adaptive Prompt Fusion'
authors: ['Quanmin Liang', 'Qiang Li', 'Shuai Liu', 'Xinzi Cao', 'Jinyi Lu', 'Feidiao Yang', 'Wei Zhang', 'Kai Huang', 'Yonghong Tian']
conference: 'ICCV'
year: 2025
level: 'B'
category: 'Event Camera'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Liang_Efficient_Event_Camera_Data_Pretraining_with_Adaptive_Prompt_Fusion_ICCV_2025_paper.html'
tags: []
abstract: 'Applying pretraining-finetuning paradigm to event cameras presents significant challenges due to the scarcity of large-scale event datasets and the inherently sparse nature of event data, which increases the risk of overfitting during extensive pretraining.In this paper, we explore the transfer of pretrained image knowledge to the domain of event cameras to address this challenge. The key to our approach lies in adapting event data representations to align with image pretrained models while simultaneously integrating spatiotemporal information and mitigating data sparsity. To achieve this, we propose a lightweight SpatioTemporal information fusion Prompting (STP) method, which progressively fuses the spatiotemporal characteristics of event data through a dynamic perception module with multi-scale spatiotemporal receptive fields, enabling compatibility with image pretrained models.STP enhances event data representation by capturing local information within a large receptive field and performing global information exchange along the temporal dimension. This strategy effectively reduces sparse regions in event data while refining fine-grained details, all while preserving its inherent spatiotemporal structure. Our method significantly outperforms previous state-of-the-art approaches across classification, semantic segmentation, and optical flow estimation tasks. For instance, it achieves a top-1 accuracy of 68.87% (+4.04%) on N-ImageNet with only 1/10 of the pretraining parameters and 1/3 of the training epochs.'
status: 'auto-generated; brief scan note'
---
## Core Problem

事件相机在该任务中的主要瓶颈是时序信息很强，但噪声、运动模糊或稀疏事件会让标准视觉方法失效。

## Core Method

方法围绕 event camera / event stream 输入，利用事件的异步变化特征完成任务建模。

## Key Metrics and Findings

需要结合官方论文页与正文核对具体指标；当前仅确认其属于事件相机侧工作。

## Personal Notes

可作为事件相机背景论文进入对应任务章节。
