---
title: 'EventUPS: Uncalibrated Photometric Stereo Using an Event Camera'
authors: ['Jinxiu Liang', 'Bohan Yu', 'Siqi Yang', 'Haotian Zhuang', 'Jieji Ren', 'Peiqi Duan', 'Boxin Shi']
conference: 'ICCV'
year: 2025
level: 'B'
category: 'Event Camera'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Liang_EventUPS_Uncalibrated_Photometric_Stereo_Using_an_Event_Camera_ICCV_2025_paper.html'
tags: []
abstract: 'We present EventUPS, the first uncalibrated photometric stereo (UPS) method using an event camera--a neuromorphic sensor that asynchronously detects brightness changes with microsecond resolution. Traditional frame-based UPS methods are hindered by high bandwidth demands and limited use in dynamic scenes. These methods require dense image correspondence under varying illumination and are incompatible with the fundamentally different sensing paradigm of event data. Our approach introduces three key innovations: an augmented null space formulation that directly relates each event to joint constraints on surface normals and lighting, naturally handling ambient illumination; a continuous parameterization of time-varying illumination that connects asynchronous events to synchronized lighting estimation; and a lighting fixture with known relative geometry that reduces ambiguity to a convex-concave uncertainty. We validate EventUPS using a custom-built LED lighting system. Experimental results show that our method achieves accuracy surpassing its frame-based counterpart while requiring only 5% of the data bandwidth.'
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
