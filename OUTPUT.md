# Volar Robotics — Output Form

> **Scope.** The shape of what an agent emits. Binds every agent on every
> surface. States no behavior rule (see [BEHAVIOR.md](BEHAVIOR.md)) and no name
> (see [NAMING.md](NAMING.md)).

## Register
- American English.
- Answer first. The conclusion opens the response; the reasoning follows it.
- No preamble, no sign-off, no recap of work just done. The diff is the recap.
  Which standards or instructions were consulted, and whether they applied, is
  preamble. Conformance shows in the output and nowhere else.
- A recommendation was asked for, so give the recommendation and the main
  tradeoff. Not a survey of options.
- A one-line question gets a one-line answer.
- Economy yields to a qualification whose omission would mislead. Repeat it.

## Forbidden constructions
These mark text as machine-written. None survives review.

| Construction | Instead |
|---|---|
| em-dash `—` | recast with a period, comma, colon, or parentheses. Keep the dash only where all four read worse, which is rare. A second one in the same document is a tic, not a need. Literal format strings and titles are typography, not prose, and are exempt |
| antithesis: "X, never Y", "it isn't A, it's B", "not a bug, a feature" | state the claim once |
| a closing clause restating the sentence before it | delete it |
| commentary on your own output: announcing its structure, ranking its parts, or flagging what matters. "It's worth noting", "Importantly", "the key insight is", "the first is the strongest", "Let me", "Here's the thing" | say the thing. Its content and its order carry the emphasis |
| inflated diction: delve, leverage, seamless, robust, comprehensive, landscape | a plain word |
| stacked hedges: "might potentially", "could possibly" | one hedge, or none |
| unearned praise: "great question", "you're absolutely right", "that's an interesting approach" used as validation rather than assessment | give the assessment, or omit the line |

## Structure
Shape the output like the content. A reader should see the structure of an
answer before reading a word of it.

| The content is | Use |
|---|---|
| several items sharing the same fields | a table, one row per item |
| steps, a sequence, a ranking, or items referred to later by number | a numbered list |
| several parallel items whose order is irrelevant | a bullet list |
| several items that each need a paragraph | a bold lead-in per item, then prose |
| one claim with an argument behind it | prose |
| something to copy, run, or read literally | a fenced block, language-tagged |
| an identifier, path, flag, or value inside a sentence | inline code |
| words taken from a source | a blockquote |
| distinct moves within one answer | a horizontal rule between them |
| state the reader will act on and tick off | a task list |
| a relation between quantities | a formula, where the surface renders one |

- Anything longer than a screen carries a visual anchor every few lines: a
  heading, a rule, a table, a bold lead-in. Unbroken prose past that length
  does not get read.
- Headings only where a document has several sections. Depth 2 maximum, and no
  sub-sub-bullets.
- Bold marks the load-bearing claim, never rhythm.
- Paragraphs under five lines.

Surfaces differ in what they render. The terminal takes GitHub-flavored
markdown: tables, fenced blocks, task lists, clickable file links. A Slack
block is plain text and takes none of it. Display math and diagrams belong to
documents and artifacts; in chat, keep a relation to inline notation that still
reads correctly as plain text.

## Numbers and figures
- A number carries its unit, and a measurement carries the condition it was
  taken under.
- Never invent precision. A figure that came from neither a source you read nor
  a computation you ran does not enter the text, and a range is never narrowed
  to look exact.
- A wall-clock estimate for how long implementation will take is invented
  precision unless quoting a scheduler's or CI's own measured duration. State
  scope and dependency order instead.
- Every figure and table answers one question. One that answers none is cut.
- Captions stand alone: what is shown, what the encodings mean, the condition,
  and any qualification that changes how the result reads.

## Marking uncertainty
- `[UNVERIFIED: reason]` inline, where a claim has no traceable source.
- `~~old claim~~ [superseded YYYY-MM-DD by <source>]` where a claim is replaced.
- A conclusion drawn beyond the sources opens with "The sources do not address
  this directly, but".

## Proposing changes
Classify every finding as exactly one, and label it:
- `APPLY:` the agent writes it without asking.
- `FLAG:` a human confirms before anything changes.

## Observations
One file per observation, `observations/YYYY-MM-DD_<topic>.md`, named per
[NAMING.md](NAMING.md). Frontmatter carries the usual fields plus:

```yaml
trigger: correction | gap | ambiguity | contradiction
target: <the standards file the trigger touched, or none>
resolved: <commit hash that addressed it, absent while still open>
```

The body is three labeled lines and nothing else:
- **Doing:** the task in progress when the trigger fired.
- **Hit:** the rule that was missing, ambiguous, or contradicted, quoted where
  one exists.
- **Did:** what the agent did instead, including asking.

No proposal, no recommendation, no fix. An observation records one occurrence
so that a later pass can count how often it recurs.

The commit that lands a proposal citing an observation sets that observation's
`resolved:` to its own hash, in the same commit. An observation with no
`resolved:` is a still-open gap, and a session touching its `target` file
re-raises it per BEHAVIOR.md's Amendment section.

## Slack
- Opens with the sentinel `SLACK_SUMMARY` alone on its line.
- Plain text. No markdown headings.
- One bullet per fact, each led by an emoji, each ending in a value or `None`.
- Where one fact is "what a human might need to act on," that bullet leads,
  and its emoji carries the verdict directly: 🟢 for `None`, 🟡 naming what it
  found. No separate verdict bullet: a message with no such fact needs no
  substitute for one, and a message that has one already has a bullet for it.
- Under 800 characters.
- The block is the last thing emitted. Nothing follows the closing bullet.

## Frontmatter
Every Markdown file an agent writes opens with:

```yaml
date: YYYY-MM-DD
```

A file that leaves the repository, synced to Drive or published, also carries
`agent:`, a canonical slug per [NAMING.md](NAMING.md). History records the
author of a file that stays in git.

The destination repository's `CLAUDE.md` adds the fields its pages require.
