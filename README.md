# ai-agent-knowledge

个人 AI Agent / LLM Engineering 知识库，使用 GitHub 作为持久化的唯一数据源（Single Source of Truth）。

此仓库支持 Markdown、HTML、JSON、CSS 和 Python。ChatGPT Mobile、Desktop、Web、Work 与 Codex 可以围绕相同文件路径协作，但**这些客户端不会自动双向同步 ChatGPT Project Sources**。更新必须由有 GitHub 写入权限的客户端显式提交；其他会话在读取前要重新获取最新版本。

## 目录

| 路径 | 用途 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | AI / Codex 读写规则 |
| [docs/python-interview.md](docs/python-interview.md) | Python 面试知识主笔记 |
| [docs/data-structures.md](docs/data-structures.md) | Union Find、Priority Queue 等模板 |
| [docs/agent-frameworks.md](docs/agent-frameworks.md) | Agent 框架和选型笔记 |
| [notes/python-interview.html](notes/python-interview.html) | Python 交互式网页讲解 |
| [notes/langgraph.html](notes/langgraph.html) | LangGraph 可视化学习页面 |
| [notes/rag-evaluation.html](notes/rag-evaluation.html) | RAG 评估指标学习页面 |
| [data/learning-progress.json](data/learning-progress.json) | 可机器读取的学习进度 |
| [assets/styles.css](assets/styles.css) | HTML 页面共用样式 |
| [assets/diagrams/](assets/diagrams/) | 图表资源目录 |
| [code/examples.py](code/examples.py) | 可运行 Python 示例 |

## 跨设备更新流程

1. 在当前设备打开同一个 GitHub 仓库，确定要更新的**规范路径**。
2. 读取目标文件最新内容与 blob SHA。
3. 只合并所需更改，保留旧内容；不要创建 `-v2`、`-new`、`-final` 等副本。
4. 使用当前 SHA 提交更新（或在 Codex 中同步分支后 Commit / Push）。
5. 向用户返回文件链接及提交信息；下个会话重新读取仓库最新版本。
6. 如果权限不足或提交冲突，必须明确说明，不能假称保存成功。

**格式分工**：`docs/` 保存知识的规范文字版；`notes/` 是网页学习体验，修改事实内容时保持对应文字笔记一致。`data/` 仅保存结构化进度；`code/` 保存可运行代码。

**安全**：仓库为私有不代表可以存储密钥。不要提交 API keys、tokens、密码、个人敏感数据或未经授权的机密材料。GitHub HTML 文件不能直接在仓库页面当作交互网页运行；如需发布 GitHub Pages，请单独审查其公开性和访问控制。
