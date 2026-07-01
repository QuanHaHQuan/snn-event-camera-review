---
title: 'Unsupervised Joint Learning of Optical Flow and Intensity with Event Cameras'
authors: ['Shuang Guo', 'Friedhelm Hamann', 'Guillermo Gallego']
conference: 'ICCV'
year: 2025
level: 'B'
category: 'Event Camera'
pdf_link: ''
official_page: 'https://openaccess.thecvf.com/content/ICCV2025/html/Guo_Unsupervised_Joint_Learning_of_Optical_Flow_and_Intensity_with_Event_ICCV_2025_paper.html'
tags: []
abstract: "Event cameras rely on motion to obtain information about scene appearance. This means that appearance and motion are inherently linked: either both are present and recorded in the event data, or neither is captured. Previous works treat the recovery of these two visual quantities as separate tasks, which does not fit with the above-mentioned nature of event cameras and overlooks the inherent relations between them. We propose an unsupervised learning framework that jointly estimates optical flow (motion) and image intensity (appearance) using a single network. From the data generation model, we newly derive the event-based photometric error as a function of optical flow and image intensity. This error is further combined with the contrast maximization framework to form a comprehensive loss function that provides proper constraints for both flow and intensity estimation. Exhaustive experiments show our method's state-of-the-art performance: in optical flow estimation, it reduces EPE by 20% and AE by 25% compared to unsupervised approaches, while delivering competitive intensity estimation results, particularly in high dynamic range scenarios. Our method also achieves shorter inference time than all other optical flow methods and many of the image reconstruction methods, while they output only one quantity. Project page: https://github.com/tub-rip/E2FAI"
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
