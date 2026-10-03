---
date: 2026-10-03
trigger: contradiction
target: CODING.md
---

- **Doing:** Standardizing the minithex `.gitignore` against the CODING.md
  template.
- **Hit:** The template's comments "# Secrets — never commit" and "# LaTeX
  intermediates — track only source and final PDF" carry em-dashes, which
  OUTPUT.md forbids in emitted text; copying the template verbatim imports
  them.
- **Did:** Wrote "# Secrets: never commit" in the repository copy.
