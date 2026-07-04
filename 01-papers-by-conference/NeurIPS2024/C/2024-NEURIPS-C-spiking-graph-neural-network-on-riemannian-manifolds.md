---
title: "Spiking Graph Neural Network on Riemannian Manifolds"
authors: ["Li Sun, Zhenhao Huang, Qiqi Wan, Hao Peng, Philip S. Yu"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/3ba7560b4c3e66d760fbdd472cf4a5a9-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/3ba7560b4c3e66d760fbdd472cf4a5a9-Abstract-Conference.html"
tags: []
abstract: "Graph neural networks (GNNs) have become the dominant solution for learning on graphs, the typical non-Euclidean structures. Conventional GNNs, constructed with the Artificial Neuron Network (ANN), have achieved impressive performance at the cost of high computation and energy consumption. In parallel, spiking GNNs with brain-like spiking neurons are drawing increasing research attention owing to the energy efficiency. So far, existing spiking GNNs consider graphs in Euclidean space, ignoring the structural geometry, and suffer from the high latency issue due to Back-Propagation-Through-Time (BPTT) with the surrogate gradient. In light of the aforementioned issues, we are devoted to exploring spiking GNN on Riemannian manifolds, and present a Manifold-valued Spiking GNN (MSG). In particular, we design a new spiking neuron on geodesically complete manifolds with the diffeomorphism, so that BPTT regarding the spikes is replaced by the proposed differentiation via manifold. Theoretically, we show that MSG approximates a solver of the manifold ordinary differential equation. Extensive experiments on common graphs show the proposed MSG achieves superior performance to previous spiking GNNs and energy efficiency to conventional GNNs."
status: "auto-generated; brief scan note"
---
## Core Problem

Graph neural networks (GNNs) have become the dominant solution for learning on graphs, the
typical non-Euclidean structures.

## Core Method

Conventional GNNs, constructed with the Artificial Neuron Network (ANN), have achieved
impressive performance at the cost of high computation and energy consumption.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence found.。 备注：strict two-stage rescan; official
abstract/page inspected; Track: Main Conference Track; needs human verification.。
