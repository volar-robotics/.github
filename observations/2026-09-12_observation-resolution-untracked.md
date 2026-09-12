---
date: 2026-09-12
trigger: gap
target: OUTPUT.md
---

- **Doing:** Reading the observations directory at the user's request, to
  assess whether a continuous feedback loop exists.
- **Hit:** The Observations section gives an observation no way to record
  that a later commit addressed it, so the directory cannot distinguish an
  open gap from a closed one without cross-referencing git log.
- **Did:** Proposed a `resolved:` frontmatter field and raised it in
  conversation.
