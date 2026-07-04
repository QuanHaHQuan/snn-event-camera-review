---
title: "Full-DoF Egomotion Estimation for Event Cameras Using Geometric Solvers"
authors: ["Ji Zhao", "Banglei Guan", "Zibin Liu", "Laurent Kneip"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_Full-DoF_Egomotion_Estimation_for_Event_Cameras_Using_Geometric_Solvers_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_Full-DoF_Egomotion_Estimation_for_Event_Cameras_Using_Geometric_Solvers_CVPR_2025_paper.html"
tags: []
abstract: "For event cameras, current sparse geometric solvers for egomotion estimation assume that the rotational displacements are known, such as those provided by an IMU. Thus, they can only recover the translational motion parameters. Recovering full-DoF motion parameters using a sparse geometric solver is a more challenging task, and has not yet been investigated. In this paper, we propose several solvers to estimate both rotational and translational velocities within a unified framework. Our method leverages event manifolds induced by line segments. The problem formulations are based on either an incidence relation for lines or a novel coplanarity relation for normal vectors. We demonstrate the possibility of recovering full-DoF egomotion parameters for both angular and linear velocities without requiring extra sensor measurements or motion priors. To achieve efficient optimization, we exploit the Adam framework with a first-order approximation of rotations for quick initialization. Experiments on both synthetic and real-world data demonstrate the effectiveness of our method. The code is available at https://github.com/jizhaox/relpose-event."
status: "auto-generated; brief scan note"
---
## Core Problem

For event cameras, current sparse geometric solvers for egomotion estimation assume that the
rotational displacements are known, such as those provided by an IMU.

## Core Method

Thus, they can only recover the translational motion parameters.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event cameras; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official
CVF page inspected under broad high-recall title workflow.。
