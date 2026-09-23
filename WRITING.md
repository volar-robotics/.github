# Volar Robotics — Technical Writing

> **Scope.** Papers, reports, proposals, and any document that argues from
> evidence to a claim. Adds to [BEHAVIOR.md](BEHAVIOR.md) and
> [OUTPUT.md](OUTPUT.md), which bind this work and are not restated here.

## Before writing
Settle these, in order, before the first section:

1. What the task requires.
2. What information is available.
3. What is unavailable, unobservable, or impractical.
4. Which assumptions delimit the problem.
5. Which representation and architecture follow from those constraints.
6. What evidence validates each claim.

A document is one engineered system, not a set of independent sections.

## Argument
Order the document so each element is the consequence of the one before it:

physical or operational motivation → related work grouped by methodological
category → the capability and the limitation of each category → the precise
missing combination or unresolved trade-off → the proposed pipeline as the
consequence of that gap → contributions as concrete technical objects or
demonstrated outcomes.

- Assumptions appear before the method they delimit.
- Notation and conventions are fixed before they become ambiguous.
- Components appear in dependency order, and are evaluated individually before
  the integrated system.
- Novelty names the exact combination, capability, or demonstrated integration
  that is new. A vague claim of novelty is not a claim.
- Limitations and future extensions are stated, not implied.

## Interfaces
For every important quantity, state where it originates, in which frame or
representation it is expressed, how it is transformed, and where it is
consumed. A reader must be able to trace any signal end to end through the
architecture.

Online and offline information sources are separated unmistakably, wherever
either appears: prose, figure, caption, table.

## Prose
- A paragraph runs: statement or requirement, justification, consequence,
  transition to the next design element.
- Terms are defined before use.
- An equation is introduced with its purpose and interpreted afterwards in
  operational terms. An equation left to speak for itself says nothing.
- "however", "conversely", "unlike" and "therefore" mark a real trade-off or a
  real logical consequence. Elsewhere they are cut.

## Figures
- An architecture figure for the complete pipeline appears early.
- Flow diagrams distinguish command, measurement, physical and offline paths
  visibly.
- Tables carry exact mappings, design ledgers, parameters, conditions, and
  quantitative comparisons.
- Procedures get sequential panels. Related signals get aligned multi-panel
  plots. A snapshot is paired with the sensor or model output from the same
  instant.
- Restrained scientific palette, consistent semantic colors, compact and
  aligned at publication size.

## Validation
A staircase, in this order:

1. The underlying model, regressor, or representation.
2. Accuracy and uncertainty, under explicit metrics.
3. A baseline, ground truth, or independent reference.
4. Computational or real-time feasibility, where it bears on the claim.
5. The complete system in its intended task.
6. A harder or shifted-condition case, where one is available.
7. What each experiment does and does not establish.

Interpret results against the requirements settled before writing. Explain why
an observed accuracy, timing, stability, or boundedness is sufficient for the
proposed use, or where it falls short. Narrating a plot is not interpretation.

## Final audit
Before delivering:

- Is every claim carried by an equation, a citation, a result, or a marked
  inference?
- Are assumptions and limitations visible before the reader needs them?
- Are frames, symbols, dimensions, and units consistent throughout, with every
  compound unit written as a product of powers, such as `N s m^-1` or
  `Nm rad^-1`?
- Can a reader trace every important signal through the architecture?
- Are online and offline sources unmistakably separated?
- Does each figure answer a question the text asks?
- Are the contributions concrete, and matched by the results?
- Is the scope narrow enough to survive skeptical review?
