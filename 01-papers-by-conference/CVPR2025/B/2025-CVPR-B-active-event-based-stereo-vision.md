---
title: "Active Event-based Stereo Vision"
authors: ["Jianing Li", "Yunjian Zhang", "Haiqian Han", "Xiangyang Ji"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Active_Event-based_Stereo_Vision_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Li_Active_Event-based_Stereo_Vision_CVPR_2025_paper.html"
tags: []
abstract: "Conventional frame-based imaging for active stereo systems has encountered major challenges in fast-motion scenarios. However, how to design a novel paradigm for high-speed depth sensing still remains an open issue. In this paper, we propose a novel problem setting, namely active event-based stereo vision, which provides the first insight of integrating binocular event cameras and an infrared projector for high-speed depth sensing. Technically, we first build a stereo camera prototype system and present a real-world dataset with over 21.5k spatiotemporal synchronized labels at 15 Hz, while also creating a realistic synthetic dataset with stereo event streams and 23.8k synchronized labels at 20 Hz. Then, we propose ActiveEventNet, a lightweight yet effective active event-based stereo matching neural network that learns to generate high-quality dense disparity maps from stereo event streams with low latency. Experiments demonstrate that our ActiveEventNet outperforms state-of-the-art methods meanwhile significantly reducing computational complexity. Our solution offers superior depth sensing compared to conventional stereo cameras in high-speed scenes, while also achieving the inference speed of up to 150 FPS with our prototype. We believe that this novel paradigm will provide new insights into future depth sensing systems. Our project can be available at https://github.com/jianing-li/active_event_based_stereo."
status: "auto-generated; brief scan note"
---
## Core Problem

Conventional frame-based imaging for active stereo systems has encountered major challenges
in fast-motion scenarios.

## Core Method

However, how to design a novel paradigm for high-speed depth sensing still remains an open
issue.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official
CVF page inspected under broad high-recall title workflow.。
