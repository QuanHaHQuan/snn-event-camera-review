---
title: "Event-3DGS: Event-based 3D Reconstruction Using 3D Gaussian Splatting"
authors: ["Haiqian Han, Jianing Li, Henglu Wei, Xiangyang Ji"]
conference: "NeurIPS"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/e73ad1f690542144ce354637bb913c35-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/e73ad1f690542144ce354637bb913c35-Abstract-Conference.html"
tags: []
abstract: "Event cameras, offering high temporal resolution and high dynamic range, have brought a new perspective to addressing 3D reconstruction challenges in fast-motion and low-light scenarios. Most methods use the Neural Radiance Field (NeRF) for event-based photorealistic 3D reconstruction. However, these NeRF methods suffer from time-consuming training and inference, as well as limited scene-editing capabilities of implicit representations. To address these problems, we propose Event-3DGS, the first event-based reconstruction using 3D Gaussian splatting (3DGS) for synthesizing novel views freely from event streams. Technically, we first propose an event-based 3DGS framework that directly processes event data and reconstructs 3D scenes by simultaneously optimizing scenario and sensor parameters. Then, we present a high-pass filter-based photovoltage estimation module, which effectively reduces noise in event data to improve the robustness of our method in real-world scenarios. Finally, we design an event-based 3D reconstruction loss to optimize the parameters of our method for better reconstruction quality. The results show that our method outperforms state-of-the-art methods in terms of reconstruction quality on both simulated and real-world datasets. We also verify that our method can perform robust 3D reconstruction even in real-world scenarios with extreme noise, fast motion, and low-light conditions. Our code is available in https://github.com/lanpokn/Event-3DGS."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras, offering high temporal resolution and high dynamic range, have brought a new
perspective to addressing 3D reconstruction challenges in fast-motion and low-light
scenarios.

## Core Method

Most methods use the Neural Radiance Field (NeRF) for event-based photorealistic 3D
reconstruction.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：strict two-stage
rescan; official abstract/page inspected; Track: Main Conference Track; needs human
verification.。
