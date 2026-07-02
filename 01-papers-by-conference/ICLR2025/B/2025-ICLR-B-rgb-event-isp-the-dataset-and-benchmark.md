---
title: "RGB-Event ISP: The Dataset and Benchmark"
authors: ["Yunfan LU", "Yanlin Qian", "Ziyang Rao", "Junren Xiao", "Liming Chen", "Hui Xiong"]
conference: "ICLR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2025/file/2a25d9d873e9ae6d242c62e36f89ee3a-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/2a25d9d873e9ae6d242c62e36f89ee3a-Abstract-Conference.html"
tags: []
abstract: "Event-guided imaging has received significant attention due to its potential to revolutionize instant imaging systems. However, the prior methods primarily focus on enhancing RGB images in a post-processing manner, neglecting the challenges of image signal processor (ISP) dealing with event sensor and the benefits events provide for reforming the ISP process. To achieve this, we conduct the first research on event-guided ISP. First, we present a new event-RAW paired dataset, collected with a novel but still confidential sensor that records pixel-level aligned events and RAW images. This dataset includes 3373 RAW images with $2248\\times 3264$ resolution and their corresponding events, spanning 24 scenes with 3 exposure modes and 3 lenses. Second, we propose a convential ISP pipeline to generate good RGB frames as reference. This convential ISP pipleline performs basic ISP operations, e.g., demosaicing, white balancing, denoising and color space transforming, with a ColorChecker as reference. Third, we classify the existing learnable ISP methods into 3 classes, and select multiple methods to train and evaluate on our new dataset. Lastly, since there is no prior work for reference, we propose a simple event-guided ISP method and test it on our dataset. We further put forward key technical challenges and future directions in RGB-Event ISP. In summary, to the best of our knowledge, this is the very first research focusing on event-guided ISP, and we hope it will inspire the community."
status: "auto-generated; brief scan note"
---

## Core Problem

Event-guided imaging has received significant attention due to its potential to revolutionize instant imaging systems.

## Core Method

However, the prior methods primarily focus on enhancing RGB images in a post-processing manner, neglecting the challenges of image signal processor (ISP) dealing with event sensor and the benefits events provide for reforming the ISP process.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
