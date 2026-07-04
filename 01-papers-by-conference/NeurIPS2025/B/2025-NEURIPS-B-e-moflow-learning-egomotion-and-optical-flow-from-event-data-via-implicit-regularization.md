---
title: "E-MoFlow: Learning Egomotion and Optical Flow from Event Data via Implicit Regularization"
authors: ["Wenpu Li, Bangyan Liao, Yi Zhou, QiXu, Pian Wan, Peidong Liu"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/2b7539f0892fdb0e096a2b718c6890f9-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/2b7539f0892fdb0e096a2b718c6890f9-Abstract-Conference.html"
tags: []
abstract: "The estimation of optical flow and 6-DoF ego-motion—two fundamental tasks in 3-D vision—has typically been addressed independently. For neuromorphic vision (e.g., event cameras), however, the lack of robust data association makes solving the two problems separately an ill-posed challenge, especially in the absence of supervision via ground truth. Existing works mitigate this ill-posedness by either enforcing the smoothness of the flow field via an explicit variational regularizer or leveraging explicit structure-and-motion priors in the parametrization to improve event alignment. The former notably introduces bias in results and computational overhead, while the latter—which parametrizes the optical flow in terms of the scene depth and the camera motion—often converges to suboptimal local minima. To address these issues, we propose an unsupervised pipeline that jointly optimizes egomotion and flow via implicit spatial-temporal and geometric regularization. First, by modeling camera's egomotion as a continuous spline and optical flow as an implicit neural representation, our method inherently embeds spatial-temporal coherence through inductive biases. Second, we incorporate structure-and-motion priors through differential geometric constraints, bypassing explicit depth estimation while maintaining rigorous geometric consistency. As a result, our framework (called \\textbf{E-MoFlow}) unifies egomotion and optical flow estimation via implicit regularization under a fully unsupervised paradigm. Experiments demonstrate its versatility to general 6-DoF motion scenarios, achieving state-of-the-art performance among unsupervised methods and competitive even with supervised approaches. Code will be released upon acceptance."
status: "auto-generated; brief scan note"
---
## Core Problem

The estimation of optical flow and 6-DoF ego-motion—two fundamental tasks in 3-D vision—has
typically been addressed independently.

## Core Method

For neuromorphic vision (e.g., event cameras), however, the lack of robust data association
makes solving the two problems separately an ill-posed challenge, especially in the absence
of supervision via ground truth.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event cameras; event camera visual-event context; event cameras visual-event
context。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor
evidence; no clear SNN evidence found.。 备注：strict two-stage rescan; official abstract/page
inspected; needs human verification; Track: Main Conference Track。
