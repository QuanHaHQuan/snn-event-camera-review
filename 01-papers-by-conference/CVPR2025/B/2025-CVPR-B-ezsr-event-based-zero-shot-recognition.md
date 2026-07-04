---
title: "EZSR: Event-based Zero-Shot Recognition"
authors: ["Yan Yang", "Liyuan Pan", "Dongxu Li", "Liu Liu"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_EZSR_Event-based_Zero-Shot_Recognition_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Yang_EZSR_Event-based_Zero-Shot_Recognition_CVPR_2025_paper.html"
tags: []
abstract: "This paper studies zero-shot object recognition using event camera data. Guided by CLIP, which is pre-trained on RGB images, existing approaches achieve zero-shot object recognition by optimizing embedding similarities between event data and RGB images respectively encoded by an event encoder and the CLIP image encoder. Alternatively, several methods learn RGB frame reconstructions from event data for the CLIP image encoder. However, they often result in suboptimal zero-shot performance. This study develops an event encoder without relying on additional reconstruction networks. We theoretically analyze the performance bottlenecks of previous approaches: the embedding optimization objectives are prone to suffer from the spatial sparsity of event data, causing semantic misalignments between the learned event embedding space and the CLIP text embedding space. To mitigate the issue, we explore a scalar-wise modulation strategy. Furthermore, to scale up the number of events and RGB data pairs for training, we also study a pipeline for synthesizing event data from static RGB images in mass. Experimentally, we demonstrate an attractive scaling property in the number of parameters and synthesized data. We achieve superior zero-shot object recognition performance on extensive standard benchmark datasets, even compared with past supervised learning approaches. For example, our model with a ViT/B-16 backbone achieves 47.84% zero-shot accuracy on the N-ImageNet dataset."
status: "auto-generated; brief scan note"
---
## Core Problem

This paper studies zero-shot object recognition using event camera data.

## Core Method

Guided by CLIP, which is pre-trained on RGB images, existing approaches achieve zero-shot
object recognition by optimizing embedding similarities between event data and RGB images
respectively encoded by an event encoder and the CLIP image encoder.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official
CVF page inspected under broad high-recall title workflow.。
