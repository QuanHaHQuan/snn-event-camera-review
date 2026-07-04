---
title: "Efficient Event-Based Object Detection: A Hybrid Neural Network with Spatial and Temporal Attention"
authors: ["Soikat Hasan Ahmed", "Jan Finkbeiner", "Emre Neftci"]
conference: "CVPR"
year: 2025
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Ahmed_Efficient_Event-Based_Object_Detection_A_Hybrid_Neural_Network_with_Spatial_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Ahmed_Efficient_Event-Based_Object_Detection_A_Hybrid_Neural_Network_with_Spatial_CVPR_2025_paper.html"
tags: []
abstract: "Event cameras offer high temporal resolution and dynamic range with minimal motion blur, making them promising for robust object detection. While Spiking Neural Networks (SNNs) on neuromorphic hardware are often considered for energy efficient and low latency event-based data processing, they often fall short of Artificial Neural Networks (ANNs) in accuracy and flexibility. Here, we introduce Attention-based Hybrid SNN-ANN backbones for event-based object detection to leverage the strengths of both SNN and ANN architectures. A novel Attention-based SNN-ANN bridge module proposed to captures sparse spatial and temporal relations from the SNN layer and converts them into dense feature maps for the ANN part of the backbone. Additionally, we present a variant that integrates DWConvLSTMs to the ANN blocks to capture slower dynamics. This multi-timescale network combines fast SNN processing for short timesteps with long-term dense RNN processing, effectively capturing both fast and slow dynamics.Experimental results demonstrate that our proposed method surpasses SNN-based approaches by significant margins, with results comparable to existing ANN and RNN-based methods. Unlike ANN-only networks, the hybrid setup allow us to implement the SNN blocks on digital neuromorphic hardware to investigate the feasibility of our approach.Extensive ablation studies and implementation on neuromorphic hardware confirm the effectiveness of our proposed modules and architectural choices.Our hybrid SNN-ANN architectures pave the way for ANN-like performance at a drastically reduced parameter, latency, and power budget."
status: "auto-generated; needs human review"
---
## Core Problem

Event cameras offer high temporal resolution and dynamic range with minimal motion blur,
making them promising for robust object detection.

## Core Method

While Spiking Neural Networks (SNNs) on neuromorphic hardware are often considered for
energy efficient and low latency event-based data processing, they often fall short of
Artificial Neural Networks (ANNs) in accuracy and flexibility.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms both event-
camera/DVS/visual-event-stream evidence and SNN/spiking neural computation.。 备注：CVPR 2025
official CVF page inspected under broad high-recall title workflow.。
该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

Here, we introduce Attention-based Hybrid SNN-ANN backbones for event-based object detection
to leverage the strengths of both SNN and ANN architectures. A novel Attention-based SNN-ANN
bridge module proposed to captures sparse spatial and temporal relations from the SNN layer
and converts them into dense feature maps for the ANN part of the backbone. Additionally, we
present a variant that integrates DWConvLSTMs to the ANN blocks to capture slower dynamics.
This multi-timescale network combines fast SNN processing for short timesteps with long-term
dense RNN processing, effectively capturing both fast and slow dynamics.Experimental results
demonstrate that our proposed method surpasses SNN-based approaches by significant margins,
with results comparable to existing ANN and RNN-based methods. Unlike ANN-only networks, the
hybrid setup allow us to implement the SNN blocks on digital neuromorphic hardware to
investigate the feasibility of our approach.Extensive ablation studies and implementation on
neuromorphic hardware confirm the effectiveness of our proposed modules and architectural
choices.Our hybrid SNN-ANN architectures pave the way for ANN-like performance at a
drastically reduced parameter, latency, and power budget.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
