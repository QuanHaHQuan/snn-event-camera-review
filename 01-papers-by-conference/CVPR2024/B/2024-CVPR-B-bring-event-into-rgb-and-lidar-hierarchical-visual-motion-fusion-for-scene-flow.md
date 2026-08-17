---
title: "Bring Event into RGB and LiDAR: Hierarchical Visual-Motion Fusion for Scene Flow"
authors: ["Hanyu Zhou", "Yi Chang", "Zhiwei Shi"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Zhou_Bring_Event_into_RGB_and_LiDAR_Hierarchical_Visual-Motion_Fusion_for_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_Bring_Event_into_RGB_and_LiDAR_Hierarchical_Visual-Motion_Fusion_for_CVPR_2024_paper.html"
tags: []
abstract: "Single RGB or LiDAR is the mainstream sensor for the challenging scene flow which relies heavily on visual features to match motion features. Compared with single modality existing methods adopt a fusion strategy to directly fuse the cross-modal complementary knowledge in motion space. However these direct fusion methods may suffer the modality gap due to the visual intrinsic heterogeneous nature between RGB and LiDAR thus deteriorating motion features. We discover that event has the homogeneous nature with RGB and LiDAR in both visual and motion spaces. In this work we bring the event as a bridge between RGB and LiDAR and propose a novel hierarchical visual-motion fusion framework for scene flow which explores a homogeneous space to fuse the cross-modal complementary knowledge for physical interpretation. In visual fusion we discover that event has a complementarity (relative v.s. absolute) in luminance space with RGB for high dynamic imaging and has a complementarity (local boundary v.s. global shape) in scene structure space with LiDAR for structure integrity. In motion fusion we figure out that RGB event and LiDAR are complementary (spatial-dense temporal-dense v.s. spatiotemporal-sparse) to each other in correlation space which motivates us to fuse their motion correlations for motion continuity. The proposed hierarchical fusion can explicitly fuse the multimodal knowledge to progressively improve scene flow from visual space to motion space. Extensive experiments have been performed to verify the superiority of the proposed method."
status: "official-abstract screening card"
---

## Official Abstract

Single RGB or LiDAR is the mainstream sensor for the challenging scene flow which relies heavily on visual features to match motion features. Compared with single modality existing methods adopt a fusion strategy to directly fuse the cross-modal complementary knowledge in motion space. However these direct fusion methods may suffer the modality gap due to the visual intrinsic heterogeneous nature between RGB and LiDAR thus deteriorating motion features. We discover that event has the homogeneous nature with RGB and LiDAR in both visual and motion spaces. In this work we bring the event as a bridge between RGB and LiDAR and propose a novel hierarchical visual-motion fusion framework for scene flow which explores a homogeneous space to fuse the cross-modal complementary knowledge for physical interpretation. In visual fusion we discover that event has a complementarity (relative v.s. absolute) in luminance space with RGB for high dynamic imaging and has a complementarity (local boundary v.s. global shape) in scene structure space with LiDAR for structure integrity. In motion fusion we figure out that RGB event and LiDAR are complementary (spatial-dense temporal-dense v.s. spatiotemporal-sparse) to each other in correlation space which motivates us to fuse their motion correlations for motion continuity. The proposed hierarchical fusion can explicitly fuse the multimodal knowledge to progressively improve scene flow from visual space to motion space. Extensive experiments have been performed to verify the superiority of the proposed method.

## Survey Role

The official abstract confirms RGB-event-LiDAR fusion for scene flow. It is non-spiking event-side evidence on multimodal representation and motion fusion, suitable as a reference rather than Core reading.

## Advisor Role

Event-mediated RGB-LiDAR fusion is an adjacent downstream comparator, not an Event Cloud or Fourier/SNN mechanism for the SECNet extension.

## Verification Boundary

This card records official-title/abstract screening evidence. Verify the PDF before citing implementation details, formulas, tables, or numerical claims.
