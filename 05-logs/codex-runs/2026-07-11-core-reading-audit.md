# Core Reading Audit - 2026-07-11

## Scope

- Audited all 351 current-corpus A/B/C papers using reviewed official abstracts and existing paper cards.
- Checked every current core B/C paper individually.
- Reverse-screened non-core B/C abstracts for combined event-camera and SNN evidence and for the SECNet / SpikePoint / EventMamba method chain.
- Used the local PDF only to resolve the EventGait B/A boundary.
- Did not search new venues, summarize P1/P2 papers, or change the confirmed SSM/Mamba core subset.

## Confirmed Promotion

- `CVPR2026-2918` EventGait: B -> A. The main dynamic stream is built from LIF neurons, a Mixture of Spiking Experts, and a spiking gating network; this is method-level SNN use rather than benchmark-only evidence.

## Advisor-Track Addition

- `CVPR2024-1880` PEPNet was added. It is a same-group point-based event-camera predecessor explicitly identified in the EventMamba method chain.

## Advisor-Track Demotions to P1

These remain useful background papers, but the repository contained no direct evidence that they belong to the SECNet/advisor method chain:

- `ICML2025-0323` A Chaotic Dynamics Framework Inspired by Dorsal Stream for Event Signal Processing
- `NeurIPS2025-4086` V2V: Scaling Event-Based Vision through Efficient Video-to-Voxel Simulation
- `CVPR2026-1228` Scaling Dense Event-Stream Pretraining from Visual Foundation Models
- `ICCV2025-1879` TESPEC: Temporally-Enhanced Self-Supervised Pretraining for Event Cameras
- `ICCV2025-1798` Efficient Event Camera Data Pretraining with Adaptive Prompt Fusion
- `ICLR2025-1232` Rethinking Spiking Neural Networks from an Ensemble Learning Perspective

## P0 Demotions to P1

The following papers remain selected reading, but are not direct SNN x Event Camera papers or indispensable core background:

- Event-camera side: `ICCV2025-0082`, `ICCV2025-1538`, `CVPR2026-0479`, `NeurIPS2025-4822`, `CVPR2026-3561`, `CVPR2026-2514`, `CVPR2026-1573`, `CVPR2026-0881`, `NeurIPS2025-2978`, `NeurIPS2025-2173`.
- SNN side: `ICLR2025-0522`, `ICML2025-3251`, `NeurIPS2025-3401`.

## Boundary Checks Retained

- `CVPR2024-0028` LED remains B/P1: its LIF component is an auxiliary denoising baseline, while the paper's main contribution is the dataset and event-denoising framework.
- Generic SNN papers evaluated only on CIFAR10-DVS, N-Caltech101, DVS-Gesture, or similar benchmarks remain C.
- All confirmed SSM/Mamba entries were retained at the user's request because EventMamba is part of the advisor's predecessor chain.

## Counts

| Metric | Before | After |
| --- | ---: | ---: |
| Refined A | 18 | 19 |
| Refined B | 201 | 200 |
| Refined C | 132 | 132 |
| P0 | 50 | 34 |
| P1 | 93 | 109 |
| P2 | 197 | 197 |
| P3 | 11 | 11 |
| Advisor-track current corpus | 18 | 13 |
| Core current corpus | 51 | 34 |
| SECNet reference-only | 5 | 5 |
| Core total | 56 | 39 |

All 19 A papers are in P0/core. No uncertain paper remains in core. The list was not padded toward the approximate target of 60.
