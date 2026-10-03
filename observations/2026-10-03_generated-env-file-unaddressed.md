---
date: 2026-10-03
trigger: gap
target: CODING.md
---

- **Doing:** Applying the CODING.md `.gitignore` template to minithex, where
  the generator writes `.env` with one non-secret line that `compose.yaml`
  interpolates.
- **Hit:** "# Secrets — never commit / .env / *.env". The template treats every
  `.env` as a secret and says nothing about a generated, non-secret one that a
  fresh clone needs.
- **Did:** Untracked `.env` and added a Makefile rule that generates it before
  `make build` and `make up`.
