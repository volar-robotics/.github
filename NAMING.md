# Volar Robotics — Naming Convention

> **Single source of truth.** Every naming rule at Volar Robotics lives in this
> file and nowhere else. `AGENTS.md`, repository `CLAUDE.md` files, the wiki,
> and personal configuration must *link* here, never restate a rule. If another
> document contradicts this file, this file wins and the other document is a bug.

Applies to every surface: GitHub, Slack, Google Drive, the wiki, calendars,
local working directories.

---

## 1. The canonical slug

Every program, product, client, platform, and organization has exactly **one
slug**: lowercase, ASCII, hyphen-separated, never abbreviated.

```
soar-ndt   soar-touch   doordash-air   minithex   digitac   volar-robotics
```

That one string is reused verbatim on every surface:

| Surface | Use |
|---|---|
| Repository | `doordash-air-sim` |
| Slack channel | `#doordash-air` |
| Drive folder | `07_engineering/doordash-air/` |
| Wiki page | `vault/products/doordash-air.md` |
| Branch | `feat/doordash-air-reel-model` |
| Document field | `2026-09-09_doordash-air_report.pdf` |

A slug is never shortened per surface (`dd-air`), never expanded (`doordash-aerial`),
and never re-cased (`DoorDash-Air`). Its proper-name form — used only in prose,
slide titles, and meeting titles — is written normally: *DoorDash Air*.

Retiring or renaming a slug is a decision recorded in `vault/decisions/`.

---

## 2. The separator law

Two separators, two meanings, no exceptions:

- **`-` joins words inside a field.**
- **`_` joins fields.**

```
2026-12-25_christmas-is-today.md
2026-09-09_doordash-air_report.pdf
bom_minithex-recommended-diff.md
2026-03-25_minithex_imu-calib_02.json
```

Everything is lowercase ASCII. No spaces, no accented characters, no `&`, no
parentheses.

**Field order.** Date first when the file is one instance of a recurring series —
meeting notes, reports, invoices, digests, calibration runs, datasets — because
chronological sort is the point. Topic first otherwise.

**Dates are always ISO 8601: `YYYY-MM-DD`.** Never `20260325`, never `25-03-2026`.
A date is a field, so it is bounded by `_`, and its internal hyphens are part of
the format rather than word separators.

---

## 3. When `snake_case` applies

`snake_case` is used **only where a language or tool requires a valid
identifier** — not for files in general:

- Python packages, modules, functions, variables
- MATLAB scripts, functions, variables
- YAML and JSON keys
- Environment variables, as `SCREAMING_SNAKE_CASE`

Everything else — any name a human reads as a name — follows the separator law
in §2.

A `.py` or `.m` file is always `snake_case`, wherever it sits: a kebab filename
cannot be imported, so there is no such thing as a "script that does not need to
be an identifier". A directory is `snake_case` only when it is an importable
package — one that contains `__init__.py`. Every other directory is kebab.

```
src/doordash_air/control/reel.py     # package + module: snake_case
scripts/plot_reel_response.py        # still a module: snake_case
gazebo/models/mrsim-minithex/        # not importable: kebab
docs/2026-09-09_doordash-air_report.md
```

---

## 4. Prohibited, everywhere

- Spaces in any filename
- `(1)`, ` 1`, `copy`, `final`, `FINAL`, `v2` — use a date field, or use git
- Uppercase outside acronyms in prose
- Accented or non-ASCII characters
- An abbreviation of an existing slug
- Two files whose names differ only by case

---

## 5. GitHub

**Repository.** `<slug>[-<component>]`. No `volar-` prefix — the organization
already scopes it. No verbs.

```
soar-ndt-report   doordash-air-sim   soar-touch-phynt   business-plan
```

Component comes from a closed vocabulary: `sim`, `report`, `paper`, `web`, `fw`,
`hw`, `data`. Adding a component word requires updating this list.

**Branch.** `<type>/<kebab-slug>`, where `<type>` is a commit type from below.
`claude/` is reserved for agent-generated branches. Default branch is `main`.

```
fix/website-claims-vault-crosscheck
feat/doordash-air-reel-model
```

**Commit.** `<type>(<scope>): <description>`

Types: `feat` · `update` · `fix` · `lint` · `chore` · `refactor`
Scope: the primary affected directory. Description: imperative, lowercase, no
trailing period.

```
feat(scripts): add eval_cnn for per-sample predictions
fix(ingest): batch Drive PDFs by token cost, not just encoded byte size
```

**Pull request title.** Identical format to a commit. A PR titled
`Rework workplan` is out of convention.

**Repository layout.**

- Python: `src/<package_name>/`, with `pyproject.toml` at the root
- LaTeX figures: `figs/` — not `figures/`
- Figure-generating code: `scripts/` for Python, `matlab/` for MATLAB
- LaTeX preamble macros: `macros.tex`
- The top-level compiled document is `main.tex` → `main.pdf`, unless the
  repository builds several, in which case each is named for its slug

---

## 6. Slack

Channel name is the canonical slug: `#soar-ndt`, `#doordash-air`.

Reserved prefixes, and the only ones:

| Prefix | Meaning |
|---|---|
| `all-` | org-wide announcement channel |
| `ext-` | Slack Connect, external members present |
| `agent-` | automated output, no human conversation expected |

Channels created by an external organization keep the name that organization
gave them. We do not rename someone else's channel.

---

## 7. Google Drive

**Top-level folders are frozen** at their numbered function-first names. The wiki
Source Map resolves against them; renaming one is a coordinated change, not a
cleanup.

```
01_ip  02_legal  03_finance  04_funding  05_research
06_strategy  07_engineering  08_comms  09_data
```

The numeric prefix is a sort key, not a field, and is the one sanctioned
exception to §2.

**Subfolders** use the canonical slug, lowercase kebab: `07_engineering/doordash-air/`.

**Files** follow the separator law. Vendor- and tool-generated names are renamed
at filing time — that is the point at which a document enters our record:

```
GCITD0007594019.pdf              → 2026-09-09_google-workspace_invoice.pdf
VOLAR ROBOTICS CONCEPT.docx      → 2026-07-21_volar-robotics_concept.docx
Professional_Services_Agreement_-_Volar_Robotics_S.r.l.._-_20260707.pdf
                                 → 2026-07-07_doordash_psa.pdf
```

A file whose name is an external identifier of record — a signed contract, a
filed tax document — keeps that identifier as a trailing field rather than
losing it:

```
2026-09-09_slack_invoice_sbie-12598087.pdf
```

---

## 8. Wiki vault

Page filename: `<type>_<slug>.md`, where `<type>` is the node type and `<slug>`
is the canonical slug or a descriptive kebab slug. Both are fields, so the type
is separated by `_` and its own words by `-`.

```
vault/entities/person_antonio-rapuano.md
vault/entities/funding-call_autoassess-oc2.md
vault/entities/competitor_voliro.md
vault/sources/recap-meeting_2026-07-23.md
vault/sources/paper_zhang-xiaodong_2026.md
vault/concepts/aerial-cable-manipulation.md
vault/products/soar-ndt.md
```

Type prefixes in use, and the only ones: `person` · `competitor` · `partner` ·
`university` · `prospect` · `funding-call` · `paper` · `digest` · `recap-meeting` ·
`bom` · `dataset` · `brand` · `company` · `voucher` · `pitch` · `website`.

`vault/concepts/`, `vault/decisions/`, `vault/market/`, `vault/legal/`, and
`vault/products/` carry no type prefix — the directory is the type — so their
filenames are a single kebab slug.

After the type prefix the descriptive remainder is a single kebab field, so
`bom_minithex-recommended-diff.md` — not a chain of `_`-separated fields. A
trailing date or year is the exception and stays its own field.

Papers are `paper_<surname>_<year>.md`; a multi-part surname is one field:
`paper_cordova-bulens_2023.md`. Where two papers collide, the given name joins
the surname field: `paper_zhang-xiaodong_2026.md`.

Wikilinks use the path without extension and must resolve: `[[vault/products/soar-ndt]]`.

---

## 9. Meetings and calls

Human-facing meeting titles use `<>` to mean *between*:

```
Volar <> DoorDash
Volar <> Accounting
Volar <> UTwente
```

`Volar` is always on the left. The right side is the counterparty in proper-name
form, or the internal function for a recurring internal call. `<>` appears only
in calendar titles and channel topics — never in a filename or a URL, where the
characters are illegal or unreadable.

Artifacts derived from a meeting drop the operator and use the separator law:

```
2026-09-09_volar-doordash_notes.md
2026-07-23_volar-utwente_recap.pdf
```

Invitations created by an external organization keep their title. We rename only
what we own.

---

## 10. Datasets and experimental runs

```
YYYY-MM-DD_<platform>_<what>[_<run>]
```

```
2026-03-25_minithex_imu-calib_02.json
2026-07-14_digitac_tactile-capture.zip
```

The run index is zero-padded to two digits and only present when a date carries
more than one run.

---

## 11. Adopting this convention

Existing names are corrected on three occasions: when the file is touched for
another reason, when it is filed into Drive, and when a dedicated rename pass is
run and recorded. A rename that would break a live external reference — a signed
contract path, a published URL — is not performed; the inconsistency is noted
instead.
