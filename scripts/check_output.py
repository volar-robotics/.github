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


# Inline code and quoted material are literals, not this document's own prose.
LITERAL = re.compile(r"`[^`]*`|\"[^\"]{0,200}\"")

for path in sys.argv[1:]:
    lines = list(prose_lines(Path(path).read_text(errors="ignore")))
    body = LITERAL.sub(" ", "\n".join(lines))
    hits = {}
    for name, rx in CHECKS.items():
        n = sum(1 for l in lines if rx.match(l)) if rx.pattern.startswith("^") else len(rx.findall(body))
        if n:
            hits[name] = n
    n = long_paragraphs(lines)
    if n:
        hits["para>5"] = n
    print(f"{path}: " + ("  ".join(f"{k}={v}" for k, v in sorted(hits.items())) if hits else "clean"))
