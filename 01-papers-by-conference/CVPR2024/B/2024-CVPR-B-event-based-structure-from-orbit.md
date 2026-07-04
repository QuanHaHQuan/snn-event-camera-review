---
title: "Event-based Structure-from-Orbit"
authors: ["Ethan Elms", "Yasir Latif", "Tae Ha Park", "Tat-Jun Chin"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Elms_Event-based_Structure-from-Orbit_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Elms_Event-based_Structure-from-Orbit_CVPR_2024_paper.html"
tags: []
abstract: "Event sensors offer high temporal resolution visual sensing which makes them ideal for perceiving fast visual phenomena without suffering from motion blur. Certain applications in robotics and vision-based navigation require 3D perception of an object undergoing circular or spinning motion in front of a static camera such as recovering the angular velocity and shape of the object. The setting is equivalent to observing a static object with an orbiting camera. In this paper we propose event-based structure-from-orbit (eSfO) where the aim is to simultaneously reconstruct the 3D structure of a fast spinning object observed from a static event camera and recover the equivalent orbital motion of the camera. Our contributions are threefold: since state-of-the-art event feature trackers cannot handle periodic self-occlusion due to the spinning motion we develop a novel event feature tracker based on spatio-temporal clustering and data association that can better track the helical trajectories of valid features in the event data. The feature tracks are then fed to our novel factor graph-based structure-from-orbit back-end that calculates the orbital motion parameters (e.g. spin rate relative rotational axis) that minimize the reprojection error. For evaluation we produce a new event dataset of objects under spinning motion. Comparisons against ground truth indicate the efficacy of eSfO."
status: "auto-generated; brief scan note"
---
## Core Problem

Event sensors offer high temporal resolution visual sensing which makes them ideal for
perceiving fast visual phenomena without suffering from motion blur.

## Core Method

Certain applications in robotics and vision-based navigation require 3D perception of an
object undergoing circular or spinning motion in front of a static camera such as recovering
the angular velocity and shape of the object.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
