# Advisor Core Reading Plan

Serves the **SECNet ICML 2026 oral to TPAMI extension** direction: Event Camera + frequency/Fourier + SNN. Mamba/SSM is outside the planned extension and is not part of the Advisor Core.

Current proceedings core: **8 papers**.

Composition: **5 required + 3 helpful**.
Helpful assignments are focused mechanism reads. They do not enroll an entire architecture or make Mamba/SSM part of the Advisor direction.

The bounded Advisor reading set is **9 papers**: 8 proceedings-corpus assignments and 1 external focus paper.

## Focus Paper

| Paper | Year | Venue | Assignment | Why it is included |
| --- | ---: | --- | --- | --- |
| Scalable Event Cloud Network for Event-based Classification (SECNet) | 2026 | ICML oral | focus | The TPAMI extension starts from SECNet. Its Event Cloud hierarchy already contains Spatial-FA and Temporal-FA FFT-filter-iFFT modules; the extension question is how to refine those frequency mechanisms and couple them to SNN computation. |

## Required Knowledge

| # | Paper | Year | Venue | Track | Assignment | Why it is core |
| ---: | --- | ---: | --- | --- | --- | --- |
| 1 | [Beyond Duality: A Hybrid Framework of Leveraging Shared and Private Features for RGB-Event Object Detection](../01-papers-by-conference/CVPR2026/B/2026-CVPR-B-beyond-duality-a-hybrid-framework-of-leveraging-shared-and-private-features-for-rgb-event-.md) | 2026 | CVPR | - | required | The PDF applies 2D FFT to RGB/event feature maps and uses power, cross spectra, and spectral coherence before iFFT, making it a direct event-side FFT design. |
| 2 | [Exploiting Frequency Dynamics for Enhanced Multimodal Event-based Action Recognition](../01-papers-by-conference/ICCV2025/B/2025-ICCV-B-exploiting-frequency-dynamics-for-enhanced-multimodal-event-based-action-recognition.md) | 2025 | ICCV | - | required | The PDF applies 3D FFT to stacked and reconstructed event frames, learns a frequency filter, and returns through iFFT, making it a direct event-side FFT representation design. |
| 3 | [SpikF: Spiking Fourier Network for Efficient Long-term Prediction](../01-papers-by-conference/ICML2025/C/2025-ICML-C-spikf-spiking-fourier-network-for-efficient-long-term-prediction.md) | 2025 | ICML | - | required | The official abstract establishes a Spiking Fourier Network with frequency-domain selection for long sequences, providing direct SNN-side Fourier foundations. |
| 4 | [FEEL-SNN: Robust Spiking Neural Networks with Frequency Encoding and Evolutionary Leak Factor](../01-papers-by-conference/NeurIPS2024/C/2024-NEURIPS-C-feel-snn-robust-spiking-neural-networks-with-frequency-encoding-and-evolutionary-leak-fact.md) | 2024 | NeurIPS | Main Conference Track | required | The PDF confirms input DFT, timestep-dependent frequency masks, and inverse DFT before the SNN, making FEEL-SNN a direct Fourier-to-SNN coupling mechanism. |
| 5 | [Frequency-aware Event-based Video Deblurring for Real-World Motion Blur](../01-papers-by-conference/CVPR2024/B/2024-CVPR-B-frequency-aware-event-based-video-deblurring-for-real-world-motion-blur.md) | 2024 | CVPR | - | required | The PDF uses 2D FFT for spatial feature filtering and 1D FFT over the flattened time-channel dimension for event/RGB fusion, providing a direct event-side FFT architecture. |

## Focused Helpful Mechanisms

| # | Paper | Year | Venue | Track | Assignment | Why it is core |
| ---: | --- | ---: | --- | --- | --- | --- |
| 6 | [Spiking Neural Networks Need High-Frequency Information](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-spiking-neural-networks-need-high-frequency-information.md) | 2025 | NeurIPS | Main Conference Track | helpful | Read as conceptual inspiration for the frequency bias of spiking neurons and the difference between frequency analysis and inserting an FFT module. |
| 7 | [SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md) | 2024 | ICLR | - | helpful | Read as Event Cloud + SNN inspiration for where frequency processing could connect to a sparse point-based spiking pipeline. |
| 8 | [Spiking Wavelet Transformer](../01-papers-by-conference/ECCV2024/C/2024-ECCV-C-spiking-wavelet-transformer.md) | 2024 | ECCV | - | helpful | The PDF places a sparse wavelet transform inside a spike-driven token mixer; it is a direct SNN time-frequency alternative, but wavelet is not FFT. |

## Coverage Map

### Event Cloud and point processing

[SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md)

### Grouping, sampling and aggregation

[SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md)

### Frequency-aware modeling

[Beyond Duality: A Hybrid Framework of Leveraging Shared and Private Features for RGB-Event Object Detection](../01-papers-by-conference/CVPR2026/B/2026-CVPR-B-beyond-duality-a-hybrid-framework-of-leveraging-shared-and-private-features-for-rgb-event-.md); [Exploiting Frequency Dynamics for Enhanced Multimodal Event-based Action Recognition](../01-papers-by-conference/ICCV2025/B/2025-ICCV-B-exploiting-frequency-dynamics-for-enhanced-multimodal-event-based-action-recognition.md); [SpikF: Spiking Fourier Network for Efficient Long-term Prediction](../01-papers-by-conference/ICML2025/C/2025-ICML-C-spikf-spiking-fourier-network-for-efficient-long-term-prediction.md); [Spiking Neural Networks Need High-Frequency Information](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-spiking-neural-networks-need-high-frequency-information.md); [FEEL-SNN: Robust Spiking Neural Networks with Frequency Encoding and Evolutionary Leak Factor](../01-papers-by-conference/NeurIPS2024/C/2024-NEURIPS-C-feel-snn-robust-spiking-neural-networks-with-frequency-encoding-and-evolutionary-leak-fact.md); [Frequency-aware Event-based Video Deblurring for Real-World Motion Blur](../01-papers-by-conference/CVPR2024/B/2024-CVPR-B-frequency-aware-event-based-video-deblurring-for-real-world-motion-blur.md); [Spiking Wavelet Transformer](../01-papers-by-conference/ECCV2024/C/2024-ECCV-C-spiking-wavelet-transformer.md)

### Fourier transform and FFT

[Beyond Duality: A Hybrid Framework of Leveraging Shared and Private Features for RGB-Event Object Detection](../01-papers-by-conference/CVPR2026/B/2026-CVPR-B-beyond-duality-a-hybrid-framework-of-leveraging-shared-and-private-features-for-rgb-event-.md); [Exploiting Frequency Dynamics for Enhanced Multimodal Event-based Action Recognition](../01-papers-by-conference/ICCV2025/B/2025-ICCV-B-exploiting-frequency-dynamics-for-enhanced-multimodal-event-based-action-recognition.md); [SpikF: Spiking Fourier Network for Efficient Long-term Prediction](../01-papers-by-conference/ICML2025/C/2025-ICML-C-spikf-spiking-fourier-network-for-efficient-long-term-prediction.md); [FEEL-SNN: Robust Spiking Neural Networks with Frequency Encoding and Evolutionary Leak Factor](../01-papers-by-conference/NeurIPS2024/C/2024-NEURIPS-C-feel-snn-robust-spiking-neural-networks-with-frequency-encoding-and-evolutionary-leak-fact.md); [Frequency-aware Event-based Video Deblurring for Real-World Motion Blur](../01-papers-by-conference/CVPR2024/B/2024-CVPR-B-frequency-aware-event-based-video-deblurring-for-real-world-motion-blur.md)

### Wavelet and localized time-frequency analysis

[Spiking Wavelet Transformer](../01-papers-by-conference/ECCV2024/C/2024-ECCV-C-spiking-wavelet-transformer.md)

### Scalability and efficiency

[SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md); [Spiking Wavelet Transformer](../01-papers-by-conference/ECCV2024/C/2024-ECCV-C-spiking-wavelet-transformer.md)

### Task and domain generalization

[Beyond Duality: A Hybrid Framework of Leveraging Shared and Private Features for RGB-Event Object Detection](../01-papers-by-conference/CVPR2026/B/2026-CVPR-B-beyond-duality-a-hybrid-framework-of-leveraging-shared-and-private-features-for-rgb-event-.md); [Exploiting Frequency Dynamics for Enhanced Multimodal Event-based Action Recognition](../01-papers-by-conference/ICCV2025/B/2025-ICCV-B-exploiting-frequency-dynamics-for-enhanced-multimodal-event-based-action-recognition.md); [Frequency-aware Event-based Video Deblurring for Real-World Motion Blur](../01-papers-by-conference/CVPR2024/B/2024-CVPR-B-frequency-aware-event-based-video-deblurring-for-real-world-motion-blur.md); [SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md)

### SNN and hybrid extensions

[SpikF: Spiking Fourier Network for Efficient Long-term Prediction](../01-papers-by-conference/ICML2025/C/2025-ICML-C-spikf-spiking-fourier-network-for-efficient-long-term-prediction.md); [Spiking Neural Networks Need High-Frequency Information](../01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-spiking-neural-networks-need-high-frequency-information.md); [FEEL-SNN: Robust Spiking Neural Networks with Frequency Encoding and Evolutionary Leak Factor](../01-papers-by-conference/NeurIPS2024/C/2024-NEURIPS-C-feel-snn-robust-spiking-neural-networks-with-frequency-encoding-and-evolutionary-leak-fact.md); [SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](../01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md); [Spiking Wavelet Transformer](../01-papers-by-conference/ECCV2024/C/2024-ECCV-C-spiking-wavelet-transformer.md)
