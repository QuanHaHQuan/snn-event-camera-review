---
title: "EventGPT: Event Stream Understanding with Multimodal Large Language Models"
authors: ["Shaoyu Liu", "Jianing Li", "Guanghui Zhao", "Yunjian Zhang", "Xin Meng", "Fei Richard Yu", "Xiangyang Ji", "Ming Li"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_EventGPT_Event_Stream_Understanding_with_Multimodal_Large_Language_Models_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Liu_EventGPT_Event_Stream_Understanding_with_Multimodal_Large_Language_Models_CVPR_2025_paper.html"
tags: []
abstract: "Event cameras capture visual information as asynchronous pixel change streams, excelling in challenging lighting and high-dynamic scenarios. Existing multimodal large language models (MLLMs) concentrate on natural RGB images, failing in scenarios where event data fits better. In this paper, we introduce EventGPT, the first MLLM for event stream understanding, pioneering the integration of large language models (LLMs) with event-based vision. To bridge the huge domain gap, we propose a three-stage optimization paradigm to progressively equip a pre-trained LLM with event understanding. Our EventGPT consists of an event encoder, a spatio-temporal aggregator, a linear projector, an event-language adapter, and an LLM. Firstly, GPT-generated RGB image-text pairs warm up the linear projector, following LLaVA, as the gap between natural images and language is smaller. Secondly, we construct N-ImageNet-Chat, a large synthetic dataset of event data and corresponding texts to enable the use of the spatio-temporal aggregator and to train the event-language adapter, thereby aligning event features more closely with the language space. Finally, we gather an instruction dataset, Event-Chat, which contains extensive real-world data to fine-tune the entire model, further enhancing its generalization ability. We construct a comprehensive benchmark, and experiments show that EventGPT surpasses previous state-of-the-art MLLMs in generation quality, descriptive accuracy, and reasoning capability."
status: "auto-generated; brief scan note"
---
## Core Problem

Event cameras capture visual information as asynchronous pixel change streams, excelling in
challenging lighting and high-dynamic scenarios.

## Core Method

Existing multimodal large language models (MLLMs) concentrate on natural RGB images, failing
in scenarios where event data fits better.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event stream; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official
CVF page inspected under broad high-recall title workflow.。
