---
title: "Low-Light Image Enhancement Using Event-Based Illumination Estimation"
authors: ["Lei Sun", "Yuhan Bao", "Jiajun Zhai", "Jingyun Liang", "Yulun Zhang", "Kaiwei Wang", "Danda Pani Paudel", "Luc Van Gool"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Sun_Low-Light_Image_Enhancement_Using_Event-Based_Illumination_Estimation_ICCV_2025_paper.html"
tags: []
abstract: "Low-light image enhancement (LLIE) aims to improve the visibility of images captured in poorly lit environments. Prevalent event-based solutions primarily utilize events triggered by motion, i.e., \"motion events\" to strengthen only the edge texture, while leaving the high dynamic range and excellent low-light responsiveness of event cameras largely unexplored. This paper instead opens a new avenue from the perspective of estimating the illumination using \"temporal-mapping\" events, i.e., by converting the timestamps of events triggered by a transmittance modulation into brightness values. The resulting fine-grained illumination cues facilitate a more effective decomposition and enhancement of the reflectance component in low-light images through the proposed Illumination-aided Reflectance Enhancement module. Furthermore, the degradation model of temporal-mapping events under low-light condition is investigated for realistic training data synthesis. To address the lack of datasets under this regime, we construct a beam-splitter setup and collect EvLowLight dataset that includes images, temporal-mapping events, and motion events. Extensive experiments across 5 synthetic datasets and our real-world EvLowLight dataset substantiate that the devised pipeline, dubbed RetinEV, excels in producing well-illuminated, high dynamic range images, outperforming previous state-of-the-art event-based methods by up to 6.62 dB, while maintaining an efficient inference speed of 35.6 frames per second on a 640x480 image. Codes and datasets: https://github.com/AHupuJR/RetinEV."
status: "auto-generated; brief scan note"
---

## Core Problem

Low-light image enhancement (LLIE) aims to improve the visibility of images captured in poorly lit environments.

## Core Method

Prevalent event-based solutions primarily utilize events triggered by motion, i.e., "motion events" to strengthen only the edge texture, while leaving the high dynamic range and excellent low-light responsiveness of event cameras largely unexplored.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
