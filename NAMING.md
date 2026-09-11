# Volar Robotics — Naming Convention

> **Scope.** Every naming rule at Volar lives here. `AGENTS.md`, repository
> `CLAUDE.md` files, and personal configuration link here and state no rule of
> their own. A rule written twice is a bug in the copy outside this file.
> Applies to GitHub, Slack, Drive, the wiki, calendars, and local work.

## Core
- **Canonical slug.** One lowercase ASCII slug per program, product, client, and
  platform, reused verbatim on every surface, never abbreviated, expanded, or
  re-cased: `soar-ndt`, `acme-air`, `minithex`. The proper-name form
  (*Acme Air*) is for prose and meeting titles only. Retiring or changing a
  slug is a `vault/decisions/` entry.
- **Separator law.** `-` joins words inside a field, `_` joins fields:
  `2026-09-09_acme-air_report.pdf`.
- Dates are ISO `YYYY-MM-DD`, and are a field.
- Date first when the file is one of a recurring series (reports, meetings,
  invoices, digests, runs); topic first otherwise.
- Lowercase. No spaces, accents, `&`, parentheses, `copy` / `final` / `v2` / `(1)` suffixes,
  or two names differing only by case.

## snake_case
Only where a tool requires an identifier: Python and MATLAB modules, functions,
and variables; YAML and JSON keys; environment variables as `SCREAMING_SNAKE`.
- Every `.py` and `.m` file, since a kebab module cannot be imported.
- A directory only if it contains `__init__.py`; every other directory is kebab.

## GitHub
- Repository: `<slug>[-<component>]`, no `volar-` prefix, no verbs. Component
  from `sim | report | paper | web | fw | hw | data`.
- Branch: `<type>/<kebab-slug>`. `claude/` is reserved for agents; default `main`.
- Commit and PR title: `<type>(<scope>): <description>`, imperative, lowercase,
  no trailing period. Types: `feat | update | fix | lint | chore | refactor`.
  Scope is the primary affected directory.
- Layout: `src/<package_name>/` with `pyproject.toml` at the root; LaTeX figures
  in `figs/`; generating code in `scripts/` or `matlab/`; preamble macros in
  `macros.tex`; top-level document `main.tex` → `main.pdf`, or named for its slug
  where a repository builds several.

## Slack
- Channel name is the slug: `#soar-ndt`.
- Reserved prefixes, and the only ones: `all-` org-wide, `ext-` external members,
  `agent-` automated output.
- Channels another organization created keep the name it gave them.

## Drive
- Top-level `NN_function/` folders are frozen (`00_corporate` … `09_data`). The wiki
  Source Map resolves against them. The numeric prefix is a sort key and the one
  exception to the separator law.
- Subfolders are the slug.
- Files follow the separator law, corrected at filing time:
  `GCITD0007594019.pdf` → `2026-09-09_google-workspace_invoice.pdf`.
- An external identifier of record survives as a trailing field:
  `2026-09-09_slack_invoice_sbie-12598087.pdf`.

## Wiki vault
- `<type>_<slug>.md`, where the type is a field: `funding-call_acme-oc2.md`.
- Types, and the only ones: `person · competitor · partner · university ·
  prospect · funding-call · paper · digest · recap-meeting · bom · dataset ·
  brand · company · voucher · pitch · website`.
- `concepts/`, `decisions/`, `market/`, `legal/`, `products/` take no prefix,
  because the directory is the type, so a single kebab slug.
- After the prefix the remainder is one kebab field
  (`bom_minithex-recommended-diff.md`); a trailing date or year stays its own
  field (`paper_cordova-bulens_2023.md`).

## Meetings
- Title: `Volar <> Acme`, `Volar <> Accounting`. Volar left, counterparty or
  internal function right.
- `<>` is for calendar titles and channel topics only, never a filename or URL.
  Derived artifacts drop it: `2026-09-09_volar-acme_notes.md`.
- Invitations another organization created keep their title.

## Datasets and runs
`YYYY-MM-DD_<platform>_<what>[_<run>]`, run index zero-padded, present only when
a date carries more than one: `2026-03-25_minithex_imu-calib_02.json`.

## Adoption
Correct a name when the file is touched, when it is filed into Drive, or in a
recorded rename pass. Do not rename where it would break a live external
reference (a signed contract, a published URL). Note the exception instead.

`scripts/check_naming.py` checks a checkout on demand (filenames, branch, PR title).
It is not wired into CI. Vendored and upstream trees are exempted per repository
via `.namingignore`.
