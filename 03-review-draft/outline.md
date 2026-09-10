# Survey Outline

Status: **provisional after Checkpoint 01 and taxonomy-closure audit**. Live Core progress is maintained in the generated [Survey V2 index](../06-reading-summaries/v2/survey/index.md).

This is a working structure, not the final V1.0 outline. Checkpoint 01 is recorded in [outline-checkpoints/checkpoint-01-11-v2.md](outline-checkpoints/checkpoint-01-11-v2.md). The external-survey [taxonomy closure audit](taxonomy-closure-audit.md) broadens recall without replacing evidence from paper-level V2 reading. Decisions that depend on the remaining 2025/2026 anchors, tracking, ANN-SNN conversion, or hardware evaluation remain open.

The review-and-reading sequence is maintained in [core-reading-roadmap-13-to-26.md](core-reading-roadmap-13-to-26.md). The filename records the roadmap's original 13/26 starting point; it is not a live progress counter.

## Working Title

Spiking Neural Networks for Event Cameras

## Draft Structure

The survey should use **parallel foundations plus an explicit intersection chapter**. Event representation is not a subcategory of SNN, and SNN is not a subcategory of event representation. They are two independent axes that meet in the SNN-for-event-camera literature.

The chapter order is therefore not a nested taxonomy. Chapters 2 and 3 define the two axes independently; Chapter 4 studies their combinations; Chapter 5 compares those combinations across tasks; Chapter 6 synthesizes the evidence. A paper can appear in more than one cross-cutting table, but it should not be treated as a new category every time it crosses an axis.

1. Introduction and scope
   - Define event cameras, SNNs, and the strict intersection.
   - State the survey question: how do event representations and SNN computation interact?
   - Explain the two-axis taxonomy and prevent broad event-based-vision drift.

2. Event-camera data organization and representations: the sensor-side axis
   - Raw asynchronous event stream and event tuple semantics.
   - Temporal organization before representation: fixed-duration slicing, fixed-event-count slicing, packetization, and adaptive sampling/slicing.
   - Implementation families: image/event frames, time surfaces, voxel grids, point/Event Cloud, graphs, learned representations, and spike-native inputs.
   - Cross-cutting storage/processing property: dense versus sparse. Do not force time surfaces, graphs, points, and learned representations into a single mutually exclusive dense/sparse tree.
   - Learned/adaptive representations after the temporal boundary has been chosen, including task-aware aggregation, polarity-aware encoding and, where the transformation is applied to the event signal itself, frequency-aware representations.
   - Keep slicing and representation distinct: slicing chooses which events belong together; representation determines how that group is encoded.
   - Comparison dimensions: sparsity, temporal precision, spatial completeness, polarity retention, preprocessing cost, memory, latency, and information loss.

3. Spiking neural networks: the computation-side axis
   - Spike coding, neuron state, membrane dynamics, reset, and temporal simulation.
   - Architectural boundary: directly trained SNN, converted SNN, fully spiking network, hybrid ANN-SNN, and non-spiking comparator.
   - Architecture families: convolutional/residual SNNs, recurrent/stateful SNNs, Spiking Transformers/attention/mixers, and point/graph SNNs. These are sibling families; `Spiking Transformer` is not a synonym for modern SNNs as a whole.
   - Temporal axis: short-term dynamics, long-range state/memory, delay, temporal credit assignment, and timestep flexibility.
   - Training axis: surrogate gradient, BPTT/STBP, online/local learning, STDP, distillation, normalization, and stability.
   - Efficiency axis: sparse activation, addition-only computation, state and memory overhead, latency, energy, and hardware mapping.
   - Apply `fully spiking` at an explicit boundary: a spiking backbone, a fully spiking task network, and an end-to-end event-processing pipeline are not equivalent claims.

4. SNN for Event Cameras: the intersection axis
   - Event-to-spike interfaces: distinguish sensor events, event groups, encoded event tensors/points, model input spikes, internal spikes, and decoded continuous outputs.
   - Integration topology I, task network: the SNN is the main feature extractor, backbone, decoder, or predictor.
   - Integration topology II, hybrid module: the SNN supplies temporal filtering or spiking features while ANN modules perform registration, fusion, decoding, or prediction.
   - Integration topology III, event-interface controller: spike timing or membrane state controls sampling, slicing, aggregation, or routing before a downstream model.
   - Integration topology IV, inference/optimization engine: spiking dynamics implement latent coding, Bayesian competition, local learning, or an unfolded algorithm.
   - Compare each topology across dense and sparse event representations rather than treating dense/sparse as the only method taxonomy.
   - Event-stream-specific learning: spike-aware objectives, task-guided slicing, relevance-guided augmentation, local plasticity, and representation-dynamics coupling.
   - For each family, ask the same questions: what is represented, what is spiking, what role the SNN plays, where temporal state is kept, how it is trained, and what evidence supports the efficiency claim.
   - Keep frequency and wavelet as cross-cutting mechanisms. Use SSM/Mamba only when a specific non-spiking temporal comparator is needed; do not turn it into a survey axis or infer SNN relevance from long-memory modeling alone.

5. Tasks and empirical evidence across the intersection
   - Recognition and action classification.
   - Object detection.
   - Tracking.
   - Reconstruction/restoration.
   - Pose, depth, optical flow, motion estimation, and segmentation.
   - Datasets and evaluation protocols: temporal granularity, cross-subject/generalization settings, camera motion, noise, and distribution shift.
   - Robustness and security at the event-SNN interface.
   - Evidence hierarchy: task accuracy/quality; timesteps and firing rate; operation-count energy proxy; GPU/CPU runtime; neuromorphic or device-level latency and energy.
   - Treat tasks as an evidence-organizing axis, not as a replacement for the representation/SNN taxonomy.

6. Two-axis synthesis and open problems
   - A matrix with event representation on one axis and SNN mechanism on the other.
   - A second view mapping task to integration topology, because the same representation can place the SNN at different points in the pipeline.
   - Empty, weak, and well-supported cells in the matrix.
   - Representation-dynamics mismatch, temporal slicing sensitivity, event sparsity versus spatial completeness, long-term memory, frequency modeling, robustness, and reproducible efficiency claims.
   - Separate estimated arithmetic savings from software runtime and measured hardware efficiency; do not infer one from another.
   - Open problems for event representation, SNN computation, and their intersection separately.
