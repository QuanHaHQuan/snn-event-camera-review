---
title: "Event-based Motion Deblurring with Unpaired Data"
authors: ["Hoonhee Cho", "Yuhwan Jeong", "Kuk-Jin Yoon"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Cho_Event-based_Motion_Deblurring_with_Unpaired_Data_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Cho_Event-based_Motion_Deblurring_with_Unpaired_Data_CVPR_2026_paper.html"
tags: ["event-camera", "advisor-frequency", "fourier"]
abstract: "Event cameras provide high-temporal-resolution, motion-centric measurements that remain reliable under fast motion and challenging illumination, making them a promising sensing modality for motion deblurring. However, existing deblurring methods typically require large-scale paired blur--sharp datasets, which are extremely difficult to obtain in real-world settings, especially when an additional modality such as events is involved. In this work, we introduce EMP, an event-based motion deblurring framework that operates entirely in an unpaired setting, removing the need for aligned blur--sharp supervision. EMP bridges the disjoint blur and sharp domains through event information and leverages two complementary training mechanisms tailored to the unpaired regime: (1) an event-based physical prior with confidence masking that provides reliable self-supervisory signals for blurry inputs, and (2) a generative blur modeling process that extracts blur-related frequency-domain cues from blur--event pairs and transfers them to sharp images to synthesize realistic blur. Together, these mechanisms enable stable and effective deblurring without paired labels. Extensive experiments on various real event datasets, including REBlur, EventAid, and HighREV, show that EMP outperforms existing unpaired baselines and achieves performance competitive with paired methods."
status: "official abstract reviewed; PDF boundary checked"
---

## Scope

This is a non-spiking event-camera paper. It is not Survey Core evidence.

## Advisor-Frequency Evidence

The blur synthesis path extracts centered blur-event log-magnitude spectra, predicts spatial/channel modulation, scales sharp-feature magnitude while preserving normalized phase, and returns through centered iFFT.

## Classification Boundary

Retained as an Advisor-frequency reference. This card is screening provenance, not a Summary V1/V2.
