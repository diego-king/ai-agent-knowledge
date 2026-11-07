# AI Agent YouTube 精品短课索引（按 Topic 分类）

> **范围**：YouTube 上的 AI Agent / LLM Engineering 概念教学短课；**单个视频时长 ≤ 30:00**。优先 Google for Developers、Google Cloud Tech、OpenAI、Anthropic 等官方频道及可信教育者。与仅收录大学课程的 `university-ai-agent-courses.md` 严格分离。
>
> **更新日期**：2026-11-07 · **版本**：v1.0 · **状态**：索引框架已建立，待首次完成逐条核验的视频收录。
>
> **唯一维护路径**：`docs/youtube-ai-agent-courses.md`（GitHub main）；每次更新先读取最新内容和 SHA，在原文件合并，不创建副本。

## 收录标准与评分

- **时长硬限制**：≤ 30:00（30:00 可收录；30:01 不可）。
- **形式**：课程式概念解释、原理、架构、图解、案例分析为主；排除逐行读代码、长时间 IDE 操作、纯 Demo、营销、产品广告、无实质教学内容。
- **真实性**：逐条验证视频 URL、频道身份、发布日期、准确时长、视频是否仍可访问；无法验证不收录。
- **优先推荐**：综合评分 ≥ 80/100；概念清晰度 35、技术准确性 25、课程结构 20、Agent Engineer 实用性 20。评分为编辑判断，非 YouTube 官方评分。
- **避免重复**：以 YouTube Video ID 去重；同一视频只在最相关的主 Topic 收录，其他 Topic 可使用内部交叉链接。
- **新增候选**：每次优先检索最近 14 天发布的视频；若不足则如实说明，不用旧视频冒充新发布。
- **语言**：中文解释，保留必要英文技术名词。

## 时效与复核

| 内容类型 | 复核建议 | 过时判定 |
|---|---|---|
| Agent Fundamentals、ReAct、RAG 基础原理 | 每 6 个月 | 概念性错误或已有重要新共识 |
| Architecture、MCP、Context Engineering、Multi-Agent | 每 3 个月 | 标准、能力、推荐实践发生实质变化 |
| ADK、Agents SDK、具体框架/API/版本 | 每次双周扫描检查 | API 废弃、示例与当前版本不兼容、官方替代方案出现 |
| 所有视频 | 每两周检查可用性及明显时效问题 | 删除、私有化、无法访问、标题/内容严重不符 |

**状态**：`Current`（当前可推荐）、`Evergreen`（经典基础内容仍准确）、`Needs Review`（待核实）、`Outdated`（已过时；从主推荐区移至归档）、`Unavailable`（失效；保留简要记录便于审计）。

不要仅凭发布时间将经典原理视频判定为过时；也不要因为视频新就认定其技术准确。对于框架教程，核对官方文档/版本及视频具体主张；无法核实标记 `Needs Review`，不得写成 `Current`。

## 主题索引

### 1. AI Agent Fundamentals
Agent 与 Workflow 的区别、LLM 决策循环、ReAct、Planning、工具使用基础。

_待收录已核验课程。_

### 2. Agent Architecture
Router / Worker、Orchestration、Event-driven Agent、状态与执行模型。

_待收录已核验课程。_

### 3. Tool Calling & MCP
Function Calling、Tool Discovery、Model Context Protocol、工具权限与边界。

_待收录已核验课程。_

### 4. Context Engineering & Memory
Context Window、记忆、压缩、检索、上下文管理。

_待收录已核验课程。_

### 5. Multi-Agent Systems
Agent Teams、协作、任务分配、并行执行、共享状态。

_待收录已核验课程。_

### 6. RAG & Knowledge Retrieval
Retrieval、Embedding、Chunking、Reranking、Agentic RAG。

_待收录已核验课程。_

### 7. Agent Evaluation & Safety
评估指标、Tracing、可靠性、Prompt Injection、安全与权限。

_待收录已核验课程。_

### 8. Agent Frameworks
Google ADK、OpenAI Agents SDK、LangGraph 等框架的概念和架构课程；不收纯 Coding Demo。

_待收录已核验课程。_

## 视频条目模板（每个视频填写）

```markdown
#### 视频英文标题（中文主题）
- **YouTube**: https://www.youtube.com/watch?v=<verified-video-id>
- **频道 / 发布日期**: <official-channel> / YYYY-MM-DD
- **时长**: MM:SS（≤ 30:00）
- **评分**: XX/100（概念 XX/35、准确 XX/25、结构 XX/20、实用 XX/20）
- **核心知识点**: ...
- **适合人群与推荐理由**: ...
- **代码演示比例**: 低 / 中（以概念讲解为主）
- **涉及框架 / 版本**: ...
- **时效状态**: Current / Evergreen / Needs Review / Outdated / Unavailable
- **最后核验**: YYYY-MM-DD
- **核验依据**: 视频页面 + 必要时的官方技术文档
```

## 每两周更新流程

1. 读取 GitHub `main` 最新 `AGENTS.md` 与本文件（包括 SHA），保留全部既有有效条目。
2. 搜索近 14 天官方及可信频道的 Agent 概念教学视频；核验 URL、准确时长、发布日期和教学形式，评分后按 Topic 去重合并。
3. 对已有视频检查可访问性与技术时效，必要时查官方文档；更新状态、最后核验日期。过时视频从主推荐区转移到下方归档，不无故删除历史。
4. 仅在确有变更时更新版本、日期并提交原路径；并发冲突时重新读取并合并。
5. 输出中文简报：新增、保留、过时/失效、无新增、实际 Commit 链接；GitHub 写入失败时明确报告，绝不声称成功。

## 过时与失效视频归档

_暂无条目。_
