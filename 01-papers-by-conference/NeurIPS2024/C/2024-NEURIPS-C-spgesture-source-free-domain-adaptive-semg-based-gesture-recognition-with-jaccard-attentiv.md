---
title: "SpGesture: Source-Free Domain-adaptive sEMG-based Gesture Recognition with Jaccard Attentive Spiking Neural Network"
authors: ["Weiyu Guo, Ying Sun, Yijie Xu, Ziyue Qiao, Yongkui Yang, Hui Xiong"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/409334f42cbb57d07aa152f2d0433ec7-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/409334f42cbb57d07aa152f2d0433ec7-Abstract-Conference.html"
tags: []
abstract: "Surface electromyography (sEMG) based gesture recognition offers a natural and intuitive interaction modality for wearable devices. Despite significant advancements in sEMG-based gesture recognition models, existing methods often suffer from high computational latency and increased energy consumption. Additionally, the inherent instability of sEMG signals, combined with their sensitivity to distribution shifts in real-world settings, compromises model robustness. To tackle these challenges, we propose a novel SpGesture framework based on Spiking Neural Networks, which possesses several unique merits compared with existing methods: (1) Robustness: By utilizing membrane potential as a memory list, we pioneer the introduction of Source-Free Domain Adaptation into SNN for the first time. This enables SpGesture to mitigate the accuracy degradation caused by distribution shifts. (2) High Accuracy: With a novel Spiking Jaccard Attention, SpGesture enhances the SNNs' ability to represent sEMG features, leading to a notable rise in system accuracy. To validate SpGesture's performance, we collected a new sEMG gesture dataset which has different forearm postures, where SpGesture achieved the highest accuracy among the baselines ($89.26\\%$). Moreover, the actual deployment on the CPU demonstrated a latency below 100ms, well within real-time requirements. This impressive performance showcases SpGesture's potential to enhance the applicability of sEMG in real-world scenarios. The code is available at https://github.com/guoweiyu/SpGesture/."
status: "auto-generated; brief scan note"
---
## Core Problem

Surface electromyography (sEMG) based gesture recognition offers a natural and intuitive
interaction modality for wearable devices.

## Core Method

Despite significant advancements in sEMG-based gesture recognition models, existing methods
often suffer from high computational latency and increased energy consumption.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural network; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage rescan; official abstract/page inspected; Track: Main Conference Track; needs human
verification.。
