# AI Agent Knowledge — Repository Instructions

## Mission
Maintain ONE canonical GitHub copy of each topic across ChatGPT mobile/web/desktop, Work, and Codex. This file guides tools that read repository instructions; ChatGPT Project Instructions must also be configured separately.

## Canonical file map
- Python interview concepts: `docs/python-interview.md`
- Data structures and algorithms: `docs/data-structures.md`
- Agent frameworks, MCP, architecture: `docs/agent-frameworks.md`
- Interactive presentations: `notes/python-interview.html`, `notes/langgraph.html`, `notes/rag-evaluation.html`
- Machine-readable study progress: `data/learning-progress.json`
- Shared HTML styles: `assets/styles.css`
- Runnable Python examples: `code/examples.py`

## Mandatory edit protocol
1. Only save when the user requests persistence (e.g. “保存”, “更新项目”, “add to project”, or explicitly asks for an edit).
2. Before reading or editing, fetch the latest file from `main`; do not trust a prior conversation's cached copy.
3. Match the established canonical path; update it in place. Do not produce duplicate names such as `-v2`, `-updated`, `-new`, `-final`, or timestamp copies.
4. Preserve existing sections and manually merge new facts. When updating through GitHub Contents API, use the fetched blob SHA to prevent overwriting concurrent edits. In a Git workspace, pull/rebase before pushing.
5. If the remote changed or push fails, refetch, inspect the diff, reconcile, and retry safely. Never force-push over another writer.
6. Commit with a specific message; only claim the save succeeded after confirmation, and give the exact file path and commit link.
7. When making material conceptual changes to an HTML presentation, align its related Markdown reference, if applicable.
8. If the current client lacks a GitHub write tool, state the limitation and offer a supported Work/Codex or manual workflow. Never silently save only to a temporary sandbox or ChatGPT Project attachment.

## Content conventions
- Chinese explanations with accurate English technical terms.
- Prefer concise notes, reproducible examples, and links to authoritative sources.
- For code, prioritize runnable Python examples and lightweight tests. Avoid fictitious benchmarks or unverified API details.
- No secrets, API keys, passwords, personal/sensitive information, or copyrighted course material copied without permission.
- Do not publish private HTML through GitHub Pages without explicitly checking access restrictions.

## Format roles
Markdown in `docs/` is the canonical prose knowledge source. HTML in `notes/` is presentation/interactive content; CSS is shared, and JSON is structured progress. A topic may have both a doc and a view, but edits must not create uncontrolled duplicate sources.
