---
title: "EventDrive: Event Cameras for Vision-Language Driving Intelligence"
authors: ["Dongyue Lu", "Rong Li", "Ao Liang", "Lingdong Kong", "Wei Yin", "Lai Xing Ng", "Benoit R. Cottereau", "Camille Simon Chane", "Wei Tsang Ooi"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_EventDrive_Event_Cameras_for_Vision-Language_Driving_Intelligence_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Lu_EventDrive_Event_Cameras_for_Vision-Language_Driving_Intelligence_CVPR_2026_paper.html"
tags: []
abstract: "Event cameras sense the world through asynchronous brightness changes with microsecond latency and high dynamic range, offering motion fidelity far beyond frame-based sensors and capturing temporal structure that conventional exposures often miss. These properties make events a powerful complement to RGB in autonomous driving, especially under blur, glare, and rapid motion, where frame-based perception can become unreliable. However, existing event-aware vision-language models remain limited to generic perception and do not reveal how event sensing contributes to reasoning and decision-making across the full driving loop. We present EventDrive, a large-scale benchmark and model suite that unifies event streams, RGB frames, and language supervision across four core dimensions: Perception, Understanding, Prediction, and Planning, covering captions, structured QA, grounding, motion-state recognition, trajectory forecasting, and planning tasks. Building on this foundation, EventDrive-VLM introduces a multi-horizon event pyramid and a modality-routing mixture-of-experts to adaptively encode and fuse asynchronous and frame-based information for downstream reasoning. Comprehensive evaluation across diverse tasks shows that event streams provide substantial gains in temporal precision, motion awareness, and robustness, bringing event sensing into the center of driving intelligence."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras sense the world through asynchronous brightness changes with microsecond
latency and high dynamic range, offering motion fidelity far beyond frame-based sensors and
capturing temporal structure that conventional exposures often miss.

## Core Method

These properties make events a powerful complement to RGB in autonomous driving, especially
under blur, glare, and rapid motion, where frame-based perception can become unreliable.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event stream。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
