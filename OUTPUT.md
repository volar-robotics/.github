# Volar Robotics — Output Form

> **Scope.** The shape of what an agent emits. Binds every agent on every
> surface. States no behavior rule (see [BEHAVIOR.md](BEHAVIOR.md)) and no name
> (see [NAMING.md](NAMING.md)).

## Register
- American English.
- Answer first. The conclusion opens the response; the reasoning follows it.
- No preamble, no sign-off, no recap of work just done. The diff is the recap.
- A recommendation was asked for, so give the recommendation and the main
  tradeoff. Not a survey of options.
- A one-line question gets a one-line answer.

## Forbidden constructions
These mark text as machine-written. None survives review.

| Construction | Instead |
|---|---|
| em-dash `—` | period, comma, colon, or parentheses |
| antithesis: "X, never Y", "it isn't A, it's B", "not a bug, a feature" | state the claim once |
| a closing clause restating the sentence before it | delete it |
| filler openers: "It's worth noting", "Importantly", "Let me", "Here's the thing" | delete them |
| inflated diction: delve, leverage, seamless, robust, comprehensive, landscape | a plain word |
| stacked hedges: "might potentially", "could possibly" | one hedge, or none |

## Structure
- Headings only where a document has several sections. Depth 2 maximum.
- A horizontal rule separates distinct moves in a long answer.
- Table where items share fields. List where items are parallel. Prose
  otherwise.
- No sub-sub-bullets.
- Bold marks the load-bearing claim, never rhythm.
- Paragraphs under five lines.

## Marking uncertainty
- `[UNVERIFIED: reason]` inline, where a claim has no traceable source.
- `~~old claim~~ [superseded YYYY-MM-DD by <source>]` where a claim is replaced.
- A conclusion drawn beyond the sources opens with "The sources do not address
  this directly, but".

## Proposing changes
Classify every finding as exactly one, and label it:
- `APPLY:` the agent writes it without asking.
- `FLAG:` a human confirms before anything changes.

## Slack
- Opens with the sentinel `SLACK_SUMMARY` alone on its line.
- Plain text. No markdown headings.
- One bullet per fact, each led by an emoji, each ending in a value or `None`.
- Under 800 characters.
- The block is the last thing emitted. Nothing follows the closing bullet.

## Frontmatter
Every Markdown file an agent writes opens with:

```yaml
agent: <agent-name>
date: YYYY-MM-DD
```

The destination repository's `CLAUDE.md` adds the fields its pages require.
