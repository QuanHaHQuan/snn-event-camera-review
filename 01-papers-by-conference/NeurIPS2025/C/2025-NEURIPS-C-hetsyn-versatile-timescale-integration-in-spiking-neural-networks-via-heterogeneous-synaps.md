---
title: "HetSyn: Versatile Timescale Integration in Spiking Neural Networks via Heterogeneous Synapses"
authors: ["Zhichao Deng, Zhikun Liu, Junxue Wang, Shengqian Chen, Xiang Wei, Qiang Yu"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/3a4e2c6a07ede771fbe53201d31df1e9-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/3a4e2c6a07ede771fbe53201d31df1e9-Abstract-Conference.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) offer a biologically plausible and energy-efficient framework for temporal information processing. However, existing studies overlook a fundamental property widely observed in biological neurons—synaptic heterogeneity, which plays a crucial role in temporal processing and cognitive capabilities. To bridge this gap, we introduce HetSyn, a generalized framework that models synaptic heterogeneity with synapse-specific time constants. This design shifts temporal integration from the membrane potential to the synaptic current, enabling versatile timescale integration and allowing the model to capture diverse synaptic dynamics. We implement HetSyn as HetSynLIF, an extended form of the leaky integrate-and-fire (LIF) model equipped with synapse-specific decay dynamics. By adjusting the parameter configuration, HetSynLIF can be specialized into vanilla LIF neurons, neurons with threshold adaptation, and neuron-level heterogeneous models. We demonstrate that HetSynLIF not only improves the performance of SNNs across a variety of tasks—including pattern generation, delayed match-to-sample, speech recognition, and visual recognition—but also exhibits strong robustness to noise, enhanced working memory performance, efficiency under limited neuron resources, and generalization across timescales. In addition, analysis of the learned synaptic time constants reveals trends consistent with empirical observations in biological synapses. These findings underscore the significance of synaptic heterogeneity in enabling efficient neural computation, offering new insights into brain-inspired temporal modeling. Code available at: https://github.com/dzcgood/HetSyn."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs) offer a biologically plausible and energy-efficient framework
for temporal information processing.

## Core Method

However, existing studies overlook a fundamental property widely observed in biological
neurons—synaptic heterogeneity, which plays a crucial role in temporal processing and
cognitive capabilities.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNN/spiking neural computation。自动分类理由：Official abstract confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence.。 备注：Track: Main Conference Track. Official
abstract/page inspected under broad high-recall title workflow.。
