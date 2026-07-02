---
title: "A Chaotic Dynamics Framework Inspired by Dorsal Stream for Event Signal Processing"
authors: ["Yu Chen", "Jing Lian", "Zhaofei Yu", "Jizhao Liu", "Jisheng Dang", "Gang Wang"]
conference: "ICML"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25am/chen25am.pdf"
official_page: "https://proceedings.mlr.press/v267/chen25am.html"
tags: []
abstract: "Event cameras are bio-inspired vision sensors that encode visual information with high dynamic range, high temporal resolution, and low latency. Current state-of-the-art event stream processing methods rely on end-to-end deep learning techniques. However, these models are heavily dependent on data structures, limiting their stability and generalization capabilities across tasks, thereby hindering their deployment in real-world scenarios. To address this issue, we propose a chaotic dynamics event signal processing framework inspired by the dorsal visual pathway of the brain. Specifically, we utilize Continuous-coupled Neural Network (CCNN) to encode the event stream. CCNN encodes polarity-invariant event sequences as periodic signals and polarity-changing event sequences as chaotic signals. We then use continuous wavelet transforms to analyze the dynamical states of CCNN neurons and establish the high-order mappings of the event stream. The effectiveness of our method is validated through integration with conventional classification networks, achieving state-of-the-art classification accuracy on the N-Caltech101 and N-CARS datasets, with results of 84.3% and 99.9%, respectively. Our method improves the accuracy of event camera-based object classification while significantly enhancing the generalization and stability of event representation."
status: "auto-generated; brief scan note"
---

## Core Problem

Event cameras are bio-inspired vision sensors that encode visual information with high dynamic range, high temporal resolution, and low latency.

## Core Method

Current state-of-the-art event stream processing methods rely on end-to-end deep learning techniques.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Official abstract/page confirms event-camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
