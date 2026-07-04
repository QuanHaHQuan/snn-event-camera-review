---
title: "Bridge Frame and Event: Common Spatiotemporal Fusion for High-Dynamic Scene Optical Flow"
authors: ["Hanyu Zhou", "Haonan Wang", "Haoyue Liu", "Yuxing Duan", "Yi Chang", "Luxin Yan"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhou_Bridge_Frame_and_Event_Common_Spatiotemporal_Fusion_for_High-Dynamic_Scene_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_Bridge_Frame_and_Event_Common_Spatiotemporal_Fusion_for_High-Dynamic_Scene_CVPR_2025_paper.html"
tags: []
abstract: "High-dynamic scene optical flow is a challenging task, which suffers spatial blur and temporal discontinuous motion due to large displacement in frame imaging, thus deteriorating the spatiotemporal feature of optical flow. Typically, existing methods mainly introduce event camera to directly fuse the spatiotemporal features between the two modalities. However, this direct fusion is ineffective, since there exists a large gap due to the heterogeneous data representation between frame and event modalities. To address this issue, we explore a common-latent space as an intermediate bridge to mitigate the modality gap. In this work, we propose a novel common spatiotemporal fusion between frame and event modalities for high-dynamic scene optical flow, including visual boundary localization and motion correlation fusion. Specifically, in visual boundary localization, we figure out that frame and event share the similar spatiotemporal gradients, whose similarity distribution is consistent with the extracted boundary distribution. This motivates us to design the common spatiotemporal gradient to constrain the reference boundary localization. In motion correlation fusion, we discover that the frame-based motion possesses spatially dense but temporally discontinuous correlation, while the event-based motion has spatially sparse but temporally continuous correlation. This inspires us to use the reference boundary to guide the complementary motion knowledge fusion between the two modalities. Moreover, common spatiotemporal fusion can not only relieve the cross-modal feature discrepancy, but also make the fusion process interpretable for dense and continuous optical flow. Extensive experiments have been performed to verify the superiority of the proposed method."
status: "auto-generated; brief scan note"
---
## Core Problem

High-dynamic scene optical flow is a challenging task, which suffers spatial blur and
temporal discontinuous motion due to large displacement in frame imaging, thus deteriorating
the spatiotemporal feature of optical flow.

## Core Method

Typically, existing methods mainly introduce event camera to directly fuse the
spatiotemporal features between the two modalities.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-
stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official CVF page inspected
under broad high-recall title workflow.。
