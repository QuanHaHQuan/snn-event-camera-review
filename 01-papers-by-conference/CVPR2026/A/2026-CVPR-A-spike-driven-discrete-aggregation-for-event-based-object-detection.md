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

With their high dynamic range and temporal resolution, event cameras are well-suited for
object detection, especially under motion blur and extreme illumination.

## Core Method

Recent state-of-the-art works for event-based object detection primarily focus on the high-
level design of backbones.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：event camera; event stream; spiking neural network; spiking neuron; spike-
driven。自动分类理由：Official abstract/page confirms both event-camera/DVS/event-stream evidence
and SNN/spiking neural computation.。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

However, developing effective event representations is equally crucial, as it bridges
asynchronous event streams with the dense tensors required by detection networks. Most
existing aggregation strategies for event representation continuously accumulate all events
within sampled intervals without selective filtering, inevitably introducing uninformative
events that degrade detection accuracy. To address this limitation, we introduce a novel
perspective, termed Discrete Aggregation, which adaptively and discretely selects
informative events for differentiable aggregation. We realize this through the Spiking
Discrete Aggregation (SDA) module, which is inspired by the threshold-based spike firing
mechanism in Spiking Neural Networks (SNNs) and implemented using gated recurrent spiking
neurons. Additionally, we introduce the Multi-Timescale Fusion (MTF) method which leverages
coarse-grained temporal features from continuous event streams to further enhance the
representation capability of SDA. Experimental results on neuromorphic datasets demonstrate
that our method achieves state-of-the-art performance among all fully spiking architectures
while using fewer parameters, reaching 43.4% mAP\textsubscript 50:95 on Gen1 (+ 4.5% over
prior art). Moreover, our method exhibits superior robustness under noisy conditions and
shows strong compatibility with non-spiking models.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
