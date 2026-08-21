# Advisor V2 Index

Human-guided reading progress for the SECNet to TPAMI extension direction: Event Camera + frequency/Fourier + SNN.

Progress: **3/9 complete**, **6 missing**.

A V2 paper has one canonical file in `../papers/`. This index records its track-specific purpose; it does not duplicate the summary.

| # | Paper | Year | Venue | Assignment | Status | V2 | Track purpose |
| ---: | --- | ---: | --- | --- | --- | --- | --- |
| 1 | Beyond Duality: A Hybrid Framework of Leveraging Shared and Private Features for RGB-Event Object Detection | 2026 | CVPR | required | missing | - | The PDF applies 2D FFT to RGB/event feature maps and uses power, cross spectra, and spectral coherence before iFFT, making it a direct event-side FFT design. |
| 2 | Scalable Event Cloud Network for Event-based Classification (SECNet) | 2026 | ICML oral | focus | missing | - | Focus paper for the TPAMI extension. SECNet already contains Spatial-FA and Temporal-FA FFT-filter-iFFT modules; read their exact signals, axes, and interfaces before assessing how the existing frequency path can be refined and coupled to SNNs. |
| 3 | Exploiting Frequency Dynamics for Enhanced Multimodal Event-based Action Recognition | 2025 | ICCV | required | missing | - | The PDF applies 3D FFT to stacked and reconstructed event frames, learns a frequency filter, and returns through iFFT, making it a direct event-side FFT representation design. |
| 4 | SpikF: Spiking Fourier Network for Efficient Long-term Prediction | 2025 | ICML | required | missing | - | The official abstract establishes a Spiking Fourier Network with frequency-domain selection for long sequences, providing direct SNN-side Fourier foundations. |
| 5 | Spiking Neural Networks Need High-Frequency Information | 2025 | NeurIPS | helpful | missing | - | Read as conceptual inspiration for the frequency bias of spiking neurons and the difference between frequency analysis and inserting an FFT module. |
| 6 | FEEL-SNN: Robust Spiking Neural Networks with Frequency Encoding and Evolutionary Leak Factor | 2024 | NeurIPS | required | missing | - | The PDF confirms input DFT, timestep-dependent frequency masks, and inverse DFT before the SNN, making FEEL-SNN a direct Fourier-to-SNN coupling mechanism. |
| 7 | Frequency-aware Event-based Video Deblurring for Real-World Motion Blur | 2024 | CVPR | required | complete | [2024-CVPR-frequency-aware-event-based-video-deblurring-for-real-world-motion-blur-v2.md](../papers/2024-CVPR-frequency-aware-event-based-video-deblurring-for-real-world-motion-blur-v2.md) | The PDF uses 2D FFT for spatial feature filtering and 1D FFT over the flattened time-channel dimension for event/RGB fusion, providing a direct event-side FFT architecture. |
| 8 | SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition | 2024 | ICLR | helpful | complete | [2024-ICLR-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recognition-v2.md](../papers/2024-ICLR-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recognition-v2.md) | Read as Event Cloud + SNN inspiration for where frequency processing could connect to a sparse point-based spiking pipeline. |
| 9 | Spiking Wavelet Transformer | 2024 | ECCV | helpful | complete | [2024-ECCV-spiking-wavelet-transformer-v2.md](../papers/2024-ECCV-spiking-wavelet-transformer-v2.md) | The PDF places a sparse wavelet transform inside a spike-driven token mixer; it is a direct SNN time-frequency alternative, but wavelet is not FFT. |
