---
title: "Spiking Meets Attention: Efficient Remote Sensing Image Super-Resolution with Attention Spiking Neural Networks"
authors: ["Yi Xiao, Qiangqiang Yuan, Kui Jiang, Wenke Huang, Qiang Zhang, Tingting Zheng, Chia-Wen Lin, Liangpei Zhang"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/5e3f2028c5a78fbfb6e1754b7cfb6153-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/5e3f2028c5a78fbfb6e1754b7cfb6153-Abstract-Conference.html"
tags: []
abstract: "Spiking neural networks (SNNs) are emerging as a promising alternative to traditional artificial neural networks (ANNs), offering biological plausibility and energy efficiency. Despite these merits, SNNs are frequently hampered by limited capacity and insufficient representation power, yet remain underexplored in remote sensing image (RSI) super-resolution (SR) tasks. In this paper, we first observe that spiking signals exhibit drastic intensity variations across diverse textures, highlighting an active learning state of the neurons. This observation motivates us to apply SNNs for efficient SR of RSIs. Inspired by the success of attention mechanisms in representing salient information, we devise the spiking attention block (SAB), a concise yet effective component that optimizes membrane potentials through inferred attention weights, which, in turn, regulates spiking activity for superior feature representation. Our key contributions include: 1) we bridge the independent modulation between temporal and channel dimensions, facilitating joint feature correlation learning, and 2) we access the global self-similar patterns in large-scale remote sensing imagery to infer spatial attention weights, incorporating effective priors for realistic and faithful reconstruction. Building upon SAB, we proposed SpikeSR, which achieves state-of-the-art performance across various remote sensing benchmarks such as AID, DOTA, and DIOR, while maintaining high computational efficiency. Code of SpikeSR will be available at https://github.com/XY-boy/SpikeSR."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking neural networks (SNNs) are emerging as a promising alternative to traditional
artificial neural networks (ANNs), offering biological plausibility and energy efficiency.

## Core Method

Despite these merits, SNNs are frequently hampered by limited capacity and insufficient
representation power, yet remain underexplored in remote sensing image (RSI) super-
resolution (SR) tasks.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; snns。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage rescan; official abstract/page inspected; needs human verification; Track: Main
Conference Track。
