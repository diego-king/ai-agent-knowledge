# AI Agent Knowledge — Editing Rules

## Canonical repository
- GitHub: `diego-king/ai-agent-knowledge`
- Branch: `main`
- Persistent study files (four canonical paths):
  - Python language/general interview: `docs/python-interview.html`
  - Python data structures and algorithms: `docs/data-structures.html`
  - University AI Agent / LLM Engineering course material index, organized by topic: `docs/university-ai-agent-courses.md`
- YouTube AI Agent conceptual short-video course index: `docs/youtube-ai-agent-courses.md` (user-authorized fourth study source; vendor/creator content is allowed here only).
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
- **University-only scope (mandatory for all future updates):** `docs/university-ai-agent-courses.md` contains exclusively university-provided AI Agent / LLM Engineering courses and their official university or instructor-linked lecture slides, lecture notes, syllabi, and course code. Before adding or editing an entry, verify the university affiliation, course identity, semester/year when available, and the official source URL. A university course's explicitly linked GitHub teaching repository is allowed; a standalone vendor course or generic open-source tutorial is not. Exclude LangChain Academy, commercial/vendor training, standalone framework tutorials, and non-university bootcamps, even when their topics match. Preserve historical statistics and avoid inflating university course counts. Apply this rule to manual edits and scheduled automations alike.
- **YouTube beginner-first scope (mandatory for all future manual and scheduled edits):** `docs/youtube-ai-agent-courses.md` is for a learner new to AI Agent Engineering who wants a systematic **general-purpose** Agent foundation (Fundamentals, Tool Calling/MCP, Memory/Context, Architectures, Multi-Agent, RAG, Evaluation/Safety, Production Reliability). Prefer concept/architecture teaching **≤20 minutes**, ideally 5–15; the **strict maximum is 30:00**. A 20:01–30:00 item requires clear added value. Deprioritize Voice/Vision/real-time multimodal specialties, product marketing, and code-only demos; a specialty course is eligible only as an explicitly labelled supplemental exception when its underlying architecture broadly transfers.
- **YouTube ranking and deduplication (mandatory):** Before each update, reread the latest criteria in `docs/youtube-ai-agent-courses.md`; apply relevance-to-beginners 30, accuracy/freshness 25, clarity 20, curriculum structure 15, length/information density 10. Prefer A ≥85, B 75–84, otherwise defer. Normalize and deduplicate **YouTube video IDs** across all topics and the archive. Also compare **learning objectives and conceptual overlap**: different titles/videos covering the same point should not automatically become multiple must-watch entries. Choose the clearest, shortest, accurate main recommendation; label genuinely useful alternatives as optional, noting overlap. Each video has one primary topic; cross-link rather than duplicating. Prefer up to five genuinely new nonredundant videos per monthly scan; report no additions when none qualify. Verify channel, video URL, publish date, duration, access and current technical correctness before assigning `Current`; otherwise `Needs Review`. Do not invent metadata or treat previously catalogued videos as new.
- Explain in Chinese with original technical terminology in English. Avoid introducing unsupported factual claims into sourced course notes.
- No secrets, personal/sensitive data or unauthorized copyrighted full-text resources.

Do not reintroduce `data/`, `assets/`, `code/` or `notes/` folders unless the user explicitly asks.
