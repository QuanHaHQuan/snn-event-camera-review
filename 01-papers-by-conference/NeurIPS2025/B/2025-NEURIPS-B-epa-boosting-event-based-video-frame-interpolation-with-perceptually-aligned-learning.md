---
title: "EPA: Boosting Event-based Video Frame Interpolation with Perceptually Aligned Learning"
authors: ["Yuhan Liu, LingHui Fu, Zhen Yang, Hao Chen, Youfu Li, Yongjian Deng"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/4ec0b6648bdf487a2f1c815924339022-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/4ec0b6648bdf487a2f1c815924339022-Abstract-Conference.html"
tags: []
abstract: "Event cameras, with their capacity to provide high temporal resolution information between frames, are increasingly utilized for video frame interpolation (VFI) in challenging scenarios characterized by high-speed motion and significant occlusion. However, prevalent issues of blur and distortion within the keyframes and ground truth data used for training and inference in these demanding conditions are frequently overlooked. This oversight impedes the perceptual realism and multi-scene generalization capabilities of existing event-based VFI (E-VFI) methods when generating interpolated frames. Motivated by the observation that semantic-perceptual discrepancies between degraded and pristine images are considerably smaller than their image-level differences, we introduce EPA. This novel E-VFI framework diverges from approaches reliant on direct image-level supervision by constructing multilevel, degradation-insensitive semantic perceptual supervisory signals to enhance the perceptual realism and multi-scene generalization of the model's predictions. Specifically, EPA operates in two phases: it first employs a DINO-based perceptual extractor, a customized style adapter, and a reconstruction generator to derive multi-layered, degradation-insensitive semantic-perceptual features ($\\mathcal{S}$). Second, a novel Bidirectional Event-Guided Alignment (BEGA) module utilizes deformable convolutions to align perceptual features from keyframes to ground truth with inter-frame temporal guidance extracted from event signals. By decoupling the learning process from direct image-level supervision, EPA enhances model robustness against degraded keyframes and unreliable ground truth information. Extensive experiments demonstrate that this approach yields interpolated frames more consistent with human perceptual preferences. *The code will be released upon acceptance.*"
status: "auto-generated; brief scan note"
---

## Core Problem

Event cameras, with their capacity to provide high temporal resolution information between frames, are increasingly utilized for video frame interpolation (VFI) in challenging scenarios characterized by high-speed motion and significant occlusion.

## Core Method

However, prevalent issues of blur and distortion within the keyframes and ground truth data used for training and inference in these demanding conditions are frequently overlooked.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-based video visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
