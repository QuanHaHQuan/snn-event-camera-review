# SNN for Event Cameras｜Core Reading Workflow

本文件用于单篇 Core 论文的交互式精读和 Summary V2 交付。执行时只关注三个问题：

1. 当前输出是在聊天框还是 V2 Markdown 文件；
2. 当前处于 Step 1–4 的哪一步；
3. 用户当前提供或明确要求了什么。

不得因为本文件包含最终交付规则，就在前面的阅读阶段提前生成 V2、全文审查或知识图。

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
- 3–6 个后续精读问题。

### 边界

不要在 Step 1：

- 给论文分 A/B/C 或 P0/P1/P2；
- 决定是否 Core、略读或无需继续；
- 展开全部公式、实验和消融；
- 写完整 Strengths and Limitations；
- 生成 V2 或全文审稿报告。

## 4. Step 2｜逐段精读

用户会依次提供 Abstract、Introduction、Related Work、Method、Experiments、Conclusion 或 Appendix。每次固定按以下顺序回答。

### 4.1 完整中文翻译

必须先翻译完当前提供的全部内容，再进行解释。

- 保留段落顺序和逻辑，不删句，不用概括替代翻译；
- 技术术语可保留英文，或使用“中文解释 + English term”；
- 不把作者的推测翻译成确定事实；
- 公式、图注、表注和算法文字属于当前内容时一并翻译；
- 不加入原文没有的实现细节。

### 4.2 必要解释与分析

只解释当前内容中实际出现、且有助于理解的部分。根据内容选择，不强行凑栏目：

- 段落作用、问题动机和前后逻辑；
- 输入、输出、组件关系和 forward data flow；
- 公式逐项含义、tensor shape 和计算顺序；
- 正文提供训练信息时解释 loss、optimization 和 gradient path；
- 有图表时解释结构、比较对象、关键数据和作者结论；
- 指出真实存在的符号冲突、维度疑点、实验限制或过强结论。

当前内容没有公式、图表或实验时，不创建对应分析。短段落保持简洁；复杂方法可以详细解释，但不要扩展成完整技术审查。

### 4.3 不确定内容

只有确实无法确认时写 `Needs further check`，并说明需要核查的具体页面、符号、数据或实现边界。parsed text 与 PDF 页面冲突时以页面为准。

## 5. Step 3｜问题讨论与用户记录

回答用户问题时结合当前论文，优先说明：为什么需要该机制、原方法的问题、当前数据流、优化对象、维度变化、梯度路径，以及实验是否支持作者说法。必要时使用具体或小规模数值例子，但不得虚构实现。

持续维护以下三类记录：

### Questions and Clarifications

只记录用户实际提出、且需要在 V2 保留的问题及其论文内答案。不得用助手自选知识点填充。

### Additional Technical Details

只有用户明确要求“保留到 V2”“加入技术细节”或同等意思时记录。可保留完整算法、维度流程、前置假设和适用边界。

### Personal Reflections

只有用户明确表达个人判断或研究启发，并要求保留时记录。不得替用户推断观点。

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
## 7. Relation to Other Papers and Survey Taxonomy
## 8. Survey-Usable Takeaways

## Supplement Points
### Questions and Clarifications
### Additional Technical Details
### Personal Reflections
```

没有对应用户内容时，省略该 Supplement 子章节；三个子章节都为空时省略整个 `Supplement Points`。不单设 `Needs Further Check` 章节。

### 6.2 内容要求

- 正文使用中文；model、dataset、metric、module、loss 和核心技术名称保留英文。
- Conference paper 正文通常为 1200–1600 个中文语义单位，通常不超过 1800，复杂核心论文最多约 2000；Supplement 不计入。
- 方法部分说明输入、输出、数据流、关键组件、训练/优化逻辑，以及 fully spiking、hybrid、converted 或 non-spiking 属性。
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

生成 V2 时主动核查 PDF 的 Introduction、Related Work、关键 baseline 和 bibliography。用户没有逐段粘贴 Related Work，也不能省略这一步。

### 7.1 选择范围

- Survey Core V2 选择 0–6 篇真正关键的前驱、comparator 或相邻工作；0 是合法结果，不得凑数。
- 历史/reference V2 可选择 0–4 篇；`lightweight` 只减少数量和分析深度，不降低证据标准。
- 关系类型只用：`foundation`、`extends`、`contrasts_with`、`baseline`、`alternative`、`same_task_different_mechanism`。
- 普通背景长列表、仅共享任务但没有比较价值的论文不进入关系图。

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
- V2 第 7 节、registry 和 matrix 必须在同一次交付中同步，不能只修改其中一个。
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
2. 同步 registry 和 matrix。
3. 运行：

```bash
python3 scripts/update_v2_indexes.py
python3 scripts/validate_literature_graph.py
git diff --check
```

4. 报告 V2 路径、Survey/Advisor 进度、关系验证、修改文件和 `git status`。
5. 不修改 `candidate-screening-audit.csv`、Core membership、reading assignments、outline 或 Advisor map，除非用户明确要求。
6. 不自行 commit 或 push。

## 9. 最终检查

### 聊天回复

- 已先完整翻译，再做必要解释；
- 未提前分析后文章节或扩展成全文审查；
- 聊天公式只使用 `\(...\)` 和 `\[...\]`，没有 `$` 定界符；
- 不确定内容已具体标记 `Needs further check`。

### V2 文件

- 标题、SNN 属性、数据流和实验数字与 PDF 一致；
- author claim、SOTA、trade-off 和 efficiency evidence 类型表述准确；
- Supplement 只含用户真实问题、明确要求保留的细节和反思；
- 数学公式只使用 `$...$` 和 `$$...$$`，定界符与命令完整；
- 第 7 节每条 edge 均通过三道证据门，citation 与 bibliography 对应；
- V2、registry、matrix 和 backward-search key 一致；
- 文件名、保存路径、三个验证命令和下载链接均正确。
