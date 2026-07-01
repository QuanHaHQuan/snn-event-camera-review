---
title: 'From Sharp to Blur: Unsupervised Domain Adaptation for 2D Human Pose Estimation Under Extreme Motion Blur Using Event Cameras'
authors: ['Youngho Kim', 'Hoonhee Cho', 'Kuk-Jin Yoon']
conference: 'ICCV'
year: 2025
level: 'B'
category: 'Event Camera'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Kim_From_Sharp_to_Blur_Unsupervised_Domain_Adaptation_for_2D_Human_ICCV_2025_paper.html'
tags: []
abstract: 'Human pose estimation is critical for applications such as rehabilitation, sports analytics, and AR/VR systems. However, rapid motion and low-light conditions often introduce motion blur, significantly degrading pose estimation due to the domain gap between sharp and blurred images. Most datasets assume stable conditions, making models trained on sharp images struggle in blurred environments. To address this, we introduce a novel domain adaptation approach that leverages event cameras, which capture high temporal resolution motion data and are inherently robust to motion blur. Using event-based augmentation, we generate motion-aware blurred images, effectively bridging the domain gap between sharp and blurred domains without requiring paired annotations. Additionally, we develop a student-teacher framework that iteratively refines pseudo-labels, leveraging mutual uncertainty masking to eliminate incorrect labels and enable more effective learning. Experimental results demonstrate that our approach outperforms conventional domain-adaptive human pose estimation methods, achieving robust pose estimation under motion blur without requiring annotations in the target domain. Our findings highlight the potential of event cameras as a scalable and effective solution for domain adaptation in real-world motion blur environments. Our project codes are available at https://github.com/kmax2001/EvSharp2Blur.'
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
