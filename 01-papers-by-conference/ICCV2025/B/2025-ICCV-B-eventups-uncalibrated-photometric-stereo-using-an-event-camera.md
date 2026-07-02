---
title: "EventUPS: Uncalibrated Photometric Stereo Using an Event Camera"
authors: ["Jinxiu Liang", "Bohan Yu", "Siqi Yang", "Haotian Zhuang", "Jieji Ren", "Peiqi Duan", "Boxin Shi"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Liang_EventUPS_Uncalibrated_Photometric_Stereo_Using_an_Event_Camera_ICCV_2025_paper.html"
tags: []
abstract: "We present EventUPS, the first uncalibrated photometric stereo (UPS) method using an event camera--a neuromorphic sensor that asynchronously detects brightness changes with microsecond resolution. Traditional frame-based UPS methods are hindered by high bandwidth demands and limited use in dynamic scenes. These methods require dense image correspondence under varying illumination and are incompatible with the fundamentally different sensing paradigm of event data. Our approach introduces three key innovations: an augmented null space formulation that directly relates each event to joint constraints on surface normals and lighting, naturally handling ambient illumination; a continuous parameterization of time-varying illumination that connects asynchronous events to synchronized lighting estimation; and a lighting fixture with known relative geometry that reduces ambiguity to a convex-concave uncertainty. We validate EventUPS using a custom-built LED lighting system. Experimental results show that our method achieves accuracy surpassing its frame-based counterpart while requiring only 5% of the data bandwidth."
status: "auto-generated; brief scan note"
---

## Core Problem

We present EventUPS, the first uncalibrated photometric stereo (UPS) method using an event camera--a neuromorphic sensor that asynchronously detects brightness changes with microsecond resolution.

## Core Method

Traditional frame-based UPS methods are hindered by high bandwidth demands and limited use in dynamic scenes.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; brightness change visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
