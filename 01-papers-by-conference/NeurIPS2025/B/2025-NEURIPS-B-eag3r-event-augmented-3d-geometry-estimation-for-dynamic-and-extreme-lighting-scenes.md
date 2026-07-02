---
title: "EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes"
authors: ["Xiaoshan Wu, Yifei Yu, Xiaoyang Lyu, Yihua Huang, Bo Wang, Baoheng Zhang, Zhongrui Wang, Xiaojuan Qi"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/6a0480190bbe6b622c7f1d3aa9be9c0f-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/6a0480190bbe6b622c7f1d3aa9be9c0f-Abstract-Conference.html"
tags: []
abstract: "Robust 3D geometry estimation from videos is critical for applications such as autonomous navigation, SLAM, and 3D scene reconstruction. Recent methods like DUSt3R demonstrate that regressing dense pointmaps from image pairs enables accurate and efficient pose-free reconstruction. However, existing RGB-only approaches struggle under real-world conditions involving dynamic objects and extreme illumination, due to the inherent limitations of conventional cameras. In this paper, we propose \\textbf{EAG3R}, a novel geometry estimation framework that augments pointmap-based reconstruction with asynchronous event streams. Built upon the MonST3R backbone, EAG3R introduces two key innovations: (1) a retinex-inspired image enhancement module and a lightweight event adapter with SNR-aware fusion mechanism that adaptively combines RGB and event features based on local reliability; and (2) a novel event-based photometric consistency loss that reinforces spatiotemporal coherence during global optimization. Our method enables robust geometry estimation in challenging dynamic low-light scenes without requiring retraining on night-time data. Extensive experiments demonstrate that EAG3R significantly outperforms state-of-the-art RGB-only baselines across monocular depth estimation, camera pose tracking, and dynamic reconstruction tasks."
status: "auto-generated; brief scan note"
---
## Core Problem

Robust 3D geometry estimation from videos is critical for applications such as autonomous
navigation, SLAM, and 3D scene reconstruction.

## Core Method

Recent methods like DUSt3R demonstrate that regressing dense pointmaps from image pairs
enables accurate and efficient pose-free reconstruction.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event-camera/DVS/visual event stream evidence。自动分类理由：Official abstract/page confirms
event-camera/DVS/visual-event-stream data; no clear SNN evidence.。 备注：Track: Main Conference
Track. Official abstract/page inspected under broad high-recall title workflow.。
