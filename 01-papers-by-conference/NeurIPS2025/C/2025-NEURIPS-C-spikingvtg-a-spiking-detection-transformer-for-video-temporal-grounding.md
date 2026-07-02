---
title: "SpikingVTG: A Spiking Detection Transformer for Video Temporal Grounding"
authors: ["Malyaban Bal, Brian Matejek, Susmit Jha, Adam Cobb"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/44ed4444d01714694ad6a4478532f330-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/44ed4444d01714694ad6a4478532f330-Abstract-Conference.html"
tags: []
abstract: "Video Temporal Grounding (VTG) aims to retrieve precise temporal segments in a video conditioned on natural language queries. Unlike conventional neural frameworks that rely heavily on computationally expensive dense matrix multiplications, Spiking Neural Networks (SNNs)—previously underexplored in this domain—offer a unique opportunity to tackle VTG tasks through bio-plausible spike-based communication and an event-driven accumulation-based computational paradigm. We introduce SpikingVTG, a multi-modal spiking detection transformer, designed to harness the computational simplicity and sparsity of SNNs for VTG tasks. Leveraging the temporal dynamics of SNNs, our model introduces a Saliency Feedback Gating (SFG) mechanism that assigns dynamic saliency scores to video clips and applies multiplicative gating to highlight relevant clips while suppressing less informative ones. SFG enhances performance and reduces computational overhead by minimizing neural activity. We analyze the layer-wise convergence dynamics of SFG-enabled model and apply implicit differentiation at equilibrium to enable efficient, BPTT-free training. To improve generalization and maximize performance, we enable knowledge transfer by optimizing a Cos-L2 representation matching loss that aligns the layer-wise representation and attention maps of a non-spiking teacher with those of our student SpikingVTG. Additionally, we present Normalization-Free (NF)-SpikingVTG, which eliminates non-local operations like softmax and layer normalization, and an extremely quantized 1-bit (NF)-SpikingVTG variant for potential deployment on edge devices. Our models achieve competitive results on QVHighlights, Charades-STA, TACoS, and YouTube Highlights, establishing a strong baseline for multi-modal spiking VTG solutions."
status: "auto-generated; brief scan note"
---
## Core Problem

Video Temporal Grounding (VTG) aims to retrieve precise temporal segments in a video
conditioned on natural language queries.

## Core Method

Unlike conventional neural frameworks that rely heavily on computationally expensive dense
matrix multiplications, Spiking Neural Networks (SNNs)—previously underexplored in this
domain—offer a unique opportunity to tackle VTG tasks through bio-plausible spike-based
communication and an event-driven accumulation-based computational paradigm.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNN/spiking neural computation。自动分类理由：Official abstract confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence.。 备注：Track: Main Conference Track. Official
abstract/page inspected under broad high-recall title workflow.。
