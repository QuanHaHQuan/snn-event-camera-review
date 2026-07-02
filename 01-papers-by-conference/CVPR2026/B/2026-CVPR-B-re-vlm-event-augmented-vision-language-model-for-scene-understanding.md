---
title: "RE-VLM: Event-Augmented Vision-Language Model for Scene Understanding"
authors: ["Hanqing Liu", "Mingjie Liu", "Luoping Cui", "Endian Lin", "Donghong Jiang", "Chuang Zhu"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_RE-VLM_Event-Augmented_Vision-Language_Model_for_Scene_Understanding_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Liu_RE-VLM_Event-Augmented_Vision-Language_Model_for_Scene_Understanding_CVPR_2026_paper.html"
tags: []
abstract: "Conventional vision-language models (VLMs) struggle to interpret scenes captured under adverse conditions (e.g., low light, high dynamic range, or fast motion) because standard RGB images degrade in such environments. Event cameras provide a complementary modality: they asynchronously record per-pixel brightness changes with high temporal resolution and wide dynamic range, preserving motion cues where frames fail. We propose RE-VLM, the first dual-stream vision-language model that jointly leverages RGB images and event streams for robust scene understanding across both normal and challenging conditions. RE-VLM employs parallel RGB and event encoders together with a progressive training strategy that aligns heterogeneous visual features with language. To address the scarcity of RGB-Event-Text supervision, we further propose a graph-driven pipeline that converts synchronized RGB-Event streams into verifiable scene graphs, from which we synthesize captions and question-answer (QA) pairs. To develop and evaluate RE-VLM, we construct two datasets: PEOD-Chat, targeting illumination-challenged scenes, and RGBE-Chat, covering diverse scenarios. On captioning and VQA benchmarks, RE-VLM consistently outperforms state-of-the-art RGB-only and event-only models with comparable parameter counts, with particularly large gains under challenging conditions. These results demonstrate the effectiveness of event-augmented VLMs in achieving robust vision-language understanding across a wide range of real-world environments. Code and datasets are available at https://github.com/bupt-ai-cz/RE-VLM."
status: "auto-generated; brief scan note"
---
## Core Problem

Conventional vision-language models (VLMs) struggle to interpret scenes captured under
adverse conditions (e.g., low light, high dynamic range, or fast motion) because standard
RGB images degrade in such environments.

## Core Method

Event cameras provide a complementary modality: they asynchronously record per-pixel
brightness changes with high temporal resolution and wide dynamic range, preserving motion
cues where frames fail.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event stream; rgb-event。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
