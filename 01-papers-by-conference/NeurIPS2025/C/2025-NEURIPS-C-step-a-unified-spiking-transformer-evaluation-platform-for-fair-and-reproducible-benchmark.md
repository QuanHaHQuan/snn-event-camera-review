---
title: "STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking"
authors: ["Sicheng Shen, Dongcheng Zhao, Linghao Feng, Zeyang Yue, Jindong Li, Tenglong Li, Guobin Shen, Yi Zeng"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/e9fece10c0f4ffdcf015ab676f370fbd-Paper-Datasets_and_Benchmarks_Track.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/e9fece10c0f4ffdcf015ab676f370fbd-Abstract-Datasets_and_Benchmarks_Track.html"
tags: []
abstract: "Spiking Transformers have recently emerged as promising architectures for combining the efficiency of spiking neural networks with the representational power of self-attention. However, the lack of standardized implementations, evaluation pipelines, and consistent design choices has hindered fair comparison and principled analysis. In this paper, we introduce \\textbf{STEP}, a unified benchmark framework for Spiking Transformers that supports a wide range of tasks, including classification, segmentation, and detection across static, event-based, and sequential datasets. STEP provides modular support for diverse components such as spiking neurons, input encodings, surrogate gradients, and multiple backends (e.g., SpikingJelly, BrainCog). Using STEP, we reproduce and evaluate several representative models, and conduct systematic ablation studies on attention design, neuron types, encoding schemes, and temporal modeling capabilities. We also propose a unified analytical model for energy estimation, accounting for spike sparsity, bitwidth, and memory access, and show that quantized ANNs may offer comparable or better energy efficiency. Our results suggest that current Spiking Transformers rely heavily on convolutional frontends and lack strong temporal modeling, underscoring the need for spike-native architectural innovations. The full code is available at: https://github.com/Fancyssc/STEP."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Transformers have recently emerged as promising architectures for combining the
efficiency of spiking neural networks with the representational power of self-attention.

## Core Method

However, the lack of standardized implementations, evaluation pipelines, and consistent
design choices has hindered fair comparison and principled analysis.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking neurons; surrogate gradients; spiking
transformers。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural computation;
no clear event-camera/DVS evidence found.。 备注：strict two-stage rescan; official
abstract/page inspected; needs human verification; Track: Datasets and Benchmarks Track;
NeurIPS all-track special handling: non-main track is eligible as a formal long paper but
should be lower priority for A/P0 unless highly relevant.。
