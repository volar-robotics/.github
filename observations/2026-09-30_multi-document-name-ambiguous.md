---
date: 2026-09-30
trigger: ambiguity
target: NAMING.md
---

- **Doing:** Splitting a client report repository (`acme-air-report` stands
  in) into one folder per contract phase, each building its own document.
- **Hit:** "top-level document `main.tex` → `main.pdf`, or named for its slug
  where a repository builds several." A canonical slug names a program,
  product, client, or platform, so every document in one repository shares
  it, and the rule does not say what a document's own slug is.
- **Did:** Followed the repository's precedent of a document named for its
  folder (`<study>/<study>.tex`), giving `phase-1/phase-1.tex`, and showed the
  name to the user in the proposal.
