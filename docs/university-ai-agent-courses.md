# AI Agent / LLM Engineering 大学课件主题索引

> 资源状态截至 **2026-10-23**（America/Toronto）。中文整理；lecture 名称保留官方英文，方便检索原文。

## 收录范围：仅限大学课程（所有后续更新必须遵守）

**本文件仅收录大学（University）开设或由大学教师明确作为正式课程发布的 AI Agent / LLM Engineering 课程资源。** 可收录大学官方课程页、syllabus、lecture slides（PDF/PPTX）、lecture notes、以及由该课程官方链接的教学代码仓库。新增前必须核实大学归属、具体课程身份、学期／年份（如可得）、官方 URL 和资源状态；按课程＋学期＋URL 去重，并保留原有历史统计口径。

**不收录** 独立的商业／厂商课程（例如 LangChain Academy）、非大学训练营、一般开源项目教程、框架产品文档或没有大学课程关联的实战材料。即使内容涉及 MCP、Multi-Agent、RAG、Memory、Evals、Coding Agents 等 Topic，也不能因为主题匹配而纳入。此限制适用于人工修改、定期 Automation、未来所有版本更新；发现误收录应先核实后移除，并说明更正原因。每次更新必须先阅读 `AGENTS.md` 和本文件最新版本。

## 使用范围与核验方法

本文件用于未来添加到 ChatGPT Project Sources。它是**课程课件导航与证据索引**，不是课件正文合集；上传本文件不会自动把所有外链 PDF 的内容导入项目。要对某份课件逐页分析，应另行上传该课件或要求打开其链接。

本次承接“查找AI课程讲义”对话，读取后发现旧助手回答只返回引用占位符，未取得原清单正文。因此依据用户明确列出的课程，从大学、教师及课程官方仓库重建。覆盖所列课程系列及明确标注的学期，不声称复原了旧对话所有链接，也不声称包含学校内部 Canvas 资料。

本版共 **21 个课程版本、377 条课堂／专题记录**：其中 **291 条有具体 PDF/PPTX/Notes 链接**，另 **86 条列入缺失／仅视频／未来课程附录**。具体文档 URL 去重后 **319 个**，其中 **289 个通过文件类型或正文页面检查**；其余状态逐项注明。

- **已验证**：在核验日发起公开 GET 请求，得到 HTTP 200/206；PDF 检查 `%PDF-`，PPTX 检查 ZIP 文件头与对应文件扩展名，HTML Notes 检查页面响应。未逐页校对所有课件内容，HTTP 成功不代表课件已读完。
- **页面可达／内容待验证**：官方交互式 Notes 页面返回 HTML，但未逐一验证其动态 trace 内容；不得当作已验证 PDF。
- **待验证**：已在官方目录或官方搜索索引发现确切 URL，但本次访问超时／返回异常。超时不等于链接永久失效。
- **仅目录／未发现直链**：有课程安排，未获得可确认的 PDF/PPTX/Notes URL；只链接原目录，绝不按编号、日期或文件名补造地址。
- **去重**：同一 lecture 在主主题只展开一次，其他主题通过编号交叉引用；同一 URL 不重复当作不同文件。不同学期、不同 URL 的材料保留，不仅凭同名合并。未做所有文件的全文哈希去重。
- **分类**：主题归类由整理者根据官方 lecture 标题、目录描述与公开资源形式判断，不代表学校原有分类。编号用于本版引用，不等同学校 lecture number。
- **日期**：每条的月日应与其“学期”合读。2026 秋季未到上课日期的条目明确标记“计划”，不会算作已发布课件。

## 主题导航

- [LLM Foundations｜语言模型基础](#topic-foundations)
- [RAG｜检索增强生成](#topic-rag)
- [Context Engineering｜上下文工程](#topic-context)
- [Tool Use / MCP｜工具调用与协议](#topic-tools)
- [Agent Architecture / Orchestration｜架构与编排](#topic-architecture)
- [Reasoning / Planning｜推理与规划](#topic-reasoning)
- [Memory / Skills｜记忆与技能](#topic-memory)
- [Multi-Agent｜多智能体](#topic-multi)
- [Evaluation｜评估](#topic-eval)
- [Optimization｜优化](#topic-optimization)
- [Coding Agents｜编程智能体](#topic-coding)
- [Production / Reliability / Security / Infra｜生产、可靠性、安全与基础设施](#topic-production)
- [补充主题｜数据、对齐、人机交互、多模态与应用](#topic-supplement)
- [课程原始目录与版本说明](#courses)
- [缺失、仅视频和未来课程](#missing)
- [核验局限与待补齐项](#limitations)
- [如何添加到 Project Sources](#project-sources)

<a id="courses"></a>
## 课程原始目录与版本说明

| 编码 | 学校／课号与课程 | 学期 | 具体资料记录 / 全部记录 | 官方目录 |
|---|---|---|---:|---|
| SZ26 | Stanford · CS329Z · Engineering AI Agents | 2026 秋 | 9 / 19 | [课程目录](https://cs329z.stanford.edu/) |
| ST25 | Stanford · CS329T · Trustworthy Machine Learning / Agentic AI | 2025 秋 | 10 / 11 | [课程目录](https://web.stanford.edu/class/cs329t/syllabus.html) |
| SG26 | Stanford · CS224G · Building and Scaling LLM Applications | 2026 冬 | 14 / 16 | [课程目录](https://web.stanford.edu/class/cs224g/schedule.html) |
| SG25 | Stanford · CS224G · Apps with LLMs Inside | 2025 冬 | 13 / 14 | [课程目录](https://web.stanford.edu/class/cs224g/2025/schedule.html) |
| SX26 | Stanford · CS329X · Human-Centered LLMs | 2026 秋 | 9 / 17 | [课程目录](https://web.stanford.edu/class/cs329x/index.html) |
| SX25 | Stanford · CS329X · Human-Centered LLMs | 2025 秋 | 16 / 17 | [课程目录](https://web.stanford.edu/class/cs329x/2526_index.html) |
| S33626 | Stanford · CS336 · Language Modeling from Scratch | 2026 春 | 17 / 19 | [课程目录](https://cs336.stanford.edu/) |
| S33625 | Stanford · CS336 · Language Modeling from Scratch | 2025 春 | 17 / 19 | [课程目录](https://cs336.stanford.edu/spring2025/index.html) |
| C76826 | CMU · 11-768 · AI Agents | 2026 秋 | 15 / 25 | [课程目录](https://www.cmu-agents.com/#/schedule) |
| C76626 | CMU · 11-766 · Large Language Model Applications | 2026 春 | 25 / 25 | [课程目录](https://cmu-llms.org/schedule/) |
| C71125 | CMU · 11-711 · Advanced Natural Language Processing | 2025 秋 | 22 / 23 | [课程目录](https://cmu-l3.github.io/anlp-fall2025/#schedule) |
| B24 | UC Berkeley · CS194/294-196 · LLM Agents | 2024 秋 | 12 / 12 | [课程目录](https://rdi.berkeley.edu/llm-agents/f24) |
| BA25 | UC Berkeley · CS194/294-280 · Advanced LLM Agents | 2025 春 | 12 / 12 | [课程目录](https://rdi.berkeley.edu/adv-llm-agents/sp25) |
| B25 | UC Berkeley · CS194/294-196 · Agentic AI | 2025 秋 | 9 / 13 | [课程目录](https://rdi.berkeley.edu/agentic-ai/f25) |
| I59825 | UIUC · CS598 · Topics in LLM Agents（Jiaxuan You） | 2025 春 | 16 / 20 | [课程目录](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents) |
| U23426 | UC San Diego · CSE/DSC234 · Data-Centric AI and AI Engineering（Arun Kumar） | 2026 春 | 5 / 12 | [课程目录](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html) |
| U23425 | UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang） | 2025 冬 | 20 / 20 | [课程目录](https://haoailab.com/cse234-w25/) |
| US25 | UC San Diego · CSE291A · Systems for LLMs and AI Agents（Yiying Zhang） | 2025 秋 | 6 / 29 | [课程目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| UA26 | UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu） | 2026 冬 | 16 / 16 | [课程目录](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html) |
| UA25 | UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu） | 2025 冬 | 16 / 16 | [课程目录](https://pearls-lab.github.io/ai-agents-course/lectures.html) |
| H26 | Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations | 2026 秋 | 12 / 22 | [课程目录](https://cs2680.seas.harvard.edu/) |

版本辨析：CS329T 本版采用 2025 秋季面向 Agent 构建与评估的 syllabus，不能与 2021 年 Trustworthy ML 老版本混用。CS224G、CS329X、CS336 均保留 2025 和 2026 版本。CMU 11-766 的旧版常见课号为 11-667，本版不把它写成同一学期。UIUC CS598 是专题课号，本版特指 Jiaxuan You 的 Topics in LLM Agents，不混入其他 CS598 班。

UCSD 特别注意：2026 春 CSE/DSC234（Arun Kumar）侧重 Data-Centric AI / AI Engineering；2025 冬 CSE234（Hao Zhang）侧重 ML Systems。CSE291A 另分别有 Yiying Zhang 的 Systems for LLMs and AI Agents 与 Prithviraj Ammanabrolu 的 AI Agents。Yiying Zhang 的 [2026 秋主页](https://cseweb.ucsd.edu/~yiying/cse291a-fall26/)已确认存在，但本次无法读取其 lecture 目录，未把 2025 讲义冒充为 2026。

建议入门路径：模型基础 → RAG／上下文 → Tool Use → 单 Agent 架构 → 记忆 → 多 Agent → 评估 → 优化 → 生产与安全。CS336 与 UCSD 的系统课可作为底层补充；形式化数学、机器人、社会交互按需求选读。

<a id="topic-foundations"></a>
## LLM Foundations｜语言模型基础

模型结构、分词、预训练、解码、基础表示学习。

<a id="sz26-02"></a>
### SZ26-02 · LLMs for Builders

**学校／课程**：Stanford · CS329Z · Engineering AI Agents；**学期**：2026 秋；**课堂日期**：Mon Sep 28。

**原始目录**：[课程 syllabus / schedule](https://cs329z.stanford.edu/)。**主题**：[LLM Foundations](#topic-foundations)、[Context Engineering](#topic-context)、[Optimization](#topic-optimization)。

- [PDF · Slides](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx26-02"></a>
### SX26-02 · The Ultimate Crash into LLMs

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2026 秋；**课堂日期**：Sep 28, Monday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/index.html)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/2627/Lecture2_llms_prompting.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-02"></a>
### SX25-02 · The Ultimate Crash into LLMs

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Sep 25, Thursday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture2_llms_prompting.pdf) — 已验证 · HTTP 206 / PDF。

<a id="st25-07"></a>
### ST25-07 · Deep dive into LLMs

**学校／课程**：Stanford · CS329T · Trustworthy Machine Learning / Agentic AI；**学期**：2025 秋；**课堂日期**：Tue Oct 21。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329t/syllabus.html)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · Slides](https://web.stanford.edu/class/cs329t/slides/Lecture%207%20--%20CS%20329T%20Fall%202025.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-02"></a>
### SG25-02 · LLMs and LMMs

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：1/14。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · LLMs and LMMs](https://web.stanford.edu/class/cs224g/2025/lectures/CS_224G_About%20LLMs_LMMs_2025.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33626-01"></a>
### S33626-01 · L1 Overview, tokenization [Percy]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Mon March 30。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[LLM Foundations](#topic-foundations)。

- [交互式 Python Notes（HTML） · lecture_01.py](https://cs336.stanford.edu/lectures/?trace=lecture_01) — 页面可达；动态 Notes 内容待验证。

<a id="s33626-03"></a>
### S33626-03 · L3 Architectures, hyperparameters [Tatsu]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Mon April 6。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · lecture 3.pdf](https://raw.githubusercontent.com/stanford-cs336/lectures/main/lecture_03.pdf)；[官方仓库预览](https://github.com/stanford-cs336/lectures/blob/main/lecture_03.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33626-04"></a>
### S33626-04 · L4 Attention alternatives and mixture of experts [Tatsu]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Wed April 8。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · lecture 4.pdf](https://raw.githubusercontent.com/stanford-cs336/lectures/main/lecture_04.pdf)；[官方仓库预览](https://github.com/stanford-cs336/lectures/blob/main/lecture_04.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33625-01"></a>
### S33625-01 · L1 Overview, tokenization (Percy)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Tues April 1。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[LLM Foundations](#topic-foundations)。

- [交互式 Python Notes（HTML） · lecture_01.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_01.json) — 页面可达；动态 Notes 内容待验证。

<a id="s33625-03"></a>
### S33625-03 · L3 Architectures, hyperparameters (Tatsu)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Tues April 8。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · lecture 3.pdf](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/e9cb2488fdb53ea37f0e38924ec3a1701925cef3/nonexecutable/2025%20Lecture%203%20-%20architecture.pdf)；[官方仓库预览](https://github.com/stanford-cs336/spring2025-lectures/blob/e9cb2488fdb53ea37f0e38924ec3a1701925cef3/nonexecutable/2025%20Lecture%203%20-%20architecture.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33625-04"></a>
### S33625-04 · L4 Mixture of experts (Tatsu)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Thurs April 10。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · lecture 4.pdf](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/98455ec198c9a88ec1ab2b1c4058662431b54ce3/nonexecutable/2025%20Lecture%204%20-%20MoEs.pdf)；[官方仓库预览](https://github.com/stanford-cs336/spring2025-lectures/blob/98455ec198c9a88ec1ab2b1c4058662431b54ce3/nonexecutable/2025%20Lecture%204%20-%20MoEs.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-01"></a>
### C76626-01 · Origins of LLMs

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：01/13/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-01-13-llm-history.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-02"></a>
### C76626-02 · Natural language understanding vs generation

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：01/15/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-01-15-nlu-nlg.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-01"></a>
### C71125-01 · Introduction & Fundamentals

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 1 08/26/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-01-intro.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-02"></a>
### C71125-02 · Fundamentals: Learned Representations

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 2 08/28/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-02-learned-representations.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-03"></a>
### C71125-03 · Fundamentals: Autoregressive Language Modeling

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 3 09/02/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-03-lm.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-04"></a>
### C71125-04 · Architectures I: Recurrent Neural Networks

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 4 09/04/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-04-rnns.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-05"></a>
### C71125-05 · Architectures II: Attention and Transformers

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 5 09/09/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-05-transformers.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-06"></a>
### C71125-06 · Learning I: Pretraining

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 6 09/11/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-06-pretraining.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-21"></a>
### C71125-21 · Advanced Architectures II: Mixture of Experts

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 25 11/18/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-21-moe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua26-09"></a>
### UA26-09 · Attention and Language Modeling

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Tue, Feb 10, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/attention_and_language_modeling.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-09"></a>
### UA25-09 · Attention and Language Modeling

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Tue, Feb 11, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/attention_language_modeling.pdf) — 已验证 · HTTP 206 / PDF。

**跨主题索引**（完整链接与核验状态见主条目）：

| 条目 | Lecture | 学校／版本 |
|---|---|---|
| [ST25-01](#st25-01) | Course introduction and overview | Stanford CS329T（2025 秋） |
| [SG26-01](#sg26-01) | CS 224G Re-introduction | Stanford CS224G（2026 冬） |
| [C71125-15](#c71125-15) | Reinforcement Learning I: Fundamentals | CMU 11-711（2025 秋） |
| [C71125-20](#c71125-20) | Advanced Architectures I: Long Sequence Models | CMU 11-711（2025 秋） |
| [B25-01](#b25-01) | Introduction | UC Berkeley CS194/294-196（2025 秋） |
| [I59825-01](#i59825-01) | Course Introduction | UIUC CS598（2025 春） |
| [UA26-01](#ua26-01) | Intro | UC San Diego CSE291A（2026 冬） |
| [UA25-01](#ua25-01) | Intro | UC San Diego CSE291（2025 冬） |
| [U23425-16](#u23425-16) | 16 LLM - 1: transformers, attention | UC San Diego CSE234（2025 冬） |
| [U23425-19](#u23425-19) | 19 LLM - 3: Continuous batching, paged attention, Disaggreged prefill and decoding | UC San Diego CSE234（2025 冬） |
| [U23425-20](#u23425-20) | 20 LLM - 4: flash attention, deepseek-v3 review, ending words | UC San Diego CSE234（2025 冬） |
| [H26-01](#h26-01) | Course overview and logistics | Harvard CS2680（2026 秋） |
| [H26-11](#h26-11) | Efficient LLM serving basics I: intro to LLMs | Harvard CS2680（2026 秋） |
| [US25-01](#us25-01) | Course Introduction and Generative AI Overview | UC San Diego CSE291A（2025 秋） |

<a id="topic-rag"></a>
## RAG｜检索增强生成

检索、向量与图检索、知识组织、Deep Research；检索系统的推理开销另交叉索引到 Infra。

<a id="sz26-03"></a>
### SZ26-03 · Retrieval-Augmented Generation (RAG)

**学校／课程**：Stanford · CS329Z · Engineering AI Agents；**学期**：2026 秋；**课堂日期**：Wed Sep 30。

**原始目录**：[课程 syllabus / schedule](https://cs329z.stanford.edu/)。**主题**：[RAG](#topic-rag)、[Context Engineering](#topic-context)、[Evaluation](#topic-eval)。

- [PDF · Slides](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf) — 已验证 · HTTP 206 / PDF。

<a id="st25-02"></a>
### ST25-02 · Models, Prompting and RAG

**学校／课程**：Stanford · CS329T · Trustworthy Machine Learning / Agentic AI；**学期**：2025 秋；**课堂日期**：Thu Sep 25。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329t/syllabus.html)。**主题**：[RAG](#topic-rag)、[Context Engineering](#topic-context)。

- [PDF · Slides](https://web.stanford.edu/class/cs329t/slides/Lecture%202%20-%20CS%20329T%20Fall%202025.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg26-05"></a>
### SG26-05 · Context Engineering & RAG

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：TueJan 20。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[RAG](#topic-rag)、[Context Engineering](#topic-context)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%205%20-%20Context%20Engineering.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-12"></a>
### SG25-12 · RAG and Fine Tuning

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：3/4。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[RAG](#topic-rag)、[Optimization](#topic-optimization)。

- [PDF · RAG and Fine Tuning](https://web.stanford.edu/class/cs224g/2025/lectures/RAG_Finetuning.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-05"></a>
### C76626-05 · Learning representations and embeddings

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：01/27/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[RAG](#topic-rag)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-01-27-embeddings.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-06"></a>
### C76626-06 · Retrieval 1: Storing and retrieving knowledge

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：01/29/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[RAG](#topic-rag)、[Evaluation](#topic-eval)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-01-29-retrieval.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-07"></a>
### C76626-07 · Retrieval 2: Retrieval augmented generation, deep research

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：02/03/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[RAG](#topic-rag)、[Evaluation](#topic-eval)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-02-03-retrieval+rag.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-08"></a>
### C76626-08 · Retrieval 3: Retrieval augmented generation (2) and deep research

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：02/05/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[RAG](#topic-rag)、[Evaluation](#topic-eval)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-02-05-rag+deepresearch.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-09"></a>
### C76626-09 · Deep research

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：02/10/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[RAG](#topic-rag)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-02-10-deep-research.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-10"></a>
### C71125-10 · Modeling I: Retrieval and RAG

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 10 09/25/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[RAG](#topic-rag)、[Evaluation](#topic-eval)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/akari_anlp_2025_rag_lecture.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-10"></a>
### C76826-10 · Domains 3: Deep Research Agents

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Thu, Sep 24。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[RAG](#topic-rag)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Lecture 10 slides](https://www.cmu-agents.com/slides/lecture-10-deep-research-agents.pdf) — 已验证 · HTTP 206 / PDF。

<a id="b24-03"></a>
### B24-03 · Agentic AI Frameworks & AutoGen / Building a Multimodal Knowledge Assistant

**学校／课程**：UC Berkeley · CS194/294-196 · LLM Agents；**学期**：2024 秋；**课堂日期**：Sept 23。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/llm-agents/f24)。**主题**：[RAG](#topic-rag)、[Multi-Agent](#topic-multi)、[Agent Architecture / Orchestration](#topic-architecture)、[补充主题](#topic-supplement)。

- [PDF · Chi’s Slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/autogen.pdf) — 已验证 · HTTP 206 / PDF。
- [PDF · Jerry’s Slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/MKA.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/watch?v=OOdtmCMSOo4) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="i59825-11"></a>
### I59825-11 · Retrieval-Augmented Generation

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：March 4。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[RAG](#topic-rag)、[Evaluation](#topic-eval)。

- [PPTX · Oliver Li, Ting-Wei Li, Xuying Ning (Group 12)](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/11_RAG.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/11_RAG.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="u23426-06"></a>
### U23426-06 · Topic 2: Retrieval and Context Engineering — Part 2

**学校／课程**：UC San Diego · CSE/DSC234 · Data-Centric AI and AI Engineering（Arun Kumar）；**学期**：2026 春；**课堂日期**：第4–6周。

**原始目录**：[课程 syllabus / schedule](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html)。**主题**：[RAG](#topic-rag)、[Context Engineering](#topic-context)、[Evaluation](#topic-eval)。

- [PDF · PDF](https://cseweb.ucsd.edu/classes/sp26/cse234-a/downloads/Topic2-RetrievalContextEng-Part2.pdf) — 待验证 · 连接超时。

备注：官方目录按主题课件包组织，包不等于一次课堂。目录列出 PDF/PPTX；本次源站超时，只收录搜索索引实际返回的 PDF 地址，其余直链及 PPTX 待验证，未按文件名推测。

<a id="u23426-07"></a>
### U23426-07 · Topic 2: Retrieval and Context Engineering — Part 3

**学校／课程**：UC San Diego · CSE/DSC234 · Data-Centric AI and AI Engineering（Arun Kumar）；**学期**：2026 春；**课堂日期**：第4–6周。

**原始目录**：[课程 syllabus / schedule](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html)。**主题**：[RAG](#topic-rag)、[Context Engineering](#topic-context)、[Evaluation](#topic-eval)。

- [PDF · PDF](https://cseweb.ucsd.edu/classes/sp26/cse234-a/downloads/Topic2-RetrievalContextEng-Part3.pdf) — 待验证 · 连接超时。

备注：官方目录按主题课件包组织，包不等于一次课堂。目录列出 PDF/PPTX；本次源站超时，只收录搜索索引实际返回的 PDF 地址，其余直链及 PPTX 待验证，未按文件名推测。

<a id="topic-context"></a>
## Context Engineering｜上下文工程

提示设计、上下文构建与压缩、长上下文、检索与上下文的取舍。

<a id="sg26-06"></a>
### SG26-06 · More Context Engineering

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：ThuJan 22。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[Context Engineering](#topic-context)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%206%20-%20More%20Context%20Engineering.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-04"></a>
### SG25-04 · Prompt Engineering

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：1/21。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[Context Engineering](#topic-context)。

- [PDF · Prompt Engineering](https://web.stanford.edu/class/cs224g/2025/lectures/Prompts.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-03"></a>
### C76626-03 · The science of prompting

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：01/20/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[Context Engineering](#topic-context)、[补充主题](#topic-supplement)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-01-20-prompting.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-07"></a>
### C71125-07 · Learning II/Inference I: In-Context Learning

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 7 09/16/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[Context Engineering](#topic-context)、[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-07-icl-prompting.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-20"></a>
### C71125-20 · Advanced Architectures I: Long Sequence Models

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 24 11/13/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[Context Engineering](#topic-context)、[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-20-longcontext.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-03"></a>
### C76826-03 · Agent Capabilities 2: Context Management for Long-Context Agents

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Tue, Sep 1。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Context Engineering](#topic-context)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Lecture 3 slides](https://www.cmu-agents.com/slides/lecture-03-long-context.pdf) — 已验证 · HTTP 206 / PDF。

<a id="h26-04"></a>
### H26-04 · Agents design I: context management and tool design

**学校／课程**：Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations；**学期**：2026 秋；**课堂日期**：2026-09-16。

**原始目录**：[课程 syllabus / schedule](https://cs2680.seas.harvard.edu/)。**主题**：[Context Engineering](#topic-context)、[Tool Use / MCP](#topic-tools)。

- [PDF · [slide]](https://cs2680.seas.harvard.edu/slides/4_agent_design_1.pdf) — 已验证 · HTTP 200 / PDF。

<a id="us25-19"></a>
### US25-19 · Agent Memory and Context

**学校／课程**：UC San Diego · CSE291A · Systems for LLMs and AI Agents（Yiying Zhang）；**学期**：2025 秋；**课堂日期**：11/7。

**原始目录**：[课程 syllabus / schedule](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/)。**主题**：[Context Engineering](#topic-context)、[Memory / Skills](#topic-memory)。

- [PDF · PDF](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/agent-memory.pdf) — 待验证 · 连接超时。

备注：目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。

**跨主题索引**（完整链接与核验状态见主条目）：

| 条目 | Lecture | 学校／版本 |
|---|---|---|
| [SZ26-02](#sz26-02) | LLMs for Builders | Stanford CS329Z（2026 秋） |
| [SZ26-03](#sz26-03) | Retrieval-Augmented Generation (RAG) | Stanford CS329Z（2026 秋） |
| [SZ26-06](#sz26-06) | Agent Design Patterns & Scaffolds | Stanford CS329Z（2026 秋） |
| [SZ26-07](#sz26-07) | Agent Memory Architectures | Stanford CS329Z（2026 秋） |
| [SX26-08](#sx26-08) | Building Full-Stack HAI Systems | Stanford CS329X（2026 秋） |
| [ST25-02](#st25-02) | Models, Prompting and RAG | Stanford CS329T（2025 秋） |
| [SG26-05](#sg26-05) | Context Engineering & RAG | Stanford CS224G（2026 冬） |
| [U23426-06](#u23426-06) | Topic 2: Retrieval and Context Engineering — Part 2 | UC San Diego CSE/DSC234（2026 春） |
| [U23426-07](#u23426-07) | Topic 2: Retrieval and Context Engineering — Part 3 | UC San Diego CSE/DSC234（2026 春） |

<a id="topic-tools"></a>
## Tool Use / MCP｜工具调用与协议

工具描述、函数调用、MCP、工具和环境接口。

<a id="sz26-04"></a>
### SZ26-04 · Tool Use & Function Calling

**学校／课程**：Stanford · CS329Z · Engineering AI Agents；**学期**：2026 秋；**课堂日期**：Mon Oct 5。

**原始目录**：[课程 syllabus / schedule](https://cs329z.stanford.edu/)。**主题**：[Tool Use / MCP](#topic-tools)、[Evaluation](#topic-eval)。

- [PDF · Slides](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf) — 已验证 · HTTP 206 / PDF。

<a id="st25-06"></a>
### ST25-06 · MCP, effective tool descriptions, evals

**学校／课程**：Stanford · CS329T · Trustworthy Machine Learning / Agentic AI；**学期**：2025 秋；**课堂日期**：Thu Oct 16。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329t/syllabus.html)。**主题**：[Tool Use / MCP](#topic-tools)、[Evaluation](#topic-eval)。

- [PDF · Slides](https://web.stanford.edu/class/cs329t/slides/Model%20Context%20Protocol%20%28%20Yusuf%20Ozuysal%29.pdf) — 已验证 · HTTP 206 / PDF。
- [PDF · Slides (Ishita)](https://web.stanford.edu/class/cs329t/slides/ishita-mcp.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-11"></a>
### C76626-11 · Tool-use, chitchat, personas, and companionship

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：02/17/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[Tool Use / MCP](#topic-tools)、[补充主题](#topic-supplement)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-02-17-chatbots.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-02"></a>
### C76826-02 · Agent Capabilities 1: Tool Use

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Thu, Aug 27。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Tool Use / MCP](#topic-tools)。

- [PDF · Lecture 2 slides](https://www.cmu-agents.com/slides/lecture-02-tool-use.pdf) — 已验证 · HTTP 206 / PDF。

<a id="i59825-10"></a>
### I59825-10 · Tool Use

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：Feb 27。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[Tool Use / MCP](#topic-tools)。

- [PPTX · Aryan Bhardwaj, Ke Yang, Kashob Kumar Roy (Group 14)](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/10_tool_use.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/10_tool_use.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="ua26-13"></a>
### UA26-13 · Neurosymbolic Tool Use Methods and Agent Reasoning

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Tue, Feb 24, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[Tool Use / MCP](#topic-tools)、[Reasoning / Planning](#topic-reasoning)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/neurosymbolic_tool_use.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-13"></a>
### UA25-13 · Neurosymbolic Tool Use Methods and Agent Reasoning

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Tue, Feb 25, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[Tool Use / MCP](#topic-tools)、[Reasoning / Planning](#topic-reasoning)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/neurosymbolic_control.pdf) — 已验证 · HTTP 206 / PDF。

<a id="us25-17"></a>
### US25-17 · Agent Tooling

**学校／课程**：UC San Diego · CSE291A · Systems for LLMs and AI Agents（Yiying Zhang）；**学期**：2025 秋；**课堂日期**：11/3。

**原始目录**：[课程 syllabus / schedule](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/)。**主题**：[Tool Use / MCP](#topic-tools)。

- [PDF · PDF](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/tooling.pdf) — 待验证 · 连接超时。

备注：目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。

**跨主题索引**（完整链接与核验状态见主条目）：

| 条目 | Lecture | 学校／版本 |
|---|---|---|
| [H26-04](#h26-04) | Agents design I: context management and tool design | Harvard CS2680（2026 秋） |
| [U23426-10](#u23426-10) | Topic 3: Agent Engineering | UC San Diego CSE/DSC234（2026 春） |

<a id="topic-architecture"></a>
## Agent Architecture / Orchestration｜架构与编排

Agent loop、工作流、状态与控制流、DSPy、LangGraph、OpenHands、PydanticAI 等课程材料。

<a id="sz26-01"></a>
### SZ26-01 · Introduction — What Are Agentic Systems?

**学校／课程**：Stanford · CS329Z · Engineering AI Agents；**学期**：2026 秋；**课堂日期**：Wed Sep 23。

**原始目录**：[课程 syllabus / schedule](https://cs329z.stanford.edu/)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Slides](https://web.stanford.edu/class/cs329z/slides/lecture01.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sz26-05"></a>
### SZ26-05 · Frameworks & Orchestration

**学校／课程**：Stanford · CS329Z · Engineering AI Agents；**学期**：2026 秋；**课堂日期**：Wed Oct 7。

**原始目录**：[课程 syllabus / schedule](https://cs329z.stanford.edu/)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[Optimization](#topic-optimization)、[Coding Agents](#topic-coding)、[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://web.stanford.edu/class/cs329z/slides/lecture05.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sz26-06"></a>
### SZ26-06 · Agent Design Patterns & Scaffolds

**学校／课程**：Stanford · CS329Z · Engineering AI Agents；**学期**：2026 秋；**课堂日期**：Mon Oct 12。

**原始目录**：[课程 syllabus / schedule](https://cs329z.stanford.edu/)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[Reasoning / Planning](#topic-reasoning)、[Context Engineering](#topic-context)。

- [PDF · Slides](https://web.stanford.edu/class/cs329z/slides/lecture06.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx26-08"></a>
### SX26-08 · Building Full-Stack HAI Systems

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2026 秋；**课堂日期**：Oct 19, Monday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/index.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[Memory / Skills](#topic-memory)、[Context Engineering](#topic-context)、[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/2627/Lecture8_building_full_stack_hai_systems.pdf) — 已验证 · HTTP 206 / PDF。

<a id="st25-01"></a>
### ST25-01 · Course introduction and overview

**学校／课程**：Stanford · CS329T · Trustworthy Machine Learning / Agentic AI；**学期**：2025 秋；**课堂日期**：Tue Sep 23。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329t/syllabus.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[LLM Foundations](#topic-foundations)。

- [PDF · Slides](https://web.stanford.edu/class/cs329t/slides/Lecture%201%20-%20CS%20329T%20Fall%202025.pdf) — 已验证 · HTTP 206 / PDF。

<a id="st25-03"></a>
### ST25-03 · Agentic AI

**学校／课程**：Stanford · CS329T · Trustworthy Machine Learning / Agentic AI；**学期**：2025 秋；**课堂日期**：Tue Sep 30。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329t/syllabus.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[Evaluation](#topic-eval)、[Memory / Skills](#topic-memory)。

- [PDF · Slides](https://web.stanford.edu/class/cs329t/slides/Lecture%203%20--%20CS%20329T%20Fall%202025.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg26-01"></a>
### SG26-01 · CS 224G Re-introduction

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：TueJan 6。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[LLM Foundations](#topic-foundations)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%201%20-%20Introduction.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg26-07"></a>
### SG26-07 · Agentic Workflows & Design Patterns

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：TueJan 27。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%207%20-%20Agent%20Orchestration%20&%20Workflow%20Design.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg26-11"></a>
### SG26-11 · Agentic Orchestration with PydanticAI

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：ThuFeb 19。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%2014%20-%20Agentic%20Orchestration%20with%20PydanticAI.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-08"></a>
### SG25-08 · Agentic Design Patterns

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：2/11。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Agentic Design Patterns](https://web.stanford.edu/class/cs224g/2025/lectures/Agentic_Design_Patterns.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-14"></a>
### SG25-14 · Design Databases for Multimodal AI; Building Agentic Systems

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：3/11。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[补充主题](#topic-supplement)。

- [PDF · Building Agentic Systems](https://web.stanford.edu/class/cs224g/2025/lectures/Building_Agentic_Systems_CS224.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-17"></a>
### C71125-17 · Agents

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 19 10/28/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-17-agents.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-01"></a>
### C76826-01 · Course Overview: What Is an Agent?

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Tue, Aug 25。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Lecture 1 slides](https://www.cmu-agents.com/slides/lecture-01-agents.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-07"></a>
### C76826-07 · Computer Use Agents

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Tue, Sep 15。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Lecture 7 slides](https://www.cmu-agents.com/slides/lecture-07-computer-use-agents.pdf) — 已验证 · HTTP 206 / PDF。

<a id="b24-02"></a>
### B24-02 · LLM agents: brief history and overview

**学校／课程**：UC Berkeley · CS194/294-196 · LLM Agents；**学期**：2024 秋；**课堂日期**：Sept 16。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/llm-agents/f24)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Slides](https://rdi.berkeley.edu/llm-agents/assets/llm_agent_history.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/watch?v=RM6ZArd2nVc) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="b24-05"></a>
### B24-05 · Compound AI Systems & the DSPy Framework

**学校／课程**：UC Berkeley · CS194/294-196 · LLM Agents；**学期**：2024 秋；**课堂日期**：Oct 7。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/llm-agents/f24)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[补充主题](#topic-supplement)。

- [PDF · Slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/dspy_lec.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/JEMYuzrKLUw) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="b24-07"></a>
### B24-07 · AI Agents for Enterprise Workflows

**学校／课程**：UC Berkeley · CS194/294-196 · LLM Agents；**学期**：2024 秋；**课堂日期**：Oct 21。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/llm-agents/f24)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Slides](https://rdi.berkeley.edu/llm-agents/assets/agentworkflows.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/-yf-e-9FvOc) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="ba25-06"></a>
### BA25-06 · Multimodal Autonomous AI Agents

**学校／课程**：UC Berkeley · CS194/294-280 · Advanced LLM Agents；**学期**：2025 春；**课堂日期**：Mar 10th。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/adv-llm-agents/sp25)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[补充主题](#topic-supplement)。

- [PDF · Slides](https://rdi.berkeley.edu/adv-llm-agents/slides/ruslan-multimodal.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/RPINOYM12RU) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="b25-01"></a>
### B25-01 · Introduction

**学校／课程**：UC Berkeley · CS194/294-196 · Agentic AI；**学期**：2025 秋；**课堂日期**：Sep 8。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/agentic-ai/f25)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[LLM Foundations](#topic-foundations)。

- [PDF · Slides](https://rdi.berkeley.edu/agentic-ai/slides/introduction_25.pdf) — 已验证 · HTTP 206 / PDF。

<a id="b25-02"></a>
### B25-02 · LLM Agents Overview

**学校／课程**：UC Berkeley · CS194/294-196 · Agentic AI；**学期**：2025 秋；**课堂日期**：Sep 15。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/agentic-ai/f25)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Slides](https://rdi.berkeley.edu/agentic-ai/slides/lecture1.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/watch?v=r1qZpYAmqmg) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="i59825-01"></a>
### I59825-01 · Course Introduction

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：Jan 21。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[LLM Foundations](#topic-foundations)。

- [PPTX · Jiaxuan](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/01_Introduction.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/01_Introduction.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="i59825-02"></a>
### I59825-02 · AI Agent Overview I

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：Jan 23。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PPTX · Jiaxuan](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/02_AGI_1.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/02_AGI_1.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="i59825-03"></a>
### I59825-03 · AI Agent Overview II

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：Jan 28。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PPTX · Jiaxuan](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/03_AGI_2.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/03_AGI_2.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="i59825-04"></a>
### I59825-04 · AI Agent Overview III

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：Jan 30。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PPTX · Jiaxuan](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/04_AGI_3.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/04_AGI_3.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="i59825-16"></a>
### I59825-16 · Gaming Agents

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：April 8。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[补充主题](#topic-supplement)。

- [PDF · Dwip Dalal, Chuxuan Hu, Xiaona Zhou (Group 5)](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/14_GamingAgents.pdf)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/14_GamingAgents.pdf) — 已验证 · HTTP 206 / PDF。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="ua26-01"></a>
### UA26-01 · Intro

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Tue, Jan 6, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/intro.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua26-02"></a>
### UA26-02 · What are Agents?

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Thu, Jan 8, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/what_is_an_agent.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-01"></a>
### UA25-01 · Intro

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Tue, Jan 7, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/intro.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-02"></a>
### UA25-02 · What are Agents?

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Thu, Jan 9, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/what_is_an_agent.pdf) — 已验证 · HTTP 206 / PDF。

<a id="h26-01"></a>
### H26-01 · Course overview and logistics

**学校／课程**：Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations；**学期**：2026 秋；**课堂日期**：2026-09-02。

**原始目录**：[课程 syllabus / schedule](https://cs2680.seas.harvard.edu/)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[LLM Foundations](#topic-foundations)。

- [PDF · [slide]](https://cs2680.seas.harvard.edu/slides/1_intro.pdf) — 已验证 · HTTP 200 / PDF。

<a id="u23426-10"></a>
### U23426-10 · Topic 3: Agent Engineering

**学校／课程**：UC San Diego · CSE/DSC234 · Data-Centric AI and AI Engineering（Arun Kumar）；**学期**：2026 春；**课堂日期**：第8–10周。

**原始目录**：[课程 syllabus / schedule](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[Tool Use / MCP](#topic-tools)、[Memory / Skills](#topic-memory)、[Reasoning / Planning](#topic-reasoning)、[Multi-Agent](#topic-multi)、[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · PDF](https://cseweb.ucsd.edu/classes/sp26/cse234-a/downloads/Topic3-AgentEngineering.pdf) — 待验证 · 连接超时。

备注：官方目录按主题课件包组织，包不等于一次课堂。目录列出 PDF/PPTX；本次源站超时，只收录搜索索引实际返回的 PDF 地址，其余直链及 PPTX 待验证，未按文件名推测。

<a id="us25-01"></a>
### US25-01 · Course Introduction and Generative AI Overview

**学校／课程**：UC San Diego · CSE291A · Systems for LLMs and AI Agents（Yiying Zhang）；**学期**：2025 秋；**课堂日期**：9/26。

**原始目录**：[课程 syllabus / schedule](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)、[LLM Foundations](#topic-foundations)。

- [PDF · PDF](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/Overview.pdf) — 待验证 · 连接超时。

备注：目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。

<a id="us25-20"></a>
### US25-20 · AI Workflow and Agent Autotuning

**学校／课程**：UC San Diego · CSE291A · Systems for LLMs and AI Agents（Yiying Zhang）；**学期**：2025 秋；**课堂日期**：11/10。

**原始目录**：[课程 syllabus / schedule](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/)。**主题**：[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · PDF](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/agent-autotuning.pdf) — 待验证 · 连接超时。

备注：目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。

**跨主题索引**（完整链接与核验状态见主条目）：

| 条目 | Lecture | 学校／版本 |
|---|---|---|
| [SZ26-08](#sz26-08) | Multi-Agent Systems | Stanford CS329Z（2026 秋） |
| [ST25-05](#st25-05) | Systematic evaluation of agentic systems | Stanford CS329T（2025 秋） |
| [ST25-08](#st25-08) | Data curation and RL to optimize agents | Stanford CS329T（2025 秋） |
| [SG26-12](#sg26-12) | Data Strategy & Memory Layer for AI Agents | Stanford CS224G（2026 冬） |
| [SG25-06](#sg25-06) | Building AI Agents for IT Ops | Stanford CS224G（2025 冬） |
| [SG25-09](#sg25-09) | LLM Orchestration; Memory Layer for AI Agents | Stanford CS224G（2025 冬） |
| [C76826-03](#c76826-03) | Agent Capabilities 2: Context Management for Long-Context Agents | CMU 11-768（2026 秋） |
| [C76826-05](#c76826-05) | Agent Capabilities 4: Planning, Task Decomposition, and Multi-Agent Coordination | CMU 11-768（2026 秋） |
| [C76826-06](#c76826-06) | Domains 1: Coding Agents | CMU 11-768（2026 秋） |
| [C76826-10](#c76826-10) | Domains 3: Deep Research Agents | CMU 11-768（2026 秋） |
| [C76826-14](#c76826-14) | Frameworks 1: OpenHands | CMU 11-768（2026 秋） |
| [C76826-15](#c76826-15) | Frameworks 2: Orchestration and Monitoring | CMU 11-768（2026 秋） |
| [B24-03](#b24-03) | Agentic AI Frameworks & AutoGen / Building a Multimodal Knowledge Assistant | UC Berkeley CS194/294-196（2024 秋） |
| [BA25-03](#ba25-03) | On Reasoning, Memory, and Planning of Language Agents | UC Berkeley CS194/294-280（2025 春） |
| [BA25-11](#ba25-11) | Abstraction and Discovery with Large Language Model Agents | UC Berkeley CS194/294-280（2025 春） |
| [BA25-12](#ba25-12) | Towards building safe and secure agentic AI | UC Berkeley CS194/294-280（2025 春） |
| [B25-03](#b25-03) | Evolution of system designs from an AI engineer perspective | UC Berkeley CS194/294-196（2025 秋） |
| [B25-04](#b25-04) | Post-Training Verifiable Agents | UC Berkeley CS194/294-196（2025 秋） |
| [B25-05](#b25-05) | Agent Evaluation & Project Overview | UC Berkeley CS194/294-196（2025 秋） |
| [B25-10](#b25-10) | Practical Lessons from Deploying Real-World AI Agents | UC Berkeley CS194/294-196（2025 秋） |
| [U23425-02](#u23425-02) | 2 Basics: Modern DL, computational graph, frameworks | UC San Diego CSE234（2025 冬） |
| [H26-02](#h26-02) | Agents use I: How Claude Code Works | Harvard CS2680（2026 秋） |
| [H26-05](#h26-05) | Agents design II: multi-agent architecture, coordination, and communication | Harvard CS2680（2026 秋） |
| [H26-22](#h26-22) | Cost-effective agents | Harvard CS2680（2026 秋） |

<a id="topic-reasoning"></a>
## Reasoning / Planning｜推理与规划

搜索、计划、测试时计算、神经符号推理与形式化证明。

<a id="st25-04"></a>
### ST25-04 · Recap, further discussion, and planning for projects

**学校／课程**：Stanford · CS329T · Trustworthy Machine Learning / Agentic AI；**学期**：2025 秋；**课堂日期**：Thu Oct 2。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329t/syllabus.html)。**主题**：[Reasoning / Planning](#topic-reasoning)。

- [PDF · Slides](https://web.stanford.edu/class/cs329t/slides/Lecture%204%20--%20CS%20329T%20Fall%202025.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg26-03"></a>
### SG26-03 · LLMs, LMMs & Reasoning Models 2026

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：TueJan 13。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[Reasoning / Planning](#topic-reasoning)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%203%20-%20About%20LLMs%202026.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-05"></a>
### C76826-05 · Agent Capabilities 4: Planning, Task Decomposition, and Multi-Agent Coordination

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Tue, Sep 8。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Reasoning / Planning](#topic-reasoning)、[Multi-Agent](#topic-multi)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Lecture 5 slides](https://www.cmu-agents.com/slides/lecture-05-planning.pdf) — 已验证 · HTTP 206 / PDF。

<a id="b24-01"></a>
### B24-01 · LLM Reasoning

**学校／课程**：UC Berkeley · CS194/294-196 · LLM Agents；**学期**：2024 秋；**课堂日期**：Sept 9。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/llm-agents/f24)。**主题**：[Reasoning / Planning](#topic-reasoning)。

- [PDF · Intro](https://rdi.berkeley.edu/llm-agents/assets/intro.pdf) — 已验证 · HTTP 206 / PDF。
- [PDF · Slides](https://rdi.berkeley.edu/llm-agents/assets/llm-reasoning.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/watch?v=QL-FS_Zcmyo) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="b24-08"></a>
### B24-08 · Towards a unified framework of Neural and Symbolic Decision Making

**学校／课程**：UC Berkeley · CS194/294-196 · LLM Agents；**学期**：2024 秋；**课堂日期**：Oct 28。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/llm-agents/f24)。**主题**：[Reasoning / Planning](#topic-reasoning)。

- [PDF · Slides](https://rdi.berkeley.edu/llm-agents/assets/102824-yuandongtian.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/wm9-7VBpdEo) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="ba25-01"></a>
### BA25-01 · Inference-Time Techniques for LLM Reasoning

**学校／课程**：UC Berkeley · CS194/294-280 · Advanced LLM Agents；**学期**：2025 春；**课堂日期**：Jan 27th。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/adv-llm-agents/sp25)。**主题**：[Reasoning / Planning](#topic-reasoning)、[Optimization](#topic-optimization)。

- [PDF · Intro](https://rdi.berkeley.edu/adv-llm-agents/slides/llm-agents-berkeley-intro-sp25.pdf) — 已验证 · HTTP 206 / PDF。
- [PDF · Slides](https://rdi.berkeley.edu/adv-llm-agents/slides/inference_time_techniques_lecture_sp25.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/g0Dwtf3BH-0) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="ba25-02"></a>
### BA25-02 · Learning to reason with LLMs

**学校／课程**：UC Berkeley · CS194/294-280 · Advanced LLM Agents；**学期**：2025 春；**课堂日期**：Feb 3rd。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/adv-llm-agents/sp25)。**主题**：[Reasoning / Planning](#topic-reasoning)。

- [PDF · Slides](https://rdi.berkeley.edu/adv-llm-agents/slides/Jason-Weston-Reasoning-Alignment-Berkeley-Talk.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/_MNlLhU33H0) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="ba25-04"></a>
### BA25-04 · Open Training Recipes for Reasoning in Language Models

**学校／课程**：UC Berkeley · CS194/294-280 · Advanced LLM Agents；**学期**：2025 春；**课堂日期**：Feb 24th。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/adv-llm-agents/sp25)。**主题**：[Reasoning / Planning](#topic-reasoning)。

- [PDF · Slides](https://rdi.berkeley.edu/adv-llm-agents/slides/OLMo-Tulu-Reasoning-Hanna.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/cMiu3A7YBks) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="ba25-08"></a>
### BA25-08 · AlphaProof: when reinforcement learning meets formal mathematics

**学校／课程**：UC Berkeley · CS194/294-280 · Advanced LLM Agents；**学期**：2025 春；**课堂日期**：Mar 31st。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/adv-llm-agents/sp25)。**主题**：[Reasoning / Planning](#topic-reasoning)、[Optimization](#topic-optimization)。

- [PDF · Slides](https://rdi.berkeley.edu/adv-llm-agents/slides/alphaproof.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/3gaEMscOMAU) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="ba25-09"></a>
### BA25-09 · Language models for autoformalization and theorem proving

**学校／课程**：UC Berkeley · CS194/294-280 · Advanced LLM Agents；**学期**：2025 春；**课堂日期**：Apr 7th。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/adv-llm-agents/sp25)。**主题**：[Reasoning / Planning](#topic-reasoning)。

- [PDF · Slides](https://rdi.berkeley.edu/adv-llm-agents/slides/mathverification.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/cLhWEyMQ4mQ) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="ba25-10"></a>
### BA25-10 · Advanced topics in theorem proving

**学校／课程**：UC Berkeley · CS194/294-280 · Advanced LLM Agents；**学期**：2025 春；**课堂日期**：Apr 14th。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/adv-llm-agents/sp25)。**主题**：[Reasoning / Planning](#topic-reasoning)。

- [PDF · Slides](https://rdi.berkeley.edu/adv-llm-agents/slides/welleck2025_berkeley_bridging.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/Gy5Nm17l9oo) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="ba25-11"></a>
### BA25-11 · Abstraction and Discovery with Large Language Model Agents

**学校／课程**：UC Berkeley · CS194/294-280 · Advanced LLM Agents；**学期**：2025 春；**课堂日期**：Apr 21st。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/adv-llm-agents/sp25)。**主题**：[Reasoning / Planning](#topic-reasoning)、[Agent Architecture / Orchestration](#topic-architecture)、[补充主题](#topic-supplement)。

- [PDF · Slides](https://rdi.berkeley.edu/adv-llm-agents/slides/swarat.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/IHc0TEMrEdY) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="i59825-05"></a>
### I59825-05 · Reasoning

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：Feb 11。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[Reasoning / Planning](#topic-reasoning)。

- [PPTX · Shraddhaa Mohan, Kartik Ramesh, Allen Thomas (Group 4)](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/05_Reasoning.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/05_Reasoning.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="i59825-07"></a>
### I59825-07 · Planning

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：Feb 18。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[Reasoning / Planning](#topic-reasoning)。

- [PPTX · Siddarth Madala, Risham Sidhu, Tianjiao Yu (Group 9)](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/07_Planning.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/07_Planning.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="ua26-05"></a>
### UA26-05 · Search for Planning in Simulations

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Tue, Jan 20, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[Reasoning / Planning](#topic-reasoning)、[补充主题](#topic-supplement)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/search_for_planning_in_simulations.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua26-14"></a>
### UA26-14 · Agent Reasoning and Inference Time Methods

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Thu, Feb 26, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[Reasoning / Planning](#topic-reasoning)、[Optimization](#topic-optimization)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/inf_scaling.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-05"></a>
### UA25-05 · Search for Planning in Simulations

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Tue, Jan 21, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[Reasoning / Planning](#topic-reasoning)、[补充主题](#topic-supplement)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/search_planning_simulation.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-14"></a>
### UA25-14 · Agent Reasoning and Inference Time Methods

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Thu, Feb 27, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[Reasoning / Planning](#topic-reasoning)、[Optimization](#topic-optimization)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/inference_time_scaling.pdf) — 已验证 · HTTP 206 / PDF。

**跨主题索引**（完整链接与核验状态见主条目）：

| 条目 | Lecture | 学校／版本 |
|---|---|---|
| [SZ26-06](#sz26-06) | Agent Design Patterns & Scaffolds | Stanford CS329Z（2026 秋） |
| [BA25-03](#ba25-03) | On Reasoning, Memory, and Planning of Language Agents | UC Berkeley CS194/294-280（2025 春） |
| [UA26-13](#ua26-13) | Neurosymbolic Tool Use Methods and Agent Reasoning | UC San Diego CSE291A（2026 冬） |
| [UA25-13](#ua25-13) | Neurosymbolic Tool Use Methods and Agent Reasoning | UC San Diego CSE291（2025 冬） |
| [U23426-10](#u23426-10) | Topic 3: Agent Engineering | UC San Diego CSE/DSC234（2026 春） |

<a id="topic-memory"></a>
## Memory / Skills｜记忆与技能

工作记忆、长期记忆、技能库、个性化与程序性知识。GPU 显存不等同 Agent Memory。

<a id="sz26-07"></a>
### SZ26-07 · Agent Memory Architectures

**学校／课程**：Stanford · CS329Z · Engineering AI Agents；**学期**：2026 秋；**课堂日期**：Wed Oct 14。

**原始目录**：[课程 syllabus / schedule](https://cs329z.stanford.edu/)。**主题**：[Memory / Skills](#topic-memory)、[Context Engineering](#topic-context)。

- [PDF · Slides](https://web.stanford.edu/class/cs329z/slides/lecture07.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-06"></a>
### SX25-06 · Guest Lecture: Omar Shaikh and Taylor Sorensen: Personalization

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Oct 9, Thursday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[Memory / Skills](#topic-memory)、[补充主题](#topic-supplement)。

- [PDF · slides - Omar](https://web.stanford.edu/class/cs329x/slides/Lecture6_A_hai_grounding.pdf) — 已验证 · HTTP 206 / PDF。
- [PDF · slides - Taylor](https://web.stanford.edu/class/cs329x/slides/Lecture6_B_pluralistic.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg26-12"></a>
### SG26-12 · Data Strategy & Memory Layer for AI Agents

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：TueFeb 24。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[Memory / Skills](#topic-memory)、[Agent Architecture / Orchestration](#topic-architecture)、[补充主题](#topic-supplement)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%2015%20-%20Data%20Strategy%20and%20Memory%20Layer%20for%20AI%20Agents.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-09"></a>
### SG25-09 · LLM Orchestration; Memory Layer for AI Agents

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：2/18。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[Memory / Skills](#topic-memory)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · LLM Orchestration](https://web.stanford.edu/class/cs224g/2025/lectures/LLM_Orchestration.pdf) — 已验证 · HTTP 206 / PDF。
- [PDF · Memory Layer for AI Agents](https://web.stanford.edu/class/cs224g/2025/lectures/Mem0_CS224.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-04"></a>
### C76826-04 · Agent Capabilities 3: Skills and Memory

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Thu, Sep 3。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Memory / Skills](#topic-memory)。

- [PDF · Lecture 4 slides](https://www.cmu-agents.com/slides/lecture-04-memory-and-skills.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ba25-03"></a>
### BA25-03 · On Reasoning, Memory, and Planning of Language Agents

**学校／课程**：UC Berkeley · CS194/294-280 · Advanced LLM Agents；**学期**：2025 春；**课堂日期**：Feb 10th。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/adv-llm-agents/sp25)。**主题**：[Memory / Skills](#topic-memory)、[Reasoning / Planning](#topic-reasoning)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Slides](https://rdi.berkeley.edu/adv-llm-agents/slides/language_agents_YuSu_Berkeley.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/zvI4UN2_i-w) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="i59825-06"></a>
### I59825-06 · Memory

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：Feb 13。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[Memory / Skills](#topic-memory)。

- [PPTX · Tianyi Huang, Boyang Sun, Yuyang Wang (Group 6)](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/06_Memory.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/06_Memory.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="h26-06"></a>
### H26-06 · Agents design III: agent memory and reliability

**学校／课程**：Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations；**学期**：2026 秋；**课堂日期**：2026-09-28。

**原始目录**：[课程 syllabus / schedule](https://cs2680.seas.harvard.edu/)。**主题**：[Memory / Skills](#topic-memory)、[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · [slide]](https://cs2680.seas.harvard.edu/slides/6_agent_design_3.pdf) — 已验证 · HTTP 200 / PDF。

**跨主题索引**（完整链接与核验状态见主条目）：

| 条目 | Lecture | 学校／版本 |
|---|---|---|
| [SX26-08](#sx26-08) | Building Full-Stack HAI Systems | Stanford CS329X（2026 秋） |
| [ST25-03](#st25-03) | Agentic AI | Stanford CS329T（2025 秋） |
| [S33626-02](#s33626-02) | L2 PyTorch (einops), resource accounting (FLOPs, memory, arithmetic intensity) [Percy] | Stanford CS336（2026 春） |
| [U23426-10](#u23426-10) | Topic 3: Agent Engineering | UC San Diego CSE/DSC234（2026 春） |
| [US25-19](#us25-19) | Agent Memory and Context | UC San Diego CSE291A（2025 秋） |

<a id="topic-multi"></a>
## Multi-Agent｜多智能体

任务分解、协作通信、角色与协调；同时覆盖人机协作的关联材料。

<a id="sz26-08"></a>
### SZ26-08 · Multi-Agent Systems

**学校／课程**：Stanford · CS329Z · Engineering AI Agents；**学期**：2026 秋；**课堂日期**：Mon Oct 19。

**原始目录**：[课程 syllabus / schedule](https://cs329z.stanford.edu/)。**主题**：[Multi-Agent](#topic-multi)、[Agent Architecture / Orchestration](#topic-architecture)、[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://web.stanford.edu/class/cs329z/slides/lecture08.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-14"></a>
### C76626-14 · Multi-agent systems

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：02/26/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[Multi-Agent](#topic-multi)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-02-26-multi-agent-systems.pdf) — 已验证 · HTTP 206 / PDF。

<a id="b25-07"></a>
### B25-07 · Multi-Agent AI

**学校／课程**：UC Berkeley · CS194/294-196 · Agentic AI；**学期**：2025 秋；**课堂日期**：Oct 20。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/agentic-ai/f25)。**主题**：[Multi-Agent](#topic-multi)。

- [PDF · Slides](https://rdi.berkeley.edu/agentic-ai/slides/multiagent_berkeley_2025.pptx.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/watch?v=SrLcGdVOb9w) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="i59825-13"></a>
### I59825-13 · Agent Framework: Multi-agent Systems

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：March 27。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[Multi-Agent](#topic-multi)。

- [PPTX · Nimet Beyza Bozdag, Hyeonjeong Ha, Shuhaib Mehri (Group 2)](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/12_MultiAgent.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/12_MultiAgent.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="ua26-15"></a>
### UA26-15 · Multi-Agent Systems and Human-AI Collaboration

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Tue, Mar 3, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[Multi-Agent](#topic-multi)、[补充主题](#topic-supplement)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/multi_agent.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-15"></a>
### UA25-15 · Multi-Agent Systems and Human-AI Collaboration

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Tue, Mar 4, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[Multi-Agent](#topic-multi)、[补充主题](#topic-supplement)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/multi_agent.pdf) — 已验证 · HTTP 206 / PDF。

<a id="h26-03"></a>
### H26-03 · Agents use II: 100x Engineer with Multi-agents

**学校／课程**：Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations；**学期**：2026 秋；**课堂日期**：2026-09-14。

**原始目录**：[课程 syllabus / schedule](https://cs2680.seas.harvard.edu/)。**主题**：[Multi-Agent](#topic-multi)、[Coding Agents](#topic-coding)。

- [PDF · [slide]](https://cs2680.seas.harvard.edu/slides/3_agent_use_2.pdf) — 已验证 · HTTP 200 / PDF。

<a id="h26-05"></a>
### H26-05 · Agents design II: multi-agent architecture, coordination, and communication

**学校／课程**：Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations；**学期**：2026 秋；**课堂日期**：2026-09-23。

**原始目录**：[课程 syllabus / schedule](https://cs2680.seas.harvard.edu/)。**主题**：[Multi-Agent](#topic-multi)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · [slide]](https://cs2680.seas.harvard.edu/slides/5_agent_design_2.pdf) — 已验证 · HTTP 200 / PDF。

**跨主题索引**（完整链接与核验状态见主条目）：

| 条目 | Lecture | 学校／版本 |
|---|---|---|
| [C76826-05](#c76826-05) | Agent Capabilities 4: Planning, Task Decomposition, and Multi-Agent Coordination | CMU 11-768（2026 秋） |
| [B24-03](#b24-03) | Agentic AI Frameworks & AutoGen / Building a Multimodal Knowledge Assistant | UC Berkeley CS194/294-196（2024 秋） |
| [U23426-10](#u23426-10) | Topic 3: Agent Engineering | UC San Diego CSE/DSC234（2026 春） |

<a id="topic-eval"></a>
## Evaluation｜评估

模型与 Agent 评估、LLM-as-Judge、实验设计、统计可靠性、人机互动评估。

<a id="sx26-06"></a>
### SX26-06 · Evaluating Human-AI interaction

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2026 秋；**课堂日期**：Oct 12, Monday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/index.html)。**主题**：[Evaluation](#topic-eval)、[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/2627/Lecture6_evaluate_HAI.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-08"></a>
### SX25-08 · Evaluating Human-AI interaction

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Oct 16, Thursday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[Evaluation](#topic-eval)、[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture8_evaluate_HAI.pdf) — 已验证 · HTTP 206 / PDF。

<a id="st25-05"></a>
### ST25-05 · Systematic evaluation of agentic systems

**学校／课程**：Stanford · CS329T · Trustworthy Machine Learning / Agentic AI；**学期**：2025 秋；**课堂日期**：Tue Oct 14。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329t/syllabus.html)。**主题**：[Evaluation](#topic-eval)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Slides](https://web.stanford.edu/class/cs329t/slides/Allison%20Jia%20-%20slides.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-07"></a>
### SG25-07 · Evaluation Methods

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：2/6。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[Evaluation](#topic-eval)。

- [PDF · Evaluation Methods](https://web.stanford.edu/class/cs224g/2025/lectures/Prompt_Eval.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33626-12"></a>
### S33626-12 · L12 Evaluation [Percy]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Wed May 6。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[Evaluation](#topic-eval)。

- [交互式 Python Notes（HTML） · lecture_12.py](https://cs336.stanford.edu/lectures/?trace=lecture_12) — 页面可达；动态 Notes 内容待验证。

<a id="s33625-12"></a>
### S33625-12 · L12 Evaluation (Percy)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Thurs May 8。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[Evaluation](#topic-eval)。

- [交互式 Python Notes（HTML） · lecture_12.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_12.json) — 页面可达；动态 Notes 内容待验证。

<a id="c76626-13"></a>
### C76626-13 · LLMs for evaluation: Synthetic data generation, simulation, automatic evaluation, AI-as-judge

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：02/24/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[Evaluation](#topic-eval)、[补充主题](#topic-supplement)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-02-24-evaluation.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-13"></a>
### C71125-13 · Evaluation Techniques

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 13 10/07/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[Evaluation](#topic-eval)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-13-evaluation.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-14"></a>
### C71125-14 · Research Skills and Experimental Design

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 14 10/09/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[Evaluation](#topic-eval)、[补充主题](#topic-supplement)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-14-experimentation.pdf) — 已验证 · HTTP 206 / PDF。

<a id="b24-11"></a>
### B24-11 · Measuring Agent capabilities and Anthropic’s RSP

**学校／课程**：UC Berkeley · CS194/294-196 · LLM Agents；**学期**：2024 秋；**课堂日期**：Nov 25。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/llm-agents/f24)。**主题**：[Evaluation](#topic-eval)。

- [PDF · Slides](https://rdi.berkeley.edu/llm-agents/assets/antrsp.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/6y2AnWol7oo) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="b25-05"></a>
### B25-05 · Agent Evaluation & Project Overview

**学校／课程**：UC Berkeley · CS194/294-196 · Agentic AI；**学期**：2025 秋；**课堂日期**：Oct 6。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/agentic-ai/f25)。**主题**：[Evaluation](#topic-eval)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Slides](https://rdi.berkeley.edu/agentic-ai/slides/LLM%20Agent%20Evaluations%20&%20Project%20Overview.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/watch?v=VfOA2a0dj4w) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="b25-08"></a>
### B25-08 · Predictable Noise in LLM

**学校／课程**：UC Berkeley · CS194/294-196 · Agentic AI；**学期**：2025 秋；**课堂日期**：Oct 27。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/agentic-ai/f25)。**主题**：[Evaluation](#topic-eval)。

- [PDF · Slides](https://rdi.berkeley.edu/agentic-ai/slides/PredEval.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/watch?v=HV8pugcFVO0) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="i59825-09"></a>
### I59825-09 · via benchmarks/LLMs/VLMs

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：Feb 25。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[Evaluation](#topic-eval)。

- [PPTX · Vincent Han, Rui Pan, RUI Yang (Group 10)](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/09_Evaluation.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/09_Evaluation.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="h26-07"></a>
### H26-07 · Agent design IV: agent evaluation

**学校／课程**：Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations；**学期**：2026 秋；**课堂日期**：2026-09-30。

**原始目录**：[课程 syllabus / schedule](https://cs2680.seas.harvard.edu/)。**主题**：[Evaluation](#topic-eval)。

- [PDF · [slide]](https://cs2680.seas.harvard.edu/slides/7_agent_design_4.pdf) — 已验证 · HTTP 200 / PDF。

<a id="h26-21"></a>
### H26-21 · Agent evaluation and benchmarks

**学校／课程**：Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations；**学期**：2026 秋；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://cs2680.seas.harvard.edu/)。**主题**：[Evaluation](#topic-eval)。

- [HTML Notes · Agent evaluation and benchmarks](https://cs2680.seas.harvard.edu/notes/agent-evaluation.html) — 已验证 · HTTP 200 / HTML。

备注：教师专题 Notes，可与对应 lecture 配套阅读。

<a id="us25-23"></a>
### US25-23 · Agent Evaluation and Benchmarks

**学校／课程**：UC San Diego · CSE291A · Systems for LLMs and AI Agents（Yiying Zhang）；**学期**：2025 秋；**课堂日期**：11/17。

**原始目录**：[课程 syllabus / schedule](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/)。**主题**：[Evaluation](#topic-eval)。

- [PDF · PDF](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/evaluation.pdf) — 待验证 · 连接超时。

备注：目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。

**跨主题索引**（完整链接与核验状态见主条目）：

| 条目 | Lecture | 学校／版本 |
|---|---|---|
| [SZ26-03](#sz26-03) | Retrieval-Augmented Generation (RAG) | Stanford CS329Z（2026 秋） |
| [SZ26-04](#sz26-04) | Tool Use & Function Calling | Stanford CS329Z（2026 秋） |
| [ST25-03](#st25-03) | Agentic AI | Stanford CS329T（2025 秋） |
| [ST25-06](#st25-06) | MCP, effective tool descriptions, evals | Stanford CS329T（2025 秋） |
| [C76626-06](#c76626-06) | Retrieval 1: Storing and retrieving knowledge | CMU 11-766（2026 春） |
| [C76626-07](#c76626-07) | Retrieval 2: Retrieval augmented generation, deep research | CMU 11-766（2026 春） |
| [C76626-08](#c76626-08) | Retrieval 3: Retrieval augmented generation (2) and deep research | CMU 11-766（2026 春） |
| [C71125-10](#c71125-10) | Modeling I: Retrieval and RAG | CMU 11-711（2025 秋） |
| [I59825-11](#i59825-11) | Retrieval-Augmented Generation | UIUC CS598（2025 春） |
| [U23426-06](#u23426-06) | Topic 2: Retrieval and Context Engineering — Part 2 | UC San Diego CSE/DSC234（2026 春） |
| [U23426-07](#u23426-07) | Topic 2: Retrieval and Context Engineering — Part 3 | UC San Diego CSE/DSC234（2026 春） |

<a id="topic-optimization"></a>
## Optimization｜优化

提示优化、GEPA、SFT、RLHF/RLVR、蒸馏、计算与成本优化。

<a id="sz26-09"></a>
### SZ26-09 · Optimization

**学校／课程**：Stanford · CS329Z · Engineering AI Agents；**学期**：2026 秋；**课堂日期**：Wed Oct 21。

**原始目录**：[课程 syllabus / schedule](https://cs329z.stanford.edu/)。**主题**：[Optimization](#topic-optimization)。

- [PDF · Slides](https://web.stanford.edu/class/cs329z/slides/lecture09.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx26-03"></a>
### SX26-03 · Learning from Human Preferences

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2026 秋；**课堂日期**：Sep 30, Wednesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/index.html)。**主题**：[Optimization](#topic-optimization)、[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/2627/Lecture3_human_preferences.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-03"></a>
### SX25-03 · Learning from Human Preferences

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Sep 30, Tuesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[Optimization](#topic-optimization)、[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture3_human_preferences.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-04"></a>
### SX25-04 · Collective Opinions and Pluralistic Alignment

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Oct 2, Thursday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[Optimization](#topic-optimization)、[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture4_preferences.pdf) — 已验证 · HTTP 206 / PDF。

<a id="st25-08"></a>
### ST25-08 · Data curation and RL to optimize agents

**学校／课程**：Stanford · CS329T · Trustworthy Machine Learning / Agentic AI；**学期**：2025 秋；**课堂日期**：Thu Oct 23。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329t/syllabus.html)。**主题**：[Optimization](#topic-optimization)、[Agent Architecture / Orchestration](#topic-architecture)、[补充主题](#topic-supplement)。

- [PDF · Slides](https://web.stanford.edu/class/cs329t/slides/Lecture%208%20-%20%5B10_23_2025%5D%20Reinforcement%20Learning%20%20for%20Agents.pdf) — 已验证 · HTTP 206 / PDF。

<a id="st25-09"></a>
### ST25-09 · GEPA

**学校／课程**：Stanford · CS329T · Trustworthy Machine Learning / Agentic AI；**学期**：2025 秋；**课堂日期**：Tue Oct 28。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329t/syllabus.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · Slides](https://web.stanford.edu/class/cs329t/slides/Lecture%209%20-%2020251028%20GEPA_Talk.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33626-09"></a>
### S33626-09 · L9 Scaling laws [Tatsu]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Mon April 27。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[Optimization](#topic-optimization)。

- [PDF · lecture_09.pdf](https://raw.githubusercontent.com/stanford-cs336/lectures/main/lecture_09.pdf)；[官方仓库预览](https://github.com/stanford-cs336/lectures/blob/main/lecture_09.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33626-11"></a>
### S33626-11 · L11 Scaling laws [Tatsu]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Mon May 4。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[Optimization](#topic-optimization)。

- [PDF · lecture_11.pdf](https://raw.githubusercontent.com/stanford-cs336/lectures/main/lecture_11.pdf)；[官方仓库预览](https://github.com/stanford-cs336/lectures/blob/main/lecture_11.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33626-15"></a>
### S33626-15 · L15 Mid/post-training (SFT/RLHF) [Tatsu]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Mon May 18。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[Optimization](#topic-optimization)。

- [PDF · lecture_15.pdf](https://raw.githubusercontent.com/stanford-cs336/lectures/main/lecture_15.pdf)；[官方仓库预览](https://github.com/stanford-cs336/lectures/blob/main/lecture_15.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33626-16"></a>
### S33626-16 · L16 Post-training - RLVR [Tatsu]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Wed May 20。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[Optimization](#topic-optimization)。

- [PDF · lecture_16.pdf](https://raw.githubusercontent.com/stanford-cs336/lectures/main/lecture_16.pdf)；[官方仓库预览](https://github.com/stanford-cs336/lectures/blob/main/lecture_16.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33626-17"></a>
### S33626-17 · L17 Alignment - multimodality [Percy]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Wed May 27。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[Optimization](#topic-optimization)、[补充主题](#topic-supplement)。

- [交互式 Python Notes（HTML） · lecture_17.py](https://cs336.stanford.edu/lectures/?trace=lecture_17) — 页面可达；动态 Notes 内容待验证。

<a id="s33625-09"></a>
### S33625-09 · L9 Scaling laws (Tatsu)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Tues April 29。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · lecture 9.pdf](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/fb79eb018fa047bf99c4c785dcbbd62fff361e54/nonexecutable/2025%20Lecture%209%20-%20Scaling%20laws%20basics.pdf)；[官方仓库预览](https://github.com/stanford-cs336/spring2025-lectures/blob/fb79eb018fa047bf99c4c785dcbbd62fff361e54/nonexecutable/2025%20Lecture%209%20-%20Scaling%20laws%20basics.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33625-11"></a>
### S33625-11 · L11 Scaling laws (Tatsu)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Tues May 6。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · lecture 11.pdf](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/00191bba00d6d64621dc46ccaed9122681413a24/nonexecutable/2025%20Lecture%2011%20-%20Scaling%20details.pdf)；[官方仓库预览](https://github.com/stanford-cs336/spring2025-lectures/blob/00191bba00d6d64621dc46ccaed9122681413a24/nonexecutable/2025%20Lecture%2011%20-%20Scaling%20details.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33625-15"></a>
### S33625-15 · L15 Alignment - SFT/RLHF (Tatsu)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Tues May 20。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · lecture 15.pdf](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/61eddac004df975466cff0329b615f2d24230069/nonexecutable/2025%20Lecture%2015%20-%20RLHF%20Alignment.pdf)；[官方仓库预览](https://github.com/stanford-cs336/spring2025-lectures/blob/61eddac004df975466cff0329b615f2d24230069/nonexecutable/2025%20Lecture%2015%20-%20RLHF%20Alignment.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33625-16"></a>
### S33625-16 · L16 Alignment - RL (Tatsu)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Thurs May 22。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · lecture 16.pdf](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/e94e33f433985e57036b25215dff2a4292e67a4f/nonexecutable/2025%20Lecture%2016%20-%20RLVR.pdf)；[官方仓库预览](https://github.com/stanford-cs336/spring2025-lectures/blob/e94e33f433985e57036b25215dff2a4292e67a4f/nonexecutable/2025%20Lecture%2016%20-%20RLVR.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33625-17"></a>
### S33625-17 · L17 Alignment - RL (Percy)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Tues May 27。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[Optimization](#topic-optimization)。

- [交互式 Python Notes（HTML） · lecture_17.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_17.json) — 页面可达；动态 Notes 内容待验证。

<a id="c76626-04"></a>
### C76626-04 · Deciding when to finetune and finetuning efficiently

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：01/22/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[Optimization](#topic-optimization)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-01-22-finetuning.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-08"></a>
### C71125-08 · Learning III: Fine-tuning and Distillation

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 8 09/18/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[Optimization](#topic-optimization)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-08-finetuning.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-15"></a>
### C71125-15 · Reinforcement Learning I: Fundamentals

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 17 10/21/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[Optimization](#topic-optimization)、[LLM Foundations](#topic-foundations)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-15-rl.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-16"></a>
### C71125-16 · Reinforcement Learning II: Applications

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 18 10/23/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[Optimization](#topic-optimization)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-15-rl-llms.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-08"></a>
### C76826-08 · Training 1: Supervised Fine-Tuning (SFT)

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Thu, Sep 17。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Optimization](#topic-optimization)。

- [PDF · Lecture 8 slides](https://www.cmu-agents.com/slides/lecture-08-sft.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-09"></a>
### C76826-09 · Training 2: Reinforcement Learning Basics

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Tue, Sep 22。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Optimization](#topic-optimization)。

- [PDF · Lecture 9 slides](https://www.cmu-agents.com/slides/lecture-09-rl-basics.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-11"></a>
### C76826-11 · Training 3: Advanced RL Algorithms

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Tue, Sep 29。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Optimization](#topic-optimization)。

- [PDF · Lecture 11 slides](https://www.cmu-agents.com/slides/lecture-11-rl-advanced.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-12"></a>
### C76826-12 · Training 4: RL Systems

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Thu, Oct 1。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Optimization](#topic-optimization)。

- [PDF · Lecture 12 slides](https://www.cmu-agents.com/slides/lecture-12-rl-systems.pdf) — 已验证 · HTTP 206 / PDF。

<a id="b25-04"></a>
### B25-04 · Post-Training Verifiable Agents

**学校／课程**：UC Berkeley · CS194/294-196 · Agentic AI；**学期**：2025 秋；**课堂日期**：Sep 29。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/agentic-ai/f25)。**主题**：[Optimization](#topic-optimization)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Slides](https://rdi.berkeley.edu/agentic-ai/slides/AgenticAI_Jiantao%20Jiao.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/watch?v=3l0Zxus34es&list=PLS01nW3RtgoqGkm4UeqNeZLccW-OGc1fJ&index=3) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="b25-06"></a>
### B25-06 · Some Challenges and Lessons from Training Agentic Models

**学校／课程**：UC Berkeley · CS194/294-196 · Agentic AI；**学期**：2025 秋；**课堂日期**：Oct 13。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/agentic-ai/f25)。**主题**：[Optimization](#topic-optimization)、[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://rdi.berkeley.edu/agentic-ai/slides/weizhu.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/watch?v=xNxrBHZPDvM) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="ua26-07"></a>
### UA26-07 · Deep Reinforcement Learning, Pre-LLMs

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Tue, Jan 27, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/deep_rl_pre_llms.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua26-08"></a>
### UA26-08 · Reinforcement Learning and Search Combined

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Thu, Jan 29, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/rl_search_combined.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua26-10"></a>
### UA26-10 · RL for Language Agents Pt 1 (Online RL for NLP, RLHF)

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Thu, Feb 12, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/rl_for_language_pt1.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua26-11"></a>
### UA26-11 · RL for Language Agents Pt 2 (Rewards and Closed Form Methods)

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Tue, Feb 17, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/rl_for_language_pt2.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua26-12"></a>
### UA26-12 · Prompt Optimization

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Thu, Feb 19, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/prompt_optimization.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-07"></a>
### UA25-07 · Deep Reinforcement Learning, Pre-LLMs

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Tue, Jan 28, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/deep_rl_pre_llms.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-08"></a>
### UA25-08 · Reinforcement Learning and Search Combined

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Thu, Feb 6, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/rl_search_combined.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-10"></a>
### UA25-10 · RL for Language Agents Pt 1 (Online RL for NLP, RLHF)

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Thu, Feb 13, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/rl_language_agents_pt1.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-11"></a>
### UA25-11 · RL for Language Agents Pt 2 (Rewards and Closed Form Methods)

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Tue, Feb 18, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/rl_language_agents_pt2.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-12"></a>
### UA25-12 · Prompt Optimization

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Thu, Feb 20, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/prompting.pdf) — 已验证 · HTTP 206 / PDF。

<a id="h26-09"></a>
### H26-09 · Advanced agent design I: Cost and performance

**学校／课程**：Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations；**学期**：2026 秋；**课堂日期**：2026-10-07。

**原始目录**：[课程 syllabus / schedule](https://cs2680.seas.harvard.edu/)。**主题**：[Optimization](#topic-optimization)、[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · [slide]](https://cs2680.seas.harvard.edu/slides/8_agent_design_5.pdf) — 已验证 · HTTP 200 / PDF。

<a id="h26-22"></a>
### H26-22 · Cost-effective agents

**学校／课程**：Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations；**学期**：2026 秋；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://cs2680.seas.harvard.edu/)。**主题**：[Optimization](#topic-optimization)、[Agent Architecture / Orchestration](#topic-architecture)。

- [HTML Notes · Cost-effective agents](https://cs2680.seas.harvard.edu/notes/cost-effective-agents.html) — 已验证 · HTTP 200 / HTML。

备注：教师专题 Notes，可与对应 lecture 配套阅读。

<a id="u23426-09"></a>
### U23426-09 · Guest Lecture: GEPA — Lakshya Agrawal

**学校／课程**：UC San Diego · CSE/DSC234 · Data-Centric AI and AI Engineering（Arun Kumar）；**学期**：2026 春；**课堂日期**：2026-05-12。

**原始目录**：[课程 syllabus / schedule](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html)。**主题**：[Optimization](#topic-optimization)。

- [PDF · PDF](https://cseweb.ucsd.edu/classes/sp26/cse234-a/downloads/GuestLecture-GEPA-Lakshya.pdf) — 待验证 · 连接超时。

备注：官方目录按主题课件包组织，包不等于一次课堂。目录列出 PDF/PPTX；本次源站超时，只收录搜索索引实际返回的 PDF 地址，其余直链及 PPTX 待验证，未按文件名推测。

**跨主题索引**（完整链接与核验状态见主条目）：

| 条目 | Lecture | 学校／版本 |
|---|---|---|
| [SZ26-02](#sz26-02) | LLMs for Builders | Stanford CS329Z（2026 秋） |
| [SZ26-05](#sz26-05) | Frameworks & Orchestration | Stanford CS329Z（2026 秋） |
| [SG25-12](#sg25-12) | RAG and Fine Tuning | Stanford CS224G（2025 冬） |
| [BA25-01](#ba25-01) | Inference-Time Techniques for LLM Reasoning | UC Berkeley CS194/294-280（2025 春） |
| [BA25-08](#ba25-08) | AlphaProof: when reinforcement learning meets formal mathematics | UC Berkeley CS194/294-280（2025 春） |
| [UA26-14](#ua26-14) | Agent Reasoning and Inference Time Methods | UC San Diego CSE291A（2026 冬） |
| [UA25-14](#ua25-14) | Agent Reasoning and Inference Time Methods | UC San Diego CSE291（2025 冬） |
| [U23425-07](#u23425-07) | 7 Triton, graph optimization and compilation | UC San Diego CSE234（2025 冬） |
| [U23425-17](#u23425-17) | 17 LLM - 2: Scaling law, MoE | UC San Diego CSE234（2025 冬） |

<a id="topic-coding"></a>
## Coding Agents｜编程智能体

代码生成、软件工程 Agent、Claude Code、OpenHands、安全漏洞发现。

<a id="sg26-10"></a>
### SG26-10 · Code Generation with LLMs

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：TueFeb 10。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[Coding Agents](#topic-coding)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%2011%20-%20Code%20Generation%20with%20LLMs.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-05"></a>
### SG25-05 · LLMs for Code Generation

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：1/23。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[Coding Agents](#topic-coding)。

- [PDF · LLMs for Code Generation](https://web.stanford.edu/class/cs224g/2025/lectures/Stanford_Code_Generation_Lecture.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-17"></a>
### C76626-17 · Code-writing assistants (guest lecture from Zora Wang)

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：03/17/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[Coding Agents](#topic-coding)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-03-17-coding-agents.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-06"></a>
### C76826-06 · Domains 1: Coding Agents

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Thu, Sep 10。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Coding Agents](#topic-coding)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Lecture 6 slides](https://www.cmu-agents.com/slides/lecture-06-coding-agents.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-14"></a>
### C76826-14 · Frameworks 1: OpenHands

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Thu, Oct 8。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Coding Agents](#topic-coding)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Lecture 14 slides](https://www.cmu-agents.com/slides/lecture-14-openhands.pdf) — 已验证 · HTTP 206 / PDF。

<a id="b24-06"></a>
### B24-06 · Agents for Software Development

**学校／课程**：UC Berkeley · CS194/294-196 · LLM Agents；**学期**：2024 秋；**课堂日期**：Oct 14。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/llm-agents/f24)。**主题**：[Coding Agents](#topic-coding)。

- [PDF · Slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/neubig24softwareagents.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/f9L9Fkq-8K4) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="ba25-05"></a>
### BA25-05 · Coding Agents and AI for Vulnerability Detection

**学校／课程**：UC Berkeley · CS194/294-280 · Advanced LLM Agents；**学期**：2025 春；**课堂日期**：Mar 3rd。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/adv-llm-agents/sp25)。**主题**：[Coding Agents](#topic-coding)。

- [PDF · Slides](https://rdi.berkeley.edu/adv-llm-agents/slides/Code%20Agents%20and%20AI%20for%20Vulnerability%20Detection.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/JCk6qJtaCSU) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="h26-02"></a>
### H26-02 · Agents use I: How Claude Code Works

**学校／课程**：Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations；**学期**：2026 秋；**课堂日期**：2026-09-09。

**原始目录**：[课程 syllabus / schedule](https://cs2680.seas.harvard.edu/)。**主题**：[Coding Agents](#topic-coding)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · [slide]](https://cs2680.seas.harvard.edu/slides/2_agent_use_1.pdf) — 已验证 · HTTP 200 / PDF。

**跨主题索引**（完整链接与核验状态见主条目）：

| 条目 | Lecture | 学校／版本 |
|---|---|---|
| [SZ26-05](#sz26-05) | Frameworks & Orchestration | Stanford CS329Z（2026 秋） |
| [H26-03](#h26-03) | Agents use II: 100x Engineer with Multi-agents | Harvard CS2680（2026 秋） |

<a id="topic-production"></a>
## Production / Reliability / Security / Infra｜生产、可靠性、安全与基础设施

部署、监控、权限与安全、GPU、分布式训练、服务调度、KV cache、量化等。

<a id="sx25-14"></a>
### SX25-14 · Guest Lecture: Niloofar Mireshghallah

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Nov 13, Thursday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture13_Niloofar.pdf) — 已验证 · HTTP 206 / PDF。

备注：目录只给出讲者姓名；按该行隐私相关阅读归入安全主题，具体讲题待核对。

<a id="st25-10"></a>
### ST25-10 · Security for agents: adversarial attacks and guardrails

**学校／课程**：Stanford · CS329T · Trustworthy Machine Learning / Agentic AI；**学期**：2025 秋；**课堂日期**：Thu Oct 30。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329t/syllabus.html)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://web.stanford.edu/class/cs329t/slides/lecture%2010%20-%2020251030%20-%20security%20for%20agents%20-%20andy%20zou.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg26-14"></a>
### SG26-14 · AI Safety, Ethics & Guardrails

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：ThuMar 5。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%2018%20-%20Ethics%20and%20Guardrails.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-06"></a>
### SG25-06 · Building AI Agents for IT Ops

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：2/4。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Building AI Agents for IT Ops](https://web.stanford.edu/class/cs224g/2025/lectures/AI_Agents_for_IT_Ops.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33626-02"></a>
### S33626-02 · L2 PyTorch (einops), resource accounting (FLOPs, memory, arithmetic intensity) [Percy]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Wed April 1。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[Memory / Skills](#topic-memory)。

- [交互式 Python Notes（HTML） · lecture_02.py](https://cs336.stanford.edu/lectures/?trace=lecture_02) — 页面可达；动态 Notes 内容待验证。
- [交互式 Python Notes（HTML） · recording version](https://cs336.stanford.edu/lectures/?trace=lecture_02_recording) — 页面可达；动态 Notes 内容待验证。

<a id="s33626-05"></a>
### S33626-05 · L5 GPUs, TPUs [Tatsu]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Mon April 13。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · lecture 5.pdf](https://raw.githubusercontent.com/stanford-cs336/lectures/main/lecture_05.pdf)；[官方仓库预览](https://github.com/stanford-cs336/lectures/blob/main/lecture_05.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33626-06"></a>
### S33626-06 · L6 Kernels, Triton [Percy]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Wed April 15。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [交互式 Python Notes（HTML） · lecture_06.py](https://cs336.stanford.edu/lectures/?trace=lecture_06) — 页面可达；动态 Notes 内容待验证。

<a id="s33626-07"></a>
### S33626-07 · L7 Parallelism [Percy]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Mon April 20。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [交互式 Python Notes（HTML） · lecture_07.py](https://cs336.stanford.edu/lectures/?trace=lecture_07) — 页面可达；动态 Notes 内容待验证。

<a id="s33626-08"></a>
### S33626-08 · L8 Parallelism [Tatsu]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Wed April 22。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · lecture_08.pdf](https://raw.githubusercontent.com/stanford-cs336/lectures/main/lecture_08.pdf)；[官方仓库预览](https://github.com/stanford-cs336/lectures/blob/main/lecture_08.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33626-10"></a>
### S33626-10 · L10 Inference [Percy]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Wed April 29。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [交互式 Python Notes（HTML） · lecture_10.py](https://cs336.stanford.edu/lectures/?trace=lecture_10) — 页面可达；动态 Notes 内容待验证。

<a id="s33625-02"></a>
### S33625-02 · L2 PyTorch, resource accounting (Percy)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Thurs April 3。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [交互式 Python Notes（HTML） · lecture_02.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_02.json) — 页面可达；动态 Notes 内容待验证。

<a id="s33625-05"></a>
### S33625-05 · L5 GPUs (Tatsu)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Tues April 15。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · lecture 5.pdf](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/main/nonexecutable/2025%20Lecture%205%20-%20GPUs.pdf)；[官方仓库预览](https://github.com/stanford-cs336/spring2025-lectures/blob/main/nonexecutable/2025%20Lecture%205%20-%20GPUs.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33625-06"></a>
### S33625-06 · L6 Kernels, Triton (Tatsu)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Thurs April 17。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [交互式 Python Notes（HTML） · lecture_06.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_06.json) — 页面可达；动态 Notes 内容待验证。

<a id="s33625-07"></a>
### S33625-07 · L7 Parallelism (Tatsu)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Tues April 22。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · lecture 7.pdf](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/4eff81bee0a853217209e163936b264f03572b66/nonexecutable/2025%20Lecture%207%20-%20Parallelism%20basics.pdf)；[官方仓库预览](https://github.com/stanford-cs336/spring2025-lectures/blob/4eff81bee0a853217209e163936b264f03572b66/nonexecutable/2025%20Lecture%207%20-%20Parallelism%20basics.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33625-08"></a>
### S33625-08 · L8 Parallelism (Percy)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Thurs April 24。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [交互式 Python Notes（HTML） · lecture_08.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_08.json) — 页面可达；动态 Notes 内容待验证。

<a id="s33625-10"></a>
### S33625-10 · L10 Inference (Percy)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Thurs May 1。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [交互式 Python Notes（HTML） · lecture_10.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_10.json) — 页面可达；动态 Notes 内容待验证。

<a id="c76626-15"></a>
### C76626-15 · Harms caused by LLM applications

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：03/10/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-03-10-risks.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-16"></a>
### C76626-16 · Attacking LLMs and LLM applications

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：03/12/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-03-12-misuse.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-25"></a>
### C76626-25 · Deployment

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：04/16/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-03-16-deployment.pdf) — 已验证 · HTTP 206 / PDF。

备注：原目录文件名日期与上课日期不同；保留目录原始 URL，不擅自改名。

<a id="c71125-09"></a>
### C71125-09 · Inference II: Decoding Algorithms

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 9 09/23/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-09-decoding.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-18"></a>
### C71125-18 · Scaling: Parallelism and Distributed Training

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 22 11/06/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-18-scaling-parallelism.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-19"></a>
### C71125-19 · Efficiency: Quantization

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 23 11/11/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-19-quantization.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-22"></a>
### C71125-22 · Advanced Inference Strategies

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 26 11/20/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-22-inference.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-13"></a>
### C76826-13 · Safety 1: Agent Safety

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Tue, Oct 6。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Lecture 13 slides](https://www.cmu-agents.com/slides/lecture-13-agent-safety.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76826-15"></a>
### C76826-15 · Frameworks 2: Orchestration and Monitoring

**学校／课程**：CMU · 11-768 · AI Agents；**学期**：2026 秋；**课堂日期**：Tue, Oct 20。

**原始目录**：[课程 syllabus / schedule](https://www.cmu-agents.com/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Lecture 15 slides](https://www.cmu-agents.com/slides/lecture-15-orchestration-and-monitoring.pdf) — 已验证 · HTTP 206 / PDF。

<a id="b24-12"></a>
### B24-12 · Towards Building Safe & Trustworthy AI Agents and A Path for Science‑ and Evidence‑based AI Policy

**学校／课程**：UC Berkeley · CS194/294-196 · LLM Agents；**学期**：2024 秋；**课堂日期**：Dec 2。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/llm-agents/f24)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[补充主题](#topic-supplement)。

- [PDF · Slides](https://rdi.berkeley.edu/llm-agents/assets/dawn-agent-safety.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/QAgR4uQ15rc) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="ba25-12"></a>
### BA25-12 · Towards building safe and secure agentic AI

**学校／课程**：UC Berkeley · CS194/294-280 · Advanced LLM Agents；**学期**：2025 春；**课堂日期**：Apr 28th。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/adv-llm-agents/sp25)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Slides](https://rdi.berkeley.edu/adv-llm-agents/slides/dawn-agentic-ai.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/ti6yPE2VPZc) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="b25-03"></a>
### B25-03 · Evolution of system designs from an AI engineer perspective

**学校／课程**：UC Berkeley · CS194/294-196 · Agentic AI；**学期**：2025 秋；**课堂日期**：Sep 22。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/agentic-ai/f25)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Slides](https://rdi.berkeley.edu/agentic-ai/slides/Yangqing.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/watch?v=xqRAS6rAouo&list=PLS01nW3RtgoqGkm4UeqNeZLccW-OGc1fJ&index=2) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="b25-10"></a>
### B25-10 · Practical Lessons from Deploying Real-World AI Agents

**学校／课程**：UC Berkeley · CS194/294-196 · Agentic AI；**学期**：2025 秋；**课堂日期**：Nov 10。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/agentic-ai/f25)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Slides](https://rdi.berkeley.edu/agentic-ai/slides/Practical_Lessons_AI_Agents.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/watch?v=sfJM4LaiYsM) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="i59825-18"></a>
### I59825-18 · Safety

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：April 15。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PPTX · Zirui Cheng, Peixuan Han, Xiaocheng Yang (Group 3)](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/16_Safety.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/16_Safety.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="ua26-16"></a>
### UA26-16 · Agent Safety, Security, and Legality

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Thu, Mar 5, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/agent_safety.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-16"></a>
### UA25-16 · Societal Impacts and Agent Safety

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Thu, Mar 6, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[补充主题](#topic-supplement)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/agent_safety.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-01"></a>
### U23425-01 · 1 Introduction

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/jan7.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-02"></a>
### U23425-02 · 2 Basics: Modern DL, computational graph, frameworks

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[Agent Architecture / Orchestration](#topic-architecture)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/jan9.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/jan9_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-03"></a>
### U23425-03 · 3 Basics: autodiff, ML system architecture overview

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/jan14.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/jan14_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-04"></a>
### U23425-04 · 4 Tensor format, matmul deep dive, accelerators

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/jan16.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/jan16_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-05"></a>
### U23425-05 · 5 GPUs and CUDA

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/jan21.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/jan21_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-06"></a>
### U23425-06 · 6 GPU matmul, operator compilation

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/jan23.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/jan23_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-07"></a>
### U23425-07 · 7 Triton, graph optimization and compilation

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[Optimization](#topic-optimization)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/jan28.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/jan28_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-08"></a>
### U23425-08 · 8 Memory

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/jan30.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/jan30_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-09"></a>
### U23425-09 · 9 Quantization

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/feb4.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/feb4_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-10"></a>
### U23425-10 · 10 Guest Lecture by Tianqi Chen

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/feb6.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/feb6_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-11"></a>
### U23425-11 · 11 Parallelization

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/feb11.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/feb11_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-12"></a>
### U23425-12 · 12 Parallelization - 2, collective communication

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/feb13.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/feb13_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-13"></a>
### U23425-13 · 13 Parallelization - 3, data, inter- and intra-op parallelism

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[补充主题](#topic-supplement)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/feb18.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/feb_18_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-14"></a>
### U23425-14 · 14 Guest Lecture by Hector Liu

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/feb20.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/feb20_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-15"></a>
### U23425-15 · 15 Parallelization - 4

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/feb25.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/feb25_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-16"></a>
### U23425-16 · 16 LLM - 1: transformers, attention

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[LLM Foundations](#topic-foundations)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/feb27.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/feb27_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-17"></a>
### U23425-17 · 17 LLM - 2: Scaling law, MoE

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[Optimization](#topic-optimization)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/mar4.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/mar_4_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-18"></a>
### U23425-18 · 18 Guest Lecture by Hongyang Zhang

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/mar6.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Note](https://haoailab.com/cse234-w25/assets/scribe_notes/mar6_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-19"></a>
### U23425-19 · 19 LLM - 3: Continuous batching, paged attention, Disaggreged prefill and decoding

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[LLM Foundations](#topic-foundations)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/mar11.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Notes](https://haoailab.com/cse234-w25/assets/scribe_notes/march11_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23425-20"></a>
### U23425-20 · 20 LLM - 4: flash attention, deepseek-v3 review, ending words

**学校／课程**：UC San Diego · CSE234 · Data Systems for Machine Learning（Hao Zhang）；**学期**：2025 冬；**课堂日期**：目录未单独写入本条；按课次定位。

**原始目录**：[课程 syllabus / schedule](https://haoailab.com/cse234-w25/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[LLM Foundations](#topic-foundations)。

- [PDF · Slides](https://haoailab.com/cse234-w25/assets/slides/mar13.pdf) — 已验证 · HTTP 206 / PDF。
- [学生 Scribe Notes（PDF） · Scribe Notes](https://haoailab.com/cse234-w25/assets/scribe_notes/mar13_scribe.pdf) — 已验证 · HTTP 206 / PDF。

<a id="h26-11"></a>
### H26-11 · Efficient LLM serving basics I: intro to LLMs

**学校／课程**：Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations；**学期**：2026 秋；**课堂日期**：2026-10-19。

**原始目录**：[课程 syllabus / schedule](https://cs2680.seas.harvard.edu/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)、[LLM Foundations](#topic-foundations)。

- [PDF · [slide]](https://cs2680.seas.harvard.edu/slides/9_llm_serving_basics_1.pdf) — 已验证 · HTTP 200 / PDF。

<a id="h26-12"></a>
### H26-12 · Efficient LLM serving basics II: intro to GPUs

**学校／课程**：Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations；**学期**：2026 秋；**课堂日期**：2026-10-21。

**原始目录**：[课程 syllabus / schedule](https://cs2680.seas.harvard.edu/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · [slide]](https://cs2680.seas.harvard.edu/slides/10_llm_serving_basics_2a.pdf) — 已验证 · HTTP 200 / PDF。

<a id="us25-27"></a>
### US25-27 · AgentOps and Agent Security

**学校／课程**：UC San Diego · CSE291A · Systems for LLMs and AI Agents（Yiying Zhang）；**学期**：2025 秋；**课堂日期**：11/26。

**原始目录**：[课程 syllabus / schedule](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/)。**主题**：[Production / Reliability / Security / Infra](#topic-production)。

- [PDF · PDF](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/ops-security.pdf) — 待验证 · 连接超时。

备注：目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。

**跨主题索引**（完整链接与核验状态见主条目）：

| 条目 | Lecture | 学校／版本 |
|---|---|---|
| [SZ26-05](#sz26-05) | Frameworks & Orchestration | Stanford CS329Z（2026 秋） |
| [SZ26-08](#sz26-08) | Multi-Agent Systems | Stanford CS329Z（2026 秋） |
| [C71125-07](#c71125-07) | Learning II/Inference I: In-Context Learning | CMU 11-711（2025 秋） |
| [B25-06](#b25-06) | Some Challenges and Lessons from Training Agentic Models | UC Berkeley CS194/294-196（2025 秋） |
| [H26-06](#h26-06) | Agents design III: agent memory and reliability | Harvard CS2680（2026 秋） |
| [H26-09](#h26-09) | Advanced agent design I: Cost and performance | Harvard CS2680（2026 秋） |
| [U23426-10](#u23426-10) | Topic 3: Agent Engineering | UC San Diego CSE/DSC234（2026 春） |

<a id="topic-supplement"></a>
## 补充主题｜数据、对齐、人机交互、多模态与应用

数据策展、社会与伦理、产品创业、语音、多模态、机器人、科学发现，以及研究方法。

<a id="sx26-01"></a>
### SX26-01 · Introduction to Human Centered LLMs

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2026 秋；**课堂日期**：Sep 23, Wednesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/2627/Lecture1_intro.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx26-04"></a>
### SX26-04 · ✨ Guest Lecture: Will Held (Open Athena) and Rafal Wojdyla (Open Athena): Data, Data, and Data

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2026 秋；**课堂日期**：Oct 5, Monday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/2627/Lecture4_data_data.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx26-05"></a>
### SX26-05 · Human-AI Interaction

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2026 秋；**课堂日期**：Oct 7, Wednesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/2627/Lecture5_enable_HAI.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx26-07"></a>
### SX26-07 · Human-Agent Collaboration

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2026 秋；**课堂日期**：Oct 14, Wednesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/2627/Lecture7_human_agent_collaboration.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx26-09"></a>
### SX26-09 · New Frontiers in Generative Interaction

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2026 秋；**课堂日期**：Oct 21, Wednesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/2627/Lecture9_design_thinking.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-01"></a>
### SX25-01 · Introduction to Human Centered NLP

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Sep 23, Tuesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture1_intro.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-05"></a>
### SX25-05 · Guest Lecture: Will Held: Data, Data, and Data

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Oct 7, Tuesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture5_datadatadata.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-07"></a>
### SX25-07 · Human-AI Interaction

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Oct 14, Tuesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture7_enable_HAI.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-09"></a>
### SX25-09 · Design Thinking + New User Interface

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Oct 21, Tuesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture9_design_thinking.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-11"></a>
### SX25-11 · New Frontiers in Generative Interaction

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Oct 30, Thursday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture10_interfaces.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-12"></a>
### SX25-12 · Culture and Values in LLMs

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Nov 6, Thursday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture11_culture.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-13"></a>
### SX25-13 · Anthropomorphism and  Guest Lecture: Alice Oh

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Nov 11, Tuesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture12_anthropomorphism.pdf) — 已验证 · HTTP 206 / PDF。
- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture12_B_Codeswitching%20LLMs.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-15"></a>
### SX25-15 · The Rise of AI Companions and  Guest Lecture: Myra Cheng

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Nov 18, Tuesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture14_ai_companions.pdf) — 已验证 · HTTP 206 / PDF。
- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture14_B_Myra.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-16"></a>
### SX25-16 · LLMs and the Future of Work

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Nov 20, Thursday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture15_future_of_work.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sx25-17"></a>
### SX25-17 · Open Questions in Human-Centered LLMs

**学校／课程**：Stanford · CS329X · Human-Centered LLMs；**学期**：2025 秋；**课堂日期**：Dec 2, Tuesday。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs329x/2526_index.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://web.stanford.edu/class/cs329x/slides/Lecture16_summary.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg26-02"></a>
### SG26-02 · 224G Project Ideas & Modern LLM Stack

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：ThuJan 8。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%202%20-%20Project%20Pitches.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg26-04"></a>
### SG26-04 · AI Entrepreneurship & Building with GenAI

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：ThuJan 15。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%204%20-%20The%20New%20Source%20Code.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg26-08"></a>
### SG26-08 · Building AI-Native Companies

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：TueFeb 3。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%209%20-%20Building%20AI-Native%20Companies.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg26-09"></a>
### SG26-09 · Building Good LLM Products with the Theory of Constraints

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：ThuFeb 5。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%2010%20-%20Building%20Good%20LLM%20Products%20with%20the%20Theory%20of%20Constraints.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg26-13"></a>
### SG26-13 · Workshop: Building & Scaling Realtime Voice AI Apps

**学校／课程**：Stanford · CS224G · Building and Scaling LLM Applications；**学期**：2026 冬；**课堂日期**：TueMar 3。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/schedule.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · 📄 Lecture Notes](https://web.stanford.edu/class/cs224g/lectures/CS%20224G%202026%20Lecture%2017%20-%20Workshop%20Building%20and%20Scaling%20Realtime%20Voice%20AI%20Apps.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-01"></a>
### SG25-01 · Introduction and Project Logistics

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：1/7。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · Introduction and Project Logistics](https://web.stanford.edu/class/cs224g/2025/lectures/CS_224G_Introduction.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-03"></a>
### SG25-03 · AI Entrepreneurship

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：1/16。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · AI Entrepreneurship](https://web.stanford.edu/class/cs224g/2025/lectures/CS_224G_AI_Entrepreneurship.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-11"></a>
### SG25-11 · Voice AI

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：2/25。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · Voice AI](https://web.stanford.edu/class/cs224g/2025/lectures/Voice_AI_CS224.pdf) — 已验证 · HTTP 206 / PDF。

<a id="sg25-13"></a>
### SG25-13 · Lessons in Building Consumer AI; Giving a Great Pitch

**学校／课程**：Stanford · CS224G · Apps with LLMs Inside；**学期**：2025 冬；**课堂日期**：3/6。

**原始目录**：[课程 syllabus / schedule](https://web.stanford.edu/class/cs224g/2025/schedule.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · Giving a Great Pitch](https://web.stanford.edu/class/cs224g/2025/lectures/Giving_a_Great_Pitch.pdf) — 已验证 · HTTP 206 / PDF。

<a id="s33626-13"></a>
### S33626-13 · L13 Data (sources, datasets) [Percy]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Mon May 11。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[补充主题](#topic-supplement)。

- [交互式 Python Notes（HTML） · lecture_13.py](https://cs336.stanford.edu/lectures/?trace=lecture_13) — 页面可达；动态 Notes 内容待验证。

<a id="s33626-14"></a>
### S33626-14 · L14 Data (filtering, deduplication, mixing, synthetic data) [Percy]

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2026 春；**课堂日期**：Wed May 13。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/)。**主题**：[补充主题](#topic-supplement)。

- [交互式 Python Notes（HTML） · lecture_14.py](https://cs336.stanford.edu/lectures/?trace=lecture_14) — 页面可达；动态 Notes 内容待验证。

<a id="s33625-13"></a>
### S33625-13 · L13 Data (Percy)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Tues May 13。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[补充主题](#topic-supplement)。

- [交互式 Python Notes（HTML） · lecture_13.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_13.json) — 页面可达；动态 Notes 内容待验证。

<a id="s33625-14"></a>
### S33625-14 · L14 Data (Percy)

**学校／课程**：Stanford · CS336 · Language Modeling from Scratch；**学期**：2025 春；**课堂日期**：Thurs May 15。

**原始目录**：[课程 syllabus / schedule](https://cs336.stanford.edu/spring2025/index.html)。**主题**：[补充主题](#topic-supplement)。

- [交互式 Python Notes（HTML） · lecture_14.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_14.json) — 页面可达；动态 Notes 内容待验证。

<a id="c76626-10"></a>
### C76626-10 · Task-Oriented Dialogue

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：02/12/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-02-12-task.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-12"></a>
### C76626-12 · Writing and ideation assistants and AI creative writing

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：02/19/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-02-19-creativity-v2.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-18"></a>
### C76626-18 · [tentative] Image generation and conversing about images

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：03/19/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-03-19-vision.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-19"></a>
### C76626-19 · LLMs for Non-English Languages and non-American Cultures (guest lecture from Shaily Bhatt)

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：03/24/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-03-24-non-english.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-20"></a>
### C76626-20 · World models (guest lecture from Mingkai Deng)

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：03/26/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-03-26-world-models.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-21"></a>
### C76626-21 · LLMs for biological understanding (guest lecture by Prof Lei Li)

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：03/31/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-03-31-drug-design.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-22"></a>
### C76626-22 · Music generation (guest lecture by Prof Chris Donahue)

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：04/02/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-04-02-music.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c76626-23"></a>
### C76626-23 · Numbers

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：04/07/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-03-7-detection-and-numbers.pdf) — 已验证 · HTTP 206 / PDF。

备注：原目录文件名日期与上课日期不同；保留目录原始 URL，不擅自改名。

<a id="c76626-24"></a>
### C76626-24 · Robots and embodied AI (guest lecture from Leena Mathur)

**学校／课程**：CMU · 11-766 · Large Language Model Applications；**学期**：2026 春；**课堂日期**：04/14/2026。

**原始目录**：[课程 syllabus / schedule](https://cmu-llms.org/schedule/)。**主题**：[补充主题](#topic-supplement)。

- [PDF · slides](https://storage.googleapis.com/cmu-llms/2026/2026-04-14-robotics.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-11"></a>
### C71125-11 · Modeling II: Multimodal I

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 11 09/30/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[补充主题](#topic-supplement)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-11-multimodal.pdf) — 已验证 · HTTP 206 / PDF。

<a id="c71125-12"></a>
### C71125-12 · Modeling III: Multimodal II

**学校／课程**：CMU · 11-711 · Advanced Natural Language Processing；**学期**：2025 秋；**课堂日期**：# 12 10/02/2025。

**原始目录**：[课程 syllabus / schedule](https://cmu-l3.github.io/anlp-fall2025/)。**主题**：[补充主题](#topic-supplement)。

- [PDF · [slides]](https://cmu-l3.github.io/anlp-fall2025/static_files/anlp-f2025-12-multimodal-ii.pdf) — 已验证 · HTTP 206 / PDF。

<a id="b24-04"></a>
### B24-04 · Enterprise trends for generative AI, and key components of building successful agents/applications

**学校／课程**：UC Berkeley · CS194/294-196 · LLM Agents；**学期**：2024 秋；**课堂日期**：Sept 30。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/llm-agents/f24)。**主题**：[补充主题](#topic-supplement)。

- [PDF · Slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/Burak_slides.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/Sy1psHS3w3I) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="b24-09"></a>
### B24-09 · Project GR00T: A Blueprint for Generalist Robotics

**学校／课程**：UC Berkeley · CS194/294-196 · LLM Agents；**学期**：2024 秋；**课堂日期**：Nov 4。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/llm-agents/f24)。**主题**：[补充主题](#topic-supplement)。

- [PDF · Slides](https://rdi.berkeley.edu/llm-agents/assets/jimfangr00t.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/Qhxr0uVT2zs) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="b24-10"></a>
### B24-10 · Open-Source and Science in the Era of Foundation Models

**学校／课程**：UC Berkeley · CS194/294-196 · LLM Agents；**学期**：2024 秋；**课堂日期**：Nov 18。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/llm-agents/f24)。**主题**：[补充主题](#topic-supplement)。

- [PDF · Slides](https://rdi.berkeley.edu/llm-agents/assets/percyliang.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/f3KKx9LWntQ) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="ba25-07"></a>
### BA25-07 · Multimodal Agents – From Perception to Action

**学校／课程**：UC Berkeley · CS194/294-280 · Advanced LLM Agents；**学期**：2025 春；**课堂日期**：Mar 17th。

**原始目录**：[课程 syllabus / schedule](https://rdi.berkeley.edu/adv-llm-agents/sp25)。**主题**：[补充主题](#topic-supplement)。

- [PDF · Slides](https://rdi.berkeley.edu/adv-llm-agents/slides/Multimodal_Agent_caiming.pdf) — 已验证 · HTTP 206 / PDF。
- 补充：[官方目录所列视频](https://www.youtube.com/live/n__Tim8K2IY) — 仅确认目录链接存在，未验证播放／登录权限。

<a id="i59825-08"></a>
### I59825-08 · Multi-modal Understanding

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：Feb 20。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[补充主题](#topic-supplement)。

- [PPTX · Sudhit Rao, Vir Sikand, Rui Zhou (Group 8)](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/08_MultiMudal.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/08_MultiMudal.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="i59825-17"></a>
### I59825-17 · Data

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：April 10。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[补充主题](#topic-supplement)。

- [PPTX · Rashi Tyagi, Haoran Wu, Ziyang Zheng (Group 11)](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/15_Data.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/15_Data.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。

<a id="i59825-20"></a>
### I59825-20 · Conclusion:Graph+LLM

**学校／课程**：UIUC · CS598 · Topics in LLM Agents（Jiaxuan You）；**学期**：2025 春；**课堂日期**：April 29。

**原始目录**：[课程 syllabus / schedule](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents)。**主题**：[补充主题](#topic-supplement)。

- [PPTX · Prof.Jiaxuan You(Only slides, Lecture Canceled)](https://raw.githubusercontent.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/main/Slides/Conclusion.pptx)；[官方仓库预览](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents/blob/main/Slides/Conclusion.pptx) — 已验证 · HTTP 206 / PPTX/ZIP。

备注：教师导论或学生研讨报告，非统一教师讲义。 原目录注明 Lecture Canceled；仅公开 slides。

<a id="ua26-03"></a>
### UA26-03 · Simulated Environments and Reality

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Tue, Jan 13, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/simulations_and_reality.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua26-04"></a>
### UA26-04 · How to Make a Simulation?

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Thu, Jan 15, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/how_to_make_a_simulation.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua26-06"></a>
### UA26-06 · Classical Control, Pre-Deep Learning

**学校／课程**：UC San Diego · CSE291A · AI Agents（Prithviraj Ammanabrolu）；**学期**：2026 冬；**课堂日期**：Thu, Jan 22, 2026。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course-WI26/lectures.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course-WI26/assets/lectures/classical_control_pre_deep_learning.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-03"></a>
### UA25-03 · Simulated Environments and Reality

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Tue, Jan 14, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/simulations_and_reality.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-04"></a>
### UA25-04 · How to Make a Simulation?

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Thu, Jan 16, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/how_to_make_a_simulation.pdf) — 已验证 · HTTP 206 / PDF。

<a id="ua25-06"></a>
### UA25-06 · Classical Control, Pre-Deep Learning

**学校／课程**：UC San Diego · CSE291 · AI Agents（Prithviraj Ammanabrolu）；**学期**：2025 冬；**课堂日期**：Thu, Jan 23, 2025。

**原始目录**：[课程 syllabus / schedule](https://pearls-lab.github.io/ai-agents-course/lectures.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · [slides]](https://pearls-lab.github.io/ai-agents-course/assets/lectures/classical_control.pdf) — 已验证 · HTTP 206 / PDF。

<a id="u23426-01"></a>
### U23426-01 · Introduction; From AI to AGI

**学校／课程**：UC San Diego · CSE/DSC234 · Data-Centric AI and AI Engineering（Arun Kumar）；**学期**：2026 春；**课堂日期**：第1周。

**原始目录**：[课程 syllabus / schedule](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html)。**主题**：[补充主题](#topic-supplement)。

- [PDF · PDF](https://cseweb.ucsd.edu/classes/sp26/cse234-a/downloads/Topic0-Introduction.pdf) — 待验证 · 连接超时。

备注：官方目录按主题课件包组织，包不等于一次课堂。目录列出 PDF/PPTX；本次源站超时，只收录搜索索引实际返回的 PDF 地址，其余直链及 PPTX 待验证，未按文件名推测。

**跨主题索引**（完整链接与核验状态见主条目）：

| 条目 | Lecture | 学校／版本 |
|---|---|---|
| [SX26-03](#sx26-03) | Learning from Human Preferences | Stanford CS329X（2026 秋） |
| [SX26-06](#sx26-06) | Evaluating Human-AI interaction | Stanford CS329X（2026 秋） |
| [SX26-08](#sx26-08) | Building Full-Stack HAI Systems | Stanford CS329X（2026 秋） |
| [SX25-03](#sx25-03) | Learning from Human Preferences | Stanford CS329X（2025 秋） |
| [SX25-04](#sx25-04) | Collective Opinions and Pluralistic Alignment | Stanford CS329X（2025 秋） |
| [SX25-06](#sx25-06) | Guest Lecture: Omar Shaikh and Taylor Sorensen: Personalization | Stanford CS329X（2025 秋） |
| [SX25-08](#sx25-08) | Evaluating Human-AI interaction | Stanford CS329X（2025 秋） |
| [SX25-14](#sx25-14) | Guest Lecture: Niloofar Mireshghallah | Stanford CS329X（2025 秋） |
| [ST25-08](#st25-08) | Data curation and RL to optimize agents | Stanford CS329T（2025 秋） |
| [SG26-12](#sg26-12) | Data Strategy & Memory Layer for AI Agents | Stanford CS224G（2026 冬） |
| [SG25-14](#sg25-14) | Design Databases for Multimodal AI; Building Agentic Systems | Stanford CS224G（2025 冬） |
| [S33626-17](#s33626-17) | L17 Alignment - multimodality [Percy] | Stanford CS336（2026 春） |
| [C76626-03](#c76626-03) | The science of prompting | CMU 11-766（2026 春） |
| [C76626-11](#c76626-11) | Tool-use, chitchat, personas, and companionship | CMU 11-766（2026 春） |
| [C76626-13](#c76626-13) | LLMs for evaluation: Synthetic data generation, simulation, automatic evaluation, AI-as-judge | CMU 11-766（2026 春） |
| [C71125-14](#c71125-14) | Research Skills and Experimental Design | CMU 11-711（2025 秋） |
| [B24-03](#b24-03) | Agentic AI Frameworks & AutoGen / Building a Multimodal Knowledge Assistant | UC Berkeley CS194/294-196（2024 秋） |
| [B24-05](#b24-05) | Compound AI Systems & the DSPy Framework | UC Berkeley CS194/294-196（2024 秋） |
| [B24-12](#b24-12) | Towards Building Safe & Trustworthy AI Agents and A Path for Science‑ and Evidence‑based AI Policy | UC Berkeley CS194/294-196（2024 秋） |
| [BA25-06](#ba25-06) | Multimodal Autonomous AI Agents | UC Berkeley CS194/294-280（2025 春） |
| [BA25-11](#ba25-11) | Abstraction and Discovery with Large Language Model Agents | UC Berkeley CS194/294-280（2025 春） |
| [I59825-16](#i59825-16) | Gaming Agents | UIUC CS598（2025 春） |
| [UA26-05](#ua26-05) | Search for Planning in Simulations | UC San Diego CSE291A（2026 冬） |
| [UA26-15](#ua26-15) | Multi-Agent Systems and Human-AI Collaboration | UC San Diego CSE291A（2026 冬） |
| [UA25-05](#ua25-05) | Search for Planning in Simulations | UC San Diego CSE291（2025 冬） |
| [UA25-15](#ua25-15) | Multi-Agent Systems and Human-AI Collaboration | UC San Diego CSE291（2025 冬） |
| [UA25-16](#ua25-16) | Societal Impacts and Agent Safety | UC San Diego CSE291（2025 冬） |
| [U23425-13](#u23425-13) | 13 Parallelization - 3, data, inter- and intra-op parallelism | UC San Diego CSE234（2025 冬） |

<a id="missing"></a>
## 缺失、仅视频和未来课程

以下保留课程计划和缺口，**不是已验证可下载课件**。每条均有原目录定位；无确切文件 URL 时保持空缺。

### Stanford · CS329Z · Engineering AI Agents · 2026 秋

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="sz26-10"></a>SZ26-10<br>Mon Oct 26 | Guest Lecture: Terminal-Bench | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs329z.stanford.edu/) |
| <a id="sz26-11"></a>SZ26-11<br>Wed Oct 28 | What Data Do Agents Need? | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs329z.stanford.edu/) |
| <a id="sz26-12"></a>SZ26-12<br>Mon Nov 2 | Data Selection & Quality | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs329z.stanford.edu/) |
| <a id="sz26-13"></a>SZ26-13<br>Wed Nov 4 | Evaluation Fundamentals & Benchmark Design | Evaluation、LLM Foundations | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs329z.stanford.edu/) |
| <a id="sz26-14"></a>SZ26-14<br>Mon Nov 9 | LLM-as-Judge & Evaluation Infrastructure | Evaluation、Production / Reliability / Security / Infra | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs329z.stanford.edu/) |
| <a id="sz26-15"></a>SZ26-15<br>Wed Nov 11 | Agent Safety & Guardrails | Production / Reliability / Security / Infra | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs329z.stanford.edu/) |
| <a id="sz26-16"></a>SZ26-16<br>Mon Nov 16 | Guest Lecture (TBA) | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs329z.stanford.edu/) |
| <a id="sz26-17"></a>SZ26-17<br>Wed Nov 18 | Coding & Software Agents | Coding Agents、Agent Architecture / Orchestration | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs329z.stanford.edu/) |
| <a id="sz26-18"></a>SZ26-18<br>Mon Nov 30 | Proactive Agents | Agent Architecture / Orchestration | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs329z.stanford.edu/) |
| <a id="sz26-19"></a>SZ26-19<br>Wed Dec 2 | Frontiers & Open Problems | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs329z.stanford.edu/) |

### Stanford · CS329T · Trustworthy Machine Learning / Agentic AI · 2025 秋

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="st25-11"></a>ST25-11<br>Thu Nov 13 | Multi-modal frontier models with agentic capabilities | 补充主题 | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://web.stanford.edu/class/cs329t/syllabus.html) |

### Stanford · CS224G · Building and Scaling LLM Applications · 2026 冬

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="sg26-15"></a>SG26-15<br>TueMar 10 | How to Deliver a Great Pitch | 补充主题 | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://web.stanford.edu/class/cs224g/schedule.html) |
| <a id="sg26-16"></a>SG26-16<br>ThuMar 12 | OpenAI's Beginnings & How Investors Qualify Startups | 补充主题 | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://web.stanford.edu/class/cs224g/schedule.html) |

### Stanford · CS224G · Apps with LLMs Inside · 2025 冬

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="sg25-10"></a>SG25-10<br>2/20 | MindsDB | 补充主题 | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://web.stanford.edu/class/cs224g/2025/schedule.html) |

### Stanford · CS329X · Human-Centered LLMs · 2026 秋

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="sx26-10"></a>SX26-10<br>Oct 26, Monday | LLMs and the Future of Work | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://web.stanford.edu/class/cs329x/index.html) |
| <a id="sx26-11"></a>SX26-11<br>Nov 2, Monday | ✨ Guest Lecture: Valerie Chen (Stanford) and Weiyan Shi (Northeastern): Emerging Topics in Human-AI Interaction | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://web.stanford.edu/class/cs329x/index.html) |
| <a id="sx26-12"></a>SX26-12<br>Nov 4, Wednesday | ✨ Guest Lecture: Emma Pierson (UC Berkeley) | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://web.stanford.edu/class/cs329x/index.html) |
| <a id="sx26-13"></a>SX26-13<br>Nov 9, Monday | The Rise of AI Companions | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://web.stanford.edu/class/cs329x/index.html) |
| <a id="sx26-14"></a>SX26-14<br>Nov 11, Wednesday | ✨ Guest Lecture: Kunal Handa (Anthropic) | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://web.stanford.edu/class/cs329x/index.html) |
| <a id="sx26-15"></a>SX26-15<br>Nov 16, Monday | Safety and Privacy in LLM Use | Production / Reliability / Security / Infra | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://web.stanford.edu/class/cs329x/index.html) |
| <a id="sx26-16"></a>SX26-16<br>Nov 18, Wednesday | ✨ Guest Lecture: Vishakh Padmakumar (Stanford) and Myra Cheng (Stanford): Overreliance and Sycophancy | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://web.stanford.edu/class/cs329x/index.html) |
| <a id="sx26-17"></a>SX26-17<br>Nov 30, Monday | Latest Human-Centered LLM Topics in Late 2026 | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://web.stanford.edu/class/cs329x/index.html) |

### Stanford · CS329X · Human-Centered LLMs · 2025 秋

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="sx25-10"></a>SX25-10<br>Oct 23, Thursday | Guest Lecture: Eric Zelikman | 补充主题 | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://web.stanford.edu/class/cs329x/2526_index.html) |

### Stanford · CS336 · Language Modeling from Scratch · 2026 春

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="s33626-18"></a>S33626-18<br>Mon June 1 | L18 Guest lecture: Daniel Selsam | 补充主题 | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://cs336.stanford.edu/) |
| <a id="s33626-19"></a>S33626-19<br>Wed June 3 | L19 Guest lecture: Dan Fu | 补充主题 | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://cs336.stanford.edu/) |

### Stanford · CS336 · Language Modeling from Scratch · 2025 春

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="s33625-18"></a>S33625-18<br>Thurs May 29 | L18 Guest Lecture by Junyang Lin | 补充主题 | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://cs336.stanford.edu/spring2025/index.html) |
| <a id="s33625-19"></a>S33625-19<br>Tues June 3 | L19 Guest lecture by Mike Lewis | 补充主题 | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://cs336.stanford.edu/spring2025/index.html) |

### CMU · 11-768 · AI Agents · 2026 秋

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="c76826-16"></a>C76826-16<br>Thu, Oct 22 | Safety 2: Observability and Monitoring | Production / Reliability / Security / Infra | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://www.cmu-agents.com/) |
| <a id="c76826-17"></a>C76826-17<br>Tue, Oct 27 | Agents and the Future of Work | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://www.cmu-agents.com/) |
| <a id="c76826-18"></a>C76826-18<br>Thu, Oct 29 | Interaction 1: Multi-Agent Interaction | Multi-Agent、补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://www.cmu-agents.com/) |
| <a id="c76826-19"></a>C76826-19<br>Tue, Nov 10 | Interaction 2: Human-Agent Interaction | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://www.cmu-agents.com/) |
| <a id="c76826-20"></a>C76826-20<br>Thu, Nov 12 | Search 1: Reranking and Critic Models | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://www.cmu-agents.com/) |
| <a id="c76826-21"></a>C76826-21<br>Tue, Nov 17 | Search 2: Tree Search | Reasoning / Planning | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://www.cmu-agents.com/) |
| <a id="c76826-22"></a>C76826-22<br>Thu, Nov 19 | Guest Lecture | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://www.cmu-agents.com/) |
| <a id="c76826-23"></a>C76826-23<br>Tue, Nov 24 | Guest Lecture | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://www.cmu-agents.com/) |
| <a id="c76826-24"></a>C76826-24<br>Tue, Dec 1 | Final presentations (posters) | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://www.cmu-agents.com/) |
| <a id="c76826-25"></a>C76826-25<br>Thu, Dec 3 | Final presentations (posters) | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://www.cmu-agents.com/) |

### CMU · 11-711 · Advanced Natural Language Processing · 2025 秋

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="c71125-23"></a>C71125-23<br># 27 11/25/2025 | Advanced Modeling: Diffusion | 补充主题 | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://cmu-l3.github.io/anlp-fall2025/) |

### UC Berkeley · CS194/294-196 · Agentic AI · 2025 秋

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="b25-09"></a>B25-09<br>Nov 3 | AI Agents to Automate Scientific Discoveries | 补充主题 | 仅找到视频，未找到公开 PDF/PPTX/Notes；[目录所列视频](https://www.youtube.com/watch?v=yqPIsTTdUkc)（播放未验证）；[原目录](https://rdi.berkeley.edu/agentic-ai/f25) |
| <a id="b25-11"></a>B25-11<br>Nov 17 | Multi-Agent Systems in the Era of LLMs | Multi-Agent | 仅找到视频，未找到公开 PDF/PPTX/Notes；[目录所列视频](https://www.youtube.com/watch?v=ntjOxjZMaac&t=2s)（播放未验证）；[原目录](https://rdi.berkeley.edu/agentic-ai/f25) |
| <a id="b25-12"></a>B25-12<br>Dec 1 2:00-3:30pm PT | Autonomous Agents: Embodiment, Interaction, and Learning | 补充主题 | 仅找到视频，未找到公开 PDF/PPTX/Notes；[目录所列视频](https://www.youtube.com/watch?v=iDhzzugMOLA)（播放未验证）；[原目录](https://rdi.berkeley.edu/agentic-ai/f25) |
| <a id="b25-13"></a>B25-13<br>Dec 8 11:30am-1:30pm PT | Agentic AI Safety & Security | Production / Reliability / Security / Infra、Agent Architecture / Orchestration | 仅找到视频，未找到公开 PDF/PPTX/Notes；[目录所列视频](https://youtube.com/live/CvZDJxd4LKM?feature=share)（播放未验证）；[原目录](https://rdi.berkeley.edu/agentic-ai/f25) |

### UIUC · CS598 · Topics in LLM Agents（Jiaxuan You） · 2025 春

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="i59825-12"></a>I59825-12<br>March 25 | Auto-research | 补充主题 | 未发现可确认 PDF/PPTX/Notes 直链；教师导论或学生研讨报告，非统一教师讲义。；[原目录](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents) |
| <a id="i59825-14"></a>I59825-14<br>April 1 | Coding Agents | Coding Agents、Agent Architecture / Orchestration | 未发现可确认 PDF/PPTX/Notes 直链；教师导论或学生研讨报告，非统一教师讲义。；[原目录](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents) |
| <a id="i59825-15"></a>I59825-15<br>April 3 | Social Agents | Agent Architecture / Orchestration、补充主题 | 未发现可确认 PDF/PPTX/Notes 直链；原目录误指或复用 12_MultiAgent.pptx；不可确认是 Social Agents 课件。见同课 Multi-agent Systems 条目，独立 Social Agents 讲义待验证。；[原目录](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents) |
| <a id="i59825-19"></a>I59825-19<br>April 17 | Alignment | Optimization | 未发现可确认 PDF/PPTX/Notes 直链；教师导论或学生研讨报告，非统一教师讲义。；[原目录](https://github.com/ulab-uiuc/CS598-Topics-in-LLM-Agents) |

### UC San Diego · CSE/DSC234 · Data-Centric AI and AI Engineering（Arun Kumar） · 2026 春

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="u23426-02"></a>U23426-02<br>第1–4周 | Topic 1: Creating Data and Evals — Part 1 | Evaluation、补充主题 | 官方目录有课件线索；本次未取得确切文件地址，待验证；官方目录按主题课件包组织，包不等于一次课堂。目录列出 PDF/PPTX；本次源站超时，只收录搜索索引实际返回的 PDF 地址，其余直链及 PPTX 待验证，未按文件名推测。；[原目录](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html) |
| <a id="u23426-03"></a>U23426-03<br>第1–4周 | Topic 1: Creating Data and Evals — Part 2 | Evaluation、补充主题 | 官方目录有课件线索；本次未取得确切文件地址，待验证；官方目录按主题课件包组织，包不等于一次课堂。目录列出 PDF/PPTX；本次源站超时，只收录搜索索引实际返回的 PDF 地址，其余直链及 PPTX 待验证，未按文件名推测。；[原目录](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html) |
| <a id="u23426-04"></a>U23426-04<br>第1–4周 | Topic 1: Creating Data and Evals — Part 3 | Evaluation、补充主题 | 官方目录有课件线索；本次未取得确切文件地址，待验证；官方目录按主题课件包组织，包不等于一次课堂。目录列出 PDF/PPTX；本次源站超时，只收录搜索索引实际返回的 PDF 地址，其余直链及 PPTX 待验证，未按文件名推测。；[原目录](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html) |
| <a id="u23426-05"></a>U23426-05<br>第4–6周 | Topic 2: Retrieval and Context Engineering — Part 1 | RAG、Context Engineering、Evaluation | 官方目录有课件线索；本次未取得确切文件地址，待验证；官方目录按主题课件包组织，包不等于一次课堂。目录列出 PDF/PPTX；本次源站超时，只收录搜索索引实际返回的 PDF 地址，其余直链及 PPTX 待验证，未按文件名推测。；[原目录](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html) |
| <a id="u23426-08"></a>U23426-08<br>2026-05-07 | Guest Lecture: Ajay Rayasam (Osage University Partners) | 补充主题 | 官方目录有课件线索；本次未取得确切文件地址，待验证；官方目录按主题课件包组织，包不等于一次课堂。目录列出 PDF/PPTX；本次源站超时，只收录搜索索引实际返回的 PDF 地址，其余直链及 PPTX 待验证，未按文件名推测。；[原目录](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html) |
| <a id="u23426-11"></a>U23426-11<br>2026-05-28 | Guest Lecture: Kabir Nagrecha (Tessera Labs) | 补充主题 | 官方目录有课件线索；本次未取得确切文件地址，待验证；官方目录按主题课件包组织，包不等于一次课堂。目录列出 PDF/PPTX；本次源站超时，只收录搜索索引实际返回的 PDF 地址，其余直链及 PPTX 待验证，未按文件名推测。；[原目录](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html) |
| <a id="u23426-12"></a>U23426-12<br>第8–10周 | Topic 4: Model Customization | Optimization、LLM Foundations | 官方目录有课件线索；本次未取得确切文件地址，待验证；官方目录按主题课件包组织，包不等于一次课堂。目录列出 PDF/PPTX；本次源站超时，只收录搜索索引实际返回的 PDF 地址，其余直链及 PPTX 待验证，未按文件名推测。；[原目录](https://cseweb.ucsd.edu/classes/sp26/cse234-a/schedule.html) |

### UC San Diego · CSE291A · Systems for LLMs and AI Agents（Yiying Zhang） · 2025 秋

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="us25-02"></a>US25-02<br>9/29 | AI Agents Overview | Agent Architecture / Orchestration | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-03"></a>US25-03<br>10/1 | Transformer Overview and LLM Performance Analysis | Production / Reliability / Security / Infra、LLM Foundations | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-04"></a>US25-04<br>10/3 | Distributed Machine Learning Training | 补充主题 | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-05"></a>US25-05<br>10/6 | Distributed Machine Learning Training in Production — Haozheng Fan | Production / Reliability / Security / Infra | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-06"></a>US25-06<br>10/8 | Large Language Model Inference — Pt. 1 Intro and Iterative Scheduling | Production / Reliability / Security / Infra | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-07"></a>US25-07<br>10/10 | Large Language Model Inference — Pt. 2 PagedAttention | Production / Reliability / Security / Infra、LLM Foundations | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-08"></a>US25-08<br>10/13 | Speculative Decoding — Reyna Abhyankar | 补充主题 | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-09"></a>US25-09<br>10/15 | GPU Hardware and Megakernel — Zhiyuan Guo | Production / Reliability / Security / Infra | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-10"></a>US25-10<br>10/17 | Distributed Large Language Model Serving — Pt. 1 Prefix Caching | Production / Reliability / Security / Infra | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-11"></a>US25-11<br>10/20 | Distributed Large Language Model Serving — Pt. 2 Prefill-Decode Disaggregation — Junda Chen | Production / Reliability / Security / Infra | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-12"></a>US25-12<br>10/22 | Distributed Large Language Model Serving — Pt. 3 Long Context Serving | Context Engineering、Production / Reliability / Security / Infra | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-13"></a>US25-13<br>10/24 | LoRA Serving | Production / Reliability / Security / Infra | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-14"></a>US25-14<br>10/27 | Augmented LLM and Their Serving | Production / Reliability / Security / Infra | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-15"></a>US25-15<br>10/29 | Mixture-of-Expert Serving — Ruidong Zhu | Production / Reliability / Security / Infra、LLM Foundations | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-16"></a>US25-16<br>10/31 | Reasoning Models | Reasoning / Planning | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-18"></a>US25-18<br>11/5 | Reinforcement Learning Infrastructure — Vikranth Srivatsa | Optimization、Production / Reliability / Security / Infra | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-21"></a>US25-21<br>11/12 | Retrieval Augmented Generation — Siddhant Ray | RAG、Evaluation | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-22"></a>US25-22<br>11/14 | Agent Use Cases — Zhenwen Shao | 补充主题 | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-24"></a>US25-24<br>11/19 | Computer-Use Agents | Agent Architecture / Orchestration | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-25"></a>US25-25<br>11/21 | Multi-Agent Systems — Guohao Li | Multi-Agent | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-26"></a>US25-26<br>11/24 | Agent Infra in Production — Panpan Xu | Production / Reliability / Security / Infra | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-28"></a>US25-28<br>12/1 | KV Cache as the New AI Memory Abstraction — Juncheng Jiang（目录原文） | Production / Reliability / Security / Infra、Memory / Skills、RAG | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |
| <a id="us25-29"></a>US25-29<br>12/5 | Entrepreneurship in AI Infra and Agents and Course Summary | Production / Reliability / Security / Infra、补充主题 | 官方目录有课件线索；本次未取得确切文件地址，待验证；目录内容可由搜索索引读取；源站连接超时。已发现的 PDF 标待验证；其他条目仅保留目录定位，不猜测文件名。；[原目录](https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/) |

### Harvard · CS2680 · Modern AI Systems: Agents and System Optimizations · 2026 秋

| 编号／日期 | Lecture | 主题 | 资源状态与原目录 |
|---|---|---|---|
| <a id="h26-08"></a>H26-08<br>2026-10-05 | Guest lecture: Developing and Evaluating Agents in Enterprise Setting | Evaluation | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://cs2680.seas.harvard.edu/) |
| <a id="h26-10"></a>H26-10<br>2026-10-14 | Advanced agent design II: agent safety, self-evolving harness | Production / Reliability / Security / Infra | 未发现可确认 PDF/PPTX/Notes 直链；[原目录](https://cs2680.seas.harvard.edu/) |
| <a id="h26-13"></a>H26-13<br>2026-10-28 | Efficient LLM serving basics III: Batching, paging, and parallelism | Production / Reliability / Security / Infra | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs2680.seas.harvard.edu/) |
| <a id="h26-14"></a>H26-14<br>2026-11-02 | Efficient LLM serving: speculative decoding | Production / Reliability / Security / Infra | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs2680.seas.harvard.edu/) |
| <a id="h26-15"></a>H26-15<br>2026-11-04 | Efficient agentic systems: scheduling and prefix caching | Agent Architecture / Orchestration | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs2680.seas.harvard.edu/) |
| <a id="h26-16"></a>H26-16<br>2026-11-09 | Guest lecture: Why Infrastructure sets the pace of AI | Production / Reliability / Security / Infra | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs2680.seas.harvard.edu/) |
| <a id="h26-17"></a>H26-17<br>2026-11-11 | Efficient LLM serving: pruning and quantization | Production / Reliability / Security / Infra | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs2680.seas.harvard.edu/) |
| <a id="h26-18"></a>H26-18<br>2026-11-16 | Efficient LLM serving: KV-cache optimization and model architectures | Optimization、Production / Reliability / Security / Infra、LLM Foundations | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs2680.seas.harvard.edu/) |
| <a id="h26-19"></a>H26-19<br>2026-11-23 | Efficient agentic system: routing and load balancing | 补充主题 | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs2680.seas.harvard.edu/) |
| <a id="h26-20"></a>H26-20<br>2026-11-30 | Efficient agentic systems: others | Agent Architecture / Orchestration | 计划课程，2026-10-23 尚未开讲；未发现公开讲义；[原目录](https://cs2680.seas.harvard.edu/) |

<a id="limitations"></a>
## 核验局限与待补齐项

1. **UCSD cseweb 源站本次连接超时**。CSE234 2026 与 CSE291A Systems 2025 的部分地址来自官方搜索索引，因此标注待验证。CSE234 Topic 1 各部分、Topic 2 Part 1、Topic 4 及对应 PPTX 未获得确切直链；系统课其余 lecture 保留官方目录，不生成猜测路径。
2. **CS336 交互式 Notes**：官方目录链接到基于 Python trace 的阅读页面。网页可达不能保证动态内容加载成功；可从课程目录进一步进入官方 lectures 仓库。未把 HTML 页标成 PDF。
3. **UIUC Social Agents 疑似误链**：官方 README 将其指向 `12_MultiAgent.pptx`，本版将文件归于 Multi-agent Systems，并把 Social Agents 列为独立课件待验证。`08_MultiMudal.pptx` 的拼写为官方文件名，未改写。
4. **资源格式按实际文件判断**：例如 Berkeley `multiagent_berkeley_2025.pptx.pdf` 是 PDF，不能因为文件名含 pptx 就称其为可编辑 PPTX。UCSD CSE234 2025 的 scribe notes 是学生笔记，和教师 slides 分别标记。
5. **2026 秋课程持续更新**：Stanford CS329Z/CS329X、CMU 11-768、Harvard CS2680 的后续课程安排可能变化；本文只报告截止日观察结果，不承诺未来 URL。
6. **目录和内容可能不同步**：目录日期、PDF 文件名日期、网页修改时间不是同一概念。CMU 11-766 的 Numbers / Deployment 文件名日期与课堂日期不一致，保留原链接。
7. **边界**：未纳入每篇推荐论文、作业答案、Canvas 内部文件及全部视频；本文件以 lecture slides、官方 notes、学生 scribe notes 为主。未逐页翻译讲义；中文说明和主题索引是本次整理。

<a id="project-sources"></a>
## 如何添加到 Project Sources

本文件已生成于本地输出目录；本地 `sources/` 是只读同步镜像，不能通过向其中写文件来完成云端上传。当前可用接口未提供 Project Sources 文件上传操作。

下载本 `.md` 文件后，打开 ChatGPT 的 **AI Agent** 项目，在项目的 **Sources／文件** 区域选择 **添加／上传文件**，选中该 Markdown。不同客户端按钮文字可能略有不同；上传完成后确认列表中出现本文件。后续提问可写：“依据 AI Agent 大学课件主题索引，找出 Memory / Skills 的已验证课件，并注明编号与学校。”

若需要项目直接引用某份讲义正文，请下载并另行上传对应 PDF/PPTX；Markdown 中的外部链接本身不等于已上传的讲义全文。

---

维护规则：更新时保留原课程与学期，重新检查 URL；为新增资料补充核验日期；遇到重定向、登录页、404 或疑似目录误链时记录状态，不静默替换为未经核实的链接。
