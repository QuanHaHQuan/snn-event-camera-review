---
title: "EvaGaussians: Event Stream Assisted Gaussian Splatting from Blurry Images"
authors: ["Wangbo Yu", "Chaoran Feng", "Jianing Li", "Jiye Tang", "Jiashu Yang", "Zhenyu Tang", "Meng Cao", "Xu Jia", "Yuchao Yang", "Li Yuan", "Yonghong Tian"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Yu_EvaGaussians_Event_Stream_Assisted_Gaussian_Splatting_from_Blurry_Images_ICCV_2025_paper.html"
tags: []
abstract: "3D Gaussian Splatting (3D-GS) has demonstrated exceptional capabilities in synthesizing novel views of 3D scenes. However, its training is heavily reliant on high-quality images and precise camera poses. Meeting these criteria can be challenging in non-ideal real-world conditions, where motion-blurred images frequently occur due to high-speed camera movements.To address these challenges, we introduce Event Stream Assisted Gaussian Splatting (EvaGaussians), a novel approach that harnesses event streams captured by event cameras to facilitate the learning of high-quality 3D-GS from motion-blurred images. Capitalizing on the high temporal resolution and dynamic range offered by event streams, we seamlessly integrate them into the initialization and optimization of 3D-GS, thereby enhancing the acquisition of high-fidelity novel views with intricate texture details. We also contribute two novel datasets comprising RGB frames, event streams, and corresponding camera parameters, featuring a wide variety of scenes and various camera motions. The comparison results reveal that our approach not only excels in generating high-fidelity novel views, but also offers improved training and inference efficiency. Video and code are available at the project page."
status: "auto-generated; brief scan note"
---

## Core Problem

3D Gaussian Splatting (3D-GS) has demonstrated exceptional capabilities in synthesizing novel views of 3D scenes.

## Core Method

However, its training is heavily reliant on high-quality images and precise camera poses.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event stream with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
