---
title: "Video Frame Interpolation via Direct Synthesis with the Event-based Reference"
authors: ["Yuhan Liu", "Yongjian Deng", "Hao Chen", "Zhen Yang"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Video_Frame_Interpolation_via_Direct_Synthesis_with_the_Event-based_Reference_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Video_Frame_Interpolation_via_Direct_Synthesis_with_the_Event-based_Reference_CVPR_2024_paper.html"
tags: []
abstract: "Video Frame Interpolation (VFI) has witnessed a surge in popularity due to its abundant downstream applications. Event-based VFI (E-VFI) has recently propelled the advancement of VFI. Thanks to the high temporal resolution benefits event cameras can bridge the informational void present between successive video frames. Most state-of-the-art E-VFI methodologies follow the conventional VFI paradigm which pivots on motion estimation between consecutive frames to generate intermediate frames through a process of warping and refinement. However this reliance engenders a heavy dependency on the quality and consistency of keyframes rendering these methods susceptible to challenges in extreme real-world scenarios such as missing moving objects and severe occlusion dilemmas. This study proposes a novel E-VFI framework that directly synthesize intermediate frames leveraging event-based reference obviating the necessity for explicit motion estimation and substantially enhancing the capacity to handle motion occlusion. Given the sparse and inherently noisy nature of event data we prioritize the reliability of the event-based reference leading to the development of an innovative event-aware reconstruction strategy for accurate reference generation. Besides we implement a bi-directional event-guided alignment from keyframes to the reference using the introduced E-PCD module. Finally a transformer-based decoder is adopted for prediction refinement. Comprehensive experimental evaluations on both synthetic and real-world datasets underscore the superiority of our approach and its potential to execute high-quality VFI tasks."
status: "auto-generated; brief scan note"
---
## Core Problem

Video Frame Interpolation (VFI) has witnessed a surge in popularity due to its abundant
downstream applications.

## Core Method

Event-based VFI (E-VFI) has recently propelled the advancement of VFI.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
