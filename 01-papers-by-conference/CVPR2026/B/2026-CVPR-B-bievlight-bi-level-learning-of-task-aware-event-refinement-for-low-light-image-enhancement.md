---
title: "BiEvLight: Bi-level Learning of Task-Aware Event Refinement for Low-Light Image Enhancement"
authors: ["Zishu Yao", "Xiang-Xiang Su", "Shengning Zhou", "Guang-Yong Chen", "Guodong Fan", "Xing Chen"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Yao_BiEvLight_Bi-level_Learning_of_Task-Aware_Event_Refinement_for_Low-Light_Image_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Yao_BiEvLight_Bi-level_Learning_of_Task-Aware_Event_Refinement_for_Low-Light_Image_CVPR_2026_paper.html"
tags: []
abstract: "Event cameras, with their high dynamic range, show great promise for Low-light Image Enhancement (LLIE). Existing works primarily focus on designing effective modal fusion strategies. However, a key challenge is the dual degradation from intrinsic background activity (BA) noise in events and low signal-to-noise ratio (SNR) in images, which causes severe noise coupling during modal fusion, creating a critical performance bottleneck. We therefore posit that precise event denoising is the prerequisite to unlocking the full potential of event-based fusion. To this end, we propose BiEvLight, a hierarchical and task-aware framework that collaboratively optimizes enhancement and denoising by exploiting their intrinsic interdependence. Specifically, BiEvLight exploits the strong gradient correlation between images and events to build a gradient-guided event denoising prior that alleviates insufficient denoising in heavily noisy regions. Moreover, instead of treating event denoising as a static pre-processing stage--which inevitably incurs a trade-off between over- and under-denoising and cannot adapt to the requirements of a specific enhancement objective--we recast it as a bilevel optimization problem constrained by the enhancement task. Through cross-task interaction, the upper-level denoising problem learns event representations tailored to the lower-level enhancement objective, thereby substantially improving overall enhancement quality. Extensive experiments on the Real-world noise Dataset SED demonstrate that our method significantly outperforms state-of-the-art (SOTA) approaches, with average improvements of 1.30dB in PSNR , 2.03dB in PSNR* and 0.047 in SSIM, respectively. The code will be publicly available at https://github.com/iijjlk/BiEvlight."
status: "auto-generated; brief scan note"
---

## Core Problem

Event cameras, with their high dynamic range, show great promise for Low-light Image Enhancement (LLIE).

## Core Method

Existing works primarily focus on designing effective modal fusion strategies.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
