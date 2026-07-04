---
title: "ETAP: Event-based Tracking of Any Point"
authors: ["Friedhelm Hamann", "Daniel Gehrig", "Filbert Febryanto", "Kostas Daniilidis", "Guillermo Gallego"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Hamann_ETAP_Event-based_Tracking_of_Any_Point_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Hamann_ETAP_Event-based_Tracking_of_Any_Point_CVPR_2025_paper.html"
tags: []
abstract: "Tracking any point (TAP) recently shifted the motion estimation paradigm from focusing on individual salient points with local templates to tracking arbitrary points with global image contexts. However, while research has mostly focused on driving the accuracy of models in nominal settings, addressing scenarios with difficult lighting conditions and high-speed motions remains out of reach due to the limitations of the sensor. This work addresses this challenge with the first event camera-based TAP method. It leverages the high temporal resolution and high dynamic range of event cameras for robust high-speed tracking, and the global contexts in TAP methods to handle asynchronous and sparse event measurements. We further extend the TAP framework to handle event feature variations induced by motion -- thereby addressing an open challenge in purely event-based tracking -- with a novel feature alignment-loss which ensures the learning of motion-robust features. Our method is trained with data from a new data generation pipeline and systematically ablated across all design decisions. Our method shows strong cross-dataset generalization and performs 136% better on the average Jaccard metric than the baselines. Moreover, on an established feature tracking benchmark, it achieves a 20% improvement over the previous best event-only method and even surpasses the previous best events-and-frames method by 4.1%. Our code is available at https:// github.com/ tub-rip/ ETAP."
status: "auto-generated; brief scan note"
---
## Core Problem

Tracking any point (TAP) recently shifted the motion estimation paradigm from focusing on
individual salient points with local templates to tracking arbitrary points with global
image contexts.

## Core Method

However, while research has mostly focused on driving the accuracy of models in nominal
settings, addressing scenarios with difficult lighting conditions and high-speed motions
remains out of reach due to the limitations of the sensor.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official
CVF page inspected under broad high-recall title workflow.。
