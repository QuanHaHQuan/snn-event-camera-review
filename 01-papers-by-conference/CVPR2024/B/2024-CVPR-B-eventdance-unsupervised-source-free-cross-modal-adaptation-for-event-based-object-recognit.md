---
title: "EventDance: Unsupervised Source-free Cross-modal Adaptation for Event-based Object Recognition"
authors: ["Xu Zheng", "Lin Wang"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Zheng_EventDance_Unsupervised_Source-free_Cross-modal_Adaptation_for_Event-based_Object_Recognition_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Zheng_EventDance_Unsupervised_Source-free_Cross-modal_Adaptation_for_Event-based_Object_Recognition_CVPR_2024_paper.html"
tags: []
abstract: "In this paper we make the first attempt at achieving the cross-modal (i.e. image-to-events) adaptation for event-based object recognition without accessing any labeled source image data owning to privacy and commercial issues. Tackling this novel problem is non-trivial due to the novelty of event cameras and the distinct modality gap between images and events. In particular as only the source model is available a hurdle is how to extract the knowledge from the source model by only using the unlabeled target event data while achieving knowledge transfer. To this end we propose a novel framework dubbed EventDance for this unsupervised source-free cross-modal adaptation problem. Importantly inspired by event-to-video reconstruction methods we propose a reconstruction-based modality bridging (RMB) module which reconstructs intensity frames from events in a self-supervised manner. This makes it possible to build up the surrogate images to extract the knowledge (i.e. labels) from the source model. We then propose a multi-representation knowledge adaptation (MKA) module that transfers the knowledge to target models learning events with multiple representation types for fully exploring the spatiotemporal information of events. The two modules connecting the source and target models are mutually updated so as to achieve the best performance. Experiments on three benchmark datasets with two adaption settings show that EventDance is on par with prior methods utilizing the source data."
status: "auto-generated; brief scan note"
---
## Core Problem

In this paper we make the first attempt at achieving the cross-modal (i.e.

## Core Method

image-to-events) adaptation for event-based object recognition without accessing any labeled
source image data owning to privacy and commercial issues.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
