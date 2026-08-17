---
title: "Dense Metric Depth Estimation via Event-based Differential Focus Volume Prompting"
authors: ["Boyu Li", "Peiqi Duan", "Zhaojun Huang", "Xinyu Zhou", "Yifei Xia", "Boxin Shi"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/0d9057d84a9fc37523bf826232ea6820-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/0d9057d84a9fc37523bf826232ea6820-Abstract-Conference.html"
tags: []
abstract: "Dense metric depth estimation has witnessed great developments in recent years. While single-image-based methods have demonstrated commendable performance in certain circumstances, they may encounter challenges regarding scale ambiguities and visual illusions in real world. Traditional depth-from-focus methods are constrained by low sampling rates during data acquisition. In this paper, we introduce a novel approach to enhance dense metric depth estimation by fusing events with image foundation models via a prompting approach. Specifically, we build Event-based Differential Focus Volumes (EDFV) using events triggered through focus sweeping, which are subsequently transformed into sparse metric depth maps. These maps are then utilized for prompting dense depth estimation via our proposed Event-based Depth Prompting Network. We further construct synthetic and real-captured datasets to facilitate the training and evaluation of both frame-based and event-based methods. Quantitative and qualitative results, including both in-domain and zero-shot experiments, demonstrate the superior performance of our method compared to existing approaches. Code and data will be available at https://github.com/liboyu02/EDFV/."
status: "official-abstract screening card"
---

## Official Abstract

Dense metric depth estimation has witnessed great developments in recent years. While single-image-based methods have demonstrated commendable performance in certain circumstances, they may encounter challenges regarding scale ambiguities and visual illusions in real world. Traditional depth-from-focus methods are constrained by low sampling rates during data acquisition. In this paper, we introduce a novel approach to enhance dense metric depth estimation by fusing events with image foundation models via a prompting approach. Specifically, we build Event-based Differential Focus Volumes (EDFV) using events triggered through focus sweeping, which are subsequently transformed into sparse metric depth maps. These maps are then utilized for prompting dense depth estimation via our proposed Event-based Depth Prompting Network. We further construct synthetic and real-captured datasets to facilitate the training and evaluation of both frame-based and event-based methods. Quantitative and qualitative results, including both in-domain and zero-shot experiments, demonstrate the superior performance of our method compared to existing approaches. Code and data will be available at https://github.com/liboyu02/EDFV/.

## Survey Role

The paper builds event-based differential focus volumes and event-derived sparse metric-depth prompts. It is non-spiking event-side depth and dataset background outside Core.

## Advisor Role

Event-based depth prompting is an adjacent task/evaluation idea, not a direct SECNet, frequency, or SNN mechanism.

## Verification Boundary

This card records official-title/abstract screening evidence. Verify the PDF before citing implementation details, formulas, tables, or numerical claims.
