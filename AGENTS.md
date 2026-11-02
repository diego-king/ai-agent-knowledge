# Repository AI Editing Rules

## Single source of truth
- Repository: `diego-king/ai-agent-knowledge`
- Branch: `main`
- Three canonical study documents only:
  - General Python interviews: `docs/python-interview.md`
  - Python data structures and algorithms: `docs/data-structures.md`
  - University AI Agent courses summarized by topic: `docs/university-ai-agent-courses.md`
- `README.md` and `AGENTS.md` are repository-maintenance files, not study documents.

## Update policy
1. On a request to save, revise, or add learning notes, identify one of the three canonical files.
2. Read the newest contents of the target file from `main` first. For API writes, fetch its blob SHA; for Git clients, pull/rebase.
3. Merge changes without deleting useful existing notes or creating duplicate versions.
4. Use the same path and commit directly when permitted. Handle concurrent changes via a fresh read and merge; never force-push.
5. Confirm the GitHub write completed. Give a real commit URL and changed paths, not just a local copy.
6. If GitHub write access is unavailable, explicitly state that the change is **not saved** and suggest a supported route.
7. Do not reintroduce extra directories such as `data/`, `assets/`, `code/`, or `notes/` without explicit user direction.
8. Only add new files/rename canonical files with the user's permission.

## Content style
- Explanations in Chinese with precise English technical terms, short runnable Python snippets where helpful.
- For university materials: organize by **topic**, list source courses and official URLs, distinguish verified source facts from personal synthesis, and link to course slides/lectures only when available.
- Keep original notes under the same file path, never generate `-v2`, `-final`, etc.
- Do not copy restricted university course materials or store secrets and personal/sensitive data.
