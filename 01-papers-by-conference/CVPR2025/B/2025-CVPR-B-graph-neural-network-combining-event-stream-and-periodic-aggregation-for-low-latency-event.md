---
title: "Graph Neural Network Combining Event Stream and Periodic Aggregation for Low-Latency Event-based Vision"
authors: ["Manon Dampfhoffer", "Thomas Mesquida", "Damien Joubert", "Thomas Dalgaty", "Pascal Vivet", "Christoph Posch"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Dampfhoffer_Graph_Neural_Network_Combining_Event_Stream_and_Periodic_Aggregation_for_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Dampfhoffer_Graph_Neural_Network_Combining_Event_Stream_and_Periodic_Aggregation_for_CVPR_2025_paper.html"
tags: []
abstract: "Event-based cameras asynchronously detect changes in light intensity with high temporal resolution, making them a promising alternative to RGB camera for low-latency and low-power optical flow estimation. However, state-of-the-art convolutional neural network methods create frames from the event stream, therefore losing the opportunity to exploit events for both sparse computations and low-latency prediction. On the other hand, asynchronous event graph methods could leverage both, but at the cost of avoiding any form of time accumulation, which limits the prediction accuracy. In this paper, we propose to break this accuracy-latency trade-off with a novel architecture combining an asynchronous accumulation-free event branch and a periodic aggregation branch. The periodic branch performs feature aggregations on the event graphs of past data to extract global context information, which improves accuracy without introducing any latency.The solution could predict optical flow per event with a latency of tens of microseconds on asynchronous hardware, which represents a gain of three orders of magnitude with respect to state-of-the-art frame-based methods, with 48x less operations per second. We show that the solution can detect rapid motion changes faster than a periodic output. This work proposes, for the first time, an effective solution for ultra low-latency and low-power optical flow prediction from event cameras."
status: "auto-generated; brief scan note"
---
## Core Problem

Event-based cameras asynchronously detect changes in light intensity with high temporal
resolution, making them a promising alternative to RGB camera for low-latency and low-power
optical flow estimation.

## Core Method

However, state-of-the-art convolutional neural network methods create frames from the event
stream, therefore losing the opportunity to exploit events for both sparse computations and
low-latency prediction.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event stream; event; event-based; event-based vision; low latency。自动分类理由：Official
abstract/page strictly confirms event-camera/DVS/visual-event-stream evidence; no clear SNN
evidence found.。 备注：CVPR 2025 official CVF page inspected under broad high-recall title
workflow.。
