---
title: "Spiking Neural Network as Adaptive Event Stream Slicer"
authors: ["Jiahang Cao, Mingyuan Sun, Ziqing Wang, Hao Cheng, Qiang Zhang, Shibo Zhou, Renjing Xu"]
conference: "NeurIPS"
year: 2024
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/893a5db6100028ec814cfd99fe92c31b-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/893a5db6100028ec814cfd99fe92c31b-Abstract-Conference.html"
tags: []
abstract: "Event-based cameras are attracting significant interest as they provide rich edge information, high dynamic range, and high temporal resolution. Many state-of-the-art event-based algorithms rely on splitting the events into fixed groups, resulting in the omission of crucial temporal information, particularly when dealing with diverse motion scenarios (e.g., high/low speed). In this work, we propose SpikeSlicer, a novel-designed event processing framework capable of splitting events stream adaptively. SpikeSlicer utilizes a low-energy spiking neural network (SNN) to trigger event slicing. To guide the SNN to fire spikes at optimal time steps, we propose the Spiking Position-aware Loss (SPA-Loss) to modulate the neuron's state. Additionally, we develop a Feedback-Update training strategy that refines the slicing decisions using feedback from the downstream artificial neural network (ANN). Extensive experiments demonstrate that our method yields significant performance improvements in event-based object tracking and recognition. Notably, SpikeSlicer provides a brand-new SNN-ANN cooperation paradigm, where the SNN acts as an efficient, low-energy data processor to assist the ANN in improving downstream performance, injecting new perspectives and potential avenues of exploration."
status: "auto-generated; needs human review"
---
## Core Problem

Event-based cameras are attracting significant interest as they provide rich edge
information, high dynamic range, and high temporal resolution.

## Core Method

Many state-of-the-art event-based algorithms rely on splitting the events into fixed groups,
resulting in the omission of crucial temporal information, particularly when dealing with
diverse motion scenarios (e.g., high/low speed).

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：event stream; spiking neural network; event; spiking。自动分类理由：Official abstract/page
strictly confirms both event-camera/DVS/visual-event-stream evidence and SNN/spiking neural
computation.。 备注：strict two-stage rescan; official abstract/page inspected; Track: Main
Conference Track; needs human verification.。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

In this work, we propose SpikeSlicer, a novel-designed event processing framework capable of
splitting events stream adaptively. SpikeSlicer utilizes a low-energy spiking neural network
(SNN) to trigger event slicing. To guide the SNN to fire spikes at optimal time steps, we
propose the Spiking Position-aware Loss (SPA-Loss) to modulate the neuron's state.
Additionally, we develop a Feedback-Update training strategy that refines the slicing
decisions using feedback from the downstream artificial neural network (ANN). Extensive
experiments demonstrate that our method yields significant performance improvements in
event-based object tracking and recognition. Notably, SpikeSlicer provides a brand-new SNN-
ANN cooperation paradigm, where the SNN acts as an efficient, low-energy data processor to
assist the ANN in improving downstream performance, injecting new perspectives and potential
avenues of exploration.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
