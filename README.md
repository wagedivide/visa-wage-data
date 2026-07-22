# H-1B Colorado

A data investigation into how Colorado employers — especially large, profitable
technology firms — use the H-1B and PERM (green-card) programs. The organizing
question: **when a company sponsors a foreign worker, could a U.S. worker
plausibly have filled the role — and is the wage evidence consistent with
cost-cutting rather than a genuine talent shortage?**

The one public signal that speaks to this is the **prevailing wage level** an
employer assigns each role. Levels 1–2 sit below the local median wage; a heavy
tilt toward them (or paying the exact floor) is the clearest public sign a role
is routine and cost-driven rather than a scarce specialty.

> **Framing discipline (read before publishing anything):** Floor-wage
> sponsorship and tailored PERM recruitment are **legal**. Wage level is a
> market-position *proxy*, not proof any specific American was passed over. The
> accountability target is the **employer's process**, never individual visa
> holders (the data contains no worker names anyway). Say "legal but engineered,"
> not "fraud" — unless a specific finding supports the stronger word.

## What's here

```
visa-wage-data/
├── scripts/          reusable Python filters/joins over the DOL data
├── data/             raw DOL disclosure files + derived CSVs   (gitignored)
├── evidence/         primary-source captures, e.g. newspaper ads (gitignored)
├── artifacts/        shareable HTML reports (statewide + per-employer)
├── docs/             NEXT_STEPS.md and working notes
└── .venv/            python env (openpyxl)                     (gitignored)
```

### Artifacts (published)
- `artifacts/statewide-brief.html` — CO top sponsors + the wage-level framework
- `artifacts/ibotta-case-study.html` — the clean-actor counter-example
- `artifacts/charter-case-study.html` — the flagship: two-stage (H-1B floor wage →
  PERM engineered recruitment), with primary-source ad

Published URLs (claude.ai artifacts):
- Statewide: https://claude.ai/code/artifact/25d85382-90ff-47b9-ba36-056c32fbc7f7
- Ibotta:    https://claude.ai/code/artifact/e3949c86-9dcd-4251-b4e9-94a03d2b6ead
- Charter:   https://claude.ai/code/artifact/63e6429a-0aae-46c3-ba1e-f187b4bcbfed

## Data sources

All from the DOL Office of Foreign Labor Certification (OFLC) disclosure data —
https://www.dol.gov/agencies/eta/foreign-labor/performance

| File | What it is |
|------|-----------|
| `LCA_Disclosure_Data_FY####_Q4.xlsx` | H-1B labor condition apps (temporary). Wage level, worksite, offered/prevailing wage. |
| `PERM_Disclosure_Data_FY####_Q4.xlsx` | Green-card labor certs (permanent). Recruitment fields, tailored-requirement flags. |
| `PW_Disclosure_Data_FY####_Q4.xlsx` | Prevailing-wage determinations. Holds the wage AMOUNT + level the PERM file omits. |

The Q4 file is cumulative for the fiscal year. Real download hrefs carry a `_Q4`
suffix and live under `dol.gov/sites/dolgov/files/ETA/oflc/pdfs/`. Financials for
public employers come from their 10-K / earnings; live job postings from company
job boards (Greenhouse/Ashby public APIs).

## Reproduce

```bash
python3 -m venv .venv && ./.venv/bin/pip install openpyxl
# download the FY24/FY25 LCA, PERM, PW xlsx into data/ (see table above)

# any employer's H-1B roles:
./.venv/bin/python scripts/filter_employer.py "charter communications" \
    data/charter.csv data/LCA_FY2025.xlsx data/LCA_FY2024.xlsx

# any employer's green-card roles + recruitment red flags:
./.venv/bin/python scripts/filter_perm.py "charter communications" \
    data/charter_perm.csv data/PERM_FY2025.xlsx data/PERM_FY2024_newform.xlsx

# recover the prevailing-wage amount/level PERM omits (join to PW):
./.venv/bin/python scripts/join_perm_pw.py "charter communications" CO \
    --perm data/PERM_FY2025.xlsx data/PERM_FY2024_newform.xlsx \
    --pw   data/PW_FY2025.xlsx data/PW_FY2024.xlsx

# all H-1B roles seated in specific cities:
./.venv/bin/python scripts/filter_worksite.py CO "denver,boulder" \
    data/co_den_bou.csv data/LCA_FY2025.xlsx data/LCA_FY2024.xlsx
```

## Headline findings (FY2024–25)

- **Charter Communications** — CO's #1 sponsor. 134 H-1B roles, **94% paid the
  exact prevailing-wage floor** (median premium +0.0%). 113 CO green-card filings,
  **71% with requirements exceeding the occupational norm**, 40 atop attested area
  layoffs. On **$4.3B free cash flow** — affordability is not the constraint.
  The PERM roles are *browseable* on jobs.spectrum.com but engineered via tailored
  requirements + floor wage. Primary-source Denver Post ad captured.
- **Ibotta** — the counter-example. 4 total filings, paid at market, hires locally
  (11/11 live eng openings in Denver). A rich company that simply doesn't lean on
  the program.
- **Policy** — S.2928 (H-1B & L-1 Visa Reform Act of 2025) targets exactly the
  floor-wage loophole; no Colorado senator is on it.

See `docs/NEXT_STEPS.md` for where to pick up.
