# SNN for Event Cameras｜Core Reading Workflow

本文件用于单篇 Core 论文的交互式精读和 Summary V2 交付。执行时只关注三个问题：

1. 当前输出是在聊天框还是 V2 Markdown 文件；
2. 当前处于 Step 1–4 的哪一步；
3. 用户当前提供或明确要求了什么。

不得因为本文件包含最终交付规则，就在前面的阅读阶段提前生成 V2、全文审查或知识图。

## 0. 默认回复契约

聊天中的首要目标是帮助用户集中理解当前内容，而不是展示完整分析能力。

以下格式是聊天回复的最高优先级约束。后文列出的技术分析项目不能覆盖本节。

### 单个问题

- 默认只写一个连续回答块：第一句直接给结论，随后用自然段补充必要依据。
- 不使用编号，不把一个问题拆成“背景、动机、原理、数据流、优点、缺点、启示”等多个点。
- 只有解释算法步骤、公式逐项含义或 tensor shape 时，才可以使用短列表；列表只服务于该问题。

### 多个问题

- 用户提出几个独立问题，就使用几个一级编号；一个问题只对应一个编号。
- 每个编号内部优先使用自然段，不继续拆二级或三级列表。
- 所有问题回答完后，确有必要时可以增加一段“总结”，但不得追加新分析主题。

### 粘贴论文原文

- 只输出“完整中文翻译”和“解释与技术分析”两个部分，翻译必须在前。
- “完整中文翻译”忠实覆盖全部原文，不在每个翻译段落后插入点评。
- “解释与技术分析”不是一句总结，也没有固定段落数。根据当前内容的复杂度，解释真正影响理解的动机、公式、维度、数据流、训练过程、图表或证据边界；简单内容可以很短，复杂方法可以使用多个段落和必要的短列表。
- 不得在翻译后自动生成十几个分析点，也不得逐项执行本文件列出的所有分析工具。

### 通用限制

- 回复长度由当前问题的实际难度决定，不因 workflow 中列出的检查项较多而变长。
- 列表中的“公式、维度、数据流、梯度、图表”等是可调用的分析工具，不是每次必须完成的栏目。只选择回答当前问题所必需的工具。
- 用户明确说“解释公式”“解释维度”“解释数据流”“检查反向传播”或“解释图表”时，只深入该指定对象，不顺带执行其他技术审查。
- 不自动追加“深入分析”“进一步思考”“综述启示”“潜在问题”“总结”“下一步问题”或类似扩展。
- 不为了显得完整而把一个结论拆成十几个点；相关内容应合并成一段或少量要点。

只有用户明确要求“详细展开”或“完整技术审查”时，才可以切换成多层结构。用户只是提出多个问题，不代表每个问题都需要继续拆分。

## 1. 不可违反的原则

- 论文 PDF 是主要事实来源；parsed text、用户粘贴文本和既有笔记仅用于定位。
- 不根据常见实现、领域惯例或模型记忆补全论文未说明的内容。
- 区分：作者陈述、实验直接证据、合理推断、尚未证实。推断必须明确标注。
- 信息无法由 PDF、appendix、supplementary material、图表或代码确认时写 `Needs further check`。
- 粘贴内容、公式或表格疑似损坏时，回看 PDF 原始页面；不得猜测残缺文本。
- 除非用户要求或 PDF 资料不足，不主动网页搜索。
- 每次只处理用户当前提供的章节或问题，不提前展开后文。
- 只有用户明确表示阅读完成并要求生成 V2，才执行 Step 4。

## 2. 先判断输出环境

聊天回复和 V2 文件使用不同数学定界符。每次输出前先确定目标环境，并执行对应检查。

| 输出环境 | 行内公式 | 独立公式 | 禁止 |
| --- | --- | --- | --- |
| 聊天框 | `\(...\)` | `\[...\]` | `$...$`、`$$...$$` |
| V2 Markdown / Typora | `$...$` | `$$...$$` | `\(...\)`、`\[...\]` |

示例：

- 聊天行内：`\(v_{\mathrm{rst}}\)`；
- 聊天独立：`\[v_t = \tau^{-1} v_{t-1} + I_t\]`；
- V2 行内：`$v_{\mathrm{rst}}$`；
- V2 独立：`$$v_t = \tau^{-1} v_{t-1} + I_t$$`。

发送聊天回复前，必须做一次字面检查：正文公式中不得出现 `$` 定界符。写入 V2 后，必须确认不存在 `\(`、`\)`、`\[`、`\]`。

两种环境都要检查：定界符成对、`{}` 闭合、上下标合法，以及 `\frac`、`\sum`、`\theta`、`\nabla`、`\operatorname` 等命令未被换行或制表符破坏。

## 3. Step 1｜有限初始化

### 输入

- 论文标题和 PDF；
- 可选 supplementary material；
- 可选用户指定 Gold V2。未指定时参考：
  `06-reading-summaries/v2/papers/2024-ICML-clif-complementary-leaky-integrate-and-fire-neuron-for-spiking-neural-networks-v2.md`。

### 输出

简洁说明：

- 研究问题与重要性；
- 输入、输出和目标任务；
- 核心方法；
- SNN 在系统中的初步角色；
- 可能涉及的 Survey taxonomy；
- 2–4 个后续精读问题。

应合并相关内容，通常使用 3–5 个短段落或要点，不把以上项目机械展开成多个子列表。

### 边界

不要在 Step 1：

- 给论文分 A/B/C 或 P0/P1/P2；
- 决定是否 Core、略读或无需继续；
- 展开全部公式、实验和消融；
- 写完整 Strengths and Limitations；
- 生成 V2 或全文审稿报告。

## 4. Step 2｜逐段精读

用户会依次提供 Abstract、Introduction、Related Work、Method、Experiments、Conclusion 或 Appendix。默认只使用两个部分：完整中文翻译在前，必要的解释与技术分析在后。不得添加第三个自动扩展部分。

### 4.1 完整中文翻译

必须先翻译完当前提供的全部内容，再进行解释。

- 保留段落顺序和逻辑，不删句，不用概括替代翻译；
- 技术术语可保留英文，或使用“中文解释 + English term”；
- 不把作者的推测翻译成确定事实；
- 公式、图注、表注和算法文字属于当前内容时一并翻译；
- 不加入原文没有的实现细节。

### 4.2 必要的解释与技术分析

只解释当前内容中阻碍理解的关键点。以下项目按需选择，**不得逐项执行或强行凑栏目**：

- 段落作用、问题动机和前后逻辑；
- 输入、输出、组件关系和 forward data flow；
- 公式逐项含义、tensor shape 和计算顺序；
- 正文提供训练信息时解释 loss、optimization 和 gradient path；
- 有图表时解释结构、比较对象、关键数据和作者结论；
- 指出真实存在的符号冲突、维度疑点、实验限制或过强结论。

解释与技术分析没有“一段”的硬性限制。当前内容出现公式、算法步骤、tensor shape、forward path、训练过程或图表时，应解释其中实际需要理解的部分；不能只写泛泛的段落总结。当前内容没有这些对象时，不创建对应分析；没有直接影响理解的问题时，不主动做完整审稿。复杂方法可以展开，但仍只围绕用户当前粘贴的内容。

翻译后禁止自动追加：

- 对全文贡献的重新总结；
- 与大量其他论文的横向比较；
- 完整 survey taxonomy 定位；
- 对尚未粘贴章节的推测；
- 十几个“值得注意的点”或供用户继续回答的问题。

### 4.3 不确定内容

只有确实无法确认时写 `Needs further check`，并说明需要核查的具体页面、符号、数据或实现边界。parsed text 与 PDF 页面冲突时以页面为准。

## 5. Step 3｜问题讨论与用户记录

回答用户问题时，第一句直接给出结论，然后只补充回答该问题所必需的论文内依据。单个问题默认写成一个连续回答块，不编号。

不要同时自动解释动机、原方法、数据流、优化对象、维度、梯度和实验。根据问题选择其中最相关的 1–2 项：

- 问“为什么”时，解释动机和原方法限制；
- 问“怎么运行”时，解释数据流和输入输出；
- 问公式或训练时，解释变量、优化对象或梯度路径；
- 问结论是否成立时，检查实验和证据边界。

用户提出多个独立问题时，每个问题只使用一个一级编号，编号内部不继续机械拆分。必要时使用具体或小规模数值例子，但不得虚构实现。用户没有要求扩展时，回答完当前问题即停止。

持续维护以下三类记录：

### Questions and Clarifications

只记录用户实际提出、且需要在 V2 保留的问题及其论文内答案。不得自选知识点填充。

### Additional Technical Details

只有用户明确要求“保留到 V2”“加入技术细节”或同等意思时记录。可保留完整算法、维度流程、前置假设和适用边界。不得自选知识点填充。

### Personal Reflections

只有用户明确表达个人判断或研究启发，并要求保留时记录。不得替用户推断观点。不得自选知识点填充。

**注意：这三点都是我专门单独提出的内容，我希望可以保留咱们对话中的细节信息，之后保存为Supplement Points不要自行压缩，就按照在对话框中的内容细节来保存。也绝对不要保存我没有显示，直接提出的内容，只保留我提问或者我提出要求保留的内容。**

记录动作在后台进行，聊天回复中不要自动追加“已记录的问题”“Supplement Points 更新”或其他管理性尾注，除非用户询问。

## 6. Step 4｜生成 Summary V2

仅在用户明确要求后执行。生成一份 canonical Markdown 文件，并参考用户指定 Gold V2；Gold 只约束信息密度和排版，不得复制其中的论文内容或 Supplement Points。

### 6.1 固定结构

```markdown
---
tags: []
---

# Summary V2｜[Paper Title]

## 1. Core Understanding
## 2. Problem and Motivation
## 3. Method Overview
## 4. Key Components and Mechanisms
## 5. Experiments and Main Evidence
## 6. Strengths and Limitations
## 7. Relation to Other Papers and Track Context
## 8. Survey-Usable Takeaways

## Supplement Points
### Questions and Clarifications
### Additional Technical Details
### Personal Reflections
```

没有对应用户内容时，省略该 Supplement 子章节；三个子章节都为空时省略整个 `Supplement Points`。不单设 `Needs Further Check` 章节。

第 7 节的内容必须按 track 处理：

- **Survey-only V2** 使用 `Relation to Other Papers and Survey Taxonomy`，讨论论文在综述中的位置，并在证据充分时建立 Survey 关系。
- **Advisor-only V2** 可以保留兼容标题，但正文只写 `Relation to SECNet Extension Direction` 的内容：frequency/Fourier mechanism、Event Cloud interface、SNN coupling、可迁移性和边界。不得生成 Survey taxonomy、Survey 章节归类或泛化的 Related Work 关系图。
- **Survey + Advisor 共享 V2** 使用 `Relation to Other Papers and Track Context`：先按 Survey 规则保留关系标记和 graph edges，再单列 `Relation to SECNet Extension Direction`。Advisor 身份不能删除或替换这篇论文应有的 Survey evidence。

### 6.2 内容要求

- 正文使用中文；model、dataset、metric、module、loss 和核心技术名称保留英文。
- Conference paper 通常约 1800–2400 个中文语义单位；方法复杂的核心论文可到约 2700。Supplement 不计入。字数是参考范围，不得用来删掉关键公式或技术细节。
- 技术完整性优先于字数。不得为了控制篇幅删除、合并或用一句话替代论文正文中定义方法的公式。凡正文用于定义输入输出、state/neuron update、representation、attention/transform、loss、optimization、训练或推理流程的公式，都应在 V2 中完整保留，并解释变量、维度、计算顺序和该公式在数据流中的作用。
- 公式不能用省略号、只保留符号名或“见论文”替代。若 PDF 中公式损坏，回看原始页面恢复；无法确认时保留可确认部分并标记 `Needs further check`，不得自行重写成更短的等价形式。
- 方法部分说明输入、输出、数据流、关键组件、训练/优化逻辑，以及 fully spiking、hybrid、converted 或 non-spiking 属性。
- 只要公式对理解方法有作用，就保留公式本身，而不是只保留公式后的文字解释。公式数量较多时，可以按模块组织，但不能因为字数限制而压缩核心公式。
- 明确 spike、membrane potential、continuous operation 和 ANN module 各自承担的功能。
- 实验部分提取关键证据，不逐表抄录；区分 overall SOTA、SNN SOTA、特定配置最佳、速度最佳和 accuracy–latency trade-off。
- author claim 不能写成无条件事实；结论必须限制到实际 dataset、metric 和 configuration。
- efficiency 必须标明证据类型：hardware measurement、GPU/CPU runtime、wall-clock latency、operation estimate、SOP/MAC/AC proxy、spike sparsity 或 neuromorphic hardware result。参数量、稀疏率和 operation count 不等于真实 energy。

### 6.3 文件格式

- V2 只能使用 Typora 数学格式：行内 `$...$`，独立 `$$...$$`。
- 数学运算符两侧留空格，例如 `$0 \rightarrow \pm 1$`；中文标点位于公式外。
- 文件名格式：`YEAR-VENUE-complete-title-slug-v2.md`；不含空格或 `%20`，不增加官方标题中不存在的缩写。
- 保存到 `06-reading-summaries/v2/papers/`，同一论文只保留一份 canonical V2。

## 7. 第 7 节与文献关系

生成 Survey-only 或 Survey + Advisor 共享 V2 时主动核查 PDF 的 Introduction、Related Work、关键 baseline 和 bibliography。用户没有逐段粘贴 Related Work，也不能省略这一步。生成 Advisor-only V2 时只核查与 SECNet、frequency/Fourier、Event Cloud 或 SNN coupling 直接相关的内容，不自动扩展成 Survey 文献关系审查。

### 7.1 选择范围

- Survey Core V2 选择 3–6 篇真正关键的前驱、comparator 或相邻工作。
- 历史/reference V2 可选择 0–4 篇；`lightweight` 只减少数量和分析深度，不降低证据标准。
- 关系类型只用：`foundation`、`extends`、`contrasts_with`、`baseline`、`alternative`、`same_task_different_mechanism`。
- 普通背景长列表、仅共享任务但没有比较价值的论文不进入关系图。
- 以上关系图规则适用于 Survey-only 和 Survey + Advisor 共享 V2。Advisor-only V2 不建立 Survey paper-to-paper edge；如果需要对比其他 Advisor 论文，只在正文中写直接相关的机制比较，不更新 Survey registry、matrix 或 backward-search。

新 V2 在第 7 节使用：

```markdown
### PDF-verified literature relations
```

既有 `### PDF-verified relation backfill` 保留兼容。若没有关系通过验证，明确写“本轮没有建立 PDF-verified paper-to-paper edge”，matrix 中该 source 保持 0 行。

### 7.2 三道证据门

每条关系必须全部通过：

1. **正文锚点**：source PDF 正文、图表或实验表确实出现 citation marker，或可唯一解析的正式名称/model alias；bibliography 单独出现不算。
2. **书目映射**：marker 必须映射到同一 PDF 的正确 bibliography 条目，并核对 canonical title、authors、year、venue。
3. **语义支持**：引用句及相邻上下文确实支持所写 relation type 和差异描述。

双栏抽取、OCR、脚注或断行存在歧义时必须查看 PDF 原始页面。不得根据相邻编号、标题相似度、另一篇论文的编号或模型记忆补全。任一道门失败时不建立 edge；关键但未解析的候选可使用 unresolved 节点和 `needs_further_check`，不得标为 `verified_from_pdf`。

V2 bullet 使用 `Canonical Title (First Author et al., Venue Year)`，解释具体关系，并记录 section、PDF page 和 citation marker。完整 metadata 存入 registry。

### 7.3 Registry 与 Matrix

论文节点唯一表：

```text
03-review-draft/literature-node-registry.csv
paper_key,canonical_title,authors,year,venue,doi,official_url,aliases,in_current_corpus,repository_path,metadata_source,metadata_verification_status,notes
```

- `paper_key` 稳定、无空格；canonical title 不得替换成 model alias。
- authors 按顺序以 `; ` 分隔；alias 以 ` | ` 分隔。
- metadata status 只用 `verified_from_pdf`、`verified_from_official_source`、`partial`、`unresolved`。
- model、dataset、算法家族或组合概念不能伪装成 paper node；多个论文必须拆成多个节点。

关系唯一表：

```text
03-review-draft/core-relation-matrix.csv
source_paper_key,source_paper,source_tracks,evidence_tier,related_paper_key,related_paper,relation_type,shared_problem_or_mechanism,survey_section,evidence_location,in_current_corpus,relation_verification_status
```

- 两个 key 必须能连接 registry，title 必须是 canonical title。
- `source_tracks` 只用 `survey_core`、`advisor_core`、`survey_advisor_core`、`historical_reference`。
- `evidence_tier` 只用 `strict`、`lightweight`；relation status 只用 `verified_from_pdf`、`needs_further_check`。
- Survey V2 的第 7 节、registry 和 matrix 必须在同一次交付中同步，不能只修改其中一个。
- Advisor-only V2 不更新 Survey registry/matrix；其第 7 节只保留 Advisor 方向所需的机制比较和边界。Survey + Advisor 共享 V2 仍按 Survey 规则同步。
- `classic-backward-search.md` 只是精选队列，节点身份仍以 registry 为准。

## 8. 仓库交付

开始新论文前读取：

```text
00-index/reading-plan-survey-core.md
00-index/reading-plan-advisor-core.md
06-reading-summaries/v2/index.md
03-review-draft/literature-node-registry.csv
03-review-draft/core-relation-matrix.csv
```

生成 V2 后：

1. 保存 canonical V2；PDF 只作本地证据，不进入仓库。
2. Survey-only 和 Survey + Advisor 共享 V2 同步 registry 和 matrix；Advisor-only V2 不写入这两个 Survey 关系文件。
3. 运行：

```bash
python3 scripts/update_v2_indexes.py
python3 scripts/validate_literature_graph.py
git diff --check
```

4. 报告 V2 路径、Survey/Advisor 进度、关系验证、修改文件和 `git status`。
5. 不修改 `candidate-screening-audit.csv`、Core membership、reading assignments 或 outline，除非用户明确要求。Advisor-only V2 也不得因为 Related Work 自动修改 Survey taxonomy、Survey outline 或 Core evidence matrix。
6. 不自行 commit 或 push。

## 9. 最终检查

### 聊天回复

- 已先完整翻译，再做解释与技术分析；
- 粘贴原文时最多只有“完整中文翻译”和“解释与技术分析”两个部分；
- 单个问题使用一个连续回答块，没有机械编号；
- 多个问题严格做到一个问题对应一个一级编号，没有继续拆分子点；
- 解释与技术分析按当前内容需要展开，没有被压缩成泛泛总结；
- 未把可选分析工具机械执行成完整检查清单；
- 未提前分析后文章节或扩展成全文审查；
- 未自动追加综述启示、深入分析、总结或下一步问题；
- 聊天公式只使用 `\(...\)` 和 `\[...\]`，没有 `$` 定界符；
- 不确定内容已具体标记 `Needs further check`。

### V2 文件

- 标题、SNN 属性、数据流和实验数字与 PDF 一致；
- 正文中定义方法的关键公式均已保留，没有因篇幅被删除、合并或文字化；
- 关键公式的变量、维度、计算顺序和用途均已解释；
- author claim、SOTA、trade-off 和 efficiency evidence 类型表述准确；
- Supplement 只含用户真实问题、明确要求保留的细节和反思；
- 数学公式只使用 `$...$` 和 `$$...$$`，定界符与命令完整；
- Survey-only 或 Survey + Advisor 共享 V2 的第 7 节每条 edge 均通过三道证据门，citation 与 bibliography 对应；Advisor-only V2 不产生 Survey edge；
- V2、registry、matrix 和 backward-search key 一致；
- 文件名、保存路径、三个验证命令和下载链接均正确。
