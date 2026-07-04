---
title: "EvTexture: Event-driven Texture Enhancement for Video Super-Resolution"
authors: ["Dachun Kai, Jiayao Lu, Yueyi Zhang, Xiaoyan Sun"]
conference: "ICML"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kai24a/kai24a.pdf"
official_page: "https://proceedings.mlr.press/v235/kai24a.html"
tags: []
abstract: "Event-based vision has drawn increasing attention due to its unique characteristics, such as high temporal resolution and high dynamic range. It has been used in video super-resolution (VSR) recently to enhance the flow estimation and temporal alignment. Rather than for motion learning, we propose in this paper the first VSR method that utilizes event signals for texture enhancement. Our method, called EvTexture, leverages high-frequency details of events to better recover texture regions in VSR. In our EvTexture, a new texture enhancement branch is presented. We further introduce an iterative texture enhancement module to progressively explore the high-temporal-resolution event information for texture restoration. This allows for gradual refinement of texture regions across multiple iterations, leading to more accurate and rich high-resolution details. Experimental results show that our EvTexture achieves state-of-the-art performance on four datasets. For the Vid4 dataset with rich textures, our method can get up to 4.67dB gain compared with recent event-based methods. Code: https://github.com/DachunKai/EvTexture."
status: "auto-generated; brief scan note"
---
## Core Problem

Event-based vision has drawn increasing attention due to its unique characteristics, such as
high temporal resolution and high dynamic range.

## Core Method

It has been used in video super-resolution (VSR) recently to enhance the flow estimation and
temporal alignment.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-driven。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：strict two-stage
screening; official abstract/page inspected; main conference; needs human verification。
