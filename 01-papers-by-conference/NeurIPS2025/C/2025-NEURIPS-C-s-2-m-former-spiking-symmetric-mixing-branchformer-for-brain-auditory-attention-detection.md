---
title: "S$^2$M-Former: Spiking Symmetric Mixing Branchformer for Brain Auditory Attention Detection"
authors: ["Jiaqi Wang, Zhengyu Ma, Xiongri Shen, Chenlin Zhou, Leilei Zhao, Han Zhang, Yi Zhong, Siqi Cai, Zhenxi Song, Zhiguo Zhang"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/b8330f5b70b3c53172417deac6f057b1-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/b8330f5b70b3c53172417deac6f057b1-Abstract-Conference.html"
tags: []
abstract: "Auditory attention detection (AAD) aims to decode listeners' focus in complex auditory environments from electroencephalography (EEG) recordings, which is crucial for developing neuro-steered hearing devices. Despite recent advancements, EEG-based AAD remains hindered by the absence of synergistic frameworks that can fully leverage complementary EEG features under energy-efficiency constraints. We propose ***S$^2$M-Former***, a novel ***s***piking ***s***ymmetric ***m***ixing framework to address this limitation through two key innovations: i) Presenting a spike-driven symmetric architecture composed of parallel spatial and frequency branches with mirrored modular design, leveraging biologically plausible token-channel mixers to enhance complementary learning across branches; ii) Introducing lightweight 1D token sequences to replace conventional 3D operations, reducing parameters by 14.7$\\times$. The brain-inspired spiking architecture further reduces power consumption, achieving a 5.8$\\times$ energy reduction compared to recent ANN methods, while also surpassing existing SNN baselines in terms of parameter efficiency and performance. Comprehensive experiments on three AAD benchmarks (KUL, DTU and AV-GC-AAD) across three settings (within-trial, cross-trial and cross-subject) demonstrate that S$^2$M-Former achieves comparable state-of-the-art (SOTA) decoding accuracy, making it a promising low-power, high-performance solution for AAD tasks. Code is available at https://github.com/JackieWang9811/S2M-Former."
status: "auto-generated; brief scan note"
---
## Core Problem

Auditory attention detection (AAD) aims to decode listeners' focus in complex auditory
environments from electroencephalography (EEG) recordings, which is crucial for developing
neuro-steered hearing devices.

## Core Method

Despite recent advancements, EEG-based AAD remains hindered by the absence of synergistic
frameworks that can fully leverage complementary EEG features under energy-efficiency
constraints.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：snns; spike-driven。自动分类理由：Official abstract/page strictly confirms SNN/spiking
neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-stage rescan;
official abstract/page inspected; needs human verification; Track: Main Conference Track。
