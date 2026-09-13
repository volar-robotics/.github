---
date: 2026-09-13
trigger: correction
target: BEHAVIOR.md
resolved: 8751c60
---

- **Doing:** Disabling Co-Authored-By attribution trailers on commits and PRs
  at the user's request, first as a personal preference, then as a
  company-wide one.
- **Hit:** BEHAVIOR.md's Claims about yourself section bars stating a run
  cadence or an internal state, but no rule bars an agent claiming (co-)
  authorship of a commit, PR, or other artifact. The first fix landed in the
  user's personal `~/.claude/settings.json`, which cannot bind another
  engineer's agent.
- **Did:** Proposed a new bullet in conversation rather than writing it
  unasked.
