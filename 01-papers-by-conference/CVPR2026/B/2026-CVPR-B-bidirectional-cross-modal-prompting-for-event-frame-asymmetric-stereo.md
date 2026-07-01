---
title: 'Bidirectional Cross-Modal Prompting for Event-Frame Asymmetric Stereo'
authors: ['Ninghui Xu', 'Fabio Tosi', 'Lihui Wang', 'Jiawei Han', 'Luca Bartolomei', 'Zhiting Yao', 'Matteo Poggi', 'Stefano Mattoccia']
conference: 'CVPR'
year: 2026
level: 'B'
category: 'Event Camera'
pdf_link: 'https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Bidirectional_Cross-Modal_Prompting_for_Event-Frame_Asymmetric_Stereo_CVPR_2026_paper.pdf'
official_page: 'https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Bidirectional_Cross-Modal_Prompting_for_Event-Frame_Asymmetric_Stereo_CVPR_2026_paper.html'
tags: []
abstract: 'Conventional frame-based cameras capture rich contextual information but suffer from limited temporal resolution and motion blur in dynamic scenes. Event cameras offer an alternative visual representation with higher dynamic range free from such limitations. The complementary characteristics of the two modalities make event-frame asymmetric stereo promising for reliable 3D perception under fast motion and challenging illumination. However, the modality gap often leads to marginalization of domain-specific cues essential for cross-modal stereo matching. In this paper, we introduce Bi-CMPStereo, a novel bidirectional cross-modal prompting framework that fully exploits semantic and structural features from both domains for robust matching. Our approach learns finely aligned stereo representations within a target canonical space and integrates complementary representations by projecting each modality into both event and frame domains. Extensive experiments demonstrate that our approach significantly outperforms state-of-the-art methods in accuracy and generalization.'
status: 'auto-generated; brief scan note'
---

## Core Problem

事件-帧非对称 stereo 需要同时利用 RGB 帧的语义/结构信息和事件相机的高动态范围、高时间分辨率，但跨模态差异会削弱匹配所需的域内线索。

## Core Method

提出 Bi-CMPStereo，通过 bidirectional cross-modal prompting 将事件域和帧域特征投影到目标 canonical space，并融合两种模态的互补表示来做鲁棒 stereo matching。

## Key Metrics and Findings

摘要称在准确性和泛化能力上超过已有方法；具体数据集、误差指标和提升幅度需要阅读全文核对。

## Personal Notes

B 类事件相机背景论文，适合放在事件-帧融合、stereo/3D perception 和跨模态表示小节。
