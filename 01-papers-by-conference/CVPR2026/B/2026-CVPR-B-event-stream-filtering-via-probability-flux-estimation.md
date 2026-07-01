---
title: "Event Stream Filtering via Probability Flux Estimation"
authors: ["Jinze Chen", "Wei Zhai", "Yang Cao", "Bin Li", "Zheng-Jun Zha"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Event_Stream_Filtering_via_Probability_Flux_Estimation_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Event_Stream_Filtering_via_Probability_Flux_Estimation_CVPR_2026_paper.html"
tags: []
abstract: "Event cameras asynchronously capture brightness changes with microsecond latency, offering exceptional temporal precision but suffering from severe noise and signal inconsistencies. Unlike conventional signals, events carry state information through polarities and process information through inter-event time intervals. However, existing event filters often ignore the latter, producing outputs that are sparser than the raw input and limiting the reconstruction of continuous irradiance dynamics. We propose the Event Density Flow Filter (EDFilter), a framework that models event generation as threshold-crossing probability fluxes arising from the stochastic diffusion of irradiance trajectories. EDFilter performs nonparametric, kernel-based estimation of probability flux and reconstructs the continuous event density flow using an O(1) recursive solver, enabling real-time processing. The Rotary Event Dataset (RED), featuring microsecond-resolution ground-truth irradiance flow under controlled illumination is also presented for event quality evaluation. Experiments demonstrate that EDFilter achieves high-fidelity, physically interpretable event denoising and motion reconstruction."
status: "auto-generated; brief scan note"
---

## Core Problem

事件相机滤波需要在去噪与保留连续亮度动态之间取得平衡。

## Core Method

将事件生成建模为概率通量过程，提出 Event Density Flow Filter 来解释和过滤事件流。

## Key Metrics and Findings

摘要强调现有滤波器忽略了事件间时间间隔，容易让输出过稀。

## Personal Notes

属于事件流建模与滤波方向的背景论文。

