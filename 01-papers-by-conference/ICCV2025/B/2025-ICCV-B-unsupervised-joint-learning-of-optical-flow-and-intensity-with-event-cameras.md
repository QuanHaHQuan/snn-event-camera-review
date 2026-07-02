---
title: "Unsupervised Joint Learning of Optical Flow and Intensity with Event Cameras"
authors: ["Shuang Guo", "Friedhelm Hamann", "Guillermo Gallego"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Guo_Unsupervised_Joint_Learning_of_Optical_Flow_and_Intensity_with_Event_ICCV_2025_paper.html"
tags: []
abstract: "Event cameras rely on motion to obtain information about scene appearance. This means that appearance and motion are inherently linked: either both are present and recorded in the event data, or neither is captured. Previous works treat the recovery of these two visual quantities as separate tasks, which does not fit with the above-mentioned nature of event cameras and overlooks the inherent relations between them. We propose an unsupervised learning framework that jointly estimates optical flow (motion) and image intensity (appearance) using a single network. From the data generation model, we newly derive the event-based photometric error as a function of optical flow and image intensity. This error is further combined with the contrast maximization framework to form a comprehensive loss function that provides proper constraints for both flow and intensity estimation. Exhaustive experiments show our method's state-of-the-art performance: in optical flow estimation, it reduces EPE by 20% and AE by 25% compared to unsupervised approaches, while delivering competitive intensity estimation results, particularly in high dynamic range scenarios. Our method also achieves shorter inference time than all other optical flow methods and many of the image reconstruction methods, while they output only one quantity. Project page: https://github.com/tub-rip/E2FAI"
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras rely on motion to obtain information about scene appearance.

## Core Method

This means that appearance and motion are inherently linked: either both are present and
recorded in the event data, or neither is captured.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event data。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
