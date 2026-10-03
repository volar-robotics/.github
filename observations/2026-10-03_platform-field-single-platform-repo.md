---
date: 2026-10-03
trigger: ambiguity
target: NAMING.md
---

- **Doing:** Naming the SITL and flight logs the minithex test scripts write
  to `results/`.
- **Hit:** "`YYYY-MM-DD_<platform>_<what>[_<run>]`". In a repository that holds
  one platform, the rule does not say whether the platform field is still
  required or redundant.
- **Did:** Kept the field (`<date>_minithex_<what>`) so a log stays
  identifiable once it leaves the repository.
