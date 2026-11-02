# 大学 AI Agent 课程 — 按 Topic 汇总

> **唯一维护文件**：按知识主题聚合大学课程，而不是为每堂课创建新文件。
>
> 已查阅公开课程页面（2026-11-01）。以下为根据课程大纲整理的**中文主题摘要**，不是课程官方原文讲义；课程日期、录像和讲义访问权限以原站为准。

## 大学课程索引

| 课程 | 学校与学期 | 重点 | 官方入口 |
| --- | --- | --- | --- |
| 11-768 AI Agents | CMU · Fall 2026 | Agent 能力、工具、记忆、训练、安全、Coding | [Course](https://www.cmu-agents.com/) |
| CS329A Self Improving AI Agents | Stanford · 课程简介 | 自我改进、推理时搜索、评估、应用 | [Bulletin](https://bulletin.stanford.edu/courses/2263721) |
| CS194/294-196 Large Language Model Agents | UC Berkeley · Fall 2024 | Agent 基础、RAG、工具、代码与评估 | [Syllabus / Slides / Video](https://rdi.berkeley.edu/llm-agents/f24) |
| CS194/294-280 Advanced LLM Agents | UC Berkeley · Spring 2025 | 深度推理、规划、Coding Agent、数学与验证 | [Syllabus / Slides / Video](https://rdi.berkeley.edu/adv-llm-agents/sp25) |
| AI Agents for Engineers | CMU · Spring 2026 | Agent 架构、Memory、MCP、RAG 与实践 | [Lecture schedule](https://cmuagents.github.io/schedule/) |
| 11-766 Large Language Model Applications | CMU · Spring 2026 | Web Agent、检索、代码助手等 LLM 应用 | [Syllabus](https://cmu-llms.org/syllabus/) |
| CS185/285 Deep Reinforcement Learning | UC Berkeley · 课程官网 | RL 基础与 Agent 训练补充 | [Course](https://rll.berkeley.edu/deeprlcourse/) |

**使用方法**：学习某个主题时优先读对应 Topic，进入链接查到课程官方资料，再把自己的核心知识点增量写回同一个文件。无需按课程建立副本。

---

## Topic 1. LLM Foundations / Transformer / Prompting

**要掌握**：Token、Embedding、Transformer、Attention、Pretraining vs Finetuning、Instruction Following、Zero-shot/Few-shot、CoT。

**对应课程**
- CMU *AI Agents for Engineers*: Introduction to LLMs、Transformer Deep Dive、Tokenization/Embeddings、Prompting 101（课程页面含部分 slides 链接）。
- UC Berkeley *CS194/294-196*: Foundation of LLMs、Reasoning。
- CMU *11-766*: LLM 应用所需的模型与系统基础。

**一句话总结**：Agent 的规划与工具调用仍建立在 LLM 的输入输出、上下文以及指令遵循能力之上。

## Topic 2. Agent Architecture / Tool Calling / MCP

**要掌握**：ReAct、工具描述和参数 Schema、工具选择、任务循环、Workflow vs Agent、MCP、状态机、工具错误处理。

**对应课程**
- CMU *11-768*: Agent Capabilities / Tool Use / 工具化开发。
- CMU *AI Agents for Engineers*: Agent Architectures、Tool Use and Function Calling。
- UC Berkeley *CS194/294-196*: Agent Frameworks、Compound AI Systems。

**架构笔记**
- **Tool calling**：模型生成调用意图，宿主执行工具并回传结果；宿主需校验参数与权限。
- **MCP**：为 Agent 与外部工具、资源提供标准化连接，不等于 Agent 的规划算法。
- **Workflow vs Agent**：固定可预测的业务逻辑优先显式工作流；开放任务可由 Agent 决策下一步。
- **State / Checkpoint**：状态持久化使长任务更易恢复、审计和人工介入。

**建议练习**：设计一个带工具发现、人工确认、超时重试和 checkpoint 的小型 Agent。

## Topic 3. RAG / Context Engineering / Memory

**要掌握**：Chunking、Embeddings、Vector Search、Hybrid Retrieval、Reranking、Context Window、Agent Memory、长任务上下文压缩。

**对应课程**
- CMU *11-768*: Context / Memory。
- CMU *AI Agents for Engineers*: RAG and Human Feedback、Memory and State、Vector Databases。
- UC Berkeley *CS194/294-196*: Retrieval-augmented Generation。

**核心区分**
- **RAG**：运行时检索可信外部知识，减少知识陈旧或上下文缺失。
- **Memory**：跨轮次保存并提取与任务有关的信息，不等于简单把全部历史放进 prompt。
- **Context Engineering**：决定哪些工具结果、指令、历史片段与工作状态进入模型上下文。

## Topic 4. Reasoning / Planning / Search / Self-Improvement

**要掌握**：CoT、ReAct、Task Decomposition、Self-Verification、Tree Search、Test-time Compute、Verifier、Reflection、Long-horizon Planning。

**对应课程**
- Stanford *CS329A*: Learned / Domain-specific Verifiers、搜索与推理时计算、自我改进。
- Berkeley *CS194/294-280*: Inference-time Reasoning、Search & Planning。
- CMU *11-768*: Planning、Long-horizon Reasoning 与 Agent 训练。

**核心问题**：什么时候增加搜索/验证步骤可以提高可靠性？什么时候只会增加 token 和错误传播？

## Topic 5. Multi-Agent / Human-Agent Interaction

**要掌握**：多 Agent 角色拆分、Supervisor / Worker、消息传递、共享状态、任务交接、人工审批、协同失败模式。

**对应课程**
- CMU *11-768*: Multi-Agent Interaction、Human-Agent Interaction。
- Berkeley *CS194/294-196*: Multi-Agent Collaboration、Human-Agent Interaction。
- CMU *AI Agents for Engineers*: Agent Frameworks 与多 Agent 架构。

**关键原则**：能由一个 Agent + 工具解决的任务，不必默认拆成多个 Agent；多 Agent 会增加协调和调试成本。

## Topic 6. Coding Agent / Web / Computer Use

**要掌握**：Code Edit → Test → Observe → Retry 循环、工具执行沙箱、浏览器与 GUI 操作、Agent-Computer Interface、代码评测。

**对应课程**
- CMU *11-768*: Coding Agents、Computer Use Agents、Deep Research Agents。
- Berkeley *CS194/294-196*: Agents for Software Development、Enterprise Workflows。
- Berkeley *CS194/294-280*: Coding Agents、Code Verification、Multimodal Autonomous Agents。

**建议项目**：从 Issue 开始，让 Agent 修改测试仓库、运行单测、生成 diff，再由人类审批合并。

## Topic 7. Evaluation / Reliability / Safety

**要掌握**：Retrieval Recall@k/Precision@k、MRR/nDCG、答案正确性、Tool-use Correctness、Task Success Rate、Trace Evaluation、Prompt Injection、Sandbox、Credentials、Human Approval。

**对应课程**
- CMU *11-768*: Safety、Sandboxing、Credential Management、Observability。
- Berkeley *CS194/294-196*: Agent Benchmarking、Privacy、Safety、Ethics。
- Stanford *CS329A*: Evaluation 与可靠的 Orchestration。

**评估划分**
- **Retrieval**：是否检索到正确、足够且相关的证据？
- **Action / Tool**：工具名和参数是否正确？执行是否被授权？
- **Task**：最终任务是否完成？是否造成副作用？
- **Safety**：是否受外部文档 Prompt Injection 影响？机密是否泄露？

## Topic 8. Training / RL / Production Agents

**要掌握**：SFT、Preference Optimization、RL Basics、Long-horizon Credit Assignment、Tracing、Retry/Resume、部署成本、限流与可靠性。

**对应课程**
- CMU *11-768*: Agent Training（SFT / RL）、RL Systems。
- Berkeley *CS194/294-280*: Reasoning 的推理时技术与 Post-training。
- Berkeley *CS185/285*: Policy Gradients、Value/Q Learning、Actor-Critic 与 Model-based RL。

**Production Checklist**：幂等、重试、超时、状态持久化、可观测性、权限分离、人工审批、可恢复任务执行。

---

## 学习优先级（面向 AI Agent / LLM Engineer 面试）

1. **优先**：Topic 2（Tools/MCP）→ Topic 3（RAG/Memory）→ Topic 7（Evaluation/Safety）。
2. **第二阶段**：Topic 4（Planning）→ Topic 6（Coding Agent）→ Topic 5（Multi-Agent）。
3. **研究深入**：Topic 1（LLM 基础补齐）→ Topic 8（RL/Training/Production）。

## 资料更新规则

- 新增大学课程：先验证课程所属学校、学期、官网，再加到课程索引并映射 Topics。
- 新学到的内容写入对应 Topic 的现有章节；不要额外新建 `cmu-xxx-v2.md`。
- 如果只找到课程介绍，不要声称有公开 slides、视频或完整笔记。
- 课程论文、讲义仅链接，不复制受版权保护的全文。
