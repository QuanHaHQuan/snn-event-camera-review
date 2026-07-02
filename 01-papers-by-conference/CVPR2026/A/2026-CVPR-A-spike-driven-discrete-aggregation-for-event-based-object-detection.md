---
title: "Spike-driven Discrete Aggregation for Event-based Object Detection"
authors: ["Huaning Li", "Ziming Wang", "Runhao Jiang", "Yan Rui", "Huajin Tang"]
conference: "CVPR"
year: 2026
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Spike-driven_Discrete_Aggregation_for_Event-based_Object_Detection_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Li_Spike-driven_Discrete_Aggregation_for_Event-based_Object_Detection_CVPR_2026_paper.html"
tags: []
abstract: "With their high dynamic range and temporal resolution, event cameras are well-suited for object detection, especially under motion blur and extreme illumination. Recent state-of-the-art works for event-based object detection primarily focus on the high-level design of backbones. However, developing effective event representations is equally crucial, as it bridges asynchronous event streams with the dense tensors required by detection networks. Most existing aggregation strategies for event representation continuously accumulate all events within sampled intervals without selective filtering, inevitably introducing uninformative events that degrade detection accuracy. To address this limitation, we introduce a novel perspective, termed Discrete Aggregation, which adaptively and discretely selects informative events for differentiable aggregation. We realize this through the Spiking Discrete Aggregation (SDA) module, which is inspired by the threshold-based spike firing mechanism in Spiking Neural Networks (SNNs) and implemented using gated recurrent spiking neurons. Additionally, we introduce the Multi-Timescale Fusion (MTF) method which leverages coarse-grained temporal features from continuous event streams to further enhance the representation capability of SDA. Experimental results on neuromorphic datasets demonstrate that our method achieves state-of-the-art performance among all fully spiking architectures while using fewer parameters, reaching 43.4% mAP\\textsubscript 50:95 on Gen1 (+ 4.5% over prior art). Moreover, our method exhibits superior robustness under noisy conditions and shows strong compatibility with non-spiking models."
status: "auto-generated; needs human review"
---

## Core Problem

With their high dynamic range and temporal resolution, event cameras are well-suited for object detection, especially under motion blur and extreme illumination.

## Core Method

Recent state-of-the-art works for event-based object detection primarily focus on the high-level design of backbones.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-based object visual-event context; event stream with event-camera context; event-based with event-camera context; spiking neural networks; snns; spiking neurons; spike-driven`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
