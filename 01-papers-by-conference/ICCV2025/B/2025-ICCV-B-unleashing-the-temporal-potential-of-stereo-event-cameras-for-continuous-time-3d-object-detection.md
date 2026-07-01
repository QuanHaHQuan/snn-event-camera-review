---
title: 'Unleashing the Temporal Potential of Stereo Event Cameras for Continuous-Time 3D Object Detection'
authors: ['Jae-Young Kang', 'Hoonhee Cho', 'Kuk-Jin Yoon']
conference: 'ICCV'
year: 2025
level: 'B'
category: 'Event Camera'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Kang_Unleashing_the_Temporal_Potential_of_Stereo_Event_Cameras_for_Continuous-Time_ICCV_2025_paper.html'
tags: []
abstract: '3D object detection is essential for autonomous systems, enabling precise localization and dimension estimation. While LiDAR and RGB cameras are widely used, their fixed frame rates create perception gaps in high-speed scenarios. Event cameras, with their asynchronous nature and high temporal resolution, offer a solution by capturing motion continuously. The recent approach, which integrates event cameras with conventional sensors for continuous-time detection, struggles in fast-motion scenarios due to its dependency on synchronized sensors. We propose a novel stereo 3D object detection framework that relies solely on event cameras, eliminating the need for conventional 3D sensors. To compensate for the lack of semantic and geometric information in event data, we introduce a dual filter mechanism that extracts both. Additionally, we enhance regression by aligning bounding boxes with object-centric information. Experiments show that our method outperforms prior approaches in dynamic environments, demonstrating the potential of event cameras for robust, continuous-time 3D perception. The code is available at https://github.com/mickeykang16/Ev-Stereo3D.'
status: 'auto-generated; brief scan note'
---

## Core Problem

自动驾驶等动态场景中的 3D object detection 受固定帧率传感器限制；已有连续时间检测方法依赖同步常规传感器，在快速运动下不够稳健。

## Core Method

论文提出仅依赖 stereo event cameras 的连续时间 3D 检测框架，用 dual filter mechanism 弥补事件数据语义和几何信息不足，并通过 object-centric 信息改进 bounding box regression。

## Key Metrics and Findings

摘要称在动态环境中优于先前方法，展示事件相机用于连续时间 3D 感知的潜力；具体数据集与指标需人工核验。

## Personal Notes

B 类事件相机 3D 检测论文，可用于事件 stereo、连续时间感知和自动驾驶场景讨论。
