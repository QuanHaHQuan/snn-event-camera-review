---
title: "Event Trojan: Asynchronous Event-based Backdoor Attacks"
authors: ["Ruofei Wang", "Qing Guo", "Haoliang Li", "Renjie Wan"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01155.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/2700"
tags: []
abstract: "This paper has uncovered the possibility of directly poisoning event data streams by proposing Event Trojan framework, including two kinds of triggers, i.e., immutable and mutable triggers. Specifically, our two types of event triggers are based on a sequence of simulated event spikes, which can be easily incorporated into any event stream to initiate backdoor attacks. Additionally, for the mutable trigger, we design an adaptive learning mechanism to maximize its aggressiveness. To improve the stealthiness, we introduce a novel loss function that constrains the generated contents of mutable triggers, minimizing the difference between triggers and original events while maintaining effectiveness. Extensive experiments on public event datasets show the effectiveness of the proposed backdoor triggers. We hope that this paper can draw greater attention to the potential threats posed by backdoor attacks on event-based tasks."
status: "auto-generated; brief scan note"
---

## Core Problem

This paper has uncovered the possibility of directly poisoning event data streams by proposing Event Trojan framework, including two kinds of triggers, i.e., immutable and mutable triggers.

## Core Method

Specifically, our two types of event triggers are based on a sequence of simulated event spikes, which can be easily incorporated into any event stream to initiate backdoor attacks.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event dataset visual-event context; event datasets visual-event context; event stream with event-camera context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
