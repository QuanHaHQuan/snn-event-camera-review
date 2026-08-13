# Advisor Direction: Event Camera + Frequency + SNN

## Objective

The advisor direction is not an open-ended search for new ideas. The known extension direction is the combination of **event cameras, frequency modeling, and SNNs**, with FFT/Fourier methods as a central mechanism to understand. SECNet already applies Spatial-FA and Temporal-FA FFT-filter-iFFT modules inside its Event Cloud hierarchy. The reading goal is therefore to understand the existing frequency interfaces, their evidence, and how they can be refined and coupled to SNN computation. Mamba and SSM are explicitly outside the planned TPAMI extension. The bounded chain contains 14 papers: SECNet, the external TTPOINT predecessor, and 12 current proceedings-corpus assignments.

## Conceptual Sequence

1. **SECNet and Event Cloud lineage**
   - Read SECNet first as the focus paper and identify the exact inputs, transformed axes, filters, inverse transforms, and outputs of Spatial-FA and Temporal-FA, alongside its Event Cloud grouping and temporal pipeline.
   - Use `TTPOINT`, `PEPNet`, and `SpikePoint` to trace sparse event-point processing and the transition from non-spiking lightweight networks to a point-based SNN.

2. **Event-side frequency**
   - What frequency means for an asynchronous event stream.
   - How polarity, event rate, temporal windows, voxelization, and interpolation affect the signal being transformed.
   - Read `Beyond Duality`, `Frequency-aware Event-based Video Deblurring`, and `Exploiting Frequency Dynamics` as direct FFT designs.
   - Read only the detachable SCPG module in `AIMDepth` and the blur-event magnitude/phase mechanism in `Event-based Motion Deblurring with Unpaired Data`; neither whole architecture is a method-chain predecessor.

3. **Fourier/FFT and wavelet foundations**
   - DFT/FFT decomposes a sampled signal into global frequency components.
   - FFT gives frequency bins but does not by itself preserve precise time localization.
   - Wavelets provide localized multi-scale time-frequency analysis and are not the same operation as FFT.
   - Read `SpikF` for Fourier-based SNN processing and `Spiking Wavelet Transformer` for a wavelet-based SNN alternative.

4. **Frequency inside SNNs**
   - How spike trains and membrane dynamics respond to low/high-frequency input.
   - Whether the method transforms the input, hidden feature, attention/token mixing, or loss.
   - Read `Spiking Neural Networks Need High-Frequency Information` and `FEEL-SNN`.

5. **Coupling frequency with event representation and SNN computation**
   - Where the frequency transform is inserted: before SNN input, inside a block, between modalities, or in the objective.
   - Whether the transform operates over time, space, channels, or event density.
   - How complex amplitude/phase, magnitude-only features, high/low-pass bands, and sparsity interact with spikes.
   - Compare the direct FFT papers with `Spiking Wavelet Transformer`; wavelet is a localized time-frequency alternative, not a substitute term for FFT.
   - Use only PRE-Mamba's Event Cloud interface and 1D FFT regularization loss; the paper explicitly avoids an inference FFT layer.
   - Do not study the Mamba/SSM backbones in `AIMDepth` or `PRE-Mamba`; their enrollment is limited to the named separable mechanisms.

6. **Mapping back to SECNet**
   - Trace the exact Event Cloud tensors already processed by SECNet Spatial-FA and Temporal-FA, then compare alternative signals, axes, filters, and SNN coupling points.
   - Distinguish a frequency analysis tool, a learned frequency module, and a loss-only spectral constraint.
   - Check whether the proposed combination preserves asynchronous timing, polarity, sparsity, and scalability.
   - Compare claims using ablations and efficiency evidence rather than assuming FFT is automatically cheaper or more event-native.

## What to Extract From Each Paper

For every frequency-related paper, record the same mechanism trace:

1. **Signal**: raw events, event rate, voxel/tensor sequence, hidden feature, spike train, or multimodal feature.
2. **Sampling**: event window, timestep grid, interpolation, padding, or other operation that makes the signal transformable.
3. **Transform**: DFT/FFT, learned Fourier layer, high/low-pass decomposition, wavelet, or a non-Fourier frequency statistic.
4. **Axis**: time, space, channel, token, or event-density axis on which the transform is applied.
5. **Insertion point**: before the SNN, inside an SNN block, in an ANN branch, between modalities, or in the loss/objective.
6. **Spike interaction**: whether the frequency result is converted to spikes, modulates membrane dynamics, mixes spike tokens, or remains an ANN feature.
7. **Evidence**: ablation, accuracy/latency trade-off, event sparsity, energy estimate, or hardware measurement.

This trace prevents three common conflations: an event-rate statistic is not automatically an FFT, a wavelet is not an FFT, and operational/inference frequency is not Fourier frequency.

## Reading Assignment

The active list is `00-index/reading-plan-advisor-core.md`:

- external chain: SECNet is the focus paper and TTPOINT is the already-read predecessor;
- `advisor_required`: eight current-corpus papers needed for the Event Cloud and Fourier/SNN chain;
- `advisor_helpful`: four current-corpus focused reads; for AIMDepth and PRE-Mamba, read only the explicitly named FFT/Event Cloud mechanism, not the Mamba/SSM backbone;
- the generated file reports **12 current-corpus papers** and **14 papers in the complete knowledge chain**.
