# Outline Checkpoint 01: 11 Survey V2 Papers

Date: 2026-08-12

Historical evidence base: **11 papers from the pre-audit 31-paper Survey Core, all with human-guided Summary V2**.

Composition at the time: **7 anchor + 2 included + 2 background**. All eleven papers are from 2024. This checkpoint tests the structure of the survey; it does not finalize the outline, change Survey Core membership, or assign section citation quotas.

> Audit note (2026-08-12): the current Survey Core is 25 papers. `State Space Models for Event Cameras`, `DailyDVS-200`, and `REDIR` are now reference-only; their V2 evidence remains valid. `PEPNet` and `Efficient Learning of Event-based Dense Representation`, both already read, entered the current Core but were not part of this checkpoint. Current Core V2 progress is therefore 10/25. The observations below are preserved as the historical Checkpoint 01 record.

## Checkpoint Conclusions

1. **The parallel-foundation structure holds.** Event representation and SNN computation are independent axes. DailyDVS-200 explicitly shows that representation and backbone are separate experimental choices, while SpikePoint, SFOD, and EAS-SNN show different ways of combining them.
2. **Slicing is not representation.** SpikeSlicer establishes a pipeline boundary between choosing an event group's temporal extent and encoding that group. EAS-SNN partly couples the two, but it still begins with fixed early aggregation. Chapter 2 must therefore separate temporal organization from representation.
3. **Dense versus sparse is necessary but insufficient.** The same representation family can support very different SNN roles. The intersection chapter also needs integration topology: task network, hybrid module, event-interface controller, or inference/optimization engine.
4. **Sensor events are not automatically neural spikes.** Raw event tuples, event groups, voxel/point inputs, Poisson-encoded model inputs, internal neuronal spikes, and decoded continuous features are distinct objects and must be traced explicitly.
5. **`Fully spiking` needs a declared system boundary.** A spiking backbone with an analog detection head, a fully spiking network preceded by conventional point grouping, and a spike-driven latent model containing continuous operations cannot be treated as equivalent end-to-end systems.
6. **Event-specific learning deserves explicit treatment.** The read set includes spike-aware sampling losses, relevance-guided augmentation, task-guided slicing, optimization-inspired latent coding, and WTA/STDP Bayesian inference. These are more than generic surrogate-gradient variants.
7. **Efficiency evidence must be stratified.** Most current claims are operation-count or device-model estimates. None of the eleven provides end-to-end neuromorphic hardware energy evidence. Firing rate, arithmetic estimates, GPU runtime, and measured device energy cannot be merged into one efficiency number.
8. **Tasks remain an evidence axis, not the primary method taxonomy.** Detection, recognition, reconstruction, motion segmentation, tracking support, and security reveal different requirements, but organizing the whole survey by task would hide shared representation and SNN mechanisms.

## Evidence Map

| Paper | Event organization / representation | SNN role and integration topology | Training or inference mechanism | Task / evidence contribution | Efficiency evidence |
| --- | --- | --- | --- | --- | --- |
| SFOD | Fixed-window voxel cube | Spiking backbone and fusion, decoded conventional SSD head; hybrid task network | Direct surrogate-gradient training; rate decoding and loss matching | Object detection; multi-scale fusion and spike-to-analog interface | Estimated energy, firing rate, and reported runtime; no hardware measurement |
| State Space Models for Event Cameras | Dense tensors from fixed event windows | Non-spiking continuous-time comparator | S4D/S5 state dynamics and frequency regularization | Detection; cross-frequency generalization and long-memory comparator | GPU/runtime-style evidence; no spiking or neuromorphic evidence |
| DailyDVS-200 | Event frames, learned/token/spike representations benchmarked separately from backbones | Dataset paper; SNNs are evaluated baselines | Temporal integration interval and frame-gap study | Action recognition, real-world attributes, moving-camera robustness | No SNN energy or latency evaluation |
| EAS-SNN | Fixed early event-count bins followed by adaptive sampling and potential aggregation | SNN forms representation and may feed fully spiking or hybrid detector | SAT and RPD address threshold-aware training and non-firing shortcuts | Object detection; task-driven event sampling | Operation-level energy estimate and FPS; no hardware measurement |
| Raw-event adversarial attacks on SNNs | Sparse raw COO events reparameterized as three-state candidates | Attacks an existing event-SNN pipeline rather than proposing a backbone | Gumbel-Softmax, STE, and SNN surrogate gradients | Robustness/security of the raw-event interface | No deployment-efficiency claim |
| REDIR | Dense event frames and registered multi-scale features | SNN temporal filter inside ANN registration and reconstruction pipeline | Conventional losses; SNN details only partially specified | De-occlusion reconstruction; application-oriented hybrid example | No energy, latency, or operation evidence |
| Spike-Temporal Latent Representation | Event voxel, then per-pixel temporal vectors | Spiking latent encoder and SNN decoder; optimization/inference topology | Non-negative LASSO/ISTA unfolding, FPA loss, surrogate gradients | Event-to-video reconstruction and structured latent coding | Theoretical arithmetic-energy proxy; no hardware measurement |
| EventRPG | Event sequences used by existing SNN classifiers | SNN is the target model; contribution is training and interpretability | Layer/time relevance propagation, RPGDrop, and RPGMix | Classification, generalization, and model-aware augmentation | GPU augmentation runtime only; not energy evidence |
| SpikePoint | Windowed sparse pseudo-point cloud, grouping, then Poisson rate encoding | Directly trained point-based SNN task network | BPTT, surrogate gradient, spike-compatible residual path | Action recognition; sparse representation and architecture coupling | Operation/SRAM model estimate; preprocessing cost incomplete |
| Spike-based Bayesian computation | Chronological event packets, warping, and IWE | WTA/STDP inference engine in a hybrid event-motion framework | Stochastic WTA approximates E-step; STDP-like updates approximate M-step | Unsupervised online motion segmentation proof of concept | Neuromorphic motivation only; no quantitative efficiency evidence |
| SpikeSlicer | Fine fixed voxel cells dynamically grouped before downstream representation | SNN event-interface controller with downstream ANN | SPA-Loss and alternating task-feedback update | Adaptive slicing for recognition and tracking | Operation-model estimate plus software latency; no hardware measurement |

## Outline Decisions Applied

The working [survey outline](../outline.md) is revised in five places:

1. Chapter 2 now separates **temporal slicing/sampling** from **representation encoding**.
2. Chapter 3 now requires an explicit boundary for fully spiking, hybrid, converted, and non-spiking systems.
3. Chapter 4 uses **SNN integration topology** in addition to dense/sparse representation.
4. Chapter 5 adds datasets, temporal protocols, robustness/security, and an evidence hierarchy.
5. Chapter 6 adds a task-by-topology view and requires efficiency claims to be separated by evidence type.

The six-chapter macro-structure is retained. The current evidence supports refinement inside the chapters, not replacing the parallel-foundation design.

## What The Eleven Papers Already Support

### Chapter 2: Sensor-Side Axis

- Fixed temporal windows and temporal bins: SFOD, STLR, DailyDVS-200, SSM.
- Adaptive sampling or slicing: EAS-SNN and SpikeSlicer.
- Dense event tensors and voxel representations: SFOD, EAS-SNN, STLR, SSM, REDIR.
- Sparse point or raw-event representations: SpikePoint and the raw-event attack paper.
- Sensitivity to temporal granularity: DailyDVS-200, SSM, and SpikeSlicer.

### Chapter 3: SNN-Side Axis

- Membrane dynamics and spike-time decisions: EAS-SNN and SpikeSlicer.
- Direct surrogate-gradient training: SFOD, EAS-SNN, EventRPG, SpikePoint, and STLR.
- Local or alternative learning: WTA/STDP Bayesian computation.
- Structured spike coding: SpikePoint's rate encoding and STLR's unfolding-depth spike rate.
- Hybrid boundaries and decoded outputs: SFOD, REDIR, EAS-SNN, and STLR.

### Chapter 4: Intersection

- SNN as task backbone or decoder: SFOD, SpikePoint, STLR.
- SNN as hybrid temporal module: REDIR.
- SNN as representation/sampling mechanism: EAS-SNN.
- SNN as event-interface controller: SpikeSlicer.
- SNN as inference engine: spike-based Bayesian computation.
- Event-SNN-specific training and robustness: EventRPG and the raw-event attack paper.

### Chapter 5: Tasks And Evidence

- Recognition: SpikePoint, EventRPG, DailyDVS-200, and SpikeSlicer.
- Detection: SFOD and EAS-SNN; SSM provides a non-spiking temporal comparator.
- Reconstruction: STLR and REDIR.
- Motion segmentation: spike-based Bayesian computation.
- Tracking: only indirect evidence through SpikeSlicer; no dedicated SNN tracker has yet been read.
- Security: raw-event adversarial attacks.

## Evidence Gaps For The Current 16 Missing Core Papers

These are reading priorities for outline validation, not reasons to promote or demote papers.

1. **Tracking and frame-event fusion:** SDTrack, SpikeTrack, SpikeFET.
2. **Newer 2025/2026 integration patterns:** EventGait, SDA, ClearSight, hybrid event detector, HsVT.
3. **Long-context hybrid memory:** FLAME, to test whether it fits the topology-based intersection without turning SSM/Mamba into a survey axis.
4. **ANN-SNN conversion:** Inference-Scale Complexity, currently absent from the V2 evidence.
5. **Generic SNN temporal/training foundations:** CLIF and Temporal Flexibility.
6. **Fair efficiency evaluation:** STEP and the quantization perspective.
7. **Hardware evidence:** the 2025 hybrid detector and newer tracking/detection papers must be checked for actual device measurement versus arithmetic proxies.
8. **Event-side temporal organization:** ASTW must test whether the slicing/representation distinction holds under heterogeneous velocity.
9. **Frequency mechanisms:** SNN high-frequency information and later intersection papers must determine whether frequency remains a cross-cutting mechanism or needs a dedicated subsection.

## Deferred Questions

- Whether the four integration topologies are stable after the 2025/2026 papers, or whether some should be merged.
- Whether ANN-SNN conversion deserves its own intersection subsection or remains SNN-side background.
- Whether tracking and detection should share a dense-prediction subsection before task-specific evidence is presented.
- Whether frequency modeling has enough direct SNN-event evidence for more than an open-problem discussion.
- Whether any current paper supports an end-to-end measured energy advantage over a strong ANN baseline.
- Which quantitative comparison tables are feasible once datasets, timesteps, preprocessing, and hardware conditions are normalized.

## Next Checkpoint Trigger

Run Checkpoint 02 after a coherent group of newer integration papers is complete, preferably including at least:

- one dedicated SNN event tracker;
- one 2025/2026 detector;
- one conversion or generic SNN efficiency paper;
- one paper with claimed hardware evidence;
- FLAME or another long-context hybrid method.

Checkpoint 02 should test the four integration topologies and the evidence hierarchy. Final outline V1.0 remains gated on completion of all Survey Core V2 papers and a final section-level reference allocation pass.
