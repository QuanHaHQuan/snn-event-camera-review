---
title: "MER-Tracker: Towards High-Speed 3D Point Tracking via Multi-View Event-RGB Hybrid Cameras"
authors: ["Yiqian Chang", "Qinghong Ye", "Haoran Xu", "Jianing Li", "Dongyang Ma", "Xuan Wang", "Wei Zhang", "Yonghong Tian", "Peixi Peng"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Chang_MER-Tracker_Towards_High-Speed_3D_Point_Tracking_via_Multi-View_Event-RGB_Hybrid_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Chang_MER-Tracker_Towards_High-Speed_3D_Point_Tracking_via_Multi-View_Event-RGB_Hybrid_CVPR_2026_paper.html"
tags: []
abstract: "This paper proposes the first task for high-speed 3D point tracking using multi-view Event-RGB hybrid cameras. We design a cuboid observation device comprising 4 RGB cameras (30fps) and 2 Event cameras to synchronously capture high-speed motions, and propose MER-Tracker, a high-frame-rate 3D point-tracking network that fuses the complementary strengths of dual modalities. We first respectively extract 2D motion-change features from the RGB and Event modalities, then apply linear interpolation and anchor sampling to fuse the discrete RGB 3D features and continuous Event 3D features after 3D lifting, and finally employ a LoRA-tuned Transformer based on temporal correlationship to predict the high-frame-rate 3D point trajectories over fast motions, accomplishing high-speed 3D point tracking. To verify the effectiveness of our method, we construct both real-world and simulated high-speed motion datasets. Experiments on these datasets show that our method achieves accurate high-speed 3D point tracking at high-frame-rate (150fps), outperforming state-of-the-art methods."
status: "auto-generated; brief scan note"
---

## Core Problem

This paper proposes the first task for high-speed 3D point tracking using multi-view Event-RGB hybrid cameras.

## Core Method

We design a cuboid observation device comprising 4 RGB cameras (30fps) and 2 Event cameras to synchronously capture high-speed motions, and propose MER-Tracker, a high-frame-rate 3D point-tracking network that fuses the complementary strengths of dual modalities.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-rgb visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
