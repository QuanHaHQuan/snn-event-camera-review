---
title: "CMTA: Cross-Modal Temporal Alignment for Event-guided Video Deblurring"
authors: ["Taewoo Kim", "Hoonhee Cho", "KUK-JIN YOON"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06838.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/259"
tags: []
abstract: "Video deblurring aims to enhance the quality of restored results in motion-blurred videos by effectively gathering information from adjacent video frames to compensate for the insufficient data in a single blurred frame. However, when faced with consecutively severe motion blur situations, frame-based video deblurring methods often fail to find accurate temporal correspondence among neighboring video frames, leading to diminished performance. To address this limitation, we aim to solve the video deblurring task by leveraging an event camera with micro-second temporal resolution. To fully exploit the dense temporal resolution of the event camera, we propose two modules: 1) Intra-frame feature enhancement operates within the exposure time of a single blurred frame, iteratively enhancing cross-modality features in a recurrent manner to better utilize the rich temporal information of events, 2) Inter-frame temporal feature alignment gather valuable long-range temporal information to target frames, aggregating sharp features leveraging the advantages of the events. In addition, we present a novel dataset composed of real-world blurred RGB videos, corresponding sharp videos, and event data. This dataset serves as a valuable resource for evaluating event-guided deblurring methods. We demonstrate that our proposed methods outperform state-of-the-art frame-based and event-based motion deblurring methods through extensive experiments conducted on both synthetic and real-world deblurring datasets. The code and dataset will be made publicly available upon acceptance."
status: "auto-generated; brief scan note"
---
## Core Problem

Video deblurring aims to enhance the quality of restored results in motion-blurred videos by
effectively gathering information from adjacent video frames to compensate for the
insufficient data in a single blurred frame.

## Core Method

However, when faced with consecutively severe motion blur situations, frame-based video
deblurring methods often fail to find accurate temporal correspondence among neighboring
video frames, leading to diminished performance.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event data; event-based motion。自动分类理由：Official abstract/page confirms
event-camera/DVS/event-stream evidence; no clear SNN evidence.。
