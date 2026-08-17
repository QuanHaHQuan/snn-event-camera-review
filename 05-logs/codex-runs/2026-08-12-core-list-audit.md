# 2026-08-12 Core List Audit

## Scope And Evidence

- Audited all **351** records in `work/selection-corpus.jsonl` using the complete title and official abstract.
- Rechecked all **101** papers previously excluded from both tracks for missed direct SNN-event or Advisor-frequency relevance; two were restored after PDF review, leaving 99 current dual-excludes.
- Reverse-searched the corpus for direct event-camera + SNN evidence, Fourier/FFT/frequency methods, and Event Cloud/point processing.
- Used conference PDFs for twelve material boundary/mechanism checks and official abstracts for two additional boundary resolutions.
- Stored the complete evidence, abstract hashes, decisions, and boundary findings in the audit now named `00-index/candidate-screening-audit.csv`.

The audit establishes an evidence-backed current decision, not a claim that abstracts reveal every implementation detail. A later PDF correction must cite the contradictory evidence.

## Survey Core

The current Survey Core has **25 papers: 15 anchor + 2 included + 8 selected background**.

Added:

| Paper | Reason |
| --- | --- |
| A Simple and Effective Point-based Network for Event Camera 6-DOFs Pose Relocalization (PEPNet) | Fills the sparse Event Cloud, direct point-input, and lightweight non-spiking representation baseline needed before comparing SpikePoint and other event SNNs. |
| Efficient Learning of Event-based Dense Representation using Hierarchical Memories with Adaptive Update | Fills event-by-event dense representation, adaptive memory update, and latency comparison without conflating a non-spiking model with an SNN. |

Moved from Core to the reference pool:

| Paper | Reason |
| --- | --- |
| Brain-Inspired Spiking Neural Networks for Energy-Efficient Object Detection | Generic SNN detector; Gen1 is an evaluation setting rather than an event-specific method contribution. |
| Integer-Valued Training and Spike-driven Inference Spiking Neural Network for High-performance and Energy-efficient Object Detection (SpikeYOLO) | Generic SNN detection/training background; event data do not define the method. |
| Scaling Dense Event-Stream Pretraining from Visual Foundation Models | Useful event-side scaling reference, but not necessary for the first strict intersection reading pass. |
| V2V: Scaling Event-Based Vision through Efficient Video-to-Voxel Simulation | Useful simulation/scaling reference, but not a direct SNN-event mechanism. |
| DailyDVS-200 | Valuable benchmark, but task/dataset coverage alone does not require a Core deep read. |
| State Space Models for Event Cameras | Strong non-spiking temporal comparator, but SSM is not needed as a Core survey axis; its completed V2 remains reference evidence. |
| REDIR | Genuine but application-specific hybrid SNN block; redundant with stronger reconstruction and hybrid-boundary anchors for the first Core pass. |
| Spiking Neural Networks Need High-Frequency Information | Important for the Advisor frequency/SNN chain, but generic SNN frequency analysis is not required in the first event-camera-specific Survey Core pass. |

No direct event-camera + SNN `anchor` was omitted from Core. The two genuine but narrower `included` papers left outside Core are retained in the reference pool with explicit reasons: the 2025 surrogate-gradient attack is peripheral to the main architecture/training narrative, and REDIR is redundant for first-pass reconstruction/hybrid coverage.

## Advisor Core

The complete bounded knowledge chain has **14 papers**:

- SECNet: focus paper;
- TTPOINT: external advisor-group predecessor;
- 8 current-corpus `advisor_required` papers;
- 4 current-corpus `advisor_helpful` focused reads.

The 12 current-corpus assignments cover four non-substitutable needs:

1. SECNet/Event Cloud lineage: PEPNet and SpikePoint;
2. event-side FFT: Beyond Duality, Exploiting Frequency Dynamics, and Frequency-aware Event-based Video Deblurring;
3. SNN-side Fourier/frequency: SpikF, Spiking Neural Networks Need High-Frequency Information, and FEEL-SNN;
4. focused mechanism contrasts: AIMDepth's separable SCPG, EMP's magnitude/phase transfer, PRE-Mamba's loss-only FFT and Event Cloud interface, and Spiking Wavelet Transformer's non-FFT wavelet mixer.

SECNet itself already contains Spatial-FA and Temporal-FA FFT-filter-iFFT modules. The Advisor reading objective is not to discover where frequency first enters SECNet, but to understand those existing interfaces and evaluate how they can be refined and coupled to SNN computation.

The two papers with Mamba in their titles are not Mamba/SSM assignments: `AIMDepth` is included only for SCPG, and `PRE-Mamba` only for its Event Cloud interface and 1D FFT regularization loss. Their backbones remain out of scope.

Final changes relative to the previous committed Advisor assignment:

| Change | Paper | Reason |
| --- | --- | --- |
| added as required | Beyond Duality | Direct event-side 2D FFT, power/cross spectra, spectral coherence, and iFFT. |
| added as focused helpful | Event-based Motion Deblurring with Unpaired Data | Detachable magnitude/phase transfer mechanism with iFFT. |
| promoted helpful to required | FEEL-SNN | Direct DFT-mask-iDFT preprocessing coupled to an SNN. |
| narrowed required to focused helpful | Spiking Wavelet Transformer | Valuable SNN time-frequency contrast, but wavelet is not FFT. |
| removed | State Space Models for Event Cameras | Operational-frequency SSM generalization is outside the confirmed Fourier/SNN extension. |
| removed | A Chaotic Dynamics Framework | Continuous wavelet analysis plus a conventional classifier is reference-only, not a direct FFT/SNN mechanism. |
| removed | PASS | Its frequency refers to event-window/inference rate and its SSM backbone is out of scope. |
| removed | FLAME | Its SSM memory is outside Advisor scope; its LIF event feature extractor remains Survey evidence. |
| removed | EventMG | Its Event Cloud hierarchy remains a reference, but the Mamba mechanism is outside Advisor scope. |

Additional candidates explicitly kept out of Advisor Core during this audit:

| Paper | Reason |
| --- | --- |
| Temporal Residual Guided Diffusion Framework for Event-Driven Video Reconstruction | Uses semantic low/high-frequency priors in a diffusion reconstruction pipeline, but supplies neither an FFT mechanism nor SNN coupling. |
| Towards Robust Event-based Networks for Nighttime via Unpaired Day-to-Night Event Translation | Wavelet-based domain translation addresses nighttime adaptation, not SECNet Event Cloud, FFT insertion, or SNN coupling. |

The old `ssm_mamba_memory` Advisor topic was retired across the corpus. Mamba/SSM papers may remain Survey references when they offer a specific event-temporal comparator, but they no longer count as Advisor method-chain evidence.

## Boundary Checks

- PPLNs propagates real-valued outputs and explicitly distinguishes itself from SNNs.
- FEEL-SNN applies DFT, timestep-varying masks, and inverse DFT before the SNN.
- Frequency-aware Event-based Video Deblurring applies spatial 2D FFT and a separate 1D FFT over the flattened time-channel dimension.
- Exploiting Frequency Dynamics applies 3D FFT and inverse FFT to event-derived frame representations.
- Beyond Duality applies 2D FFT, power/cross spectra, spectral coherence, and inverse FFT.
- Spiking Neural Networks Need High-Frequency Information uses Fourier/Z-domain analysis but high-pass network operators rather than an FFT layer.
- Spiking Wavelet Transformer uses a sparse wavelet transform; wavelet is not FFT.
- A Chaotic Dynamics Framework uses continuous wavelet analysis with a conventional classifier; its abstract does not establish a binary SNN pipeline and it remains reference-only.
- SpikF is explicitly a Spiking Fourier Network; its exact transformed axes remain a deep-reading question.
- AIMDepth's SCPG is separable from its Mamba backbone and applies 2D FFT, amplitude replacement, phase injection, and iFFT.
- Event-based Motion Deblurring with Unpaired Data transfers blur-event magnitude cues while preserving phase before iFFT.
- PRE-Mamba uses 1D FFT in a sequence-level regularization loss and explicitly avoids an inference FFT layer.
- Event-Based Motion Magnification uses pixel-wise temporal Fourier filtering but remains Advisor reference-only because its fixed band-pass module is narrow and non-spiking.

## Current-Corpus Limitation

This audit only settles the current 2024--2026 proceedings corpus. It does not make the survey bibliography historically complete. Classic pre-2024 event representation, foundational SNN, early SNN-event integration, datasets, and hardware papers require a later backward-search stage anchored to the finalized outline and the references of Core papers.
