---
title: "SFOD: Spiking Fusion Object Detector"
authors: ["Yimeng Fan", "Wei Zhang", "Changsong Liu", "Mingyang Li", "Wenrui Lu"]
conference: "CVPR"
year: 2024
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Fan_SFOD_Spiking_Fusion_Object_Detector_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Fan_SFOD_Spiking_Fusion_Object_Detector_CVPR_2024_paper.html"
tags: []
abstract: "Event cameras characterized by high temporal resolution high dynamic range low power consumption and high pixel bandwidth offer unique capabilities for object detection in specialized contexts. Despite these advantages the inherent sparsity and asynchrony of event data pose challenges to existing object detection algorithms. Spiking Neural Networks (SNNs) inspired by the way the human brain codes and processes information offer a potential solution to these difficulties. However their performance in object detection using event cameras is limited in current implementations. In this paper we propose the Spiking Fusion Object Detector (SFOD) a simple and efficient approach to SNN-based object detection. Specifically we design a Spiking Fusion Module achieving the first-time fusion of feature maps from different scales in SNNs applied to event cameras. Additionally through integrating our analysis and experiments conducted during the pretraining of the backbone network on the NCAR dataset we delve deeply into the impact of spiking decoding strategies and loss functions on model performance. Thereby we establish state-of-the-art classification results based on SNNs achieving 93.7% accuracy on the NCAR dataset. Experimental results on the GEN1 detection dataset demonstrate that the SFOD achieves a state-of-the-art mAP of 32.1% outperforming existing SNN-based approaches. Our research not only underscores the potential of SNNs in object detection with event cameras but also propels the advancement of SNNs. Code is available at https://github.com/yimeng-fan/SFOD."
status: "auto-generated; needs human review"
---
## Core Problem

Event cameras characterized by high temporal resolution high dynamic range low power
consumption and high pixel bandwidth offer unique capabilities for object detection in
specialized contexts.

## Core Method

Despite these advantages the inherent sparsity and asynchrony of event data pose challenges
to existing object detection algorithms.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：spiking。自动分类理由：Official abstract/page strictly confirms both event-
camera/DVS/visual-event-stream evidence and SNN/spiking neural computation.。 备注：CVPR 2024
official CVF page inspected under broad high-recall title workflow.。
该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

Spiking Neural Networks (SNNs) inspired by the way the human brain codes and processes
information offer a potential solution to these difficulties. However their performance in
object detection using event cameras is limited in current implementations. In this paper we
propose the Spiking Fusion Object Detector (SFOD) a simple and efficient approach to SNN-
based object detection. Specifically we design a Spiking Fusion Module achieving the first-
time fusion of feature maps from different scales in SNNs applied to event cameras.
Additionally through integrating our analysis and experiments conducted during the
pretraining of the backbone network on the NCAR dataset we delve deeply into the impact of
spiking decoding strategies and loss functions on model performance. Thereby we establish
state-of-the-art classification results based on SNNs achieving 93.7% accuracy on the NCAR
dataset. Experimental results on the GEN1 detection dataset demonstrate that the SFOD
achieves a state-of-the-art mAP of 32.1% outperforming existing SNN-based approaches. Our
research not only underscores the potential of SNNs in object detection with event cameras
but also propels the advancement of SNNs. Code is available at https://github.com/yimeng-
fan/SFOD.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
