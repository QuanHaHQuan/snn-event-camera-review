---
title: "Separation for Better Integration: Disentangling Edge and Motion in Event-based Deblurring"
authors: ["Yufei Zhu", "Hao Chen", "Yongjian Deng", "Wei You"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Separation_for_Better_Integration_Disentangling_Edge_and_Motion_in_Event-based_ICCV_2025_paper.html"
tags: []
abstract: "Traditional motion deblurring methods struggle to effectively model motion information within the exposure time. Recently, event cameras have attracted significant research interest for its ability to model motion cues over the exposure duration. However, these methods directly fuse event features with image, overlooking the intrinsic heterogeneity of events. In this paper, we identify that the event modality contains two conflicting types of information: edge features and motion cues. Events accumulated over a short exposure period capture sharp edge details but lose motion information, while those accumulated over a long exposure period blur edge details due to motion. To address this issue, we propose a simple yet effective approach to disentangle these two cues from event features and employ an edge-aware sharpening module along with motion-driven scale-adaptive deblurring module to fully leverage both. Specifically, the first module aids in restoring sharp edges by leveraging the clear edge features provided by events, while the second module leverages motion cues to learn diverse blur kernels, adaptively adjusting the receptive field for optimal deblurring. Extensive experiments on synthetic and real-world datasets validate the effectiveness of our approach and yield a substantial improvement over state-of-the-art single-frame methods and surpasses most multi-frame-based methods. Code will be publicly available."
status: "auto-generated; brief scan note"
---
## Core Problem

Traditional motion deblurring methods struggle to effectively model motion information
within the exposure time.

## Core Method

Recently, event cameras have attracted significant research interest for its ability to
model motion cues over the exposure duration.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event-based deblurring。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
