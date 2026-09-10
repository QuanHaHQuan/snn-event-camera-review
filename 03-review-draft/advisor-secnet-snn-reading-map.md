# Advisor 方向阅读图：SECNet-SNN Implementation

状态：**current; confirmed 2026-09-10**

## 一、目标与边界

本方向服务于 SECNet ICML 2026 oral 的 TPAMI 扩展。当前问题不是再寻找一个宽泛的新主题，而是回答：

> 如何在保留 ordered Event Cloud 与 SECNet hierarchical processing 优势的前提下，把 SECNet 实现为准确、可训练、并具有真实部署意义的 SNN？

SECNet 的 Spatial-FA 与 Temporal-FA 仍是 baseline architecture 的一部分，但 frequency/Fourier 不再是 Advisor Core 的准入条件。第一版实现也不引入 Mamba/SSM。完整任务名单由 [Advisor Core Reading Plan](../00-index/reading-plan-advisor-core.md) 生成维护；详细筛选证据见 [SECNet-SNN Implementation Shortlist](advisor-secnet-snn-implementation-shortlist.md)。

当前限定阅读集共 9 篇：1 篇 focus paper SECNet，6 篇 required，2 篇 helpful。

## 二、实施依赖顺序

1. **SECNet**：冻结 ordered Event Cloud 输入、`G&S -> SFA -> AGG -> TFA -> RES` hierarchy、tensor interfaces 与 task heads；明确哪些 continuous operations 暂时保留。
2. **SpikePoint**：定义第一个 Event Cloud-to-spike baseline，包括 grouping 后的显式 spike interface、PLIF、residual path 与短 timestep 设置。
3. **STEP**：先固定公平对照协议，再选择 neuron、encoding、timestep、surrogate gradient、temporal block 与 energy accounting。
4. **Spiking Discrepancy Transformer**：设计 local-to-global point-spiking hierarchy，并测试 coordinate-aware membrane initialization 与 discrepancy attention。
5. **CLIF**：在 backbone、encoding、timestep 和 optimizer 不变时，作为 PLIF 的 controlled neuron replacement。
6. **Spike-driven Discrete Aggregation**：把 spiking mechanism 前移到 G&S/AGG interface，测试 learned event/group selection，而非只替换 backbone activation。
7. **Multi-Delay Mixer**：在 ordered group descriptors 上测试显式 temporal interaction；严格区分 physical event chronology 与 SNN simulation timestep。
8. **HD-LIF**：baseline 收敛后，再处理 STBP memory、online gradient coherence、quantization 与 deployment optimization。
9. **SMixer**：最后评估 asynchronous-friendly token mixing 与 spatial-temporal spike pruning，避免把低 operation estimate 误写成真实 event-driven deployment。

## 三、分层职责

| 层级 | 论文 | 对 SECNet-SNN 的职责 |
| --- | --- | --- |
| Focus | SECNet | 固定待转换系统、输入组织、模块边界与任务接口 |
| Required / architecture | SpikePoint | Event Cloud-to-spike baseline 与 point-wise spiking feature extraction |
| Required / architecture | Spiking Discrepancy Transformer | hierarchical point SNN、local/global interaction、spatially-aware neuron |
| Required / aggregation | Spike-driven Discrete Aggregation | spike-controlled event selection 与 multi-timescale aggregation |
| Required / evaluation | STEP | neuron/encoding/architecture/energy 的 controlled benchmark protocol |
| Required / neuron | CLIF | temporal-gradient-aware drop-in neuron ablation |
| Required / temporal | Multi-Delay Mixer | ordered descriptors 上的 delay-based temporal interaction |
| Helpful / optimization | HD-LIF | memory-aware online training 与 deployment bundle |
| Helpful / deployment | SMixer | asynchronous-friendly operator 与 spike pruning |

## 四、统一提取框架

每篇 Advisor 论文只提取能够改变实现决策的证据：

1. **Insertion point**：SECNet 的 input、G&S、SFA、AGG、TFA、RES 或 task head；
2. **Signal/state**：raw event、grouped point、continuous feature、membrane state、binary/multi-bit spike；
3. **Spike boundary**：sensor event 在哪里变成 neuronal spike，哪些模块仍是 ANN/continuous；
4. **Neuron/operator**：LIF/PLIF/CLIF/HD-LIF、attention、mixer、gate 或 aggregation；
5. **Temporal axis**：physical event time、group order、network depth、delay 或 simulation timestep；
6. **Training path**：surrogate gradient、BPTT/STBP、online/local path、normalization 与 memory cost；
7. **Deployment**：算子是否真的支持异步执行，是否依赖 dense FFT、softmax、global synchronization 或连续状态；
8. **Evidence**：task metric、timestep、firing rate、peak training memory、runtime、operation/memory estimate 或 measured hardware result。

必须区分 camera event 与 neuronal spike、physical time 与 simulation timestep、binary spikes 与 multi-bit activations、operation proxy 与真实 energy measurement。

## 五、第一版实验顺序

第一版只做单变量替换：保留 SECNet Event Cloud construction 与 hierarchy，加入明确的 point-feature-to-spike interface，以 PLIF 建立 baseline；随后依次测试 CLIF、point discrepancy hierarchy、discrete aggregation 与 delay mixing。HD-LIF 和 SMixer 只在 baseline 稳定后进入训练内存和部署分支。

频域论文与旧阅读图仍可用于分析 SFA/TFA，但不再占用当前 Core 名额。任何同时替换 grouping、neuron、temporal mixer、attention 与 training rule 的实验，都无法可靠归因，因此不作为第一版实现。
