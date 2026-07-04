---
title: "DERD-Net: Learning Depth from Event-based Ray Densities"
authors: ["Diego de Oliveira Hitzges, Suman Ghosh, Guillermo Gallego"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/019ef89617d539b15ed610ce8d1b76e1-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/019ef89617d539b15ed610ce8d1b76e1-Abstract-Conference.html"
tags: []
abstract: "Event cameras offer a promising avenue for multi-view stereo depth estimation and Simultaneous Localization And Mapping (SLAM) due to their ability to detect blur-free 3D edges at high-speed and over broad illumination conditions. However, traditional deep learning frameworks designed for conventional cameras struggle with the asynchronous, stream-like nature of event data, as their architectures are optimized for discrete, image-like inputs. We propose a scalable, flexible and adaptable framework for pixel-wise depth estimation with event cameras in both monocular and stereo setups. The 3D scene structure is encoded into disparity space images (DSIs), representing spatial densities of rays obtained by back-projecting events into space via known camera poses. Our neural network processes local subregions of the DSIs combining 3D convolutions and a recurrent structure to recognize valuable patterns for depth prediction. Local processing enables fast inference with full parallelization and ensures constant ultra-low model complexity and memory costs, regardless of camera resolution. Experiments on standard benchmarks (MVSEC and DSEC datasets) demonstrate unprecedented effectiveness: (i) using purely monocular data, our method achieves comparable results to existing stereo methods; (ii) when applied to stereo data, it strongly outperforms all state-of-the-art (SOTA) approaches, reducing the mean absolute error by at least 42\\%; (iii) our method also allows for increases in depth completeness by more than 3-fold while still yielding a reduction in median absolute error of at least 30\\%. Given its remarkable performance and effective processing of event-data, our framework holds strong potential to become a standard approach for using deep learning for event-based depth estimation and SLAM."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras offer a promising avenue for multi-view stereo depth estimation and
Simultaneous Localization And Mapping (SLAM) due to their ability to detect blur-free 3D
edges at high-speed and over broad illumination conditions.

## Core Method

However, traditional deep learning frameworks designed for conventional cameras struggle
with the asynchronous, stream-like nature of event data, as their architectures are
optimized for discrete, image-like inputs.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event cameras; event camera visual-event context; event cameras visual-event
context; event-based with event-camera context。自动分类理由：Official abstract/page strictly
confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.。
备注：strict two-stage rescan; official abstract/page inspected; needs human verification;
Track: Main Conference Track。
