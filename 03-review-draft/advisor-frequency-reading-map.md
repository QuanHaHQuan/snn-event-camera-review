# Advisor 方向阅读图：SECNet + Frequency + SNN

## 一、目标与边界

本方向服务于 **SECNet ICML 2026 oral 的 TPAMI 扩展**。目标已经确定为：

**Event Camera + frequency/Fourier，尤其是 FFT + SNN。**

这不是开放式 idea 搜索，也不需要建立庞大的方法谱系。Mamba/SSM 不属于本次扩展方向，不进入 Advisor Core。

当前限定阅读集共 **9 篇**：

- 1 篇 focus paper：SECNet；
- 5 篇直接机制论文；
- 3 篇启发性论文。

完整名单由 [Advisor Core Reading Plan](../00-index/reading-plan-advisor-core.md) 生成和维护。

## 二、Focus Paper

### SECNet

首先完整理解 SECNet：

1. Event Cloud 如何构建和分层处理；
2. Spatial-FA 与 Temporal-FA 的输入 tensor；
3. FFT 沿哪个轴执行；
4. 频域 filter 如何学习；
5. iFFT 后的结果流向哪里；
6. 现有 frequency path 与未来 SNN 模块可能在哪里连接。

后续论文都用于回答一个问题：**它提供的频率机制或 SNN 接口，能否帮助分析或改进 SECNet 已有设计？**

## 三、五篇直接机制论文

### Event-side FFT

1. **Beyond Duality**
   - 关注 RGB/event feature 的 2D FFT、power spectrum、cross spectrum、spectral coherence 和 iFFT。
   - 用于理解跨模态频谱如何区分 shared/private features。

2. **Exploiting Frequency Dynamics for Enhanced Multimodal Event-based Action Recognition**
   - 关注 stacked/reconstructed event frames 上的 3D FFT、learned frequency filter 和 iFFT。
   - 用于比较不同 event representation 进入频域后的信息差异。

3. **Frequency-aware Event-based Video Deblurring for Real-World Motion Blur**
   - 关注 spatial 2D FFT 与 flattened time-channel 1D FFT。
   - 用于区分 spatial frequency、temporal dependency 与 cross-modal fusion。

### SNN-side Fourier

4. **SpikF**
   - 关注 frequency-domain selection 如何进入 spiking long-sequence model。
   - 核查 transform axis、spike interaction 和 energy evidence，不能只依赖摘要中的效率结论。

5. **FEEL-SNN**
   - 关注 input DFT、timestep-dependent frequency mask、inverse DFT 与 SNN 的接口。
   - 用于理解 Fourier processing 放在 SNN 输入前时解决什么问题、保留什么信息。

## 四、三篇启发性论文

1. **Spiking Neural Networks Need High-Frequency Information**
   - 用于理解 spiking neuron 的 frequency bias。
   - 它提供的是 Fourier/Z-domain analysis 和 high-frequency motivation，不是 FFT module 范例。

2. **SpikePoint**
   - 用于理解 sparse Event Cloud 如何直接进入 point-based SNN。
   - 重点思考 frequency module 可以放在 event grouping、point feature、spike encoding 或 hidden state 的哪个位置。

3. **Spiking Wavelet Transformer**
   - 用于比较 localized wavelet 与 global Fourier transform。
   - Wavelet 是 time-frequency alternative，不能和 FFT 混称。

## 五、不再属于 Core 的论文

以下论文保留为可选 reference，但不要求当前阅读：

- AIMDepth：Mamba backbone 不相关，SCPG 仅在需要 amplitude/phase cross-modal prior 时回查；
- PRE-Mamba：Mamba/SSM 不相关，loss-only FFT 不属于优先机制；
- Event-based Motion Deblurring with Unpaired Data：magnitude/phase modulation 可按需回查；
- TTPOINT、PEPNet：保留为 Event Cloud lineage 背景，不作为当前扩刊必读。

被移出 Advisor Core 不代表论文被删除，也不影响它们在 Survey、reference pool 或历史 V2 中的其他用途。

## 六、统一提取框架

阅读每篇 frequency 论文时只记录以下内容：

1. **Signal**：raw events、event frame/voxel、Event Cloud、hidden feature 或 spike train；
2. **Sampling**：如何把 asynchronous events 变成可执行 transform 的信号；
3. **Transform**：FFT/DFT、learned Fourier、filter 或 wavelet；
4. **Axis**：time、space、channel、token 或 event-density；
5. **Insertion point**：SNN 前、SNN 内部、ANN branch、multimodal fusion 或 loss；
6. **Spike interaction**：frequency result 如何影响 encoding、membrane、spike token 或 output；
7. **Evidence**：ablation、accuracy、latency、operation estimate 或 hardware measurement。

必须区分：

- frequency analysis 与可训练 FFT module；
- Fourier frequency 与运行频率；
- FFT 与 wavelet；
- arithmetic estimate 与真实 hardware efficiency。

## 七、建议阅读顺序

1. SECNet；
2. Exploiting Frequency Dynamics；
3. Frequency-aware Event-based Video Deblurring；
4. Beyond Duality；
5. FEEL-SNN；
6. SpikF；
7. Spiking Neural Networks Need High-Frequency Information；
8. SpikePoint；
9. Spiking Wavelet Transformer。

完成后只需形成一张对照表，比较 signal、axis、transform、insertion point、SNN coupling 和 evidence，然后回到 SECNet 标出可借鉴与不可直接迁移的机制。
