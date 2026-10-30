---
date: 2026-10-13
trigger: correction
target: WRITING.md
resolved: 39010bd
---

- **Doing:** Notation pass on a client report.
- **Hit:** No rule governs `:=`. Reading "each new symbol is defined with its
  frame right after it" as a call to mark every definition, the agent wrote
  `\coloneq` on 29 definitions, most already marked as such by "let", "with",
  "where" or "is". The user called it an abuse of `\coloneq`.
- **Did:** Kept `\coloneq` on the seven definitions displayed beside an
  inequality or a derived relation; turned the other 22 into `=`.
