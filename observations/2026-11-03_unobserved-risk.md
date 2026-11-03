---
date: 2026-11-03
trigger: correction
target: BEHAVIOR.md
resolved: 98d5eae
---

- **Doing:** simplifying the doordash-air Phase 1 controller, whose static
  chord, chord-length inequality, implicit length target, and monotonicity
  condition were built to absorb a cable bow before any run showed it mattered
  (the Phase 2 rigid-link metric later found it negligible). The agent's first
  answer then listed four further caveats for effects not yet observed.
- **Hit:** no rule exists for unobserved risks outside code. CODING.md's
  "never add features, fallbacks, heuristics, defensive programming, or
  validation beyond what the task requires" covers code only. BEHAVIOR.md's
  drift check ("a case the domain's own precedent already produced") bounds
  anticipation by precedent but says nothing of risks without one. The user
  relayed an advisor's correction: when it is unknown whether a problem will
  appear, do not fix it in advance; prepare a plan B and let the problem
  appear (YAGNI, premature optimization, contingency over mitigation), and
  stated that it governs reasoning in general.
- **Did:** cut the static chord from Phase 1 in favor of lambda = |d| and
  lambda q_bar, kept the bow as one stated assumption, and drafted a
  BEHAVIOR.md proposal.
