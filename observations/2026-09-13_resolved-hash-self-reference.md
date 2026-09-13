---
date: 2026-09-13
trigger: contradiction
target: OUTPUT.md
resolved: 887c1619f4cc5c240c79cb3f5545fbcdd15a0ab4
---

- **Doing:** Filing observations for a set of standards amendments and
  preparing to mark them resolved.
- **Hit:** The Observations section requires the resolving commit to set
  `resolved:` "to its own hash, in the same commit." A commit hash covers the
  tree that commit records, so writing the hash into a file in that tree
  changes the hash. The repository's own history closes observations in a
  later backfill commit instead.
- **Did:** Followed the observed practice, backfilling `resolved:` after the
  resolving commit existed, and raised the wording in conversation.
