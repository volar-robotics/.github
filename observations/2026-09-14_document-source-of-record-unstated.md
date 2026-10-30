---
date: 2026-09-14
trigger: gap
target: none
---

- **Doing:** Building a project board from Report 1 of soar-ndt, given as a
  LaTeX source in `soar-ndt-report` and as "a rendered copy" in Drive.
- **Hit:** No rule states which copy of a document is of record when the same
  report exists both in git and in Drive. WRITING.md governs the argument,
  CODING.md the compiled document, NAMING.md the filing, and none of them says
  the repository source wins or that a Drive copy carries the revision it was
  exported from. The two copies here are different revisions: the Drive
  `.docx` is the 25 July draft and the `.tex` the 29 July rewrite. Both
  defects reported against the report existed only in the Drive copy and were
  already fixed in the `.tex`.
- **Did:** Treated the `.tex` as of record on its later revision date and
  commit date, built the board from it, and reported the divergence rather
  than editing either copy.
