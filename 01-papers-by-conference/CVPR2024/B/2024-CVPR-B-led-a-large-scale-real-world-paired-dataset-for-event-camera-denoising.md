---
title: "LED: A Large-scale Real-world Paired Dataset for Event Camera Denoising"
authors: ["Yuxing Duan"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Duan_LED_A_Large-scale_Real-world_Paired_Dataset_for_Event_Camera_Denoising_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Duan_LED_A_Large-scale_Real-world_Paired_Dataset_for_Event_Camera_Denoising_CVPR_2024_paper.html"
tags: []
abstract: "Event camera has significant advantages in capturingdynamic scene information while being prone to noise interferenceparticularly in challenging conditions like lowthreshold and low illumination. However most existing researchfocuses on gentle situations hindering event cameraapplications in realistic complex scenarios. To tackle thislimitation and advance the field we construct a new pairedreal-world event denoising dataset (LED) including 3K sequenceswith 18K seconds of high-resolution (1200*680)event streams and showing three notable distinctions comparedto others: diverse noise levels and scenes largerscalewith high-resolution and high-quality GT. Specificallyit contains stepped parameters and varying illuminationwith diverse scenarios. Moreover based on theproperty of noise events inconsistency and signal eventsconsistency we propose a novel effective denoising framework(DED) using homogeneous dual events to generate theGT with better separating noise from the raw. Furthermorewe design a bio-inspired baseline leveraging Leaky-Integrate-and-Fire (LIF) neurons with dynamic thresholdsto realize accurate denoising. The experimental resultsdemonstrate that the remarkable performance of the proposedapproach on different datasets.The dataset and codeare at https://github.com/Yee-Sing/led."
status: "auto-generated; brief scan note"
---
## Core Problem

Event camera has significant advantages in capturingdynamic scene information while being
prone to noise interferenceparticularly in challenging conditions like lowthreshold and low
illumination.

## Core Method

However most existing researchfocuses on gentle situations hindering event
cameraapplications in realistic complex scenarios.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event。自动分类理由：Manual boundary check: event-camera denoising dataset and
framework; LIF-neuron baseline is not enough to make the whole paper a core SNN x event-
camera method.。 备注：CVPR 2024 official CVF page inspected under broad high-recall title
workflow.。
