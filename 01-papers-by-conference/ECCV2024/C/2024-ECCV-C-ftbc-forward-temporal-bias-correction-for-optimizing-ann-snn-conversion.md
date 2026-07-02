---
title: "FTBC: Forward Temporal Bias Correction for Optimizing ANN-SNN Conversion"
authors: ["Xiaofeng Wu", "Velibor Bojkovic", "Bin Gu", "Kun Suo", "Kai Zou"]
conference: "ECCV"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08702.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/437"
tags: []
abstract: "Spiking Neural Networks (SNNs) offer a promising avenue for energy-efficient computing compared with Artificial Neural Networks (ANNs), closely mirroring biological neural processes. However, this potential comes with inherent challenges in directly training SNNs through spatio-temporal backpropagation --- stemming from the temporal dynamics of spiking neurons and their discrete signal processing --- which necessitates alternative ways of training, most notably through ANN-SNN conversion. In this work, we introduce a lightweight Forward Temporal Bias Correction (FTBC) technique, aimed at enhancing conversion accuracy without the computational overhead. We ground our method on provided theoretical findings that through proper temporal bias calibration the expected error of ANN-SNN conversion can be reduced to be zero after each time step. We further propose a heuristic algorithm for finding the temporal bias only in the forward pass, thus eliminating the computational burden of backpropagation and we evaluate our method on CIFAR-10/100 and ImageNet datasets, achieving a notable increase in accuracy on all datasets. Codes are released at a GitHub repository."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking Neural Networks (SNNs) offer a promising avenue for energy-efficient computing compared with Artificial Neural Networks (ANNs), closely mirroring biological neural processes.

## Core Method

However, this potential comes with inherent challenges in directly training SNNs through spatio-temporal backpropagation --- stemming from the temporal dynamics of spiking neurons and their discrete signal processing --- which necessitates alternative ways of training, most notably through ANN-SNN conversion.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns; spiking neurons`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
