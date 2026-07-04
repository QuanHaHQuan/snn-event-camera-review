---
title: "EF-3DGS: Event-Aided Free-Trajectory 3D Gaussian Splatting"
authors: ["Bohao Liao, Wei Zhai, Zengyu Wan, Zhixin Cheng, Wenfei Yang, Yang Cao, Tianzhu Zhang, Zheng-Jun Zha"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/7cdc4122c4d12cc80a62e6a6af555f5a-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/7cdc4122c4d12cc80a62e6a6af555f5a-Abstract-Conference.html"
tags: []
abstract: "Scene reconstruction from casually captured videos has wide real-world applications. Despite recent progress, existing methods relying on traditional cameras tend to fail in high-speed scenarios due to insufficient observations and inaccurate pose estimation. Event cameras, inspired by biological vision, record pixel-wise intensity changes asynchronously with high temporal resolution and low latency, providing valuable scene and motion information in blind inter-frame intervals. In this paper, we introduce the event cameras to aid scene construction from a casually captured video for the first time, and propose Event-Aided Free-Trajectory 3DGS, called EF-3DGS, which seamlessly integrates the advantages of event cameras into 3DGS through three key components. First, we leverage the Event Generation Model (EGM) to fuse events and frames, enabling continuous supervision between discrete frames. Second, we extract motion information through Contrast Maximization (CMax) of warped events, which calibrates camera poses and provides gradient-domain constraints for 3DGS. Third, to address the absence of color information in events, we combine photometric bundle adjustment (PBA) with a Fixed-GS training strategy that separates structure and color optimization, effectively ensuring color consistency across different views. We evaluate our method on the public Tanks and Temples benchmark and a newly collected real-world dataset, RealEv-DAVIS. Our method achieves up to 3dB higher PSNR and 40% lower Absolute Trajectory Error (ATE) compared to state-of-the-art methods under challenging high-speed scenarios."
status: "auto-generated; brief scan note"
---
## Core Problem

Scene reconstruction from casually captured videos has wide real-world applications.

## Core Method

Despite recent progress, existing methods relying on traditional cameras tend to fail in
high-speed scenarios due to insufficient observations and inaccurate pose estimation.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event cameras; event camera visual-event context; event cameras visual-event
context。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor
evidence; no clear SNN evidence found.。 备注：strict two-stage rescan; official abstract/page
inspected; needs human verification; Track: Main Conference Track。
