---
title: "Enhanced Event-based Dense Stereo via Cross-Sensor Knowledge Distillation"
authors: ["Haihao Zhang", "Yunjian Zhang", "Jianing Li", "Lin Zhu", "Meng Lv", "Yao Zhu", "Yanwei Liu", "Xiangyang Ji"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Enhanced_Event-based_Dense_Stereo_via_Cross-Sensor_Knowledge_Distillation_ICCV_2025_paper.html"
tags: []
abstract: "Accurate stereo matching under fast motion and extreme lighting conditions is a challenge for many vision applications. Event cameras have the advantages of low latency and high dynamic range, thus providing a reliable solution to this challenge. However, since events are sparse, this makes it an ill-posed problem to obtain dense disparity using only events. In this work, we propose a novel framework for event-based dense stereo via cross-sensor knowledge distillation. Specifically, a multi-level intensity-to-event distillation strategy is designed to maximize the potential of long-range information, local texture details, and task-related knowledge of the intensity images. Simultaneously, to enforce the cross-view consistency, an intensity-event joint left-right consistency module is proposed. With our framework, extensive dense and structural information contained in intensity images is distilled to the event branch. Therefore, retaining only the events can predict dense disparities during inference, preserving the low latency characteristics of the events. Adequate experiments conducted on the MVSEC and DSEC datasets demonstrate that our method exhibits superior stereo matching performance than baselines, both quantitatively and qualitatively."
status: "auto-generated; brief scan note"
---

## Core Problem

Accurate stereo matching under fast motion and extreme lighting conditions is a challenge for many vision applications.

## Core Method

Event cameras have the advantages of low latency and high dynamic range, thus providing a reliable solution to this challenge.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
