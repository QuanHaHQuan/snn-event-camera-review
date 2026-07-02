---
title: "Simultaneous Motion And Noise Estimation with Event Cameras"
authors: ["Shintaro Shiba", "Yoshimitsu Aoki", "Guillermo Gallego"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Shiba_Simultaneous_Motion_And_Noise_Estimation_with_Event_Cameras_ICCV_2025_paper.html"
tags: []
abstract: "Event cameras are emerging vision sensors whose noise is challenging to characterize. Existing denoising methods for event cameras are often designed in isolation and thus consider other tasks, such as motion estimation, separately (i.e., sequentially after denoising). However, motion is an intrinsic part of event data, since scene edges cannot be sensed without motion. We propose, to the best of our knowledge, the first method that simultaneously estimates motion in its various forms (e.g., ego-motion, optical flow) and noise. The method is flexible, as it allows replacing the one-step motion estimation of the widely-used Contrast Maximization framework with any other motion estimator, such as deep neural networks. The experiments show that the proposed method achieves state-of-the-art results on the E-MLB denoising benchmark and competitive results on the DND21 benchmark, while demonstrating effectiveness across motion estimation and intensity reconstruction tasks. Our approach advances event-data denoising theory and expands practical denoising use-cases via open-source code. Project page: https://github.com/tub-rip/ESMD"
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras are emerging vision sensors whose noise is challenging to characterize.

## Core Method

Existing denoising methods for event cameras are often designed in isolation and thus
consider other tasks, such as motion estimation, separately (i.e., sequentially after
denoising).

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event data。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
