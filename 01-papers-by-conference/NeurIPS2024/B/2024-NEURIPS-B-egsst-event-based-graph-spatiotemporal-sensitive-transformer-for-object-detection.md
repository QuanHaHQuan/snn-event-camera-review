---
title: "EGSST: Event-based Graph Spatiotemporal Sensitive Transformer for Object Detection"
authors: ["Sheng Wu, Hang Sheng, Hui Feng, Bo Hu"]
conference: "NeurIPS"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/da733d44e4be3902d952d6c1ffcb7db6-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/da733d44e4be3902d952d6c1ffcb7db6-Abstract-Conference.html"
tags: []
abstract: "Event cameras provide exceptionally high temporal resolution in dynamic vision systems due to their unique event-driven mechanism. However, the sparse and asynchronous nature of event data makes frame-based visual processing methods inappropriate. This study proposes a novel framework, Event-based Graph Spatiotemporal Sensitive Transformer (EGSST), for the exploitation of spatial and temporal properties of event data. Firstly, a well-designed graph structure is employed to model event data, which not only preserves the original temporal data but also captures spatial details. Furthermore, inspired by the phenomenon that human eyes pay more attention to objects that produce significant dynamic changes, we design a Spatiotemporal Sensitivity Module (SSM) and an adaptive Temporal Activation Controller (TAC). Through these two modules, our framework can mimic the response of the human eyes in dynamic environments by selectively activating the temporal attention mechanism based on the relative dynamics of event data, thereby effectively conserving computational resources. In addition, the integration of a lightweight, multi-scale Linear Vision Transformer (LViT) markedly enhances processing efficiency. Our research proposes a fully event-driven approach, effectively exploiting the temporal precision of event data and optimising the allocation of computational resources by intelligently distinguishing the dynamics within the event data. The framework provides a lightweight, fast, accurate, and fully event-based solution for object detection tasks in complex dynamic environments, demonstrating significant practicality and potential for application."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras provide exceptionally high temporal resolution in dynamic vision systems due
to their unique event-driven mechanism.

## Core Method

However, the sparse and asynchronous nature of event data makes frame-based visual
processing methods inappropriate.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：strict two-stage
rescan; official abstract/page inspected; Track: Main Conference Track; needs human
verification.。
