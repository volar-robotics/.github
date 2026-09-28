---
date: 2026-09-28
trigger: contradiction
target: NAMING.md
---

- **Doing:** Filing a scanned supplier invoice into
  `03_finance/invoices/incoming/2026-09` and recording its name in the asset
  register.
- **Hit:** NAMING.md shows a type field only in examples, never as a rule:
  "`2026-09-09_slack_invoice_sbie-12598087.pdf`". The invoices already in
  that folder and the register's Invoice column use
  `YYYY-MM-DD_<slug>_<number>.pdf` with no `invoice` field, so the folder
  read as conformant.
- **Did:** Named the file after the folder precedent, then renamed it to the
  NAMING.md form once a Drive handoff note cited the examples, and reported
  the mismatch to the user.
