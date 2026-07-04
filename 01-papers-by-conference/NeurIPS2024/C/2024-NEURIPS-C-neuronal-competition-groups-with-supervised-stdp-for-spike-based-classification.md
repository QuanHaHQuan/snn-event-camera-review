---
title: "Neuronal Competition Groups with Supervised STDP for Spike-Based Classification"
authors: ["Gaspard Goupy, Pierre Tirilly, Ioan Marius Bilasco"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/bfe593e151614c691323c08c0079c1f6-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/bfe593e151614c691323c08c0079c1f6-Abstract-Conference.html"
tags: []
abstract: "Spike Timing-Dependent Plasticity (STDP) is a promising substitute to backpropagation for local training of Spiking Neural Networks (SNNs) on neuromorphic hardware. STDP allows SNNs to address classification tasks by combining unsupervised STDP for feature extraction and supervised STDP for classification. Unsupervised STDP is usually employed with Winner-Takes-All (WTA) competition to learn distinct patterns. However, WTA for supervised STDP classification faces unbalanced competition challenges. In this paper, we propose a method to effectively implement WTA competition in a spiking classification layer employing first-spike coding and supervised STDP training. We introduce the Neuronal Competition Group (NCG), an architecture that improves classification capabilities by promoting the learning of various patterns per class. An NCG is a group of neurons mapped to a specific class, implementing intra-class WTA and a novel competition regulation mechanism based on two-compartment thresholds. We incorporate our proposed architecture into spiking classification layers trained with state-of-the-art supervised STDP rules. On top of two different unsupervised feature extractors, we obtain significant accuracy improvements on image recognition datasets such as CIFAR-10 and CIFAR-100. We show that our competition regulation mechanism is crucial for ensuring balanced competition and improved class separation."
status: "auto-generated; brief scan note"
---
## Core Problem

Spike Timing-Dependent Plasticity (STDP) is a promising substitute to backpropagation for
local training of Spiking Neural Networks (SNNs) on neuromorphic hardware.

## Core Method

STDP allows SNNs to address classification tasks by combining unsupervised STDP for feature
extraction and supervised STDP for classification.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spike。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence found.。 备注：strict two-stage rescan; official
abstract/page inspected; Track: Main Conference Track; needs human verification.。
