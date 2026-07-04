---
title: "EyeGraph: Modularity-aware Spatio Temporal Graph Clustering for Continuous Event-based Eye Tracking"
authors: ["Nuwan Bandara, Thivya Kandappu, Argha Sen, Ila Gokarn, Archan Misra"]
conference: "NeurIPS"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/d9d40ea135f064d9e49e0579e59ad773-Paper-Datasets_and_Benchmarks_Track.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/d9d40ea135f064d9e49e0579e59ad773-Abstract-Datasets_and_Benchmarks_Track.html"
tags: []
abstract: "Continuous tracking of eye movement dynamics plays a significant role in developing a broad spectrum of human-centered applications, such as cognitive skills (visual attention and working memory) modeling, human-machine interaction, biometric user authentication, and foveated rendering. Recently neuromorphic cameras have garnered significant interest in the eye-tracking research community, owing to their sub-microsecond latency in capturing intensity changes resulting from eye movements. Nevertheless, the existing approaches for event-based eye tracking suffer from several limitations: dependence on RGB frames, label sparsity, and training on datasets collected in controlled lab environments that do not adequately reflect real-world scenarios. To address these limitations, in this paper, we propose a dynamic graph-based approach that uses a neuromorphic event stream captured by Dynamic Vision Sensors (DVS) for high-fidelity tracking of pupillary movement. More specifically, first, we present EyeGraph, a large-scale multi-modal near-eye tracking dataset collected using a wearable event camera attached to a head-mounted device from 40 participants -- the dataset was curated while mimicking in-the-wild settings, accounting for varying mobility and ambient lighting conditions. Subsequently, to address the issue of label sparsity, we adopt an unsupervised topology-aware approach as a benchmark. To be specific, (a) we first construct a dynamic graph using Gaussian Mixture Models (GMM), resulting in a uniform and detailed representation of eye morphology features, facilitating accurate modeling of pupil and iris. Then (b) apply a novel topologically guided modularity-aware graph clustering approach to precisely track the movement of the pupil and address the label sparsity in event-based eye tracking. We show that our unsupervised approach has comparable performance against the supervised approaches while consistently outperforming the conventional clustering approaches."
status: "auto-generated; brief scan note"
---
## Core Problem

Continuous tracking of eye movement dynamics plays a significant role in developing a broad
spectrum of human-centered applications, such as cognitive skills (visual attention and
working memory) modeling, human-machine interaction, biometric user authentication, and
foveated rendering.

## Core Method

Recently neuromorphic cameras have garnered significant interest in the eye-tracking
research community, owing to their sub-microsecond latency in capturing intensity changes
resulting from eye movements.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：strict two-stage
rescan; official abstract/page inspected; Track: Datasets and Benchmarks Track; needs human
verification. NeurIPS all-track special handling: non-main track is eligible as a formal
long paper but should be lower priority for A/P0 unless highly relevant.。
