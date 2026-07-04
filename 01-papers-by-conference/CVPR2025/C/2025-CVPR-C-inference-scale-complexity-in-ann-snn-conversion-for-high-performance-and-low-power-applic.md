---
title: "Inference-Scale Complexity in ANN-SNN Conversion for High-Performance and Low-Power Applications"
authors: ["Tong Bu", "Maohua Li", "Zhaofei Yu"]
conference: "CVPR"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Bu_Inference-Scale_Complexity_in_ANN-SNN_Conversion_for_High-Performance_and_Low-Power_Applications_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Bu_Inference-Scale_Complexity_in_ANN-SNN_Conversion_for_High-Performance_and_Low-Power_Applications_CVPR_2025_paper.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) have emerged as a promising substitute for Artificial Neural Networks (ANNs) due to their advantages of fast inference and low power consumption. However, the lack of efficient training algorithms has hindered their widespread adoption. Even efficient ANN-SNN conversion methods necessitate quantized training of ANNs to enhance the effectiveness of the conversion, incurring additional training costs. To address these challenges, we propose an efficient ANN-SNN conversion framework with only inference scale complexity. The conversion framework includes a local threshold balancing algorithm, which enables efficient calculation of the optimal thresholds and fine-grained adjustment of the threshold value by channel-wise scaling. We also introduce an effective delayed evaluation strategy to mitigate the influence of the spike propagation delays. We demonstrate the scalability of our framework in typical computer vision tasks: image classification, semantic segmentation, object detection, and video classification. Our algorithm outperforms existing methods, highlighting its practical applicability and efficiency. Moreover, we have evaluated the energy consumption of the converted SNNs, demonstrating their superior low-power advantage compared to conventional ANNs. This approach simplifies the deployment of SNNs by leveraging open-source pre-trained ANN models, enabling fast, low-power inference with negligible performance reduction."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs) have emerged as a promising substitute for Artificial Neural
Networks (ANNs) due to their advantages of fast inference and low power consumption.

## Core Method

However, the lack of efficient training algorithms has hindered their widespread adoption.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNN。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural computation;
no clear event-camera/DVS evidence found.。 备注：CVPR 2025 official CVF page inspected under
broad high-recall title workflow.。
