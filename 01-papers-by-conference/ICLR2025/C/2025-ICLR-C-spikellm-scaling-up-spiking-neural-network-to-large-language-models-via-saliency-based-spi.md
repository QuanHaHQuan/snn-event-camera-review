---
title: "SpikeLLM: Scaling up Spiking Neural Network to Large Language Models via Saliency-based Spiking"
authors: ["Xingrun Xing", "Boyan Gao", "Zheng Liu", "David Clifton", "Shitao Xiao", "Wanpeng Zhang", "Li Du", "Zheng Zhang", "Guoqi Li", "Jiajun Zhang"]
conference: "ICLR"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2025/file/510e7d39fce008a3e31de54b8f5be9ac-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/510e7d39fce008a3e31de54b8f5be9ac-Abstract-Conference.html"
tags: []
abstract: "Recent advancements in large language models (LLMs) with billions of parameters have improved performance in various applications, but their inference processes demand significant energy and computational resources. In contrast, the human brain, with approximately 86 billion neurons, is much more energy-efficient than LLMs with similar parameters. Inspired by this, we redesign 7$\\sim$70 billion parameter LLMs using bio-plausible spiking mechanisms, emulating the efficient behavior of the human brain. We propose the first spiking large language model, SpikeLLM. Coupled with the proposed model, two essential approaches are proposed to improve spike training efficiency: Generalized Integrate-and-Fire (GIF) neurons to compress spike length from $T$ to $\\frac{T}{L} \\log_2 L$ bits, and an Optimal Brain Spiking framework to divide outlier channels and allocate different $T$ for GIF neurons, which further compresses spike length to approximate $log_2T$ bits. The necessity of spike-driven LLM is proved by comparison with quantized LLMs with similar operations. In the OmniQuant pipeline, SpikeLLM reduces 11.01\\% WikiText2 perplexity and improves 2.55\\% accuracy of common scene reasoning on a LLAMA-7B W4A4 model. In the GPTQ pipeline, SpikeLLM achieves direct additive in linear layers, significantly exceeding PB-LLMs. Our code is publicly available at https://github.com/Xingrun-Xing2/SpikeLLM."
status: "auto-generated; brief scan note"
---

## Core Problem

Recent advancements in large language models (LLMs) with billions of parameters have improved performance in various applications, but their inference processes demand significant energy and computational resources.

## Core Method

In contrast, the human brain, with approximately 86 billion neurons, is much more energy-efficient than LLMs with similar parameters.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：spiking neural network; spiking。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
