# Advisor Core Reading Plan

Serves the **SECNet ICML 2026 oral to TPAMI extension** direction: implement SECNet as an accurate, trainable, and deployable SNN while preserving its ordered Event Cloud hierarchy. Existing frequency modules are baseline components, not the Core admission criterion. Mamba/SSM is outside the planned first implementation.

Current proceedings core: **8 papers**.

Composition: **6 required + 2 helpful**.
Helpful assignments are focused mechanism reads. They do not enroll an entire architecture or make Mamba/SSM part of the Advisor direction.

The bounded Advisor reading set is **9 papers**: 8 proceedings-corpus assignments and 1 external focus paper.

## Focus Paper

| Paper | Year | Venue | Assignment | Why it is included |
| --- | ---: | --- | --- | --- |
| Scalable Event Cloud Network for Event-based Classification | 2026 | ICML oral | focus | The TPAMI extension starts from SECNet and asks how to implement its ordered Event Cloud hierarchy as an accurate, trainable, and genuinely efficient SNN. Its existing Spatial-FA and Temporal-FA modules remain part of the baseline, but frequency is no longer the Advisor admission criterion. |

## Required Knowledge

| # | Paper | Year | Venue | Track | Assignment | Why it is core |
| ---: | --- | ---: | --- | --- | --- | --- |
| 1 | [Spike-driven Discrete Aggregation for Event-based Object Detection](../01-papers-by-conference/CVPR2026/A/2026-CVPR-A-spike-driven-discrete-aggregation-for-event-based-object-detection.md) | 2026 | CVPR | - | required | SDA moves the spiking mechanism into event selection and aggregation, making it a direct alternative for SECNet's G&S/AGG interface rather than a generic backbone replacement. |
| 2 | [Spiking Discrepancy Transformer for Point Cloud Analysis](../01-papers-by-conference/ICLR2026/C/ICLR2026-3725.md) | 2026 | ICLR | - | required | Its hierarchical point SNN, local/global discrepancy attention, and Spatially-Aware Spiking Neuron directly inform how SECNet groups can retain geometry after spike binarization. |
| 3 | [Temporal Interaction in Spiking Transformers with Multi-Delay Mixer](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-temporal-interaction-in-spiking-transformers-with-multi-delay-mixer.md) | 2026 | CVPR | - | required | Multi-Delay Mixer is a drop-in temporal interaction mechanism for ordered group descriptors and a controlled alternative or complement to SECNet's chronological TFA path. |
| 4 | [STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-step-a-unified-spiking-transformer-evaluation-platform-for-fair-and-reproducible-benchmark.md) | 2025 | NeurIPS | Datasets and Benchmarks Track | required | STEP supplies the controlled protocol needed to compare encoding, LIF-family neurons, timestep, temporal modeling, surrogate training, and analytical energy without mixing incompatible settings. |
| 5 | [CLIF: Complementary Leaky Integrate-and-Fire Neuron for Spiking Neural Networks](../01-papers-by-conference/ICML2024/C/2024-ICML-C-clif-complementary-leaky-integrate-and-fire-neuron-for-spiking-neural-networks.md) | 2024 | ICML | - | required | CLIF is a clean binary-spike neuron ablation for testing whether complementary state and additional temporal-gradient paths improve a fixed SECNet-SNN backbone over PLIF. |
| 6 | [SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md) | 2024 | ICLR | - | required | Closest direct Event Cloud-to-SNN reference: its grouped point input, explicit rate-coded spike interface, PLIF backbone, residual training, and efficiency boundaries define the first SECNet-SNN baseline. |

## Focused Helpful Mechanisms

| # | Paper | Year | Venue | Track | Assignment | Why it is core |
| ---: | --- | ---: | --- | --- | --- | --- |
| 7 | [Rethinking SNN Online Training and Deployment: Gradient-Coherent Learning via Hybrid-Driven LIF Model](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-rethinking-snn-online-training-and-deployment-gradient-coherent-learning-via-hybrid-driven.md) | 2026 | CVPR | - | helpful | HD-LIF is a second-stage option for reducing STBP memory and aligning online gradients while jointly testing normalization, quantization, attention, and deployment trade-offs. |
| 8 | [SMixer: Rethinking Efficient-Training and Event-Driven SNNs](../01-papers-by-conference/ICLR2026/C/ICLR2026-3550.md) | 2026 | ICLR | - | helpful | SMixer is second-stage deployment evidence for asynchronous-friendly token mixing and spatial-temporal spike pruning after the basic SECNet-SNN architecture is stable. |

## Coverage Map

### Event Cloud and point processing

[Spiking Discrepancy Transformer for Point Cloud Analysis](../01-papers-by-conference/ICLR2026/C/ICLR2026-3725.md); [SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md)

### Grouping, sampling and aggregation

[Spike-driven Discrete Aggregation for Event-based Object Detection](../01-papers-by-conference/CVPR2026/A/2026-CVPR-A-spike-driven-discrete-aggregation-for-event-based-object-detection.md); [Spiking Discrepancy Transformer for Point Cloud Analysis](../01-papers-by-conference/ICLR2026/C/ICLR2026-3725.md); [SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md)

### Event-to-spike interfaces and encoding

[Spike-driven Discrete Aggregation for Event-based Object Detection](../01-papers-by-conference/CVPR2026/A/2026-CVPR-A-spike-driven-discrete-aggregation-for-event-based-object-detection.md); [Spiking Discrepancy Transformer for Point Cloud Analysis](../01-papers-by-conference/ICLR2026/C/ICLR2026-3725.md); [STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-step-a-unified-spiking-transformer-evaluation-platform-for-fair-and-reproducible-benchmark.md); [SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md)

### Spiking neuron dynamics

[Rethinking SNN Online Training and Deployment: Gradient-Coherent Learning via Hybrid-Driven LIF Model](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-rethinking-snn-online-training-and-deployment-gradient-coherent-learning-via-hybrid-driven.md); [Spike-driven Discrete Aggregation for Event-based Object Detection](../01-papers-by-conference/CVPR2026/A/2026-CVPR-A-spike-driven-discrete-aggregation-for-event-based-object-detection.md); [Spiking Discrepancy Transformer for Point Cloud Analysis](../01-papers-by-conference/ICLR2026/C/ICLR2026-3725.md); [STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-step-a-unified-spiking-transformer-evaluation-platform-for-fair-and-reproducible-benchmark.md); [CLIF: Complementary Leaky Integrate-and-Fire Neuron for Spiking Neural Networks](../01-papers-by-conference/ICML2024/C/2024-ICML-C-clif-complementary-leaky-integrate-and-fire-neuron-for-spiking-neural-networks.md); [SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md)

### SNN architecture and spike-native operators

[SMixer: Rethinking Efficient-Training and Event-Driven SNNs](../01-papers-by-conference/ICLR2026/C/ICLR2026-3550.md); [Spike-driven Discrete Aggregation for Event-based Object Detection](../01-papers-by-conference/CVPR2026/A/2026-CVPR-A-spike-driven-discrete-aggregation-for-event-based-object-detection.md); [Spiking Discrepancy Transformer for Point Cloud Analysis](../01-papers-by-conference/ICLR2026/C/ICLR2026-3725.md); [Temporal Interaction in Spiking Transformers with Multi-Delay Mixer](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-temporal-interaction-in-spiking-transformers-with-multi-delay-mixer.md); [STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-step-a-unified-spiking-transformer-evaluation-platform-for-fair-and-reproducible-benchmark.md); [SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md)

### Direct, surrogate-gradient and online SNN training

[Rethinking SNN Online Training and Deployment: Gradient-Coherent Learning via Hybrid-Driven LIF Model](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-rethinking-snn-online-training-and-deployment-gradient-coherent-learning-via-hybrid-driven.md); [SMixer: Rethinking Efficient-Training and Event-Driven SNNs](../01-papers-by-conference/ICLR2026/C/ICLR2026-3550.md); [STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-step-a-unified-spiking-transformer-evaluation-platform-for-fair-and-reproducible-benchmark.md); [CLIF: Complementary Leaky Integrate-and-Fire Neuron for Spiking Neural Networks](../01-papers-by-conference/ICML2024/C/2024-ICML-C-clif-complementary-leaky-integrate-and-fire-neuron-for-spiking-neural-networks.md)

### Temporal interaction, state and delay

[Rethinking SNN Online Training and Deployment: Gradient-Coherent Learning via Hybrid-Driven LIF Model](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-rethinking-snn-online-training-and-deployment-gradient-coherent-learning-via-hybrid-driven.md); [SMixer: Rethinking Efficient-Training and Event-Driven SNNs](../01-papers-by-conference/ICLR2026/C/ICLR2026-3550.md); [Spike-driven Discrete Aggregation for Event-based Object Detection](../01-papers-by-conference/CVPR2026/A/2026-CVPR-A-spike-driven-discrete-aggregation-for-event-based-object-detection.md); [Temporal Interaction in Spiking Transformers with Multi-Delay Mixer](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-temporal-interaction-in-spiking-transformers-with-multi-delay-mixer.md); [STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-step-a-unified-spiking-transformer-evaluation-platform-for-fair-and-reproducible-benchmark.md); [CLIF: Complementary Leaky Integrate-and-Fire Neuron for Spiking Neural Networks](../01-papers-by-conference/ICML2024/C/2024-ICML-C-clif-complementary-leaky-integrate-and-fire-neuron-for-spiking-neural-networks.md)

### Scalability and efficiency

[Rethinking SNN Online Training and Deployment: Gradient-Coherent Learning via Hybrid-Driven LIF Model](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-rethinking-snn-online-training-and-deployment-gradient-coherent-learning-via-hybrid-driven.md); [SMixer: Rethinking Efficient-Training and Event-Driven SNNs](../01-papers-by-conference/ICLR2026/C/ICLR2026-3550.md); [Spike-driven Discrete Aggregation for Event-based Object Detection](../01-papers-by-conference/CVPR2026/A/2026-CVPR-A-spike-driven-discrete-aggregation-for-event-based-object-detection.md); [Spiking Discrepancy Transformer for Point Cloud Analysis](../01-papers-by-conference/ICLR2026/C/ICLR2026-3725.md); [Temporal Interaction in Spiking Transformers with Multi-Delay Mixer](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-temporal-interaction-in-spiking-transformers-with-multi-delay-mixer.md); [STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-step-a-unified-spiking-transformer-evaluation-platform-for-fair-and-reproducible-benchmark.md); [CLIF: Complementary Leaky Integrate-and-Fire Neuron for Spiking Neural Networks](../01-papers-by-conference/ICML2024/C/2024-ICML-C-clif-complementary-leaky-integrate-and-fire-neuron-for-spiking-neural-networks.md); [SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md)

### Hardware and deployment

[Rethinking SNN Online Training and Deployment: Gradient-Coherent Learning via Hybrid-Driven LIF Model](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-rethinking-snn-online-training-and-deployment-gradient-coherent-learning-via-hybrid-driven.md); [STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-step-a-unified-spiking-transformer-evaluation-platform-for-fair-and-reproducible-benchmark.md)

### Asynchronous and memory-aware deployment

[Rethinking SNN Online Training and Deployment: Gradient-Coherent Learning via Hybrid-Driven LIF Model](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-rethinking-snn-online-training-and-deployment-gradient-coherent-learning-via-hybrid-driven.md); [SMixer: Rethinking Efficient-Training and Event-Driven SNNs](../01-papers-by-conference/ICLR2026/C/ICLR2026-3550.md)

### Datasets and evaluation

[STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-step-a-unified-spiking-transformer-evaluation-platform-for-fair-and-reproducible-benchmark.md)
