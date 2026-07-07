---
title: "Spiking Neural Network as Adaptive Event Stream Slicer"
authors: ["Jiahang Cao", "Mingyuan Sun", "Ziqing Wang", "Hao Cheng", "Qiang Zhang", "Shibo Zhou", "Renjing Xu"]
year: 2024
venue: "NeurIPS"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2024/A/2024-NEURIPS-A-spiking-neural-network-as-adaptive-event-stream-slicer.md"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/893a5db6100028ec814cfd99fe92c31b-Abstract-Conference.html"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/893a5db6100028ec814cfd99fe92c31b-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "adaptive slicing", "SpikeSlicer", "SPA-Loss", "SNN-ANN cooperation", "tracking", "recognition"]
---

# Summary V1｜Spiking Neural Network as Adaptive Event Stream Slicer

## 1. One-sentence Summary

SpikeSlicer 用低功耗 SNN 作为 adaptive event stream slicer，通过 SPA-Loss 和 Feedback-Update strategy 从 downstream ANN 反馈中学习 slicing time，并提升 event-based tracking 与 recognition 性能。

## 2. Research Problem

许多 event-based algorithms 在进入下游任务前使用 fixed duration 或 fixed event count slicing。固定 slicing 无法适应不同速度、对象大小和事件密度，可能在高速场景产生 blur 或在低速场景产生 sparse/unstable texture。

本文要解决的是 event stream preprocessing / slicing 问题：如何让 slicing 由 event information 自适应决定，而不是手工固定窗口。

## 3. Background and Motivation

event cameras 产生异步稀疏事件，具有高时间分辨率和低功耗。事件流在用于 tracking、recognition、detection 等任务前通常要转换为 event frame、voxel grid、time surface、graph 或 point representation。slicing 的好坏直接影响表示质量。

SNN 的 spike firing 可以天然作为“触发切片”的信号：当输入事件累积到足够信息量，spiking neuron firing，就切出一个 event group。

## 4. Method Overview

SpikeSlicer 先把 event stream 转成连续 event cells；event cells 逐步输入 SNN；当 SNN output neuron fires spike 时，当前时间到上一次 spike 之间的 raw events 被切成 event group；该 group 可转换为任意 downstream representation。

训练上，作者提出 SPA-Loss 控制 SNN 在期望 timestamp firing；再用 Feedback-Update strategy 从 downstream ANN 的 loss 反馈中确定 desired slicing time。输出是动态切分后的 event groups，供 tracker / recognizer 使用。

## 5. Technical Details

### Event Representation

event stream 被表示为一系列 event cells，每个 cell 对应短时间 interval。SpikeSlicer 本身不绑定具体 event representation，切片后的 event group 可转成 frame、point、graph、surface、voxel grid 等。

### Spiking Neuron / SNN Module

SNN 最后一层 hidden features 经过 FC 和 LIF neuron 映射到单个 output spike。若 `S_out = 1`，则触发 slicing action。spike time 直接决定 event group 的边界。

### Network Architecture

论文提供 SpikeSlicer-Base 和 SpikeSlicer-Small。Small 版本只有 0.42M params，0.56G OPs，0.69 mJ energy，在 PrDiMP tracking 上达到 comparable/better performance。

### Training Strategy

Feedback-Update strategy 分两阶段：ANN 对候选 slicing positions 给出 loss feedback，SNN 用反馈确定 desired spike index 并通过 SPA-Loss 更新；随后用 SNN 新切出的 event data fine-tune ANN，形成 SNN-ANN cooperation。

### Loss Function

SPA-Loss = Mem-Loss + LA-Loss。Mem-Loss 直接约束 no-reset membrane potential 在 desired time step 达到阈值附近；LA-Loss 解决 neighboring membrane potentials 的 hill effect，使 spike time 更精确。dynamic alpha tuning 避免固定 alpha 在不同任务中造成不稳定。

### Inference Process

推理时 SNN 连续读 event cells，spike 输出决定切片，不再需要下游 ANN 对候选点搜索反馈。下游 ANN 使用动态切出的 event representations 执行 tracking / recognition。

## 6. Experiments

Beginner's arena 验证 SPA-Loss 能让 SNN 在指定 time step firing。Figure 4 显示 SPA-Loss 少于 400 iterations 即可监督 SNN 正确 firing，而 MSE/CE loss 不能稳定完成。

Expert's arena 包含 event-based object tracking 和 recognition。Table 1 在 FE108 上比较多个 tracker。以 TransT 为例，fixed event ALL RSR 为 51.0，TransT+SpikeSlicer-S 达到 63.6；OP0.50 从 59.0 提升到 82.3，OP0.75 从 12.0 提升到 37.5，RPR 从 78.8 到 90.1。

Table 2 在 DVS-Gesture、N-Caltech101、DVS-CIFAR10、SL-Animals 上比较 Random/Fix/Ours slicing。ResNet-34 使用 SpikeSlicer 在 DVS-Gesture 为 96.18，N-Caltech101 为 82.54，DVS-CIFAR10 为 82.23，SL-Animals 为 89.93，均高于 fixed slicing。

Table 3 分析 efficiency：TransT w/o SpikeSlicer 为 56.36G OPs、259.26 mJ、0.045 s/img、performance 51.0；w/ SpikeSlicer 为 57.09G OPs、260.11 mJ、0.060 s/img、performance 62.4。即额外 0.85 mJ 和少量速度下降换来 22.3% RSR 提升。

Table 4 显示 SpikeSlicer 对 Time Surface、Event Spike Tensor、Voxel Grid，以及 Event Frame 等 representation 都有效。Table 5 显示 Mem-Loss 和 LA-Loss 均贡献性能。Table 7 显示 SpikeSlicer-Small 0.42M params，反而略优于 Base。

## 7. Main Contributions

1. 提出用 SNN spike firing 作为 adaptive event slicing trigger。
2. 提出 SPA-Loss，使 SNN 能在 desired time step 精确 firing。
3. 提出 Feedback-Update strategy，实现 SNN-ANN cooperative slicing。
4. 在 event-based tracking 和 recognition 上证明 dynamic slicing 优于 fixed slicing。
5. 展示 SpikeSlicer 作为 plug-and-play slicer 可适配多种 event representations。

## 8. Limitations and Risks

作者明确指出训练是 multi-stage SNN-ANN process，adaptive slicing strategy 还有改进空间。

recognition tasks 中为了得到准确 supervisory signal，论文把 event stream 转为 single-frame representation；未来还需扩展到 multi-frame representation。

实验在 GPUs 上完成，而 SNN 更适合 brain-inspired chips；GPU 上动态实时生成事件并处理可能导致整体 inference 更慢。

SpikeSlicer 增加少量 energy 和 latency，对实时系统是否值得取决于任务。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

它把 SNN 用在 event preprocessing 的关键位置：adaptive slicing。该文对 survey 很有价值，因为它展示 SNN 不一定只是最终 classifier/detector，也可以是低功耗 event data processor。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：adaptive slicing before representation。
- Hybrid ANN-SNN models：SNN slicer + ANN downstream。
- Event-based tracking：FE108 tracking。
- SNN training methods：SPA-Loss、Feedback-Update。
- Efficiency, latency, and energy：OPs、energy、speed。
- Open challenges：real-time neuromorphic deployment。

## 11. Key Terms and Concepts

- SpikeSlicer：SNN-based adaptive event stream slicer。
- Event cell：短时间间隔中的事件单元。
- SPA-Loss：Spiking Position-aware Loss。
- Mem-Loss / LA-Loss：控制 spike timing 的两个 loss components。
- Feedback-Update：downstream ANN feedback guides SNN slicing。
- RSR / RPR / OP：tracking metrics。

## 12. Questions for Human Deep Reading

1. ANN feedback 的 candidate search 范围 d 如何影响训练成本？
2. SpikeSlicer 推理阶段是否完全无需 ANN feedback？
3. Table 3 的 performance 51.0/62.4 具体对应哪个 tracking metric？
4. GPU inference 变慢与 neuromorphic hardware 预期加速之间如何平衡？
5. SpikeSlicer 是否会造成 event group 数量不稳定？
6. single-frame representation limitation 对 recognition 结果有多大影响？
7. Small 版本为何优于 Base，是否有 overfitting？
8. 是否可与 EAS-SNN adaptive sampling 统一到同一 taxonomy？

## 13. Evidence Notes

- Section 3.2，第 4 页：adaptive event slicing process。
- Section 3.3，第 4-6 页：SPA-Loss、Mem-Loss、LA-Loss、dynamic alpha。
- Algorithm 1-2，第 6 页：slicing and Feedback-Update。
- Section 4.1，第 7 页：beginner's arena。
- Table 1-2，第 8 页：tracking and recognition results。
- Table 3-7，第 9-10 页：efficiency and ablations。
- Section 5，第 10 页：limitations。

## 14. Draft Survey-Usable Sentences

Draft material: SpikeSlicer uses SNNs as adaptive event processors, where output spikes define the boundaries of event groups for downstream ANN models.

Draft material: The method is a useful example of SNN-ANN cooperation before task inference, not merely at feature extraction or classification layers.

Draft material: Its limitations highlight that adaptive slicing still needs more direct neuromorphic and real-time validation.

