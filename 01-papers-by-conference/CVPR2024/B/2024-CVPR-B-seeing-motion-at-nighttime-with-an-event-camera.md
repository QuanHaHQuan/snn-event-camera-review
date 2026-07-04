---
title: "Seeing Motion at Nighttime with an Event Camera"
authors: ["Haoyue Liu", "Shihan Peng", "Lin Zhu", "Yi Chang", "Hanyu Zhou", "Luxin Yan"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Seeing_Motion_at_Nighttime_with_an_Event_Camera_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Seeing_Motion_at_Nighttime_with_an_Event_Camera_CVPR_2024_paper.html"
tags: []
abstract: "We focus on a very challenging task: imaging at nighttime dynamic scenes. Most previous methods rely on the low-light enhancement of a conventional RGB camera. However they would inevitably face a dilemma between the long exposure time of nighttime and the motion blur of dynamic scenes. Event cameras react to dynamic changes with higher temporal resolution (microsecond) and higher dynamic range (120dB) offering an alternative solution. In this work we present a novel nighttime dynamic imaging method with an event camera. Specifically we discover that the event at nighttime exhibits temporal trailing characteristics and spatial non-stationary distribution. Consequently we propose a nighttime event reconstruction network (NER-Net) which mainly includes a learnable event timestamps calibration module (LETC) to align the temporal trailing events and a non-uniform illumination aware module (NIAM) to stabilize the spatiotemporal distribution of events. Moreover we construct a paired real low-light event dataset (RLED) through a co-axial imaging system including 64200 spatially and temporally aligned image GTs and low-light events. Extensive experiments demonstrate that the proposed method outperforms state-of-the-art methods in terms of visual quality and generalization ability on real-world nighttime datasets. The project are available at: https://github.com/Liu-haoyue/NER-Net."
status: "auto-generated; brief scan note"
---
## Core Problem

We focus on a very challenging task: imaging at nighttime dynamic scenes.

## Core Method

Most previous methods rely on the low-light enhancement of a conventional RGB camera.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
