# Agent Frameworks / MCP / RAG — 学习笔记

> 技术知识主笔记。框架 API 会变化，使用前应以最新官方文档验证。

## 核心概念

- **Agent**：模型结合状态、工具与控制逻辑处理任务的系统；可靠性依赖权限、边界与评估。
- **Tool calling**：模型提出工具调用请求，由宿主应用执行并返回结果。
- **MCP (Model Context Protocol)**：规范模型应用与外部工具 / 资源之间的交互接口。
- **Workflow vs Agent**：固定步骤使用显式工作流；需要模型动态决策时再采用自主控制。
- **Checkpoint / Resume**：持久化运行状态以支持中断后的恢复、审计和人工介入。
- **RAG**：检索上下文并结合生成；需要同时评估检索质量与最终答案质量。

## 框架比较的固定维度

| 维度 | 要问的问题 |
| --- | --- |
| 控制流 | 顺序、分支、循环、并发是否可追踪？ |
| 状态管理 | 是否有持久化、checkpoint、恢复、重试？ |
| 工具权限 | 是否可限制工具作用域、审批敏感操作？ |
| Observability | 能否采集 traces、token、latency、failure？ |
| Evaluations | 是否能复现测试并衡量正确性与安全性？ |
| 部署维护 | SDK 语言、版本兼容、成本、供应商锁定？ |

## 待持续研究

- [ ] LangGraph：StateGraph、Checkpoint、interrupt、human-in-the-loop
- [ ] Google ADK：工具、Session、Deployment
- [ ] OpenAI Agents SDK：Handoffs、Tools、Tracing
- [ ] MCP：Transport、Authorization、Tool discovery
- [ ] RAG：Recall@k、Precision@k、MRR、nDCG、groundedness

网页学习展示分别参见 [../notes/langgraph.html](../notes/langgraph.html) 与 [../notes/rag-evaluation.html](../notes/rag-evaluation.html)。
