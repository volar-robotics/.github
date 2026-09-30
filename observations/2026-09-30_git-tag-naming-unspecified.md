---
date: 2026-09-30
trigger: gap
target: NAMING.md
---

- **Doing:** Reconciling the diverging branches of a client simulation and
  report repository pair (`acme-air-sim` and `acme-air-report` stand in, per
  the Disclosure rule: this repository is public), which needed tags for a
  delivered contract phase and for archived branches.
- **Hit:** NAMING.md's GitHub section names repositories, branches, commit and
  PR titles, and layout. No rule covers git tags.
- **Did:** Proposed `YYYY-MM-DD_phase-1` for the delivery and
  `archive/<branch>` for archived branches, derived from the separator law,
  the date-first rule for a series and the branch form, and asked the user,
  who accepted both.
