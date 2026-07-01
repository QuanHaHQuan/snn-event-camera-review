---
title: 'EvaGaussians: Event Stream Assisted Gaussian Splatting from Blurry Images'
authors: ['Wangbo Yu', 'Chaoran Feng', 'Jianing Li', 'Jiye Tang', 'Jiashu Yang', 'Zhenyu Tang', 'Meng Cao', 'Xu Jia', 'Yuchao Yang', 'Li Yuan', 'Yonghong Tian']
conference: 'ICCV'
year: 2025
level: 'B'
category: 'Event Camera'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Yu_EvaGaussians_Event_Stream_Assisted_Gaussian_Splatting_from_Blurry_Images_ICCV_2025_paper.html'
tags: []
abstract: '3D Gaussian Splatting (3D-GS) has demonstrated exceptional capabilities in synthesizing novel views of 3D scenes. However, its training is heavily reliant on high-quality images and precise camera poses. Meeting these criteria can be challenging in non-ideal real-world conditions, where motion-blurred images frequently occur due to high-speed camera movements.To address these challenges, we introduce Event Stream Assisted Gaussian Splatting (EvaGaussians), a novel approach that harnesses event streams captured by event cameras to facilitate the learning of high-quality 3D-GS from motion-blurred images. Capitalizing on the high temporal resolution and dynamic range offered by event streams, we seamlessly integrate them into the initialization and optimization of 3D-GS, thereby enhancing the acquisition of high-fidelity novel views with intricate texture details. We also contribute two novel datasets comprising RGB frames, event streams, and corresponding camera parameters, featuring a wide variety of scenes and various camera motions. The comparison results reveal that our approach not only excels in generating high-fidelity novel views, but also offers improved training and inference efficiency. Video and code are available at the project page.'
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
