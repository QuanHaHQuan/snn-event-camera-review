---
title: "Improving Generalization and Robustness in SNNs Through Signed Rate Encoding and Sparse Encoding Attacks"
authors: ["Bhaskar Mukhoty", "Hilal AlQuabeh", "Bin Gu"]
conference: "ICLR"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2025/file/bfde7fb279709eff53faa074b45840d8-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/bfde7fb279709eff53faa074b45840d8-Abstract-Conference.html"
tags: []
abstract: "Rate-encoded spiking neural networks (SNNs) are known to offer superior adversarial robustness compared to direct-encoded SNNs but have relatively poor generalization on clean input. While the latter offers good generalization on clean input it suffers poor adversarial robustness under standard training. A key reason for this difference is the input noise introduced by the rate encoding, which encodes a pixel intensity with $T$ independent Bernoulli samples. To improve the generalization of rate-encoded SNNs, we propose the *signed rate encoding* (sRATE) that allows mean centering of the input and helps reduce the randomness introduced by the encoding, resulting in improved clean accuracy. In contrast to rate encoding, where input restricted to $[0,1]^d$ is encoded in $\\\\{0,1\\\\}^{d\\times T}$, the signed rate encoding allows input in $[-1,1]^d$ to be encoded with spikes in $\\\\{-1,0,1\\\\}^{d\\times T}$, where positive (negative) inputs are encoded with positive (negative) spikes. We further construct efficient \\textit{Sparse Encoding Attack} (SEA) on standard and signed rate encoded input, which performs $l_0$-norm restricted adversarial attack in the discrete encoding space. We prove the theoretical optimality of the attack under the first-order approximation of the loss and compare it empirically with the existing attacks on the input space. Adversarial training performed with SEA, under signed rate encoding, offers superior adversarial robustness to the existing attacks and itself. Experiments conducted on standard datasets show the effectiveness of sign rate encoding in improving accuracy across all settings including adversarial robustness. The code is available at https://github.com/BhaskarMukhoty/SignedRateEncoding"
status: "auto-generated; brief scan note"
---

## Core Problem

Rate-encoded spiking neural networks (SNNs) are known to offer superior adversarial robustness compared to direct-encoded SNNs but have relatively poor generalization on clean input.

## Core Method

While the latter offers good generalization on clean input it suffers poor adversarial robustness under standard training.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：snns。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
