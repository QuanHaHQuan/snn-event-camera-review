---
title: "Temporal-Mapping Photography for Event Cameras"
authors: ["Yuhan Bao", "Lei Sun", "Yuqin Ma", "Kaiwei Wang"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07171.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1000"
tags: []
abstract: "Event cameras, or Dynamic Vision Sensors (DVS) are novel neuromorphic sensors that capture brightness changes as a continuous stream of “events” rather than traditional intensity frames. Converting sparse events to dense intensity frames faithfully has long been an ill-posed problem. Previous methods have primarily focused on converting events to video in dynamic scenes or with a moving camera. In this paper, for the first time, we realize events to dense intensity image conversion using a stationary event camera in static scenes with a transmittance adjustment device for brightness modulation. Different from traditional methods that mainly rely on event integration, the proposed Event-Based Temporal Mapping Photography (EvTemMap) measures the time of event emitting for each pixel. Then, the resulting Temporal Matrix is converted to an intensity frame with a temporal mapping neural network. At the hardware level, the proposed EvTemMapis implemented by combining a transmittance adjustment device with a DVS, named Adjustable Transmittance Dynamic Vision Sensor. Additionally, we collected TemMat dataset under various conditions including low-light and high dynamic range scenes. The experimental results showcase the high dynamic range, fine-grained details, and high-grayscale-resolution of the proposed EvTemMap. The code and dataset are available in https://github.com/YuHanBaozju/EvTemMap."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras, or Dynamic Vision Sensors (DVS) are novel neuromorphic sensors that capture
brightness changes as a continuous stream of “events” rather than traditional intensity
frames.

## Core Method

Converting sparse events to dense intensity frames faithfully has long been an ill-posed
problem.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; DVS。自动分类理由：Official abstract/page confirms event-camera/DVS/event-
stream evidence; no clear SNN evidence.。
