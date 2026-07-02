---
title: "NEC-Diff: Noise-Robust Event-RAW Complementary Diffusion for Seeing Motion in Extreme Darkness"
authors: ["Haoyue Liu", "Jinghan Xu", "Luxin Feng", "Hanyu Zhou", "Haozhi Zhao", "Yi Chang", "Luxin Yan"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_NEC-Diff_Noise-Robust_Event-RAW_Complementary_Diffusion_for_Seeing_Motion_in_Extreme_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Liu_NEC-Diff_Noise-Robust_Event-RAW_Complementary_Diffusion_for_Seeing_Motion_in_Extreme_CVPR_2026_paper.html"
tags: []
abstract: "High-quality imaging of dynamic scenes in extremely low-light conditions is highly challenging. Photon scarcity induces severe noise and texture loss, causing significant image degradation. Event cameras, featuring a high dynamic range (120 dB) and high sensitivity to motion, serve as powerful complements to conventional cameras by offering crucial cues for preserving subtle textures. However, most existing approaches emphasize texture recovery from events, while paying little attention to image noise or the intrinsic noise of events themselves, which ultimately hinders accurate pixel reconstruction under photon-starved conditions. In this work, we propose NEC-Diff, a novel diffusion-based event-RAW hybrid imaging framework that extracts reliable information from heavily noisy signals to reconstruct fine scene structures. The framework is driven by two key insights: (1) combining the linear light-response property of RAW images with the brightness-change nature of events to establish a physics-driven constraint for robust dual-modal denoising; and (2) dynamically estimating the SNR of both modalities based on denoising results to guide adaptive feature fusion, thereby injecting reliable cues into the diffusion process for high-fidelity visual reconstruction. Furthermore, we construct the REAL (Raw and Event Acquired in Low-light) dataset which provides 47,800 pixel-aligned low-light RAW images, events, and high-quality references under 0.001-0.8 lux illumination. Extensive experiments demonstrate the superiority of NEC-Diff under extreme darkness."
status: "auto-generated; brief scan note"
---
## Core Problem

High-quality imaging of dynamic scenes in extremely low-light conditions is highly
challenging.

## Core Method

Photon scarcity induces severe noise and texture loss, causing significant image
degradation.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
