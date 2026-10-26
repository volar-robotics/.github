---
date: 2026-10-26
trigger: correction
target: AGENTS.md
resolved: d9c6607
---

- **Doing:** adding a `CLAUDE.md` with an `AGENTS.md` symlink to `tt-lazio`, then checking
  whether Claude Code reads `AGENTS.md`.
- **Hit:** "A repository `CLAUDE.md` specializes these files for one repository and never
  restates them." Claude Code reads `AGENTS.md` only where no `CLAUDE.md` exists in the
  directory or above, so the two names coexisted across repositories.
- **Did:** reported the loading rule from the Claude Code memory docs; the user asked to
  rename every repository `CLAUDE.md` to `AGENTS.md` and approved the proposed wording.
