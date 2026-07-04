---
title: "Event Stream-based Visual Object Tracking: A High-Resolution Benchmark Dataset and A Novel Baseline"
authors: ["Xiao Wang", "Shiao Wang", "Chuanming Tang", "Lin Zhu", "Bo Jiang", "Yonghong Tian", "Jin Tang"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_Event_Stream-based_Visual_Object_Tracking_A_High-Resolution_Benchmark_Dataset_and_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Event_Stream-based_Visual_Object_Tracking_A_High-Resolution_Benchmark_Dataset_and_CVPR_2024_paper.html"
tags: []
abstract: "Tracking with bio-inspired event cameras has garnered increasing interest in recent years. Existing works either utilize aligned RGB and event data for accurate tracking or directly learn an event-based tracker. The former incurs higher inference costs while the latter may be susceptible to the impact of noisy events or sparse spatial resolution. In this paper we propose a novel hierarchical knowledge distillation framework that can fully utilize multi-modal / multi-view information during training to facilitate knowledge transfer enabling us to achieve high-speed and low-latency visual tracking during testing by using only event signals. Specifically a teacher Transformer-based multi-modal tracking framework is first trained by feeding the RGB frame and event stream simultaneously. Then we design a new hierarchical knowledge distillation strategy which includes pairwise similarity feature representation and response maps-based knowledge distillation to guide the learning of the student Transformer network. In particular since existing event-based tracking datasets are all low-resolution (346 * 260) we propose the first large-scale high-resolution (1280 * 720) dataset named EventVOT. It contains 1141 videos and covers a wide range of categories such as pedestrians vehicles UAVs ping pong etc. Extensive experiments on both low-resolution (FE240hz VisEvent COESOT) and our newly proposed high-resolution EventVOT dataset fully validated the effectiveness of our proposed method. The dataset evaluation toolkit and source code will be released."
status: "auto-generated; brief scan note"
---
## Core Problem

Tracking with bio-inspired event cameras has garnered increasing interest in recent years.

## Core Method

Existing works either utilize aligned RGB and event data for accurate tracking or directly
learn an event-based tracker.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event stream; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
