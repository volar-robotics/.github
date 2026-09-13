---
date: 2026-09-13
trigger: ambiguity
target: NAMING.md
---

- **Doing:** Checking observed Drive folder names against the Drive section
  of NAMING.md during a structure audit.
- **Hit:** The Drive section says "Subfolders are the slug," but most second
  level folders in use are function words rather than canonical slugs
  (`invoices/`, `compliance/`, `digests/`, `meetings/`, `slides/`), and the
  slug appears one level deeper where a project is named
  (`07_engineering/soar-ndt/meetings/`). The rule does not say which levels
  it binds, so the observed layout is neither clearly conformant nor clearly
  a violation.
- **Did:** Read the rule as binding the level that names a program, product,
  client, or platform, marked that reading as an inference, and raised it.
