---
title: "Slack-Free Spiking Neural Network Formulation for Hypergraph Minimum Vertex Cover"
authors: ["Tam Ngoc-Bang Nguyen, Anh-Dzung Doan, Zhipeng Cai, Tat-Jun Chin"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/7a9745f251508a053425a256490b0665-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/7a9745f251508a053425a256490b0665-Abstract-Conference.html"
tags: []
abstract: "Neuromorphic computers open up the potential of energy-efficient computation using spiking neural networks (SNN), which consist of neurons that exchange spike-based information asynchronously. In particular, SNNs have shown promise in solving combinatorial optimization. Underpinning the SNN methods is the concept of energy minimization of an Ising model, which is closely related to quadratic unconstrained binary optimization (QUBO). Thus, the starting point for many SNN methods is reformulating the target problem as QUBO, then executing an SNN-based QUBO solver. For many combinatorial problems, the reformulation entails introducing penalty terms, potentially with slack variables, that implement feasibility constraints in the QUBO objective. For more complex problems such as hypergraph minimum vertex cover (HMVC), numerous slack variables are introduced which drastically increase the search domain and reduce the effectiveness of the SNN solver. In this paper, we propose a novel SNN formulation for HMVC. Rather than using penalty terms with slack variables, our SNN architecture introduces additional spiking neurons with a constraint checking and correction mechanism that encourages convergence to feasible solutions. In effect, our method obviates the need for reformulating HMVC as QUBO. Experiments on neuromorphic hardware show that our method consistently yielded high quality solutions for HMVC on real and synthetic instances where the SNN-based QUBO solver often failed, while consuming measurably less energy than global solvers on CPU."
status: "auto-generated; brief scan note"
---
## Core Problem

Neuromorphic computers open up the potential of energy-efficient computation using spiking
neural networks (SNN), which consist of neurons that exchange spike-based information
asynchronously.

## Core Method

In particular, SNNs have shown promise in solving combinatorial optimization.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural network; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage rescan; official abstract/page inspected; Track: Main Conference Track; needs human
verification.。
