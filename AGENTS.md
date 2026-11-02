# AI Agent Knowledge — Editing Rules

## Canonical repository
- GitHub: `diego-king/ai-agent-knowledge`
- Branch: `main`
- Only three persistent study files:
  - Python language/general interview: `docs/python-interview.html`
  - Python data structures and algorithms: `docs/data-structures.html`
  - University AI Agent / LLM Engineering course material index, organized by topic: `docs/university-ai-agent-courses.md`
- `README.md` and this `AGENTS.md` are maintenance metadata, not additional knowledge sources.

## Required read / write workflow
1. Save only when the user requests a persistent update, revision or addition. Identify the relevant canonical path above.
2. Fetch latest content and blob SHA from GitHub `main` before writing; for Codex/Git workspaces, synchronize the branch first.
3. Merge into the SAME path while keeping all useful existing information, working links, headings, examples, code, styles and interactive behavior.
4. Do not create `-v2`, `-final`, timestamp copies, new folders or parallel versions of a canonical note.
5. Resolve concurrent changes by fetching again and reconciling. Never force-push or silently overwrite another writer.
6. Commit changes and return the actual GitHub commit URL only after verifying the write.
7. If the current environment cannot read or write GitHub, clearly state the limitation instead of claiming an update is saved.

## Format requirements
- The two Python sources are FULL HTML guides; preserve their inline CSS/JavaScript, diagrams, responsive styling, interactive exercises, and mutual links:
  - `python-interview.html` → `data-structures.html`
  - `data-structures.html` → `python-interview.html`
- University courses remain ONE comprehensive Markdown file, organized by Topic, with official lecture / PDF / PPTX / notes links, course-and-semester labels, cross-topic indexing and original verification status. Do not replace it with a brief course summary.
- Explain in Chinese with original technical terminology in English. Avoid introducing unsupported factual claims into sourced course notes.
- No secrets, personal/sensitive data or unauthorized copyrighted full-text resources.

Do not reintroduce `data/`, `assets/`, `code/` or `notes/` folders unless the user explicitly asks.
