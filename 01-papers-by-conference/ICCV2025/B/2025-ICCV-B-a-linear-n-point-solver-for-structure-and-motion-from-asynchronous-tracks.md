---
title: "A Linear N-Point Solver for Structure and Motion from Asynchronous Tracks"
authors: ["Hang Su", "Yunlong Feng", "Daniel Gehrig", "Panfeng Jiang", "Ling Gao", "Xavier Lagorce", "Laurent Kneip"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Su_A_Linear_N-Point_Solver_for_Structure_and_Motion_from_Asynchronous_ICCV_2025_paper.html"
tags: []
abstract: "Structure and continuous motion estimation from point correspondences is a fundamental problem in computer vision that has been powered by well-known algorithms such as the familiar 5-point or 8-point algorithm. However, despite their acclaim, these algorithms are limited to processing point correspondences originating from a pair of views each one representing an instantaneous capture of the scene. Yet, in the case of rolling shutter cameras, or more recently, event cameras, this synchronization breaks down. In this work, we present a unified approach for structure and linear motion estimation from 2D point correspondences with arbitrary timestamps, from an arbitrary set of views. By formulating the problem in terms of first-order dynamics and leveraging a constant velocity motion model, we derive a novel, linear point incidence relation allowing for the efficient recovery of both linear velocity and 3D points with predictable degeneracies and solution multiplicities. Owing to its general formulation, it can handle correspondences from a wide range of sensing modalities such as global shutter, rolling shutter, and event cameras, and can even combine correspondences from different collocated sensors. We validate the effectiveness of our solver on both simulated and real-world data, where we show consistent improvement across all modalities when compared to recent approaches. We believe our work opens the door to efficient structure and motion estimation from asynchronous data."
status: "auto-generated; brief scan note"
---
## Core Problem

Structure and continuous motion estimation from point correspondences is a fundamental
problem in computer vision that has been powered by well-known algorithms such as the
familiar 5-point or 8-point algorithm.

## Core Method

However, despite their acclaim, these algorithms are limited to processing point
correspondences originating from a pair of views each one representing an instantaneous
capture of the scene.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
