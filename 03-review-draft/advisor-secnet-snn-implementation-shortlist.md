# SECNet-SNN Implementation Shortlist

Status: **confirmed Advisor reading set; synchronized with the current Core assignments**
Date: 2026-09-10

## 1. Updated Goal

The Advisor direction is re-scoped from a frequency-centered extension survey to a concrete implementation question:

> How should SECNet be redesigned as an accurate, trainable, and genuinely efficient SNN while preserving its ordered Event Cloud representation and hierarchical processing strengths?

SECNet's existing Fourier modules remain part of the starting architecture, but `frequency/Fourier` is no longer the admission criterion for the Advisor reading set. The new reading set must directly inform at least one implementation decision: event-to-spike interface, point/Event Cloud architecture, neuron dynamics, temporal interaction, direct/online training, spike sparsity, or deployable event-driven operations.

## 2. Screening Method

The screening started from all **572** rows in `00-index/candidate-screening-audit.csv`, each of which already stores a complete official title and abstract. A high-recall SNN implementation query retrieved **202** papers from 2024-2026; **159** of them are in the active corpus. The high-priority longlist was then assessed using five questions:

1. Does the paper preserve or directly operate on sparse point/event structure?
2. Does it make a concrete SNN architecture or neuron choice rather than merely using an SNN benchmark?
3. Can its mechanism be inserted into SECNet's `G&S -> SFA -> AGG -> TFA -> RES` hierarchy?
4. Does it address temporal learning, gradient stability, training cost, or asynchronous deployment?
5. Is there sufficiently direct official-paper evidence and an implementable mechanism?

The final eight are deliberately complementary. They are not ranked by incomparable cross-paper SOTA numbers. Full or targeted PDF checks were used for the highest-priority method and evaluation claims; energy claims remain classified by evidence type.

## 3. Recommended Eight Papers

### Tier A: architecture-defining reads

#### 1. SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition

- **Venue:** ICLR 2024
- **Repository card:** [SpikePoint](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md)
- **Official source:** [ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/75f1a165c7561e028c41d42fa6286a76-Abstract-Conference.html)
- **Why it is indispensable:** it is the closest existing paper to the desired input side: an end-to-end point-based SNN operating on sparse Event Cloud data rather than first converting events into frames or voxels.
- **SECNet decision informed:** how grouped event points can enter a direct-trained SNN; how local and global point features, PLIF neurons, residual paths, and short-timestep inference are assembled.
- **Likely transfer:** reuse the explicit Event Cloud-to-neuronal-spike interface and point-wise spiking feature extraction as the first reference implementation.
- **Boundary:** SpikePoint discards polarity, treats timestamp as a pseudo-coordinate, and regenerates rate-coded spikes. Its estimated energy excludes important preprocessing and memory costs. These choices should not be copied blindly into SECNet.

#### 2. Spiking Discrepancy Transformer for Point Cloud Analysis

- **Venue:** ICLR 2026
- **Repository card:** [Spiking Discrepancy Transformer](../01-papers-by-conference/ICLR2026/C/ICLR2026-3725.md)
- **Official source:** [ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b238324b309da12c7446d92c14db9f7e-Abstract-Conference.html)
- **Why it is indispensable:** this is the strongest recent architecture-level bridge from unordered point sets to a hierarchical Spiking Transformer. It jointly designs the point hierarchy, local/global spike attention, and a Spatially-Aware Spiking Neuron.
- **SECNet decision informed:** whether SECNet's grouped Event Cloud should use a local-to-global spiking hierarchy rather than applying a generic 2D Spiking Transformer; how centroid/neighborhood structure can influence initial membrane state.
- **Likely transfer:** map SECNet groups to the local SEDA stage, group descriptors to the global SIDA stage, and test coordinate-aware membrane initialization before discarding spatial information through spike binarization.
- **Boundary:** the experiments use conventional 3D point-cloud datasets, not asynchronous event clouds. Reported energy is theoretical, and event polarity plus chronological ordering require a separate adaptation.

#### 3. Spike-driven Discrete Aggregation for Event-based Object Detection

- **Venue:** CVPR 2026
- **Repository card:** [Spike-driven Discrete Aggregation](../01-papers-by-conference/CVPR2026/A/2026-CVPR-A-spike-driven-discrete-aggregation-for-event-based-object-detection.md)
- **Official source:** [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Spike-driven_Discrete_Aggregation_for_Event-based_Object_Detection_CVPR_2026_paper.html)
- **Why it is indispensable:** it treats spiking neurons as the event-selection and aggregation mechanism itself, using gated recurrent spiking neurons to retain informative events and Multi-Timescale Fusion to recover coarse temporal context.
- **SECNet decision informed:** whether SNN conversion should begin before the backbone, inside SECNet's G&S/AGG interface, instead of simply replacing continuous activations after aggregation.
- **Likely transfer:** construct an SDA-style learned gate for event/group retention, then compare it with SECNet's existing D-FPS/EF-KNN/CES pipeline under identical backbones.
- **Boundary:** its representation and evidence are detection-specific. The reported 43.4 Gen1 mAP50:95 and robustness results do not establish that the same aggregation will improve Event Cloud classification or pose estimation.

### Tier B: neuron and temporal-learning decisions

#### 4. STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking

- **Venue:** NeurIPS 2025, Datasets and Benchmarks Track
- **Repository card:** [STEP](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-step-a-unified-spiking-transformer-evaluation-platform-for-fair-and-reproducible-benchmark.md)
- **Official source:** [NeurIPS Proceedings](https://papers.nips.cc/paper_files/paper/2025/hash/e9fece10c0f4ffdcf015ab676f370fbd-Abstract-Datasets_and_Benchmarks_Track.html)
- **Why it is indispensable:** it is not a candidate SECNet module; it is the control framework needed to avoid choosing neurons, encodings, attention, or energy models from incomparable papers.
- **SECNet decision informed:** the minimum controlled ablations for LIF/PLIF/CLIF/GLIF/KLIF, encoding, timestep, surrogate gradient, temporal modeling, and energy accounting.
- **Direct evidence:** enhanced neurons improve several Spiking Transformer backbones, with PLIF giving the largest gain in the reported controlled comparison. Standard Spiking Transformers remain weak at temporal modeling, and sparse encoding can reduce spatial coherence when attention is not temporally aware.
- **Boundary:** its energy conclusions are analytical operation-and-memory estimates, not measured neuromorphic-chip power. SECNet needs its own point-processing and FFT cost accounting.

#### 5. CLIF: Complementary Leaky Integrate-and-Fire Neuron for Spiking Neural Networks

- **Venue:** ICML 2024
- **Repository card:** [CLIF](../01-papers-by-conference/ICML2024/C/2024-ICML-C-clif-complementary-leaky-integrate-and-fire-neuron-for-spiking-neural-networks.md)
- **Official source:** [PMLR](https://proceedings.mlr.press/v235/huang24n.html)
- **Why it is selected:** CLIF is a clean drop-in neuron candidate for direct training. It retains binary inter-layer spikes and adds a complementary state that supplies additional temporal-gradient paths without adding learnable neuron parameters.
- **SECNet decision informed:** whether SNN degradation is caused partly by temporal-gradient loss, and whether a richer neuron state improves an otherwise fixed SECNet-SNN backbone.
- **Likely transfer:** use PLIF as the controlled default suggested by STEP, then replace it with CLIF while keeping encoding, architecture, timestep, optimizer, and seed fixed.
- **Boundary:** CLIF adds continuous state, sigmoid computation, and memory traffic. Its paper supports accuracy improvements over LIF but does not show universally lower energy or true raw-event asynchronous execution.

#### 6. Temporal Interaction in Spiking Transformers with Multi-Delay Mixer

- **Venue:** CVPR 2026
- **Repository card:** [Multi-Delay Mixer](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-temporal-interaction-in-spiking-transformers-with-multi-delay-mixer.md)
- **Official source:** [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Temporal_Interaction_in_Spiking_Transformers_with_Multi-Delay_Mixer_CVPR_2026_paper.html)
- **Why it is selected:** it directly targets the weakness most relevant to SECNet: common Spiking Transformer attention is primarily spatial and does not create rich temporal interactions. MD-Mixer introduces multiple delays as a drop-in temporal mixer.
- **SECNet decision informed:** whether SECNet's chronological TFA path should remain Fourier-based, be complemented by a delay-based spiking mixer, or be replaced by one in a controlled ablation.
- **Likely transfer:** apply MD-Mixer over ordered group descriptors after AGG, not over arbitrary unordered event indices.
- **Boundary:** SECNet contains two distinct notions of time: physical event chronology and SNN simulation steps. They must not be silently collapsed into the same MD-Mixer axis.

#### 7. Rethinking SNN Online Training and Deployment: Gradient-Coherent Learning via Hybrid-Driven LIF Model

- **Venue:** CVPR 2026
- **Repository card:** [HD-LIF](../01-papers-by-conference/CVPR2026/C/2026-CVPR-C-rethinking-snn-online-training-and-deployment-gradient-coherent-learning-via-hybrid-driven.md)
- **Official source:** [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Hao_Rethinking_SNN_Online_Training_and_Deployment_Gradient-Coherent_Learning_via_Hybrid-Driven_CVPR_2026_paper.html)
- **Why it is selected:** HD-LIF addresses the training-memory problem of STBP and the gradient mismatch of ordinary online learning, while also exploring parallel neurons, membrane-oriented normalization, low-bit weights, and lightweight spike channel attention.
- **SECNet decision informed:** whether a long or high-resolution Event Cloud sequence can be trained without storing a full BPTT graph, and which deployment optimizations should be evaluated together rather than in isolation.
- **Direct evidence:** the paper reports constant-complexity online temporal backpropagation, competitive results on static and DVS datasets, and explicit ablations for parameter memory, GPU memory, SOP/NOP estimates, and model-level energy.
- **Boundary:** HD-LIF's hybrid-driven and multi-bit firing mechanisms change the semantics of a conventional binary SNN. It should be an advanced branch after a binary PLIF/CLIF baseline, not the first SECNet-SNN implementation.

### Tier C: deployment-oriented architecture

#### 8. SMixer: Rethinking Efficient-Training and Event-Driven SNNs

- **Venue:** ICLR 2026
- **Repository card:** [SMixer](../01-papers-by-conference/ICLR2026/C/ICLR2026-3550.md)
- **Official source:** [ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/aaeb635296295aa7c9f8b91c5e10960d-Abstract-Conference.html)
- **Why it is selected:** SMixer explicitly distinguishes high benchmark accuracy from genuine asynchronous deployability. It replaces synchronized spike self-attention with an event-driven-friendly token mixer and prunes redundant spike features across space and time.
- **SECNet decision informed:** whether SFA/TFA replacements use only operations supported by the intended asynchronous hardware; how to reduce training cost and firing activity after a workable SECNet-SNN baseline exists.
- **Likely transfer:** test mixer blocks on grouped descriptors and use spike-intensity-based pruning only after establishing which spatial and temporal groups carry stable SECNet information.
- **Boundary:** pruning creates an accuracy-efficiency trade-off; the paper's COCO example loses mAP under the tested pruning setup. Fully event-driven claims must still be checked against SECNet's G&S, FFT/iFFT, normalization, and pooling operations.

## 4. Recommended Reading Order

The reading order should follow implementation dependencies rather than publication year:

1. Revisit **SECNet** and freeze its input, group hierarchy, SFA/TFA axes, and task heads.
2. Read **SpikePoint** to define the first Event Cloud-to-spike baseline.
3. Read **STEP** before choosing the default neuron and evaluation protocol.
4. Read **Spiking Discrepancy Transformer** to design the local-global point-spiking hierarchy.
5. Read **CLIF** and implement it as a controlled neuron replacement after PLIF.
6. Read **Spike-driven Discrete Aggregation** for the G&S/AGG interface.
7. Read **Multi-Delay Mixer** for explicit chronological temporal interaction.
8. Read **HD-LIF** and **SMixer** only after the baseline works, to optimize training memory and asynchronous deployment.

## 5. Initial SECNet-SNN Experimental Matrix

The shortlist implies the following minimal experiment sequence:

| Decision | Baseline | Controlled alternatives | Main source |
| --- | --- | --- | --- |
| Event input | SECNet ordered Event Cloud | SpikePoint-style rate coding; polarity-preserving dual channel; direct current encoding | SpikePoint, STEP |
| Point hierarchy | Original G&S + AGG | local/global discrepancy stages; coordinate-aware membrane initialization | Spiking Discrepancy Transformer |
| Neuron | PLIF | LIF, CLIF, then HD-LIF | STEP, CLIF, HD-LIF |
| Event aggregation | Existing D-FPS/EF-KNN/CES | gated recurrent discrete selection | Spike-driven Discrete Aggregation |
| Temporal block | Existing TFA | TFA + MD-Mixer; MD-Mixer replacement | Multi-Delay Mixer |
| Architecture primitive | current continuous mixers | asynchronous-friendly Spiking-token Mixer | SMixer |
| Training | SG + BPTT/STBP | memory-aware online training after baseline validation | CLIF, HD-LIF |
| Evidence | task accuracy | firing rate, timesteps, peak training memory, wall-clock time, operation/memory estimate, measured hardware result when available | STEP |

The first implementation should be conservative: preserve SECNet's Event Cloud construction and hierarchy, introduce an explicit spike interface, and change one axis at a time. A simultaneous replacement of grouping, neuron, temporal mixer, attention, and training rule would make any gain uninterpretable.

## 6. Strong Alternatives Not in the First Eight

- **Multiplication-Free Parallelizable Spiking Neurons with Efficient Spatio-Temporal Dynamics (NeurIPS 2025):** promote if serial neuron training becomes the dominant bottleneck or bit-shift-oriented hardware is a concrete target.
- **HetSyn: Versatile Timescale Integration in Spiking Neural Networks via Heterogeneous Synapses (NeurIPS 2025):** promote if SECNet requires substantially different learned timescales across channels or stages.
- **Efficient Spiking Point Mamba for Point Cloud Analysis (ICCV 2025):** structurally relevant to point data, but it introduces a Mamba-based global-modeling detour and an asymmetric SNN-ANN training route before the simpler SECNet-SNN baseline is established.
- **SpikeTrack / SDTrack (CVPR 2026):** valuable event-camera SNN systems and useful later comparisons, but their tracking-specific template/search and trajectory mechanisms are less reusable for SECNet's classification/action/pose backbone than the selected point and aggregation papers.
- **Meta-SpikeFormer, QKFormer, and Neural Dynamics Self-Attention:** strong generic Spiking Transformer references; use them when a generic 2D Transformer backbone becomes a live design option, not as the first Event Cloud architecture.

## 7. Recommendation

Adopt all eight as the proposed new Advisor reading set, but divide implementation authority:

- **architecture authority:** SpikePoint, Spiking Discrepancy Transformer, Spike-driven Discrete Aggregation;
- **controlled neuron and temporal ablations:** STEP, CLIF, Multi-Delay Mixer;
- **advanced optimization only after baseline convergence:** HD-LIF, SMixer.

The most defensible first baseline is therefore not “convert every SECNet operation to spikes.” It is:

> Preserve the ordered Event Cloud and SECNet hierarchy; introduce a clearly defined point-feature-to-spike interface; use PLIF as the initial neuron; retain continuous operations that cannot yet be justified as spike-native; then test CLIF, discrepancy attention, discrete aggregation, and delay mixing one axis at a time.
