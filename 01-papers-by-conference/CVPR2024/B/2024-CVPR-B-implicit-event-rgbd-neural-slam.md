---
title: "Implicit Event-RGBD Neural SLAM"
authors: ["Delin Qu", "Chi Yan", "Dong Wang", "Jie Yin", "Qizhi Chen", "Dan Xu", "Yiting Zhang", "Bin Zhao", "Xuelong Li"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Qu_Implicit_Event-RGBD_Neural_SLAM_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Qu_Implicit_Event-RGBD_Neural_SLAM_CVPR_2024_paper.html"
tags: []
abstract: "Implicit neural SLAM has achieved remarkable progress recently. Nevertheless existing methods face significant challenges in non-ideal scenarios such as motion blur or lighting variation which often leads to issues like convergence failures localization drifts and distorted mapping. To address these challenges we propose EN-SLAM the first event-RGBD implicit neural SLAM framework which effectively leverages the high rate and high dynamic range advantages of event data for tracking and mapping. Specifically EN-SLAM proposes a differentiable CRF (Camera Response Function) rendering technique to generate distinct RGB and event camera data via a shared radiance field which is optimized by learning a unified implicit representation with the captured event and RGBD supervision. Moreover based on the temporal difference property of events we propose a temporal aggregating optimization strategy for the event joint tracking and global bundle adjustment capitalizing on the consecutive difference constraints of events significantly enhancing tracking accuracy and robustness. Finally we construct the simulated dataset DEV-Indoors and real captured dataset DEV-Reals containing 6 scenes 17 sequences with practical motion blur and lighting changes for evaluations. Experimental results show that our method outperforms the SOTA methods in both tracking ATE and mapping ACC with a real-time 17 FPS in various challenging environments. Project page: https://delinqu.github.io/EN-SLAM."
status: "auto-generated; brief scan note"
---
## Core Problem

Implicit neural SLAM has achieved remarkable progress recently.

## Core Method

Nevertheless existing methods face significant challenges in non-ideal scenarios such as
motion blur or lighting variation which often leads to issues like convergence failures
localization drifts and distorted mapping.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-
stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official CVF page inspected
under broad high-recall title workflow.。
