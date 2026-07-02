---
title: "Continuous-Time Human Motion Field from Event Cameras"
authors: ["Ziyun Wang", "Ruijun Zhang", "Zi-Yan Liu", "Yufu Wang", "Kostas Daniilidis"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Continuous-Time_Human_Motion_Field_from_Event_Cameras_ICCV_2025_paper.html"
tags: []
abstract: "This paper addresses the challenges of estimating a continuous-time field from a stream of events. Existing Human Mesh Recovery (HMR) methods rely predominantly on frame-based approaches, which are prone to aliasing and inaccuracies due to limited temporal resolution and motion blur. In this work, we predict a continuous-time human motion field from events caused by human motion. Prior state-of-the-art methods rely on computationally intensive optimization across a fixed number of poses at high frame rates, which becomes prohibitively expensive as we increase the temporal resolution. In comparison, our model leverages a recurrent feed-forward neural network to predict human motion in the latent space of possible human motions. We present the first work that replaces traditional event volume-based discrete-time pre-dictions with a continuous human motion field represented as a time-implicit function, enabling parallel pose queries at arbitrary temporal resolutions. To advance the evaluation of continuous-time human pose estimation, we introduce the Beam-splitter Event Agile Human Motion Dataset--a hardware-synchronized high-speed human dataset tailored for this purpose. EvHuman improves joint errors by 23.8 % compared to previous event human methods, while reducing the computational time by 69%."
status: "auto-generated; brief scan note"
---
## Core Problem

This paper addresses the challenges of estimating a continuous-time field from a stream of
events.

## Core Method

Existing Human Mesh Recovery (HMR) methods rely predominantly on frame-based approaches,
which are prone to aliasing and inaccuracies due to limited temporal resolution and motion
blur.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
