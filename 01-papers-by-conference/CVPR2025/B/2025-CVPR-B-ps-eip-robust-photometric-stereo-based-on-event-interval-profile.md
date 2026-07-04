---
title: "PS-EIP: Robust Photometric Stereo Based on Event Interval Profile"
authors: ["Kazuma Kitazawa", "Takahito Aoto", "Satoshi Ikehata", "Tsuyoshi Takatani"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Kitazawa_PS-EIP_Robust_Photometric_Stereo_Based_on_Event_Interval_Profile_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Kitazawa_PS-EIP_Robust_Photometric_Stereo_Based_on_Event_Interval_Profile_CVPR_2025_paper.html"
tags: []
abstract: "Recently, the energy-efficient photometric stereo method using an event camera has been proposed to recover surface normals from events triggered by changes in logarithmic Lambertian reflections under a moving directional light source. However, EventPS treats each event interval independently, making it sensitive to noise, shadows, and non-Lambertian reflections. This paper proposes Photometric Stereo based on Event Interval Profile (PS-EIP), a robust method that recovers pixelwise surface normals from a time-series profile of event intervals. By exploiting the continuity of the profile and introducing an outlier detection method based on profile shape, our approach enhances robustness against outliers from shadows and specular reflections. Experiments using real event data from 3D-printed objects demonstrate that PS-EIP significantly improves robustness to outliers compared to EventPS's deep-learning variant, EventPS-FCN, without relying on deep learning."
status: "auto-generated; brief scan note"
---
## Core Problem

Recently, the energy-efficient photometric stereo method using an event camera has been
proposed to recover surface normals from events triggered by changes in logarithmic
Lambertian reflections under a moving directional light source.

## Core Method

However, EventPS treats each event interval independently, making it sensitive to noise,
shadows, and non-Lambertian reflections.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-
stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official CVF page inspected
under broad high-recall title workflow.。
