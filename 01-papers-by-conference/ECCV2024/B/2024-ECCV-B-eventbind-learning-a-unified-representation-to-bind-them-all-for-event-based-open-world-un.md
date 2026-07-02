---
title: "EventBind: Learning a Unified Representation to Bind Them All for Event-based Open-world Understanding"
authors: ["jiazhou zhou", "Xu Zheng", "Yuanhuiyi Lyu", "LIN WANG"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08931.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1119"
tags: []
abstract: "In this paper, we propose EventBind, a novel and effective framework that unleashes the potential of vision-language models (VLMs) for event-based recognition to compensate for the lack of large-scale event-based datasets. In particular, due to the distinct modality gap with the image-text data and the lack of large-scale datasets, learning a common representation space for images, texts, and events is non-trivial. Intuitively, we need to address two key challenges: 1) how to generalize CLIP's visual encoder to event data while fully leveraging events' unique properties, e.g., sparsity and high temporal resolution; 2) how to effectively align the multi-modal embeddings, i.e., image, text, and events. Accordingly, we first introduce a novel event encoder that subtly models the temporal information from events and meanwhile generates event prompts for modality bridging. We then design a text encoder that generates content prompts and utilizes hybrid text prompts to enhance EventBind's generalization ability across diverse datasets. With the proposed event encoder, text encoder, and image encoder, a novel Hierarchical Triple Contrastive Alignment (HTCA}) module is introduced to jointly optimize the correlation and enable efficient knowledge transfer among the three modalities. We evaluate various settings, including fine-tuning and few-shot on three benchmarks and our EventBind achieves new state-of-art accuracy compared with the previous methods, such as N-Caltech101 (+5.34% and +1.70%) and N-Imagenet (+5.65% and +1.99%) with fine-tuning and 20-shot settings respectively. Moreover, our EventBind can be flexibly extended to the event retrieval task using text or image queries, showing plausible performance. Our project code will be made publicly available."
status: "auto-generated; brief scan note"
---
## Core Problem

In this paper, we propose EventBind, a novel and effective framework that unleashes the
potential of vision-language models (VLMs) for event-based recognition to compensate for the
lack of large-scale event-based datasets.

## Core Method

In particular, due to the distinct modality gap with the image-text data and the lack of
large-scale datasets, learning a common representation space for images, texts, and events
is non-trivial.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event data。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
