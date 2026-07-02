---
title: "From Events to Clarity: The Event-Guided Diffusion Framework for Dehazing"
authors: ["Ling Wang", "Yunfan Lu", "Wenzong Ma", "Huizai Yao", "Pengteng Li", "Hui Xiong"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_From_Events_to_Clarity_The_Event-Guided_Diffusion_Framework_for_Dehazing_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Wang_From_Events_to_Clarity_The_Event-Guided_Diffusion_Framework_for_Dehazing_CVPR_2026_paper.html"
tags: []
abstract: "Clear imaging under hazy conditions is a critical task. Prior-based and neural methods have improved results. However, they operate on RGB frames, which suffer from limited dynamic range. Therefore, dehazing remains ill- posed and can erase structure and illumination details. To address this, we use event cameras for dehazing for the first time. Event cameras offer much higher HDR (120dB vs. 60dB) and microsecond latency, therefore they suit hazy scenes. In practice, transferring HDR cues from events to frames is hard because real paired data are scarce. To tackle this, we propose an event-guided diffusion model that utilizes the strong generative priors of diffusion mod- els to reconstruct clear images from hazy inputs by effec- tively transferring HDR information from events. Specifi- cally, we design an event-guided module that maps sparse HDR event features, e.g., edges, corners, into the diffusion latent space. This clear conditioning provides precise struc- tural guidance during generation, improves visual realism, and reduces semantic drift. For real-world evaluation, we collect a drone dataset in heavy haze (AQI = 341) with synchronized RGB and event sensors. Experiments on two benchmarks and our dataset achieve state-of-the-art results."
status: "auto-generated; brief scan note"
---
## Core Problem

Clear imaging under hazy conditions is a critical task.

## Core Method

Prior-based and neural methods have improved results.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
