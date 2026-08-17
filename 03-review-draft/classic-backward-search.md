# Classic Literature Backward-Search Candidates

This is a selective queue derived from the 18 existing V2 source PDFs. Inclusion does not change Survey Core or Advisor Core membership. Entries are normally pre-2024, explicitly cited by a source PDF, absent from the current V2 corpus, and directly useful to the survey structure.

## Event Cloud and Sparse Representation

### Space-Time Event Clouds for Gesture Recognition: From RGB Cameras to Event Cameras

- Registry paper_key: `2019-wacv-space-time-event-clouds-for-gesture-recognition-from-rgb-cameras`.
- Pointed to by: PEPNet; TTPOINT.
- Relation type: `foundation`, `baseline`.
- Survey section: Section 2 event representation; Section 5 action recognition.
- Why: establishes the Event Cloud plus PointNet++ lineage later extended by lightweight point ANN and point-SNN methods.
- Evidence: PEPNet Related Work 2.3, PDF p.3, citation/bibliography [40]; TTPOINT Related Work, PDF p.2, citation/bibliography [29].
- Verification status: `verified_from_pdf`.

### Matrix-LSTM: A Differentiable Recurrent Surface for Asynchronous Event-Based Data

- Registry paper_key: `2020-eccv-matrix-lstm-a-differentiable-recurrent-surface-for-asynchronous`.
- Pointed to by: Efficient Learning of Event-based Dense Representation using Hierarchical Memories with Adaptive Update.
- Relation type: `alternative`.
- Survey section: Section 2 stateful event representation.
- Why: canonical per-pixel recurrent event surface and a useful predecessor to hierarchical or globally associated memories.
- Evidence: adaptive-memory paper Related Work, PDF p.4, citation/bibliography [7].
- Verification status: `verified_from_pdf`.

### End-to-End Learning of Representations for Asynchronous Event-Based Data

- Registry paper_key: `2019-iccv-end-to-end-learning-of-representations-for-asynchronous-event-ba`.
- Pointed to by: VMST-Net; EV-ACT; EVSTr.
- Relation type: `alternative`, `baseline`.
- Survey section: Section 2 event representation.
- Why: canonical learned dense event representation against which sparse voxel/set and recurrent representations are repeatedly positioned.
- Evidence: VMST-Net Related Work, PDF pp.2-3, citation/bibliography [27]; EV-ACT Related Work/Experiments, PDF pp.3 and 9, citation/bibliography [35]; EVSTr Related Work/Experiments, PDF pp.3 and 8, citation/bibliography [4].
- Verification status: `verified_from_pdf`.

## Adaptive Event Slicing and Memory

### From Chaos Comes Order: Ordering Event Representations for Object Recognition and Detection

- Registry paper_key: `2023-iccv-from-chaos-comes-order-ordering-event-representations-for-object`.
- Pointed to by: EAS-SNN.
- Relation type: `contrasts_with`.
- Survey section: Sections 2 and 4 adaptive slicing and SNN-event interface.
- Why: directly precedes task-driven SNN slicing by optimizing event representation and sampling windows with a non-spiking mechanism.
- Evidence: EAS-SNN Related Work, PDF p.4, citation/bibliography [75].
- Verification status: `verified_from_pdf`.

### Better and Faster: Adaptive Event Conversion for Event-based Object Detection

- Registry paper_key: `2023-aaai-better-and-faster-adaptive-event-conversion-for-event-based-object-detection`.
- Pointed to by: Spiking Neural Network as Adaptive Event Stream Slicer.
- Relation type: `same_task_different_mechanism`.
- Survey section: Sections 2 and 4 adaptive slicing and SNN-event interface.
- Why: provides a task-aware, non-spiking adaptive event-conversion route that directly contextualizes SpikeSlicer's SNN-controlled boundaries.
- Evidence: SpikeSlicer Related Work, PDF p.3, citation/bibliography [13].
- Verification status: `verified_from_pdf`.

### Asynchronous Spatio-Temporal Memory Network for Continuous Event-Based Object Detection

- Registry paper_key: `2022-tip-asynchronous-spatio-temporal-memory-network-for-continuous-event`.
- Pointed to by: EAS-SNN; Spiking Neural Network as Adaptive Event Stream Slicer.
- Relation type: `baseline`, `same_task_different_mechanism`.
- Survey section: Sections 2, 4 and 5 temporal event processing, SNN-event interface and detection.
- Why: supplies a non-spiking asynchronous-memory comparison for separating adaptive temporal processing from spike-based boundary generation.
- Evidence: EAS-SNN Related Work/Experiments, PDF pp.3 and 12, citation/bibliography [35]; SpikeSlicer Related Work, PDF p.3, citation/bibliography [14].
- Verification status: `verified_from_pdf`.

### Hierarchical Neural Memory Network for Low Latency Event Processing

- Registry paper_key: `2023-cvpr-hierarchical-neural-memory-network-for-low-latency-event-process`.
- Pointed to by: Efficient Learning of Event-based Dense Representation using Hierarchical Memories with Adaptive Update.
- Relation type: `extends`.
- Survey section: Sections 2 and 6 dense representation and conditional computation.
- Why: direct architectural base for hierarchical latent memories; the 2024 work changes its fixed higher-level update schedule to adaptive decisions.
- Evidence: adaptive-memory paper Introduction/Related Work/Experiments, PDF pp.2-4 and 10-12, citation/bibliography [17].
- Verification status: `verified_from_pdf`.

## SNN Dynamics and Learning

### DoReFa-Net: Training Low Bitwidth Convolutional Neural Networks with Low Bitwidth Gradients

- Registry paper_key: `2016-arxiv-dorefa-net-low-bitwidth-convolutional-neural-networks`.
- Pointed to by: Are Conventional SNNs Really Efficient? A Perspective from Network Quantization.
- Relation type: `foundation`.
- Survey section: Section 6 efficiency evaluation.
- Why: supplies the low-bit QANN lineage that Bit Budget extends to SNN weight, state and temporal precision.
- Evidence: source PDF Related Work, PDF p.2, citation/bibliography [43].
- Verification status: `verified_from_pdf`.

### Binarized Neural Networks: Training Deep Neural Networks with Weights and Activations Constrained to +1 or -1

- Registry paper_key: `2016-arxiv-binarized-neural-networks-training-deep-neural-networks`.
- Pointed to by: Are Conventional SNNs Really Efficient? A Perspective from Network Quantization.
- Relation type: `foundation`.
- Survey section: Sections 3 and 6 spike coding and efficiency evaluation.
- Why: provides the single-bit QANN extreme needed to distinguish binary arithmetic from SNN-specific temporal dynamics.
- Evidence: source PDF Related Work, PDF p.2, citation/bibliography [3].
- Verification status: `verified_from_pdf`.

### Spiking Deep Residual Networks

- Registry paper_key: `2021-tnnls-spiking-deep-residual-networks`.
- Pointed to by: Are Conventional SNNs Really Efficient? A Perspective from Network Quantization.
- Relation type: `baseline`.
- Survey section: Section 6 efficiency metrics.
- Why: supplies a conventional deep-SNN and SOP comparator against the paper's precision-aware accounting.
- Evidence: source PDF Related Work, PDF p.2, citation/bibliography [13]; Table 1, PDF p.7.
- Verification status: `verified_from_pdf`.

### Exploiting High Performance Spiking Neural Networks with Efficient Spiking Patterns

- Registry paper_key: `2023-arxiv-exploiting-high-performance-spiking-neural-networks-efficient-spiking-patterns`.
- Pointed to by: Are Conventional SNNs Really Efficient? A Perspective from Network Quantization.
- Relation type: `foundation`.
- Survey section: Section 3 spike coding and state representation.
- Why: provides the burst and multi-state spike-pattern precursor used to motivate QSNN step-state allocation.
- Evidence: source PDF Method 3.2, PDF p.5, citation/bibliography [33].
- Verification status: `verified_from_pdf`.

### PokeBNN: A Binary Pursuit of Lightweight Accuracy

- Registry paper_key: `2022-cvpr-pokebnn-binary-pursuit-lightweight-accuracy`.
- Pointed to by: Are Conventional SNNs Really Efficient? A Perspective from Network Quantization.
- Relation type: `foundation`.
- Survey section: Section 6 quantized computation metrics.
- Why: provides the arithmetic-computation-effort paradigm extended into S-ACE and NS-ACE.
- Evidence: source PDF Method 3.2, PDF p.5, citation/bibliography [40].
- Verification status: `verified_from_pdf`.

### Spikformer: When Spiking Neural Network Meets Transformer

- Registry paper_key: `2022-arxiv-spikformer-when-spiking-neural-network-meets-transformer`.
- Pointed to by: Are Conventional SNNs Really Efficient? A Perspective from Network Quantization.
- Relation type: `baseline`.
- Survey section: Sections 3 and 6 spiking architecture and efficiency.
- Why: supplies the Transformer-scale conventional SNN comparator quantized under the Bit Budget framework.
- Evidence: source PDF Introduction/Related Work, PDF pp.1-2, citation/bibliography [44]; Table 1, PDF p.7.
- Verification status: `verified_from_pdf`.

### Spatial Learning Through Time: Efficient Training of Deep Spiking Neural Networks

- Registry paper_key: `2023-neurips-spatial-learning-through-time-efficient-training-of-deep-spiking`.
- Pointed to by: CLIF.
- Relation type: `contrasts_with`.
- Survey section: Section 3 BPTT and temporal credit assignment.
- Why: discards temporal-gradient propagation for efficient training, providing the clearest counterpoint to CLIF's attempt to restore additional temporal paths.
- Evidence: CLIF Related Work, PDF p.3; Meng et al. (2023) bibliography entry.
- Verification status: `verified_from_pdf`.

### STDP Enables Spiking Neurons to Detect Hidden Causes of Their Inputs

- Registry paper_key: `2009-neurips-stdp-enables-spiking-neurons-to-detect-hidden-causes-of-their-in`.
- Pointed to by: Continuous Spatiotemporal Events Decoupling through Spike-based Bayesian Computation.
- Relation type: `foundation`.
- Survey section: Sections 3 and 4 local learning and Bayesian SNN computation.
- Why: supplies the latent-cause interpretation of STDP used to motivate spike-based EM for event motion segmentation.
- Evidence: spike-based Bayesian computation Introduction/Related Work, PDF pp.2-3, citation/bibliography [29].
- Verification status: `verified_from_pdf`.

## Reconstruction and Detection

### Events-to-Video: Bringing Modern Computer Vision to Event Cameras

- Registry paper_key: `2019-cvpr-events-to-video-bringing-modern-computer-vision-to-event-cameras`.
- Pointed to by: Spike-Temporal Latent Representation for Energy-Efficient Event-to-Video Reconstruction.
- Relation type: `baseline`.
- Survey section: Section 5 reconstruction.
- Why: canonical recurrent ANN event-to-video baseline for separating gains from reconstruction architecture, temporal latent coding, and spiking computation.
- Evidence: STLR Related Work/Experiments, PDF pp.3 and 10, citation/bibliography [28].
- Verification status: `verified_from_pdf`.

### Object Detection with Spiking Neural Networks on Automotive Event Data

- Registry paper_key: `2022-ijcnn-object-detection-with-spiking-neural-networks-on-automotive-even`.
- Pointed to by: SFOD.
- Relation type: `extends`.
- Survey section: Sections 4 and 5 SNN topology and detection.
- Why: direct source of SFOD's voxel cube, PLIF backbone, Extra Blocks, and SSD head; needed to isolate SFOD's actual fusion contribution.
- Evidence: SFOD Introduction/Method, PDF pp.2 and 4, citation/bibliography [9].
- Verification status: `verified_from_pdf`.

## Robustness and Interpretation

### On Pixel-Wise Explanations for Non-Linear Classifier Decisions by Layer-Wise Relevance Propagation

- Registry paper_key: `2015-plos-one-on-pixel-wise-explanations-for-non-linear-classifier-decisions-b`.
- Pointed to by: EventRPG.
- Relation type: `foundation`.
- Survey section: Sections 3 and 4 SNN interpretability and training.
- Why: provides the relevance-conservation basis that EventRPG extends across spiking layers and time.
- Evidence: EventRPG Introduction/Preliminary, PDF pp.1-2; Bach et al. (2015) bibliography entry.
- Verification status: `verified_from_pdf`.

### Adversarial Attacks on Spiking Convolutional Neural Networks for Event-based Vision

- Registry paper_key: `2021-arxiv-adversarial-attacks-on-spiking-convolutional-neural-networks-for`.
- Pointed to by: Exploring Vulnerabilities in Spiking Neural Networks: Direct Adversarial Attacks on Raw Event Data.
- Relation type: `baseline`.
- Survey section: Section 6 robustness and security.
- Why: establishes a discrete spike-flip attack baseline needed to distinguish attacks on internal spike tensors from attacks on raw variable-length event streams.
- Evidence: raw-event attack Related Work/Experiments, PDF pp.3 and 11, citation/bibliography [6].
- Verification status: `verified_from_pdf`.
