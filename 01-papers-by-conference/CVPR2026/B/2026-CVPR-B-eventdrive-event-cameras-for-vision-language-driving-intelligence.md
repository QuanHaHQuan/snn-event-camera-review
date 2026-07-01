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

自动驾驶中的模糊、眩光和快速运动会削弱传统 VLM 的感知与推理可靠性。

## Core Method

提出 EventDrive，一套面向驾驶智能的事件相机基准和模型方案。

## Key Metrics and Findings

摘要强调事件感知对 reasoning 和 decision-making 的作用。

## Personal Notes

可作为事件相机在驾驶语义任务中的应用背景。

