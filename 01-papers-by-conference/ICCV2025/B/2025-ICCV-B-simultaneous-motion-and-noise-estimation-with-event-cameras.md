---
title: 'Simultaneous Motion And Noise Estimation with Event Cameras'
authors: ['Shintaro Shiba', 'Yoshimitsu Aoki', 'Guillermo Gallego']
conference: 'ICCV'
year: 2025
level: 'B'
category: 'Event Camera'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Shiba_Simultaneous_Motion_And_Noise_Estimation_with_Event_Cameras_ICCV_2025_paper.html'
tags: []
abstract: 'Event cameras are emerging vision sensors whose noise is challenging to characterize. Existing denoising methods for event cameras are often designed in isolation and thus consider other tasks, such as motion estimation, separately (i.e., sequentially after denoising). However, motion is an intrinsic part of event data, since scene edges cannot be sensed without motion. We propose, to the best of our knowledge, the first method that simultaneously estimates motion in its various forms (e.g., ego-motion, optical flow) and noise. The method is flexible, as it allows replacing the one-step motion estimation of the widely-used Contrast Maximization framework with any other motion estimator, such as deep neural networks. The experiments show that the proposed method achieves state-of-the-art results on the E-MLB denoising benchmark and competitive results on the DND21 benchmark, while demonstrating effectiveness across motion estimation and intensity reconstruction tasks. Our approach advances event-data denoising theory and expands practical denoising use-cases via open-source code. Project page: https://github.com/tub-rip/ESMD'
status: 'auto-generated; brief scan note'
---
## Core Problem

事件相机在该任务中的主要瓶颈是时序信息很强，但噪声、运动模糊或稀疏事件会让标准视觉方法失效。

## Core Method

方法围绕 event camera / event stream 输入，利用事件的异步变化特征完成任务建模。

## Key Metrics and Findings

需要结合官方论文页与正文核对具体指标；当前仅确认其属于事件相机侧工作。

## Personal Notes

可作为事件相机背景论文进入对应任务章节。
