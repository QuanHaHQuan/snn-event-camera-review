---
title: "SpikeTrack: A Spike-driven Framework for Efficient Visual Tracking"
authors: ["Qiuyang Zhang", "Jiujun Cheng", "Qichao Mao", "Cong Liu", "Yu Fang", "Yuhong Li", "Mengying Ge", "Shangce Gao"]
conference: "CVPR"
year: 2026
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpikeTrack_A_Spike-driven_Framework_for_Efficient_Visual_Tracking_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SpikeTrack_A_Spike-driven_Framework_for_Efficient_Visual_Tracking_CVPR_2026_paper.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) promise energy-efficient vision, but applying them to RGB visual tracking remains difficult: Existing SNN tracking frameworks either do not fully align with spike-driven computation or do not fully leverage neurons' spatiotemporal dynamics, leading to a trade-off between efficiency and accuracy. To address this, we introduce SpikeTrack, a spike-driven framework for energy-efficient RGB object tracking. SpikeTrack employs a novel asymmetric design that uses asymmetric timestep expansion and unidirectional information flow, harnessing spatiotemporal dynamics while cutting computation. To ensure effective unidirectional information transfer between branches, we design a memory-retrieval module inspired by neural inference mechanisms. This module recurrently queries a compact memory initialized by the template to retrieve target cues and sharpen target perception over time. Extensive experiments demonstrate that SpikeTrack achieves the state-of-the-art among SNN-based trackers and remains competitive with advanced ANN trackers. Notably, it surpasses TransT on LaSOT dataset while consuming only 1/26 of its energy. To our knowledge, SpikeTrack is the first spike-driven framework to make RGB tracking both accurate and energy efficient."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs) promise energy-efficient vision, but applying them to RGB
visual tracking remains difficult: Existing SNN tracking frameworks either do not fully
align with spike-driven computation or do not fully leverage neurons' spatiotemporal
dynamics, leading to a trade-off between efficiency and accuracy.

## Core Method

To address this, we introduce SpikeTrack, a spike-driven framework for energy-efficient RGB
object tracking.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural network; spike-driven。自动分类理由：Official abstract/page confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence.。
