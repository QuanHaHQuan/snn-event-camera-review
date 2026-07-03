# Level T Advisor-Direction Reading List

This is a compact reading layer for preparing to extend **Scalable Event Cloud Network for Event-based Classification** (SECNet, ICML 2026 direction). It is parallel to the A/B/C survey labels and should stay small enough to actually read.

T focuses on: Event Cloud / point-based event processing, raw-event representations, scalable and efficient event networks, event-based classification or action recognition, frequency-domain modeling, and the advisor-group method chain.

## How T Relates to A/B/C

T is orthogonal to A/B/C.

- `A + T`: SNN/event-camera intersection and useful for the SECNet direction.
- `B + T`: event-camera-side paper central to SECNet-style raw-event or representation learning.
- `T-only`: important SECNet-related paper outside the currently processed A/B/C venue corpus.

## T0: Read First

These are the most directly useful papers from the current 210-paper corpus.

| Year | Venue | ABC | Title | Why T | Card | Official |
| --- | --- | --- | --- | --- | --- | --- |
| 2025 | ICCV | B | PRE-Mamba: A 4D State Space Model for Ultra-High-Frequent Event Camera Deraining | Explicit Event Cloud / point-based raw-event processing with long-sequence modeling; closest in-corpus neighbor to SECNet's representation direction. | [card](../01-papers-by-conference/ICCV2025/B/2025-ICCV-B-pre-mamba-a-4d-state-space-model-for-ultra-high-frequent-event-camera-deraining.md) | [official](https://openaccess.thecvf.com/content/ICCV2025/html/Ruan_PRE-Mamba_A_4D_State_Space_Model_for_Ultra-High-Frequent_Event_Camera_ICCV_2025_paper.html) |
| 2025 | ICCV | B | Exploiting Frequency Dynamics for Enhanced Multimodal Event-based Action Recognition | Frequency dynamics plus event-based action recognition; close to SECNet's frequency-aware event classification design. | [card](../01-papers-by-conference/ICCV2025/B/2025-ICCV-B-exploiting-frequency-dynamics-for-enhanced-multimodal-event-based-action-recognition.md) | [official](https://openaccess.thecvf.com/content/ICCV2025/html/Cao_Exploiting_Frequency_Dynamics_for_Enhanced_Multimodal_Event-based_Action_Recognition_ICCV_2025_paper.html) |
| 2025 | NeurIPS | B | PASS: Path-selective State Space Model for Event-based Recognition | Event-based recognition with state-space modeling; useful for comparing sequence modeling choices against SECNet. | [card](../01-papers-by-conference/NeurIPS2025/B/2025-NEURIPS-B-pass-path-selective-state-space-model-for-event-based-recognition.md) | [official](https://papers.nips.cc/paper_files/paper/2025/hash/f5dbd98d426772945099ccace06418ba-Abstract-Conference.html) |
| 2025 | ICML | B | A Chaotic Dynamics Framework Inspired by Dorsal Stream for Event Signal Processing | Event signal processing and representation perspective; useful for modeling raw temporal event dynamics. | [card](../01-papers-by-conference/ICML2025/B/2025-ICML-B-a-chaotic-dynamics-framework-inspired-by-dorsal-stream-for-event-signal-processing.md) | [official](https://proceedings.mlr.press/v267/chen25am.html) |
| 2025 | NeurIPS | B | EventMG: Efficient Multilevel Mamba-Graph Learning for Spatiotemporal Event Representation | Efficient spatiotemporal event representation with Mamba/graph elements; highly relevant to scalable event networks. | [card](../01-papers-by-conference/NeurIPS2025/B/2025-NEURIPS-B-eventmg-efficient-multilevel-mamba-graph-learning-for-spatiotemporal-event-representation.md) | [official](https://papers.nips.cc/paper_files/paper/2025/hash/73d829353fdd9749f9b6cf26c5387f2e-Abstract-Conference.html) |
| 2025 | NeurIPS | B | V2V: Scaling Event-Based Vision through Efficient Video-to-Voxel Simulation | Strong contrast case for SECNet: scalable event vision through voxel simulation rather than Event Cloud. | [card](../01-papers-by-conference/NeurIPS2025/B/2025-NEURIPS-B-v2v-scaling-event-based-vision-through-efficient-video-to-voxel-simulation.md) | [official](https://papers.nips.cc/paper_files/paper/2025/hash/b14cf0a01f7a8b9cd3e365e40f910272-Abstract-Conference.html) |
| 2026 | CVPR | B | Scaling Dense Event-Stream Pretraining from Visual Foundation Models | Dense event-stream pretraining and scaling; important for understanding modern event representation learning. | [card](../01-papers-by-conference/CVPR2026/B/2026-CVPR-B-scaling-dense-event-stream-pretraining-from-visual-foundation-models.md) | [official](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Scaling_Dense_Event-Stream_Pretraining_from_Visual_Foundation_Models_CVPR_2026_paper.html) |
| 2026 | CVPR | B | EventGait: Towards Robust Gait Recognition with Event Streams | Event-stream recognition benchmark direction; relevant to classification/recognition evaluation and event datasets. | [card](../01-papers-by-conference/CVPR2026/B/2026-CVPR-B-eventgait-towards-robust-gait-recognition-with-event-streams.md) | [official](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_EventGait_Towards_Robust_Gait_Recognition_with_Event_Streams_CVPR_2026_paper.html) |

## T1: Read After T0

These are still important, but should not block the first pass through SECNet and T0.

| Year | Venue | ABC | Title | Why T | Card | Official |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | CVPR | B | SMV-EAR: Bring Spatiotemporal Multi-View Representation Learning into Efficient Event-Based Action Recognition | Efficient event-based action recognition; useful for comparing event representation choices on recognition tasks. | [card](../01-papers-by-conference/CVPR2026/B/2026-CVPR-B-smv-ear-bring-spatiotemporal-multi-view-representation-learning-into-efficient-event-based.md) | [official](https://openaccess.thecvf.com/content/CVPR2026/html/Fan_SMV-EAR_Bring_Spatiotemporal_Multi-View_Representation_Learning_into_Efficient_Event-Based_Action_CVPR_2026_paper.html) |
| 2024 | ECCV | B | DailyDVS-200: A Comprehensive Benchmark Dataset for Event-Based Action Recognition | Dataset/benchmark paper for event-based action recognition; useful for understanding SECNet-style evaluation regimes. | [card](../01-papers-by-conference/ECCV2024/B/2024-ECCV-B-dailydvs-200-a-comprehensive-benchmark-dataset-for-event-based-action-recognition.md) | [official](https://eccv.ecva.net/virtual/2024/poster/330) |
| 2025 | ICCV | B | TESPEC: Temporally-Enhanced Self-Supervised Pretraining for Event Cameras | Self-supervised pretraining for event cameras; relevant if SECNet is extended toward pretraining or representation learning. | [card](../01-papers-by-conference/ICCV2025/B/2025-ICCV-B-tespec-temporally-enhanced-self-supervised-pretraining-for-event-cameras.md) | [official](https://openaccess.thecvf.com/content/ICCV2025/html/Mohammadi_TESPEC_Temporally-Enhanced_Self-Supervised_Pretraining_for_Event_Cameras_ICCV_2025_paper.html) |
| 2025 | ICCV | B | Efficient Event Camera Data Pretraining with Adaptive Prompt Fusion | Efficient event-camera pretraining; useful for representation scalability and transfer. | [card](../01-papers-by-conference/ICCV2025/B/2025-ICCV-B-efficient-event-camera-data-pretraining-with-adaptive-prompt-fusion.md) | [official](https://openaccess.thecvf.com/content/ICCV2025/html/Liang_Efficient_Event_Camera_Data_Pretraining_with_Adaptive_Prompt_Fusion_ICCV_2025_paper.html) |
| 2025 | ICLR | A | Rethinking Spiking Neural Networks from an Ensemble Learning Perspective | A-level SNN paper that evaluates on point-cloud recognition and event-camera benchmarks; useful for SpikePoint/SNN-side comparison. | [card](../01-papers-by-conference/ICLR2025/A/2025-ICLR-A-rethinking-spiking-neural-networks-from-an-ensemble-learning-perspective.md) | [official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5543342b8c45c0cba04f832390cfb23c-Abstract-Conference.html) |
| 2025 | NeurIPS | A | FLAME: Fast Long-context Adaptive Memory for Event-based Vision | Long-context event-based vision; useful for thinking about long event sequences and memory. | [card](../01-papers-by-conference/NeurIPS2025/A/2025-NEURIPS-A-flame-fast-long-context-adaptive-memory-for-event-based-vision.md) | [official](https://papers.nips.cc/paper_files/paper/2025/hash/1b71649968436c64a765e469ab6b615c-Abstract-Conference.html) |
| 2025 | ICML | A | Hybrid Spiking Vision Transformer for Object Detection with Event Cameras | Strong A-level bridge between event cameras and spiking vision transformers. | [card](../01-papers-by-conference/ICML2025/A/2025-ICML-A-hybrid-spiking-vision-transformer-for-object-detection-with-event-cameras.md) | [official](https://proceedings.mlr.press/v267/xu25e.html) |

## Reference-Only: Recent Top-Venue/Journal SECNet Context

These are cited by SECNet or directly tied to the advisor-group chain. They are not all represented as A/B/C cards yet.

| Year | Venue/Source | Title | Why T |
| --- | --- | --- | --- |
| 2025 | TPAMI | Rethinking Efficient and Effective Point-based Networks for Event Camera Classification and Regression | Direct predecessor from the advisor group; probably the most important paper for understanding SECNet's motivation. |
| 2024 | ICLR | SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition | Advisor-group point-based SNN bridge; key for linking the survey line and SECNet direction. |
| 2023 | ACM MM | TTPOINT: A Tensorized Point Cloud Network for Lightweight Action Recognition with Event Cameras | Advisor-group lightweight point/event representation baseline. |
| 2024 | TCSVT | Event Voxel Set Transformer for Spatiotemporal Representation Learning on Event Streams | Strong recent voxel/set-transformer baseline for event-stream representation. |
| 2023/2024 | TCSVT | Voxel-based Multi-Scale Transformer Network for Event Stream Processing | VMST-Net baseline; important voxel/transformer contrast for SECNet. |
| 2023 | TPAMI | Action Recognition and Benchmark Using Event Cameras | Event-camera action-recognition benchmark context used by SECNet. |
| 2023 | arXiv / core architecture | Mamba: Linear-Time Sequence Modeling with Selective State Spaces | Sequence modeling foundation for Mamba-style event networks. |

## Immediate Reading Order

1. Read SECNet once and map each claim to: representation, scalability, frequency-domain modeling, dataset/task, baseline comparison, or efficiency.
2. Read the advisor-group chain: TPAMI point-based networks / EventMamba, SpikePoint, TTPOINT, then SECNet again.
3. Read T0 in order.
4. Read T1 selectively depending on the actual extension idea your advisor gives later.

## Notes

- T0 + T1 intentionally contain only 15 in-corpus papers.
- Reference-only is limited to recent 2023+ top-venue/top-journal or core-architecture papers.
- No broad web search has been performed for T yet.
