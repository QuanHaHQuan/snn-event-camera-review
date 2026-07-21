# Advisor Direction: Event Camera + Frequency + SNN

## Objective

The advisor direction is not an open-ended search for new ideas. The known extension direction is the combination of **event cameras, frequency modeling, and SNNs**, with FFT/Fourier methods as a central mechanism to understand. The reading goal is to understand the mechanism, its evidence, and how it could attach to the SECNet event representation and temporal pipeline. The 15-paper list is a bounded knowledge chain, not a second survey corpus.

## Conceptual Sequence

1. **Event-side frequency**
   - What frequency means for an asynchronous event stream.
   - How polarity, event rate, temporal windows, voxelization, and interpolation affect the signal being transformed.
   - Read `Frequency-aware Event-based Video Deblurring`, `Exploiting Frequency Dynamics`, and `A Chaotic Dynamics Framework`.

2. **Fourier/FFT and wavelet foundations**
   - DFT/FFT decomposes a sampled signal into global frequency components.
   - FFT gives frequency bins but does not by itself preserve precise time localization.
   - Wavelets provide localized multi-scale time-frequency analysis and are not the same operation as FFT.
   - Read `SpikF` for Fourier-based SNN processing and `Spiking Wavelet Transformer` for a wavelet-based SNN alternative.

3. **Frequency inside SNNs**
   - How spike trains and membrane dynamics respond to low/high-frequency input.
   - Whether the method transforms the input, hidden feature, attention/token mixing, or loss.
   - Read `Spiking Neural Networks Need High-Frequency Information` and `FEEL-SNN`.

4. **Coupling frequency with event representation and SNN computation**
   - Where the frequency transform is inserted: before SNN input, inside a block, between modalities, or in the objective.
   - Whether the transform operates over time, space, channels, or event density.
   - How complex amplitude/phase, magnitude-only features, high/low-pass bands, and sparsity interact with spikes.
   - Use `State Space Models for Event Cameras`, `PASS`, `PRE-Mamba`, `FLAME`, and `EventMG` as temporal/state and representation comparators. Mamba/SSM is a temporal state model, not automatically an FFT method.

5. **Mapping back to SECNet**
   - Identify the exact SECNet representation tensor or Event Cloud sequence where frequency information could enter.
   - Distinguish a frequency analysis tool from a learned frequency module.
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

This trace prevents three common conflations: an event-rate statistic is not automatically an FFT, a wavelet is not an FFT, and an SSM/Mamba memory block is not a frequency-domain method merely because it models long temporal context.

## Reading Assignment

The active list is `00-index/reading-plan-advisor-core.md`:

- `advisor_required`: the ten papers needed for the frequency/SNN/event-camera chain;
- `advisor_helpful`: five papers for directly relevant comparison or inspiration;
- SECNet itself is the focus paper and is not counted in the corpus total.
