# CLAUDE.md — visa-wage-data

> **This repo is public.** This file is published with it. Keep it to neutral
> tooling guidance only: how the scripts work, data quirks, coding conventions.
> **Never** put employer names under analysis, findings, editorial framing,
> publishing strategy, or author identity in this file — those live elsewhere.

## What this is

Reusable Python tools over U.S. DOL/OFLC work-visa disclosure data (H-1B/LCA,
PERM, PW, H-2B). Scripts filter the large disclosure spreadsheets by employer,
worksite, or occupation, and join PERM filings to the prevailing-wage file. See
`README.md` for the full reproduce steps.

## Conventions

- **Python via the repo venv:** `./.venv/bin/python scripts/<name>.py …`
  (only dep is `openpyxl`). The venv and `data/` are gitignored.
- Scripts are **stream-oriented** (openpyxl `read_only=True`, row-by-row) because
  the source files are ~70–210 MB. Don't load whole sheets into memory.
- Each script is **standalone** (argv in, CSV/stdout out) — no shared imports, so
  they stay copy-pasteable. Match that style when adding one.
- Output CSVs go in `data/` (gitignored). Never commit derived data.

## Data quirks (bite every time)

- The `_Q4` disclosure file is **cumulative for the fiscal year** — use it alone
  for a full year. If a guessed URL 404s, get the real `_Q4` href from the OFLC
  performance page.
- **PERM old form ≠ new form** (FY2024 ships both files); resolve columns by name,
  not index. `filter_perm.py` shows the pattern.
- PERM's new form has **no prevailing-wage amount** — recover it by joining to the
  PW file on `JOB_OPP_PWD_NUMBER == PW.CASE_NUMBER` (`join_perm_pw.py`).
- Column names differ across programs (e.g. `EMPLOYER_NAME` vs `EMP_BUSINESS_NAME`,
  `WORKSITE_STATE` vs `PRIMARY_WORKSITE_STATE`). Resolve with a fallback lookup.
- H-2B wage lives in `BASIC_WAGE_RATE_FROM`; status strings are
  "Determination Issued - Certification", not "Certified".
- Disclosure data only shows the **visa-sponsored slice** of a workforce — near
  zero for some industries. Don't infer total employment from it.

## Framing note (applies to any analysis built on these tools)

Wage level is a market-position **proxy**, not proof about any individual. These
programs are **legal**. Analysis focuses on **employers and the public record**,
never on workers (the data has no worker names) or on private individuals who
appear as small-scale filers.
