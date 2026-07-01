---
title: 'TTAPFormer: Robust Arbitrary Point Tracking via Transient Asynchronous Fusion of Frames and Events'
authors: ['Jiaxiong Liu', 'Zhen Tan', 'Jinpu Zhang', 'Yi Zhou', 'Hui Shen', 'Xieyuanli Chen', 'Dewen Hu']
conference: 'CVPR'
year: 2026
level: 'B'
category: 'Event Camera'
pdf_link: 'https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_TTAPFormer_Robust_Arbitrary_Point_Tracking_via_Transient_Asynchronous_Fusion_of_CVPR_2026_paper.pdf'
official_page: 'https://openaccess.thecvf.com/content/CVPR2026/html/Liu_TTAPFormer_Robust_Arbitrary_Point_Tracking_via_Transient_Asynchronous_Fusion_of_CVPR_2026_paper.html'
tags: []
abstract: 'Tracking any point (TAP) is a fundamental yet challenging task in computer vision, requiring high precision and long-term motion reasoning. Recent attempts to combine RGB frames and event streams have shown promise, yet they typically rely on synchronous or non-adaptive fusion, leading to temporal misalignment and severe degradation when one modality fails. We introduce TAPFormer, a transformer-based framework that performs asynchronous temporal-consistent fusion of frames and events for robust and high-frequency arbitrary point tracking.Our key innovation is a Transient Asynchronous Fusion (TAF) mechanism, which explicitly models the temporal evolution between discrete frames through continuous event updates--bridging the gap between low-rate frames and high-rate events. In addition, a Cross-modal Locally Weighted Fusion (CLWF) module adaptively adjusts spatial attention according to modality reliability, yielding stable and discriminative features even under blur or low light.To evaluate our approach under realistic conditions, we construct a novel real-world frame-event TAP dataset under diverse illumination and motion conditions.Our method outperforms existing point trackers, achieving a 28.2% improvement in average pixel error within threshold. Moreover, on standard point tracking benchmarks, our tracker consistently achieves the best performance. We will release the code and dataset upon acceptance to support future research.'
status: 'auto-generated; brief scan note'
---

## Core Problem

任意点跟踪需要高精度和长时运动推理，帧与事件流融合若依赖同步或固定策略，会在模态失效、运动模糊或低光照下出现时间错位和性能下降。

## Core Method

TTAPFormer/TAPFormer 通过 Transient Asynchronous Fusion 用连续事件更新桥接低帧率图像和高频事件，并用 Cross-modal Locally Weighted Fusion 根据模态可靠性调节空间注意力。

## Key Metrics and Findings

摘要称构建真实 frame-event TAP 数据集，并在阈值内平均像素误差上提升 28.2%；完整 benchmark 和指标需核验。

## Personal Notes

B 类事件-帧融合跟踪论文，可与事件目标跟踪和高频视觉感知方向联读。
