---
title: "EvGGS: A Collaborative Learning Framework for Event-based Generalizable Gaussian Splatting"
authors: ["Jiaxu Wang, Junhao He, Ziyi Zhang, Mingyuan Sun, Jingkai Sun, Renjing Xu"]
conference: "ICML"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24w/wang24w.pdf"
official_page: "https://proceedings.mlr.press/v235/wang24w.html"
tags: []
abstract: "Event cameras offer promising advantages such as high dynamic range and low latency, making them well-suited for challenging lighting conditions and fast-moving scenarios. However, reconstructing 3D scenes from raw event streams is difficult because event data is sparse and does not carry absolute color information. To release its potential in 3D reconstruction, we propose the first event-based generalizable 3D reconstruction framework, which reconstructs scenes as 3D Gaussians from only event input in a feedforward manner and can generalize to unseen cases without any retraining. This framework includes a depth estimation module, an intensity reconstruction module, and a Gaussian regression module. These submodules connect in a cascading manner, and we collaboratively train them with a designed joint loss to make them mutually promote. To facilitate related studies, we build a novel event-based 3D dataset with various material objects and calibrated labels of greyscale images, depth maps, camera poses, and silhouettes. Experiments show models that have jointly trained significantly outperform those trained individually. Our approach performs better than all baselines in reconstruction quality, and depth/intensity predictions with satisfactory rendering speed."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras offer promising advantages such as high dynamic range and low latency, making
them well-suited for challenging lighting conditions and fast-moving scenarios.

## Core Method

However, reconstructing 3D scenes from raw event streams is difficult because event data is
sparse and does not carry absolute color information.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：strict two-stage
screening; official abstract/page inspected; main conference; needs human verification。
