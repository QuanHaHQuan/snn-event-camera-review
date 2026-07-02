---
title: "A Scalable, Causal, and Energy Efficient Framework for Neural Decoding with Spiking Neural Networks"
authors: ["Georgios Mentzelopoulos, Ioannis Asmanis, Konrad Kording, Eva L Dyer, Kostas Daniilidis, Flavia Vitale"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/47387bb0aeb97785f608c11f2f4bb091-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/47387bb0aeb97785f608c11f2f4bb091-Abstract-Conference.html"
tags: []
abstract: "Brain-computer interfaces (BCIs) promise to enable vital functions, such as speech and prosthetic control, for individuals with neuromotor impairments. Central to their success are neural decoders, models that map neural activity to intended behavior. Current learning-based decoding approaches fall into two classes: simple, causal models that lack generalization, or complex, non-causal models that generalize and scale offline but struggle in real-time settings. Both face a common challenge, their reliance on power-hungry artificial neural network backbones, which makes integration into real-world, resource-limited systems difficult. Spiking neural networks (SNNs) offer a promising alternative. Because they operate causally (i.e. only on present and past inputs) these models are suitable for real-time use, and their low energy demands make them ideal for battery-constrained environments. To this end, we introduce Spikachu: a scalable, causal, and energy-efficient neural decoding framework based on SNNs. Our approach processes binned spikes directly by projecting them into a shared latent space, where spiking modules, adapted to the timing of the input, extract relevant features; these latent representations are then integrated and decoded to generate behavioral predictions. We evaluate our approach on 113 recording sessions from 6 non-human primates, totaling 43 hours of recordings. Our method outperforms causal baselines when trained on single sessions using between 2.26× and 418.81× less energy. Furthermore, we demonstrate that scaling up training to multiple sessions and subjects improves performance and enables few-shot transfer to unseen sessions, subjects, and tasks. Overall, Spikachu introduces a scalable, online-compatible neural decoding framework based on SNNs, whose performance is competitive relative to state-of-the-art models while consuming orders of magnitude less energy."
status: "auto-generated; brief scan note"
---
## Core Problem

Brain-computer interfaces (BCIs) promise to enable vital functions, such as speech and
prosthetic control, for individuals with neuromotor impairments.

## Core Method

Central to their success are neural decoders, models that map neural activity to intended
behavior.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNN/spiking neural computation。自动分类理由：Official abstract confirms SNN/spiking neural
computation; no clear event-camera/DVS evidence.。 备注：Track: Main Conference Track. Official
abstract/page inspected under broad high-recall title workflow.。
