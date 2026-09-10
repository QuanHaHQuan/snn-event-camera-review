# Survey Core 阅读冲刺路线：13/26 到开始写作

状态：**持续使用；13/26 是本路线建立时的起点，不是实时进度**

实时进度由生成的 [Survey V2 index](../06-reading-summaries/v2/survey/index.md) 统一维护。

本路线的目标：**10 天内进入综述写作，不把“26 篇全部生成完整 V2”作为写作前置条件。**

原建议执行窗口为 **2026-08-16 至 2026-08-25**；该日期仅保留为历史计划基线，后续继续使用下述阅读—写作循环，不自动顺延旧日程。

## 一、先明确目标

这 26 篇论文承担的任务不同：

- 一部分是综述主干，需要真正理解方法、数据流和证据；
- 一部分是背景或比较材料，只需要确认它在 taxonomy 中的位置和能支持的具体论断；
- V2 是精读记录，不是必须在写作前全部完成的行政手续。

因此，后续采用：

**已读论文复习 + 剩余论文快速分层阅读 + 边读边写 + 写作时回查 PDF。**

不追求把每篇论文都读成同样深度，也不把 Agent 自动生成的文字当成用户已经理解的证据。

## 二、两种阅读深度

### 主干精读

适用于直接代表 SNN 与 event camera 交集的论文，以及会改变大纲结构的论文。

至少确认：

1. 论文解决的具体问题；
2. event 如何组织和表示；
3. 哪一部分是真正的 SNN，SNN 与 ANN 的边界在哪里；
4. 从 event 输入到最终输出的 forward data flow；
5. 支撑主要结论的关键实验；
6. 与最接近的 Core 论文相比新增了什么、没有解决什么。

主干精读需要用户参与提问、修正和讨论，必要时生成或更新完整 V2。

冲刺期的单篇时间上限建议为 90-150 分钟。这里的“主干精读”是面向综述论证的定向精读，不要求逐段翻译全文；写作时成为关键证据的论文可以再做第二轮深入阅读。

### 快速阅读

适用于 selected background、非 SNN comparator、相近论文和已经有充分同类证据的论文。

只确认：

- 它属于哪一个综述章节；
- 输入、representation、SNN role 和任务是什么；
- 它能支持哪一个具体论断；
- 与主干论文的一个关键差异；
- 需要回 PDF 核查的结果或限制。

快速阅读可以由 Agent 先准备 PDF section map、图表位置和证据草稿，用户只核查与当前段落有关的内容。不要为所有背景论文制作重型 V2。

快速阅读的单篇时间上限建议为 45-75 分钟。

## 三、每篇论文的最小完成标准

关闭 PDF 后，至少能够用几句话回答：

1. 它解决什么问题？
2. event 输入是什么形式？
3. SNN 在 pipeline 的什么位置？如果没有 SNN，要明确写 `non-spiking comparator`；
4. 核心数据流如何从输入到输出？
5. 哪个实验结果支持它的主要 claim？
6. 它和已经读过的哪篇论文最接近，差别是什么？

不能回答的问题只记录为待回查项，不要凭标题或摘要补全。

## 四、十天冲刺安排

以下按每天约 3-5 小时的集中工作量设计。每天时间不足时，优先完成主干论文和当天的比较产出；不要牺牲比较和写作，只为了增加“已读篇数”。

### 第 1 天：建立当前知识地图

复习已完成 V2 中的 event organization / representation 组：

- PEPNet；
- Efficient Learning of Event-based Dense Representation using Hierarchical Memories with Adaptive Update；
- SpikePoint；
- SpikeSlicer。

产出一张比较表，至少包含：输入、slicing、representation、temporal state、SNN role、输出和效率证据类型。

必须能说清楚：**slicing 是时间边界的选择，representation 是事件的编码方式，两者不能混为一谈。**

### 第 2 天：复习 SNN dynamics 与 training

复习：

- CLIF；
- Temporal Flexibility；
- EventRPG；
- Continuous Spatiotemporal Events Decoupling through Spike-based Bayesian Computation。

产出一张矩阵，比较 neuron/state、learning rule、gradient path、时间依赖和部署含义。

### 第 3 天：复习任务、边界与效率证据

复习：

- SFOD；
- EAS-SNN；
- STLR；
- Are Conventional SNNs Really Efficient?；
- Raw-event adversarial attack。

产出一张 claim-evidence 表，明确区分：operation estimate、software runtime、hardware measurement 和 energy model。

### 第 4 天：快速阅读 event organization 组

处理：

- ASTW：focused；
- Graph Neural Network Combining Event Stream and Periodic Aggregation：focused；
- Spike-driven Discrete Aggregation：主干精读。

重点是形成一条可写入综述的比较链：

**fixed grouping → rule-adaptive grouping → learned adaptive grouping → spike-controlled grouping**。

### 第 5 天：阅读 architecture / conversion 组

处理：

- Inference-Scale Complexity in ANN-SNN Conversion：focused；
- HsVT：主干精读；
- STEP：focused。

重点确认：directly trained SNN、converted SNN、hybrid ANN-SNN 和 Spiking Transformer 的边界。不要因为论文使用 Transformer 或 attention，就自动把它归为 fully spiking。

### 第 6 天：阅读 detection 与 tracking 证据

处理：

- Efficient Event-Based Object Detection：主干精读；
- SpikeFET：focused，重点核查 frame-event fusion 和 fully spiking boundary；
- SDTrack：主干精读；
- SpikeTrack：focused comparative reading。

产出 detection/tracking 横向表：representation、SNN boundary、temporal state、fusion、output、training、dataset 和 efficiency evidence。

### 第 7 天：完成剩余论文并进行大纲 Checkpoint 02

处理：

- ClearSight：主干精读；
- EventGait：focused，重点核查 Mixture of Spiking Experts、hybrid boundary 和 benchmark；
- FLAME：focused，只读 LIF event-by-event front end 与 long-context memory 的接口。

当天完成一次大纲检查：

1. 两个并行基础轴是否仍然清楚：event representation 与 SNN computation；
2. intersection chapter 的几种 integration topology 是否足够；
3. Spiking Transformer 是否需要独立小节；
4. tasks 是否作为证据组织轴，而不是唯一 taxonomy；
5. 哪些章节已有至少两篇独立论文支持；
6. 哪些论断仍然需要经典论文或 reference pool 补充。

第 7 天结束时，形成 `outline-v0.2` 的实际工作版本。它不需要等所有 V2 文件完美完成。

### 第 8 天：开始写第一节，同时补证据

从最稳定、证据最充分的章节开始写，建议顺序：

1. Event-camera data organization and representations；
2. Spiking neural networks；
3. SNN for Event Cameras 的 intersection；
4. Tasks and empirical evidence；
5. Open problems。

每次只写一个小节，不要一次让 Agent 写完整综述。每个小节先建立：

- paragraph claim；
- supporting Core papers；
- evidence location；
- limitation / counterexample；
- missing classic reference。

### 第 9 天：继续分段写作并回查高风险证据

优先写 detection、tracking、reconstruction 等任务段落。每写完一个段落：

- 核对论文是否真的支持该句；
- 限定结论的范围；
- 区分 author claim 与实验直接证明的内容；
- 检查 energy、latency 和 sparsity 是否被混用；
- 为缺失证据建立待补清单。

### 第 10 天：形成可持续写作版本

产出：

- 一版可继续扩展的综述正文草稿；
- `claim-evidence-citation` 清单；
- Core evidence matrix 的第一版；
- 每个章节的缺口和待补经典论文清单；
- 尚未完成 V2 的论文列表，但不再把它们视为写作阻塞项。

第 10 天的目标是**进入稳定写作循环**，不是声称综述已经完成，也不是强行把所有数字和表格一次性核完。

## 五、边读边写的固定循环

每篇论文或每组论文都按下面的顺序执行：

1. 先写这一组要回答的综述问题；
2. 阅读 PDF 中与问题直接相关的章节、方法图和关键表格；
3. 记录一条可验证的 claim 和对应 evidence location；
4. 与至少一篇已读论文比较；
5. 把证据放入对应小节的草稿；
6. 写作中发现缺口，再回到 PDF 或 reference pool 补查。

写作不是阅读结束后的独立阶段，而是帮助发现知识缺口的验证环节。任何无法定位证据的句子都暂时标记为 `Needs further check`，不靠 Agent 的流畅表述掩盖空缺。

## 六、Agent 的分工

Agent 可以负责：

- PDF 下载和解析；
- section map；
- 公式、图表和页码定位；
- 初步比较表；
- claim-evidence 草稿；
- V2 文件的格式整理。

用户必须掌握并能解释：

- 论文的实际问题；
- representation 和 SNN 的边界；
- forward data flow；
- 主要实验证据；
- 与相邻论文的差异；
- 该论文对综述论点的真实作用。

Agent 生成的 V2、摘要或比较表都不能替代这些判断。

## 七、十天后的工作入口

十天后不再回到“先把所有论文读完再写”的旧流程，而是采用循环：

**写一个小节 → 建立 claim-evidence-citation 对应 → 发现缺口 → 定向阅读或补充经典文献 → 修正文稿。**

剩余 Core 论文只在以下情况下提升为主干精读：

- 它改变了某个章节的结构；
- 它代表当前证据中尚未覆盖的方法族；
- 它是某个关键 claim 的唯一证据；
- 写作时发现现有 Core 无法支撑该论断。

否则，快速阅读、证据卡片和写作中的定向回查已经足够。
