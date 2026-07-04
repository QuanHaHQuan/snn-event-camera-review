---
title: "S2D-LFE: Sparse-to-Dense Light Field Event Generation"
authors: ["Yutong Liu", "Wenming Weng", "Yueyi Zhang", "Zhiwei Xiong"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_S2D-LFE_Sparse-to-Dense_Light_Field_Event_Generation_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Liu_S2D-LFE_Sparse-to-Dense_Light_Field_Event_Generation_CVPR_2025_paper.html"
tags: []
abstract: "In this paper, we present S2D-LFE, an innovative approach for sparse-to-dense light field event generation. For the first time to our knowledge, S2D-LFE enables controllable novel view synthesis only from sparse-view light field event (LFE) data, and addresses three critical challenges for the LFE generation task: simplicity, controllability, and consistency. The simplicity aspect eliminates the dependency on frame-based modality, which often suffers from motion blur and low frame-rate limitations. The controllability aspect enables precise view synthesis under sparse LFE conditions with view-related constraints. The consistency aspect ensures both cross-view and temporal coherence in the generated results. To realize S2D-LFE, we develop a novel diffusion-based generation network with two key components. First, we design an LFE-customized variational auto-encoder that effectively compresses and reconstructs LFE by integrating cross-view information. Second, we design an LFE-aware injection adaptor to extract comprehensive geometric and texture priors. Furthermore, we construct a large-scale synthetic LFE dataset containing 162 one-minute sequences using simulator, and capture a real-world testset using our custom-built sparse LFE acquisition system, covering diverse indoor and outdoor scenes. Extensive experiments demonstrate that S2D-LFE successfully generates up to 9x9 dense LFE from sparse 2x2 inputs and outperforms existing methods on both synthetic and real-world data. The datasets and code are available at https://github.com/Yutong2022/S2D-LFE."
status: "auto-generated; brief scan note"
---
## Core Problem

In this paper, we present S2D-LFE, an innovative approach for sparse-to-dense light field
event generation.

## Core Method

For the first time to our knowledge, S2D-LFE enables controllable novel view synthesis only
from sparse-view light field event (LFE) data, and addresses three critical challenges for
the LFE generation task: simplicity, controllability, and consistency.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event。自动分类理由：Manual boundary check: official abstract confirms sparse-to-dense
light-field event data and a real-world light-field event acquisition system.。 备注：CVPR 2025
official CVF page inspected under broad high-recall title workflow. Needs human verification
for event-stream wording.。
