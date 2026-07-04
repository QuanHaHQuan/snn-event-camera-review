---
title: "Object Detection using Event Camera: A MoE Heat Conduction based Detector and A New Benchmark Dataset"
authors: ["Xiao Wang", "Yu Jin", "Wentao Wu", "Wei Zhang", "Lin Zhu", "Bo Jiang", "Yonghong Tian"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Object_Detection_using_Event_Camera_A_MoE_Heat_Conduction_based_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Object_Detection_using_Event_Camera_A_MoE_Heat_Conduction_based_CVPR_2025_paper.html"
tags: []
abstract: "Object detection in event streams has emerged as a cutting-edge research area, demonstrating superior performance in low-light conditions, scenarios with motion blur, and rapid movements. Current detectors leverage spiking neural networks, Transformers, or convolutional neural networks as their core architectures, each with its own set of limitations including restricted performance, high computational overhead, or limited local receptive fields. This paper introduces a novel MoE (Mixture of Experts) heat conduction-based object detection algorithm that strikingly balances accuracy and computational efficiency. Initially, we employ a stem network for event data embedding, followed by processing through our innovative MoE-HCO blocks. Each block integrates various expert modules to mimic heat conduction within event streams. Subsequently, an IoU-based query selection module is utilized for efficient token extraction, which is then channeled into a detection head for the final object detection process. Furthermore, we are pleased to introduce EvDET200K, a novel benchmark dataset for event-based object detection. Captured with a high-definition Prophesee EVK4-HD event camera, this dataset encompasses 10 distinct categories, 200,000 bounding boxes, and 10,054 samples, each spanning 2 to 5 seconds. We also provide comprehensive results from over 15 state-of-the-art detectors, offering a solid foundation for future research and comparison."
status: "auto-generated; brief scan note"
---
## Core Problem

Object detection in event streams has emerged as a cutting-edge research area, demonstrating
superior performance in low-light conditions, scenarios with motion blur, and rapid
movements.

## Core Method

Current detectors leverage spiking neural networks, Transformers, or convolutional neural
networks as their core architectures, each with its own set of limitations including
restricted performance, high computational overhead, or limited local receptive fields.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event。自动分类理由：Manual boundary check: official abstract confirms event-
camera object detection and dataset; SNNs are mentioned as prior detector families, not the
proposed method.。 备注：CVPR 2025 official CVF page inspected under broad high-recall title
workflow.。
