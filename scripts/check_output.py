"""Check Markdown prose against OUTPUT.md. Reports counts; it does not gate."""

import re
import sys
from pathlib import Path

# Titles, fenced blocks and inline code carry literal formats and typography,
# which OUTPUT.md exempts. The Forbidden constructions table quotes the very
# constructions it bans, so its rows are skipped too.
CHECKS = {
    "em-dash":      re.compile(r"—"),
    "antithesis":   re.compile(r"\b(?:not|isn't|is not|aren't)\s+[^,.;:|]{2,45},\s*(?:but|it's|it is)\b", re.I),
    "self-comment": re.compile(r"\b(?:it's worth noting|worth noting|importantly|note that|let me|here's the thing|the key insight)\b", re.I),
    "inflated":     re.compile(r"\b(?:delve|leverag\w*|cutting-edge|state-of-the-art|revolutionar\w+|holistic)\b", re.I),
    "hedge-stack":  re.compile(r"\b(?:might|could|may|can)\s+potentially\b", re.I),
    "british":      re.compile(r"\b\w*(?:colour|behaviour|optimis|organis|analyse|analysing|recognis|favour|fibre)\w*\b", re.I),
    "heading-4":    re.compile(r"^#{4,}\s"),
    "deep-bullet":  re.compile(r"^(?: {4,}|\t{2,})[-*+]\s"),
}


def prose_lines(text):
    """Yield lines outside code fences, titles and the forbidden-constructions table."""
    fence = skip = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if line.startswith("## "):
            skip = line.strip() == "## Forbidden constructions"
        if fence or skip or line.startswith("# "):
            continue
        yield line


def long_paragraphs(lines, limit=5):
    """Count prose runs past *limit* lines, ignoring lists, tables and headings."""
    count = run = 0
    for line in lines:
        if line.strip() and not re.match(r"^\s*(?:[-*+>|#\d]|\[)", line):
            run += 1
            if run == limit + 1:
                count += 1
        else:
            run = 0
    return count


# An identifier, path, flag or value is a literal per OUTPUT.md's own inline-code
# rule, and such a span never has internal whitespace — so only a whitespace-free
# backtick span is exempt. A multi-word one is an illustrated example of real
# output (a commit message, a log line) and stays subject to the checks below;
# exempting it hid several em-dashes that agents would have reproduced verbatim.
# Quoted material (a literal string an agent emits, e.g. "None") stays exempt.
LITERAL = re.compile(r"`\S+`|\"[^\"]{0,200}\"")


def slack_blocks(text):
    """Yield each SLACK_SUMMARY block as its list of bullet lines.

    A block may be a live message (sentinel is the last thing emitted) or a
    template embedded in a larger doc (e.g. a repo CLAUDE.md), so a block ends
    at the first non-bullet line rather than at end of file.
    """
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].strip() == "SLACK_SUMMARY":
            j = i + 1
            bullets = []
            while j < len(lines) and lines[j].lstrip().startswith("•"):
                bullets.append(lines[j])
                j += 1
            yield bullets
            i = j
        else:
            i += 1


def slack_violations(text):
    """Count Slack blocks over the 800-char cap.

    Whether a block *should* lead with a 🟢/🟡 verdict bullet depends on
    whether it has a fact worth triaging at all (OUTPUT.md), which a regex
    can't judge — so only the unconditional length cap is checked here.
    """
    hits = {}
    for bullets in slack_blocks(text):
        if len("\n".join(bullets)) > 800:
            hits["slack-over-800"] = hits.get("slack-over-800", 0) + 1
    return hits


for path in sys.argv[1:]:
    text = Path(path).read_text(errors="ignore")
    lines = list(prose_lines(text))
    body = LITERAL.sub(" ", "\n".join(lines))
    hits = {}
    for name, rx in CHECKS.items():
        n = sum(1 for l in lines if rx.match(l)) if rx.pattern.startswith("^") else len(rx.findall(body))
        if n:
            hits[name] = n
    n = long_paragraphs(lines)
    if n:
        hits["para>5"] = n
    hits.update(slack_violations(text))
    print(f"{path}: " + ("  ".join(f"{k}={v}" for k, v in sorted(hits.items())) if hits else "clean"))
