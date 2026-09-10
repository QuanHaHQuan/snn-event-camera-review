# Codebook 0.2 targeted recheck

日期：2026-09-10。范围：FLAME、CVPR2025-2047、REDIR、HsVT、STLR 五个既有 role 边界，以及 ABN/HsVT 的 `mlp` 映射。此次不新增 canonical paper、不修改 30 篇 pilot annotation、不启动 572 篇扩展。

## 1. 方法与解释边界

本轮只重读原有 PDF 定位中能回答受影响字段的页面，并重新应用 codebook 0.2 的合同：interface/module 使用 I1–I4，distributed task/module 检查脉冲计算是否分布在主要任务路径，engine/task 检查显式目标、变量映射与核心算法对应，`mlp` 检查是否为多层承载网络或明确命名的功能模块。

每个新判断先写入审计表的 `independent_decision` 与 `contract_result_json`，随后才与当前 canonical 值比较。由于同一执行者和当前任务上下文已包含 checkpoint 结论，这不是新的全盲复标，也不是人类 inter-rater reliability；它仅检验规则在定向重读时能否给出可解释、可复现的相邻类判断。旧值、新判断及对照结果均保留在 [审计表](taxonomy-codebook-0.2-targeted-recheck.csv) 中。

## 2. Role 定向重判

| Paper | 受检边界 | 新判断 | 关键合同证据 | 与 canonical |
| --- | --- | --- | --- | --- |
| FLAME | interface / embedded | `event_interface` | raw events 驱动真实 LIF 发放；新 event trains 经逐 timestamp pooling/flattening 成为 `E_flat(t)`，明确交给另一连续 EA-HiPPO 主模型；I1–I4 全部通过 | match |
| CVPR2025-2047 | interface / embedded | `embedded_module` | 5 ms voxel 是早期事件单元，但卷积 PLIF 输出是低层任务特征；`E_spike` 经 ASAB densify 后进入同一 detector 的 ANN blocks，不构成事件成员、窗口或输入表示合同 | match |
| REDIR | interface / embedded | `embedded_module` | TSA-SNN 位于连续 UNet/STN 注册之后，接收注册后的内部 feature maps，并经 perceptual mask/fusion 进入 CNN reconstruction；I1–I4 不成立 | match |
| HsVT | distributed task / embedded | `task_network` | SpikingMLP 分布在每个空间块，STFE 位于最后时序块；它们与 MaxViT/LSTM 共同构成四级 principal backbone，不是局部可拆支路 | match |
| STLR | engine / task | `algorithmic_engine`；secondary `task_network` | 非负 LASSO/ISTA 的 latent、更新和 fixed point 均与 state/spike rate 显式对应；下游 U-shaped SNN decoder 另行承担重建任务 | match |

五例没有未解释分歧。特别是 PLIF-ASAB 与 FLAME 的差别不由“是否位于前端”决定：前者交付 hybrid detector 的低层隐藏特征，后者交付具有 event-time/address-or-channel 语义的新事件列给另一 principal model。REDIR 则更早已越过接口边界，因为 SNN 输入来自连续注册后的任务特征。

## 3. `mlp` 规则检查

| Paper | 新判断 | 依据 | 与 canonical |
| --- | --- | --- | --- |
| ABN | `mlp` applies | 实验协议明确称 carrier architecture 为 Spiking MLP，且该多层网络直接完成分类与 event-wise segmentation；不是单一线性层 | match |
| HsVT | `mlp` applies | 论文明确命名 SpikingMLP，定义为多层 spiking-neuron 模块，并在每个 spatial block 重复两次 | match |

这两个正例不会把普通 Transformer FFN、单一 projection 或附带 MLP 自动升级为 `architecture_family=mlp`。ABN 的 STBP/STDP 来源冲突不属于本轮字段，继续保持 deferred，不用 architecture 判断替代训练证据。

## 4. 结论与下一步

- 5/5 role 定向重判与 0.2 canonical 一致；2/2 `mlp` 规则检查一致。
- 没有出现需要第五种 primary role 才能表达的方法，也没有触发新 label、canonical migration 或旧 blind 文件改写。
- interface/module、distributed task/module、engine/task 三组相邻边界均能用现有合同给出逐项理由；这通过了 checkpoint 要求的旧例定向复核部分。
- Codebook 0.2 仍不能冻结，因为 checkpoint 规定的 G/C/F/D/P/H 六个补充证据槽位尚未完成。下一步应进入独立的最小补充校准 Batch E2；完成事实答案后再交 Astra 判断适用域和冻结版本。

本表不写入 `taxonomy-pilot-events.csv`：当前 0.2 合同没有 `targeted_recheck` 事件类型，而把本轮伪装成 `blind_recheck` 或无字段变化的 `pdf_resolution` 会造成审计语义错误。独立审计表保留了全部七项检查，不需要为记录本轮而修改 codebook/contract。
