# Volar Robotics — Coding Standard

> **Scope.** Artifacts that are code, configs, or compiled documents. States no
> name (see [NAMING.md](NAMING.md)), no agent behavior rule (see
> [BEHAVIOR.md](BEHAVIOR.md)), and no prose form (see [OUTPUT.md](OUTPUT.md)),
> each of which binds this work too.

## Code Quality
- Comments: minimal and information-dense. Comment the WHY, never the WHAT.
  No obvious, explanatory, or tutorial-style commentary. Never narrate edit
  history ("added for X", "changed to fix Y"), which belongs in the commit
  message. Any comment that survives must explain why the code exists to a
  reader with zero prior context.
- Structure: small functions, single responsibility, explicit data flow.
  Simple, explicit logic: avoid deep nesting, hidden side effects, and magic
  behavior. Prioritize clarity and interpretability over compactness or
  elegance. Assume a competent technical reader.
- No unnecessary complexity: avoid advanced patterns, decorators, factories,
  metaprogramming, and heavy exception handling.
- Research-level minimalism: never add features, fallbacks, heuristics,
  defensive programming, or validation beyond what the task requires. Trust
  internal code and framework guarantees; validate only at system boundaries.
  Three similar lines beat a premature abstraction, so do not
  deduplicate code that merely looks similar but serves different purposes.
- Don't convert variable types or shapes unless strictly necessary.
- Consistency: match the repo's naming, imports, structure, logging, and error
  messages. Reuse existing helpers. Provide one-sentence docstrings for public
  functions and a single-line description at the top of each file.
- Never leave stubs, placeholder logic, or auto-generated boilerplate in code
  meant to run.

## Python
- Python 3.10+, managed via conda (`environment.yml`).
- Packaged with `pyproject.toml` and setuptools; layout per NAMING.md.
- Formatter/linter: ruff (double quotes, 120-char line length, space indent).
- Standard ruff rules: E, W, F, I (isort), UP, B, SIM, RUF. Ignore E501
  and SIM108.
- Run `ruff check` and `ruff format` before committing.

## LaTeX
- One sentence per line (enables clean diffs).
- Use `\cref{}` (cleveref) for cross-references, and `\Cref{}` at the start
  of a sentence, where the name is spelled out; never hardcode "Fig.",
  "Figure", "Eq.", or "Sec." manually.
- Units: `\qty{value}{unit}` from siunitx, built from unit macros so that
  compound units print as products of powers:
  `\qty{2}{\newton\meter\per\radian}`.
- Prefer vector formats (`.pdf`, `.eps`) for plots; raster (`.png` at
  300 dpi) only for photographs or screenshots.
- Equations: align on the `=` sign using `align` or `IEEEeqnarray`.
- Keep preamble macros in a separate file (see NAMING.md); avoid redefining
  standard commands.

## .gitignore
```
# OS / editor
.DS_Store
Thumbs.db
desktop.ini
.vscode/
.idea/
*.swp
*~

# Secrets — never commit
.env
*.env

# Python cache
__pycache__/
*.py[cod]
.ruff_cache/
.mypy_cache/
.pytest_cache/

# Build / dist
*.egg-info/
dist/
build/

# Jupyter
.ipynb_checkpoints/

# Data and model outputs (use Drive or dedicated storage instead)
datasets/raw/
datasets/processed/
results/models/
wandb/

# LaTeX intermediates — track only source and final PDF
main.*
!main.tex
!main.pdf
*.aux
*.log
*.out
*.toc
*.lot
*.lof
*.bbl
*.blg
*.fls
*.fdb_latexmk
*.synctex.gz
*.synctex(busy)
# Beamer
*.nav
*.snm
*.vrb
# Minted / pygments cache
_minted-*/
*.pyg
# Overleaf sync
.overleaf/
```
Mirror the `main.*` / `!main.tex` / `!main.pdf` pattern for every top-level
compiled document, named per NAMING.md.

## Commits
Format and types: see [NAMING.md](NAMING.md).
