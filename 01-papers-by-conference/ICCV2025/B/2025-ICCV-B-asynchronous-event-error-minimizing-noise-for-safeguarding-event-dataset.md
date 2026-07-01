---
title: 'Asynchronous Event Error-Minimizing Noise for Safeguarding Event Dataset'
authors: ['Ruofei Wang', 'Peiqi Duan', 'Boxin Shi', 'Renjie Wan']
conference: 'ICCV'
year: 2025
level: 'B'
category: 'Event Camera'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Asynchronous_Event_Error-Minimizing_Noise_for_Safeguarding_Event_Dataset_ICCV_2025_paper.html'
tags: []
abstract: "With more event datasets being released online, safeguarding the event dataset against unauthorized usage has become a serious concern for data owners. Unlearnable Examples are proposed to prevent the unauthorized exploitation of image datasets. However, it's unclear how to create unlearnable asynchronous event streams to prevent event misuse. In this work, we propose the first unlearnable event stream generation method to prevent unauthorized training from event datasets. A new form of asynchronous event error-minimizing noise is proposed to perturb event streams, tricking the unauthorized model into learning embedded noise instead of realistic features. To be compatible with the sparse event, a projection strategy is presented to sparsify the noise to render our unlearnable event streams (UEvs). Extensive experiments demonstrate that our method effectively protects event data from unauthorized exploitation, while preserving their utility for legitimate use. We hope our UEvs contribute to the advancement of secure and trustworthy event dataset sharing. Code is available at: https://github.com/rfww/uevs."
status: 'auto-generated; brief scan note'
---

## Core Problem

事件数据集公开后可能被未授权训练使用，但现有 unlearnable examples 主要针对图像，如何保护稀疏异步 event streams 仍不明确。

## Core Method

提出 asynchronous event error-minimizing noise，用扰动事件流诱导未授权模型学习噪声特征；同时设计 projection strategy 使噪声适配稀疏事件数据。

## Key Metrics and Findings

摘要称方法能保护 event data 免受未授权利用，同时保持合法使用效用；具体攻击/训练设置和效用指标需人工核对。

## Personal Notes

B 类事件数据安全论文，适合在事件数据集共享、数据治理和 benchmark 风险部分简要引用。
