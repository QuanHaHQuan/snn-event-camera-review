---
title: "Exact Gradients for Stochastic Spiking Neural Networks Driven by Rough Signals"
authors: ["Christian Holberg, Cristopher Salvi"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/3855b10f44494f5ba4c283a00079f1e2-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/3855b10f44494f5ba4c283a00079f1e2-Abstract-Conference.html"
tags: []
abstract: "We introduce a mathematically rigorous framework based on rough path theory to model stochastic spiking neural networks (SSNNs) as stochastic differential equations with event discontinuities (Event SDEs) and driven by càdlàg rough paths. Our formalism is general enough to allow for potential jumps to be present both in the solution trajectories as well as in the driving noise. We then identify a set of sufficient conditions ensuring the existence of pathwise gradients of solution trajectories and event times with respect to the network's parameters and show how these gradients satisfy a recursive relation. Furthermore, we introduce a general-purpose loss function defined by means of a new class of signature kernels indexed on càdlàg rough paths and use it to train SSNNs as generative models. We provide an end-to-end autodifferentiable solver for Event SDEs and make its implementation available as part of the $\\texttt{diffrax}$ library. Our framework is, to our knowledge, the first enabling gradient-based training of SSNNs with noise affecting both the spike timing and the network's dynamics."
status: "auto-generated; brief scan note"
---
## Core Problem

We introduce a mathematically rigorous framework based on rough path theory to model
stochastic spiking neural networks (SSNNs) as stochastic differential equations with event
discontinuities (Event SDEs) and driven by càdlàg rough paths.

## Core Method

Our formalism is general enough to allow for potential jumps to be present both in the
solution trajectories as well as in the driving noise.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-
stage rescan; official abstract/page inspected; Track: Main Conference Track; needs human
verification.。
