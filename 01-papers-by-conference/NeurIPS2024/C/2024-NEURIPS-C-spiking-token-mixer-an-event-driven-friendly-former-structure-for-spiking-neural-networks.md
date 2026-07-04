---
title: "Spiking Token Mixer: An event-driven friendly Former structure for spiking neural networks"
authors: ["Shikuang Deng, Yuhang Wu, Kangrui Du, Shi Gu"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/e8c20cafe841cba3e31a17488dc9c3f1-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/e8c20cafe841cba3e31a17488dc9c3f1-Abstract-Conference.html"
tags: []
abstract: "Spiking neural networks (SNNs), inspired by biological processes, use spike signals for inter-layer communication, presenting an energy-efficient alternative to traditional neural networks. To realize the theoretical advantages of SNNs in energy efficiency, it is essential to deploy them onto neuromorphic chips. On clock-driven synchronous chips, employing shorter time steps can enhance energy efficiency but reduce SNN performance. Compared to the clock-driven synchronous chip, the event-driven asynchronous chip achieves much lower energy consumption but only supports some specific network operations. Recently, a series of SNN projects have achieved tremendous success, significantly improving the SNN's performance. However, event-driven asynchronous chips do not support some of the proposed structures, making it impossible to integrate these SNNs into asynchronous hardware. In response to these problems, we propose the Spiking Token Mixer (STMixer) architecture, which consists exclusively of operations supported by asynchronous scenarios, including convolutional, fully connected layers and residual paths. Our series of experiments also demonstrates that STMixer achieves performance on par with spiking transformers in synchronous scenarios with very low timesteps. This indicates its ability to achieve the same level of performance with lower power consumption in synchronous scenarios. The codes are available at \\url{https://github.com/brain-intelligence-lab/STMixer_demo}."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking neural networks (SNNs), inspired by biological processes, use spike signals for
inter-layer communication, presenting an energy-efficient alternative to traditional neural
networks.

## Core Method

To realize the theoretical advantages of SNNs in energy efficiency, it is essential to
deploy them onto neuromorphic chips.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; event; event-driven; spiking。自动分类理由：Official abstract/page
strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。
备注：strict two-stage rescan; official abstract/page inspected; Track: Main Conference Track;
needs human verification.。
