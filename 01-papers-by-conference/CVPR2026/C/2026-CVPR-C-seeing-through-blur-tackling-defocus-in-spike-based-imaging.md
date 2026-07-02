---
title: "Seeing Through Blur: Tackling Defocus in Spike-Based Imaging"
authors: ["Xiantao Ma", "Siwei Dong", "Lin Zhu", "Lizhi Wang", "Hua Huang"]
conference: "CVPR"
year: 2026
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_Seeing_Through_Blur_Tackling_Defocus_in_Spike-Based_Imaging_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Ma_Seeing_Through_Blur_Tackling_Defocus_in_Spike-Based_Imaging_CVPR_2026_paper.html"
tags: []
abstract: "Spike cameras are a novel class of neuromorphic vision sensors that capture scene dynamics with ultra-high temporal resolution via spike planes. While recent methods have addressed motion blur and noise in spike-based reconstruction, defocus blur caused by shallow depth of field or lens adjustment delays remains a critical yet underexplored issue in real-world applications such as autonomous driving. In this work, we present DeSpike, the first end-to-end defocus removal framework specifically designed for spike cameras. Our method begins by explicitly modeling the defocus formation process using a physics-inspired thin-lens approximation to simulate spike responses under optical blur. Guided by this formulation, DeSpike employs multi-temporal-scale integrate-and-fire (IF) neurons to compensate for FPN and extract defocus-aware features from spike streams. These features are then processed by a physics-informed deblurring module constructed from learnable discrete PSF priors. To address spatially variant blur, we introduce a Transformer-based fusion mechanism that adaptively weighs multi-scale deblurring results through attention across defocus levels. Finally, a coarse-to-fine iterative refinement stage combines spike features and PSF priors for progressive restoration. Extensive experiments on both synthetic and real-world defocused spike datasets demonstrate that our method achieves superior performance over state-of-the-art deblurring approaches in terms of structural fidelity, perceptual sharpness, and contrast, setting a new benchmark for defocus-aware spike-based image reconstruction."
status: "auto-generated; brief scan note"
---

## Core Problem

Spike cameras are a novel class of neuromorphic vision sensors that capture scene dynamics with ultra-high temporal resolution via spike planes.

## Core Method

While recent methods have addressed motion blur and noise in spike-based reconstruction, defocus blur caused by shallow depth of field or lens adjustment delays remains a critical yet underexplored issue in real-world applications such as autonomous driving.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `integrate-and-fire`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
