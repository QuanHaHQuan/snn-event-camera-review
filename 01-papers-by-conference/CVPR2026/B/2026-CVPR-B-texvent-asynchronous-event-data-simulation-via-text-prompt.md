---
title: "Texvent: Asynchronous Event Data Simulation via Text Prompt"
authors: ["Ruofei Wang", "Peiqi Duan", "Ka Chun Cheung", "Simon See", "Boxin Shi", "Renjie Wan"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Texvent_Asynchronous_Event_Data_Simulation_via_Text_Prompt_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Texvent_Asynchronous_Event_Data_Simulation_via_Text_Prompt_CVPR_2026_paper.html"
tags: []
abstract: "Current event simulation methods focus on employing videos to synthesize new event data, suffering from costly video capture and limited scalability across viewpoints, motions, and lighting. To this end, we propose a Text-to-event simulation framework (Texvent) that can directly generate asynchronous event data from simple text prompts. Texvent first renders prompt-driven videos via multimodal large language models and subsequently applies a new physical simulator to generate event streams. Specifically, an adaptive brightness-aware frame interpolation approach is proposed to enhance the temporal resolution of the rendered videos. A balanced logarithmic intensity comparison strategy and a cache-based voltage refreshment mechanism are introduced into the simulator to generate event data.To narrow the sim-to-real gap, we also introduce background activity noise injection and dense time stamp reconstruction operations. Extensive experiments demonstrate Texvent's superior computational efficiency and its ability to generate more realistic event data than existing simulators."
status: "official-abstract screening card"
---

## Official Abstract

Current event simulation methods focus on employing videos to synthesize new event data, suffering from costly video capture and limited scalability across viewpoints, motions, and lighting. To this end, we propose a Text-to-event simulation framework (Texvent) that can directly generate asynchronous event data from simple text prompts. Texvent first renders prompt-driven videos via multimodal large language models and subsequently applies a new physical simulator to generate event streams. Specifically, an adaptive brightness-aware frame interpolation approach is proposed to enhance the temporal resolution of the rendered videos. A balanced logarithmic intensity comparison strategy and a cache-based voltage refreshment mechanism are introduced into the simulator to generate event data.To narrow the sim-to-real gap, we also introduce background activity noise injection and dense time stamp reconstruction operations. Extensive experiments demonstrate Texvent's superior computational efficiency and its ability to generate more realistic event data than existing simulators.

## Survey Role

Texvent generates asynchronous event-camera streams from text-rendered videos with a physical simulator and noise modeling. It is useful event-data simulation background without SNN computation.

## Advisor Role

Scalable synthetic event data could support evaluation or pretraining for an extension, but Texvent is not a SECNet/Fourier/SNN method-chain paper.

## Verification Boundary

This card records official-title/abstract screening evidence. Verify the PDF before citing implementation details, formulas, tables, or numerical claims.
