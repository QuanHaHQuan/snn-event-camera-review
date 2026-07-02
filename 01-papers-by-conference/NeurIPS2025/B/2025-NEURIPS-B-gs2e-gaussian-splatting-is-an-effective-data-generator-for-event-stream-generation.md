---
title: "GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation"
authors: ["Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/5dd2d7a5dba72af7a2d78128e02514f4-Paper-Datasets_and_Benchmarks_Track.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/5dd2d7a5dba72af7a2d78128e02514f4-Abstract-Datasets_and_Benchmarks_Track.html"
tags: []
abstract: "We introduce GS2E (Gaussian Splatting to Event Generation), a large-scale synthetic event dataset designed for high-fidelity event vision tasks, captured from real-world sparse multi-view RGB images. Existing event datasets are often synthesized from dense RGB videos, which typically suffer from limited viewpoint diversity and geometric inconsistency, or rely on expensive, hard-to-scale hardware setups. GS2E addresses these limitations by first reconstructing photorealistic static scenes using 3D Gaussian Splatting, followed by a novel, physically-informed event simulation pipeline. This pipeline integrates adaptive trajectory interpolation with physically-consistent event contrast threshold modeling. As a result, it generates temporally dense and geometrically consistent event streams under diverse motion and lighting conditions, while maintaining strong alignment with the underlying scene structure. Experimental results on event-based 3D reconstruction highlight GS2E’s superior generalization capabilities and its practical value as a benchmark for advancing event vision research."
status: "auto-generated; brief scan note"
---

## Core Problem

We introduce GS2E (Gaussian Splatting to Event Generation), a large-scale synthetic event dataset designed for high-fidelity event vision tasks, captured from real-world sparse multi-view RGB images.

## Core Method

Existing event datasets are often synthesized from dense RGB videos, which typically suffer from limited viewpoint diversity and geometric inconsistency, or rely on expensive, hard-to-scale hardware setups.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event dataset visual-event context; event datasets visual-event context; event stream with event-camera context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
