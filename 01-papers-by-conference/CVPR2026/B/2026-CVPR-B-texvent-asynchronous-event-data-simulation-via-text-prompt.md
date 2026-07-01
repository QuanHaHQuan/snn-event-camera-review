---
title: 'Texvent: Asynchronous Event Data Simulation via Text Prompt'
authors: ['Ruofei Wang', 'Peiqi Duan', 'Ka Chun Cheung', 'Simon See', 'Boxin Shi', 'Renjie Wan']
conference: 'CVPR'
year: 2026
level: 'B'
category: 'Event Camera'
pdf_link: 'https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Texvent_Asynchronous_Event_Data_Simulation_via_Text_Prompt_CVPR_2026_paper.pdf'
official_page: 'https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Texvent_Asynchronous_Event_Data_Simulation_via_Text_Prompt_CVPR_2026_paper.html'
tags: []
abstract: "Current event simulation methods focus on employing videos to synthesize new event data, suffering from costly video capture and limited scalability across viewpoints, motions, and lighting. To this end, we propose a Text-to-event simulation framework (Texvent) that can directly generate asynchronous event data from simple text prompts. Texvent first renders prompt-driven videos via multimodal large language models and subsequently applies a new physical simulator to generate event streams. Specifically, an adaptive brightness-aware frame interpolation approach is proposed to enhance the temporal resolution of the rendered videos. A balanced logarithmic intensity comparison strategy and a cache-based voltage refreshment mechanism are introduced into the simulator to generate event data.To narrow the sim-to-real gap, we also introduce background activity noise injection and dense time stamp reconstruction operations. Extensive experiments demonstrate Texvent's superior computational efficiency and its ability to generate more realistic event data than existing simulators."
status: 'auto-generated; brief scan note'
---

## Core Problem

事件数据模拟通常依赖视频输入，采集成本高，且在视角、运动、光照变化上的可扩展性受限。

## Core Method

Texvent 从文本提示生成视频，再通过物理模拟器转为 event streams；包含亮度感知帧插值、平衡对数强度比较、cache-based voltage refreshment，并加入背景活动噪声和 dense timestamp reconstruction 缩小 sim-to-real gap。

## Key Metrics and Findings

摘要称生成更真实的事件数据且计算效率更高；具体对比模拟器、真实性指标和下游验证需要阅读全文。

## Personal Notes

B 类事件数据生成/仿真论文，适合放在事件相机数据稀缺、合成数据和 benchmark 扩展部分。
