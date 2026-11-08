# AI Agent YouTube 精品短课索引（按 Topic 分类）

> **范围**：面向有软件工程基础、但刚开始系统学习 AI Agent 的学习者；优先 **General-purpose AI Agent Engineering** 的短视频，而非 Voice / Vision / Multimodal 专项。与仅收录大学课程的 `docs/university-ai-agent-courses.md` 严格分离。
>
> **更新日期**：2026-11-07 · **版本**：v1.6 · **状态**：新选课标准已生效，原有课程与新增的 8 节 RAG 视频按 Topic 收录，增加发布频道与主讲人字段；尚未逐条完成官方元数据复核的候选统一标记 `Needs Review`，不冒充 `Current`。
>
> **唯一维护路径**：`diego-king/ai-agent-knowledge` / `main` / `docs/youtube-ai-agent-courses.md`。每次提交前读取最新全文与 blob SHA，原路径合并，不创建副本。

## 1. 新手优先：选课标准（每次人工或自动更新必须执行）

### 1.1 学习目标、优先级

- **学习路径**：Beginner → General AI Agent Engineer → Production-ready Agent Systems。已有编程背景，但 AI Agent 知识从基础开始；按知识依赖推荐，不要求每个 Playlist 全看。
- **核心必修**：RAG 基础 / Retrieval / Agentic RAG、Agent Fundamentals、LLM / Agent / Workflow 区别、ReAct / Agent Loop、Tool / Function Calling、MCP、Context Engineering、Session / State / Memory、Design Patterns、Multi-Agent、Agent Evaluation / Reliability / Safety。
- **逐步补充**：RAG Chunking / Reranking / Evaluation、Router / Worker、Event-driven / Long-running Agent、Persistence / Retry、Human-in-the-loop、Tracing / Observability、Production Engineering。
- **通用性优先**：先学可迁移到 LangGraph、Google ADK、OpenAI Agents SDK 的概念，再选学具体 Framework / Cloud API 实操；避免被单一厂商技术栈绑住。
- **暂缓专项**：Voice AI、Vision AI、Gemini Live、音视频流处理、实时多模态、单一产品使用演示、营销宣传及纯 Coding Demo。只有具备明确跨场景价值（例如通用 SQL / Vector / Memory Bank 架构）的专项视频才可作为 **B 补充** 收录，不进入通用新手主线。

### 1.2 时长与教学形式

- **首选 ≤ 20:00**，尤其是能完整解释一个问题的 5–15 分钟课程。
- **20:01–30:00** 仅当概念深度、跨框架价值明显、且缺少更短且同样清晰的替代课程时收录；默认标 B 补充。
- **硬上限 ≤ 30:00**；30:01 起不得纳入主索引。
- 以原理解释、架构图、设计权衡、概念对比为主；可以少量代码辅助，但不收以 IDE 跟练、逐行 Coding 为主体的视频。
- 不因出自官方频道或属于某个播放列表就自动全收；**逐个视频独立评分**。

### 1.3 硬性核验与评分

**正式标记 `Current` / `Evergreen` 前必须确认**：直接 YouTube 视频 URL / Video ID、真实频道、可访问性、发布日期、准确时长、内容与标题及收录主题相符；框架 / API 内容还需对照当前官方文档。证据不足保留在候选表并标记 `Needs Review`，不能宣称已核验。

| 评分维度 | 权重 | 判断原则 |
|---|---:|---|
| 新手适用性与通用 Agent 相关性 | **30** | 基础性、可迁移性；专项 Voice / Vision 降低权重 |
| 技术准确性与时效 | **25** | 原理正确；MCP、SDK、云服务需核对最新官方文档 |
| 讲解清晰度 | **20** | 定义、图解、示例、设计权衡 |
| 课程结构与系统性 | **15** | 知识衔接、独立完整、不重复 |
| 时长与信息密度 | **10** | ≤20 分钟优先；20–30 分钟须有显著价值 |
| **合计** | **100** | **A ≥85（主线优先）**；**B 75–84（补充）**；**C <75（暂缓/排除）** |

评分是编辑判断，非 YouTube 官方评分。初筛 A/B 是依据主题的**推荐级别**，不是未经复核的视频真实性评分；只有核验完毕才能给出完整分项数值。

### 1.4 双层去重（每次更新必做）

1. **硬去重：Video ID**。规范化 youtu.be / watch / share / 参数链接，提取 11 字符 YouTube Video ID；全文扫描主 Topic、交叉引用、历史条目和归档。同一个 ID 仅有一个正式主条目。
2. **语义去重：同一知识点**。比较新课程与已有条目的学习目标、关键概念、教学深度和目标人群，而不只比较标题。若是换标题重讲同一主题，优先保留更短、清晰、较新、准确的课程；另一条如有独立价值才列为 B 级替代课程，并注明“内容重叠 / 二选一”。
3. **跨 Topic / Playlist**：同一视频只挂一个主 Topic；其他地方用内部链接或简单引用，不重复建立条目。任何播放列表都不能绕过去重。
4. **每月添加节制**：优先新增最多 **5 节真正高价值、非重复** 精品短课；没有符合条件的新课就写“本月无新增”，不得为了数量凑课程或重收旧课。

### 1.5 视频元信息和维护

每个条目至少保存英文标题、完整直达 URL、时长、**发布频道 / Publisher**、**实际主讲人 / Presenter（未核实则标“待核实”）**、系列、中文知识点、推荐级别、主 Topic、时效状态、核验日期。发布日期、细分评分、实际播放时长如果无法核准，必须标明待核实，**不得填猜测**。

| 内容类型 | 深度复核建议 | 主要风险 |
|---|---|---|
| Agent Fundamentals、ReAct、RAG 原理 | 每 6 个月 | 核心概念明显错误 |
| Architecture、MCP、Context / Memory、Multi-Agent | 每 3 个月 | 协议或最佳实践实质变化 |
| ADK、Agents SDK、LangGraph、Cloud API、具体代码 | **每月扫描时** 与官方文档对照 | SDK / API 过时、示例无法复现 |
| 视频可用性和明显过时信号 | **每月扫描时** | 私有化、删除、内容失配 |

状态：`Current`、`Evergreen`、`Needs Review`、`Outdated`、`Unavailable`。经典原理不因发布时间较早而自动归档；确实过时的课程注明原因并移至文末归档，保留可追溯记录。

## 2. 按 Topic 的 33 节候选索引（2026-11-07）

**原始 21 节统计（保留历史基线）**：AI Agent Crash Course **11**、Modern AI Agents: From Theory to Production **6**、The Agent Factory **3**、The Omni App **1**。原始候选中 **18 节 ≤20 分钟**、**3 节 20–30 分钟**。此前另新增 **4 节候选（RAG 2 + Graph 2）**；本次手动扩充 **8 节 RAG 候选**，合计 **33 节**，其中 RAG 主题共 10 节；精确时长未确认时保持待核，不计入原始 21 节统计。本次专题人工补录不改变每月例行更新优先最多 5 节的规则。全部为候选，**统一元数据状态：`Needs Review`（最后候选整理：2026-11-07）**；部分视频链接和时长已交叉核对，但并非全部完成 YouTube 官方页面/发布日期核验，不应错误展示为正式“已验证”。

以下 **A / B** 为学习优先级初筛；具体分项评分待核验后补写。YouTube 链接为**单视频直达链接**，不以搜索结果 URL 冒充已确定的视频 ID。

### 2.1 AI Agent Fundamentals

| 级别 | 视频（YouTube 直达） | 时长* | 系列 | 中文核心知识点 |
|---|---|---:|---|---|
| **A** | [AI agents explained: Build your first agent in 8 minutes](https://www.youtube.com/watch?v=Zqno_vux6d8) | 8:29 | Modern AI Agents | LLM vs Agent、ReAct、Planning、简单 Agent 构建；后半段 ADK 实操可选看 |
| **A** | [AI agent design patterns](https://www.youtube.com/watch?v=GDm_uH6VxPY) | 8:21 | AI Agent Crash Course | Single / Sequential / Parallel、Workflow vs Agent |
| **A** | [3 Advanced AI agent design patterns](https://www.youtube.com/watch?v=89KKm_a4M7A) | 8:00 | AI Agent Crash Course | Loop、Coordinator / Router、Agent-as-Tool |

### 2.2 Agent Architecture

| 级别 | 视频 | 时长* | 系列 | 中文核心知识点 |
|---|---|---:|---|---|
| **A** | [Workflow agents and communication in ADK](https://www.youtube.com/watch?v=WfJcCeLZD2I) | 4:53 | AI Agent Crash Course | Sequential / Parallel / Loop、Shared Session State、Delegation、Agent-as-Tool |
| **B** | [Agents, their frameworks and when to use them](https://www.youtube.com/watch?v=aLYrV61rJG4) | 27:46 | The Agent Factory | 是否需要框架；LangGraph / CrewAI / ADK 的架构权衡；偏进阶长访谈 |

### 2.2A Loop & Graph Engineering（Architecture 子主题）

Agent Loop 负责迭代决策与工具调用；Graph 定义 Nodes、Edges、Router、Fan-out / Join 等显式流程。**以下为新增候选，原有 2.1 的 Loop Patterns 与 2.2 的 Workflow ADK 不重复建立条目。**

| 级别 | 视频 | 时长 | 来源 | 中文核心知识点 | 元数据状态 |
|---|---|---:|---|---|---|
| **A** | [Graph Engineering 101](https://www.youtube.com/watch?v=IrW0_f-w4kA) | **5:56** | Google Cloud Tech | Graph vs Loop、Fan-out、Join、Router | Needs Review |
| **B** | [Graph Engineering with ADK](https://www.youtube.com/watch?v=Mzr7byMFy_4) | **6:10** | Google Cloud Tech | Node、Parallel、Join、Deterministic / LLM Router | Needs Review |

### 2.3 Tool Calling & MCP

| 级别 | 视频 | 时长* | 系列 | 中文核心知识点 |
|---|---|---:|---|---|
| **A** | [How Model Context Protocol (MCP) actually works](https://www.youtube.com/watch?v=cGuyrANVi4A) | 7:58 | Modern AI Agents | MCP Client / Server / Tools、协议价值 |
| **A** | [MCP vs API: Why traditional APIs are failing AI agents](https://www.youtube.com/watch?v=185XGEMefgc) | 12:25 | Modern AI Agents | MCP 与 API 的职责比较；注意：**MCP 并不替代 API**，标题较夸张 |
| **B** | [Building your own MCP server with ADK](https://www.youtube.com/watch?v=XwlVHm3JKWU) | 9:02 | AI Agent Crash Course | MCP Server 及 ADK 示例；先学协议概念 |
| **B** | [Connecting ADK Agents to MCP Servers](https://www.youtube.com/watch?v=JnKkdHaatwU) | 7:39 | AI Agent Crash Course | MCP Client 连接与 MCPToolset；版本细节需复查 |
| **B** | [How to build an AI Agent and MCP Server (step-by-step)](https://www.youtube.com/watch?v=wBnnA8aIxUs) | 7:54 | Modern AI Agents | Agent + MCP 实操；**与前两节 MCP 实操部分重叠，二选一即可** |
| **B** | [Building custom tools for agents](https://www.youtube.com/watch?v=NiLb5DK4_rU) | 22:09 | The Agent Factory | Function / MCP / Agent-as-Tool / Authenticated Tool 的选择；较长，第二轮 |

### 2.4 Context Engineering & Memory

| 级别 | 视频 | 时长* | 系列 | 中文核心知识点 |
|---|---|---:|---|---|
| **A** | [How to add short-term memory to your AI agent](https://www.youtube.com/watch?v=vfVcDUCucSs) | 6:03 | AI Agent Crash Course · **已翻译（zh-CN）** | Session / Event / State、当前会话记忆 |
| **A** | [How to add persistent memory to your AI agent](https://www.youtube.com/watch?v=HDqzJJhZsxw) | 7:24 | AI Agent Crash Course · **已翻译（zh-CN）** | Session Persistence、跨会话恢复；区别于语义记忆 |
| **A** | [AI agent long-term memory with memory bank](https://www.youtube.com/watch?v=KZPo15M2DbM) | 6:44 | AI Agent Crash Course · **已翻译（zh-CN）** | Long-term Memory、Memory Bank、Semantic Recall |
| **A** | [Context engineering explained: What every AI developer should know](https://www.youtube.com/watch?v=BBPQYtR7oUk) | 10:05 | Modern AI Agents | Context Selection、Compression、Isolation；Context vs Prompt Engineering |
| **B** | [AI Agent Memory Architecture: Structured SQL, Semantic Vector Search & Memory Bank](https://www.youtube.com/watch?v=8C4bh59FtsI) | 12:26 | The Omni App · **已翻译（Mandarin）** | SQL 精确事实 + Vector 语义检索 + Memory Bank、Async Extraction；Voice 案例，但**架构通用** |

### 2.5 Multi-Agent Systems

| 级别 | 视频 | 时长* | 系列 | 中文核心知识点 |
|---|---|---:|---|---|
| **A** | [Foundations of multi-agent systems with ADK](https://www.youtube.com/watch?v=pX0_iIfRilU) | 5:17 | AI Agent Crash Course | 多 Agent 协作、LLM / Workflow / Custom Agent、Hierarchy |
| **B** | [Multi-agent systems, concepts & patterns](https://www.youtube.com/watch?v=TGNScswE0kU) | 23:06 | The Agent Factory | Supervisor / Swarm、协作、Context 分工；第二轮 |

### 2.6 RAG & Agentic RAG

RAG 独立覆盖 Retrieval Pipeline、Embeddings、Chunking、Hybrid Search、Reranking、Agentic Retrieval、Grounding、Evaluation。**RAG 不等于 Memory**；此前已翻译的 SQL / Vector / Memory Bank 视频仍只放在 Memory Topic，避免跨 Topic 重复。

**字段定义：Publisher / Channel（视频发布方）与 Presenter（实际主讲人）必须分开。** 例如 IBM Technology 是频道，Marina Danilevsky 是其中一节课的主讲人；没有可信资料时标注“待核实”，不猜人名。**本表 10 个唯一视频 ID**：原有 2 节 + 本轮人工选择的 8 节；相同知识点提供“二选一/补充”标识，非全部必学。

| 优先级 | 视频（YouTube 直达） | 时长 | 发布频道 Publisher | 主讲人 Presenter | 核心知识点 / 去重说明 | 元数据状态 |
|---|---|---:|---|---|---|---|
| **A** | [How to use Retrieval Augmented Generation (RAG)](https://www.youtube.com/watch?v=oVtlp72f9NQ) | 约6分钟（待核） | **Google Cloud Tech** | 待核实 | 基础 RAG 数据流、Retrieval + Generation；与 IBM RAG 入门二选一；原有条目 | Needs Review |
| **B · 入门替代** | [What is Retrieval-Augmented Generation (RAG)?](https://www.youtube.com/watch?v=T-D1OfcDW1M) | 6:35 | **IBM Technology** | Marina Danilevsky | 基础 RAG、检索/增强/生成、Grounded Answers；和 Google 入门视频二选一；2023-08-23 | Needs Review |
| **A** | [What is Agentic RAG?](https://www.youtube.com/watch?v=0z9_MhcYvcY) | 5:42 | **IBM Technology** | 待核实 | Agent 主动决定何时检索；原有条目；2024-10-28 | Needs Review |
| **B · 延伸** | [RAG's Evolution: From Simple Retrieval to Agentic AI](https://www.youtube.com/watch?v=JB2P5Gk23VI) | 8:48 | **IBM Technology** | Sam Anthony | Keyword → Semantic → Hybrid → Agentic Retrieval；与 Agentic RAG 入门略有重叠，但突出检索演进；2026-05-05 | Needs Review |
| **B · 进阶** | [Every RAG Strategy Explained in 13 Minutes (No Fluff)](https://www.youtube.com/watch?v=tLMViADvSNE) | 12:52 | **Cole Medin** | Cole Medin | Chunking、Reranking、Multi-Query、Contextual / Hierarchical / Agentic RAG；基础学完再看；2025-11-02 | Needs Review |
| **A · 架构** | [Are Vector Databases Still Needed? RAG, AI Agents & Search](https://www.youtube.com/watch?v=rXFV1ivDe6c) | 10:01 | **IBM Technology** | Martin Keen | Vector DB vs SQL Index vs Keyword Search vs Long Context：选择与权衡；2026-11-05 | Needs Review |
| **A · 通用概念** | [Skills vs MCP vs RAG vs Memory: What AI Agents Need to Know](https://www.youtube.com/watch?v=X4FVEEegCbk) | 约9:10（待核） | **IBM Technology** | Martin Keen | Skills/可复用流程、MCP/工具接入、RAG/知识检索、Memory/跨会话记忆边界；2026-09-03 | Needs Review |
| **B · 进阶** | [What Is Chunkless RAG? How Docling & AI Agents Navigate Documents](https://www.youtube.com/watch?v=vRZNJWw78BQ) | 约7:00（待核） | **IBM Technology** | 待核实 | Document Structure / Tree Navigation、Docling；补充替代传统 Chunking 的方法 | Needs Review |
| **B · 替代** | [How Do RAG and Agentic AI Enhance LLM Capabilities?](https://www.youtube.com/watch?v=fB2JQXEH_94) | 约10分钟（待核） | **IBM Technology** | 待核实 | RAG 与 Agentic AI 分工；与 What is Agentic RAG 部分重复，二选一；2025-12-08 | Needs Review |
| **B · 实操** | [RAG Reranking Explained: How To Improve RAG Results](https://www.youtube.com/watch?v=R5MPqm0V6aQ) | 约14分钟（待核） | **pixegami** | pixegami（频道作者；个人姓名待核） | Reranker、Cohere API、Cross-Encoder、Latency/成本权衡；代码偏多，选学；2025-10-06 | Needs Review |

**建议学习顺序**：① Google Cloud Tech 或 IBM RAG Fundamentals（二选一）→ ② IBM Agentic RAG → ③ IBM Vector DB 选型 → ④ IBM Skills / MCP / RAG / Memory 区分 → ⑤ Cole Medin 的 RAG Strategies → ⑥ 按需学 Chunkless 与 Reranking 实操。IBM 的 RAG Evolution 与 RAG vs Agentic AI 作为可替代补充课，不必全部观看。

**作者与元数据来源（2026-11-07）**：
- IBM 官方 [RAG’s Evolution 页面](https://mediacenter.ibm.com/media/RAGs%2BEvolution%3A%2BFrom%2BSimple%2BRetrieval%2Bto%2BAgentic%2BAI/1_jl9mb1q2) 注明 **Sam Anthony**；IBM RAG Fundamentals 的视频讲解者为 **Marina Danilevsky**。
- [Cole Medin 自维护课程笔记](https://github.com/coleam00/cole-medin-knowledge-base/blob/main/sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) 给出视频 ID、12:52、课程知识点。
- [IBM Vector Database 视频索引](https://chooseto.ai/watch/rXFV1ivDe6c) 注明 **Martin Keen**、2026-11-05；[pixegami 课程索引](https://www.classcentral.com/course/youtube-rag-reranking-explained-how-to-improve-rag-results-488821) 给出约 14 分钟与 Python 实操大纲。其余无法确认具体出镜人的条目标“待核实”。
- 本轮使用官方与第三方交叉证据；**并非每条都已完成 YouTube 官方页面、精确时长与主讲人全面核验**，因此保留 `Needs Review`。无法确认的分钟数只写近似，不能伪称精确。

**后续补齐**：RAG Retrieval Evaluation（Recall@K / MRR、Groundedness / Faithfulness）、Hybrid Search / BM25、索引时效、访问控制与 Citation Accuracy；未来新增优先 <=20 分钟、概念教学、与现有 10 节不重复。

### 2.7 Agent Evaluation & Safety

| 级别 | 视频 | 时长* | 系列 | 中文核心知识点 |
|---|---|---:|---|---|
| **A** | [The agent evaluation revolution](https://www.youtube.com/watch?v=WZZLtwnZ4w0) | 8:32 | AI Agent Crash Course | Agent 全过程/工具/状态评估，不只评价最终回答 |
| **A** | [How to evaluate agents in practice](https://www.youtube.com/watch?v=vuBvf7ZRKTA) | 10:53–10:54（待核） | AI Agent Crash Course | Component / Trajectory / Human Evaluation |

**后续优先补齐**：Prompt Injection、Tool Permissions、Guardrails、Tracing、Agent Reliability。安全内容不能只看一个 Evaluation 视频就视为完整覆盖。

### 2.8 Agent Frameworks & Deployment

| 级别 | 视频 | 时长* | 系列 | 中文核心知识点 |
|---|---|---:|---|---|
| **B** | [How to deploy an AI agent to Cloud Run (step by step)](https://www.youtube.com/watch?v=bjZ2M7ThOBc) | 13:44 | Modern AI Agents | Deployment Lifecycle、Cloud Run；偏 Google Cloud 特定实现，基础学完再看 |

\* 时长是候选索引记录；部分来源存在 ±1 秒差异，**最终以视频页复核为准**。发布日期未逐一可靠确定，不填写假日期。候选的整体“最后整理日期”不是逐条官方核验日期。

## 2A. HeyGen 中文翻译状态（永久去重记录）

> **翻译状态与课程元数据状态是两个独立字段**：`Needs Review` 表示原视频元数据尚待核验；`Translated` 表示已成功生成 HeyGen 中文配音。以后任何人工或月度自动更新、批量提交 HeyGen 前，必须先按 YouTube Video ID 检查本表及 HeyGen 任务记录，**不得重复翻译已完成视频**。除非用户明确要求重新翻译。

| YouTube Video ID / 原视频 | Translation State | 目标语言 | HeyGen Translation ID | 中文视频 |
|---|---|---|---|---|
| [vfVcDUCucSs](https://www.youtube.com/watch?v=vfVcDUCucSs) · Short-term memory | **Translated** | zh-CN | `eba09409636f49c2aba399a50af60db1-zh_zh-CN` | [中文 MP4](https://resource2.heygen.ai/video_translate/eba09409636f49c2aba399a50af60db1-zh_zh-CN/original.mp4) |
| [HDqzJJhZsxw](https://www.youtube.com/watch?v=HDqzJJhZsxw) · Persistent memory | **Translated** | zh-CN | `b5095067e5d88966ff36399a2d599026-zh_zh-CN` | [中文 MP4](https://resource2.heygen.ai/video_translate/b5095067e5d88966ff36399a2d599026-zh_zh-CN/original.mp4) |
| [KZPo15M2DbM](https://www.youtube.com/watch?v=KZPo15M2DbM) · Long-term memory bank | **Translated** | zh-CN | `9fa3f46c520142437236c86d3179ef70-zh_zh-CN` | [中文 MP4](https://resource2.heygen.ai/video_translate/9fa3f46c520142437236c86d3179ef70-zh_zh-CN/original.mp4) |
| [8C4bh59FtsI](https://www.youtube.com/watch?v=8C4bh59FtsI) · AI Agent Memory Architecture: Structured SQL, Semantic Vector Search & Memory Bank | **Translated** | Mandarin | `ca1aaca42e4b49d18d75abcce9f38da4-zh` | [中文 MP4](https://resource2.heygen.ai/video_translate/ca1aaca42e4b49d18d75abcce9f38da4-zh/original.mp4) |

**未来操作规范**：新视频默认 `Not Translated`；提交后记录 `Submitted/Running` 和 HeyGen ID；确认成功后改为 `Translated` 并保存结果 URL；失败标记 `Failed`。每次更新先读取 main 最新文件，并检查 HeyGen 账号历史作品（包括非本次对话创建的任务），按 YouTube ID 合并原路径，不复制条目。结果 URL 可能随 HeyGen 保留策略失效，翻译状态和任务 ID 仍须保留以防重复扣费。

## 3. 第一轮学习路线（精选 11 节，约 89 分钟）

先学通用概念，不必按播放列表一次刷完；其余 A 级课可按主题补齐：

1. [AI agents explained](https://www.youtube.com/watch?v=Zqno_vux6d8)（8:29）— LLM / Agent / ReAct。
2. [AI agent design patterns](https://www.youtube.com/watch?v=GDm_uH6VxPY)（8:21）— Single / Sequential / Parallel。
3. [3 Advanced AI agent design patterns](https://www.youtube.com/watch?v=89KKm_a4M7A)（8:00）— Router / Loop / Agent-as-Tool。
4. [How MCP actually works](https://www.youtube.com/watch?v=cGuyrANVi4A)（7:58）— MCP 角色。
5. [MCP vs API](https://www.youtube.com/watch?v=185XGEMefgc)（12:25）— 协议边界。
6. [Short-term memory](https://www.youtube.com/watch?v=vfVcDUCucSs)（6:03）— Session / State。
7. [Persistent memory](https://www.youtube.com/watch?v=HDqzJJhZsxw)（7:24）— 跨会话保存。
8. [Long-term memory](https://www.youtube.com/watch?v=KZPo15M2DbM)（6:44）— Recall / Memory Bank。
9. [Context engineering](https://www.youtube.com/watch?v=BBPQYtR7oUk)（10:05）— Context 选择与压缩。
10. [Foundations of multi-agent systems](https://www.youtube.com/watch?v=pX0_iIfRilU)（5:17）— Agent 分工。
11. [The agent evaluation revolution](https://www.youtube.com/watch?v=WZZLtwnZ4w0)（8:32）— Agent 评估。

**第二轮推荐**：Workflow Communication、Evaluation in Practice、MCP 实操三选一、The Omni App Memory Architecture，再酌情看 The Agent Factory 的长讨论。

**轻量实战验证**：构建一个无 Voice/Vision 的 Document / Research Assistant：单 Agent + Tool → Session State → Persistence → MCP Tool →（确有必要时）Router / Worker → 10 个测试用例的 Tool Selection、成功率、失败恢复 Evaluation。

## 4. 视频来源与系列入口

- [Google Cloud Tech：AI Agent Crash Course 播放列表](https://www.youtube.com/playlist?list=PLIivdWyY5sqLNeW9MPxldbbevMEJGMWBG)
- [Google Cloud Tech：The Agent Factory 播放列表](https://www.youtube.com/playlist?list=PLIivdWyY5sqLXR1eSkiM5bE6pFlXC-OSs)
- Modern AI Agents: From Theory to Production：六节直达链接见各 Topic；未核实唯一官方 Playlist ID，不猜测。
- The Omni App：仅纳入通用 [Memory Architecture](https://www.youtube.com/watch?v=8C4bh59FtsI)；其他 Voice / Vision 专项暂缓。
- 技术核验：[Google ADK 官方文档](https://google.github.io/adk-docs/) · [Google Cloud Agent Architecture 官方文档](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components)

## 5. 视频条目长期模板

未来逐条核验后按主 Topic 添加标准条目（现有紧凑表格可逐步转换，不能复制重复 ID）：

- **英文标题 / 直达 URL（11 字符 Video ID）**、**发布频道 / Publisher**、**主讲人 / Presenter（未核实标待核）**、**所属系列**、**视频发布日期**、**准确时长**。
- **主 Topic**、**中文重点 / 适合阶段**、**A/B/C 推荐级别**、**与已有课的重叠或互补关系**。
- **综合评分及五个分项**（相关性 /30、准确性 /25、清晰度 /20、结构 /15、时长密度 /10）。
- **所涉框架和版本**（若有）、**状态**（Current / Evergreen / Needs Review / Outdated / Unavailable）、**最后官方核验日期及依据**。
- 无法证实的字段留空或标“待核”，不要猜测。

## 6. 每月双索引更新流程（先大学、再 YouTube）

1. 读取 GitHub main 最新 `AGENTS.md`、`docs/university-ai-agent-courses.md`、`docs/youtube-ai-agent-courses.md` 及 SHA；遵守大学课程与 YouTube 短视频各自的严格边界。
2. **A 大学课程**：核实大学、正式课程身份 / 学期 / 官方课件链接，按课程+学期+URL 去重，仅在有真实新信息时合并原路径。
3. **B YouTube**：首先重新阅读**本文件第 1 节最新标准**；优先检索上次扫描以来的新片，优先 General AI Agent 概念和 ≤20 分钟，放宽至 30 分钟需给出理由；专项 Voice / Vision 默认不收。
4. 对每条候选核验视频 ID、频道、发布日期、时长、可访问性、实际内容；**全索引按 Video ID + 语义内容双层去重**。对同质视频只保留最有教学价值的主推荐，其他写替代或不添加；优先最多 5 条高质量新课。
5. 既有视频每月检查可用性 / 技术时效；过时内容注明原因归档，暂无法核实则保留 `Needs Review`，不得把旧视频充作当月新增。维护按 Topic 的学习顺序与课程重叠备注。
6. 有实质变更时重新读取最新 SHA、合并并只提交原路径；无更新则报告“无新增”。写入成功返回**实际 Commit URL**；失败如实说明。每月中文报告包括大学与 YouTube 的新增、更正、核验/过时状况、去重决策及 GitHub Commit 链接。

## 7. 过时与失效视频归档

_目前无已确认过时/失效条目；候选待核状态不是“已归档”。_
