# visa-wage-data

Reusable tools for analyzing U.S. work-visa disclosure data — H-1B (LCA), PERM
(green-card labor certification), PW (prevailing-wage determinations), and H-2B —
from the Department of Labor's Office of Foreign Labor Certification (OFLC).

The scripts filter the (very large) DOL disclosure spreadsheets by employer,
worksite, or occupation, and join the PERM filings to the prevailing-wage file to
recover the wage amount and level. The organizing question the tooling supports:
**for a given sponsored role, how does the offered wage compare to the local
prevailing wage and median — i.e. is the wage evidence consistent with a genuine
talent shortage, or with paying the legal minimum?**

> Wage level is a market-position **proxy**, not proof about any individual. These
> programs and the practices they enable are **legal**; the point of the tooling is
> transparency about the public record, focused on employers, not workers. The data
> contains no worker names.

## What's here

```
visa-wage-data/
├── scripts/   reusable Python filters/joins over the DOL data
├── data/      raw DOL disclosure files + derived CSVs   (gitignored)
└── .venv/     python env (openpyxl)                     (gitignored)
```

## Data sources

All from DOL/OFLC disclosure data — https://www.dol.gov/agencies/eta/foreign-labor/performance

| File | What it is |
|------|-----------|
| `LCA_Disclosure_Data_FY####_Q4.xlsx` | H-1B labor condition apps (temporary). Wage level, worksite, offered/prevailing wage. |
| `PERM_Disclosure_Data_FY####_Q4.xlsx` | Green-card labor certs (permanent). Recruitment fields, tailored-requirement flags. |
| `PW_Disclosure_Data_FY####_Q4.xlsx` | Prevailing-wage determinations. Holds the wage AMOUNT + level the PERM file omits. |
| `H-2B_Disclosure_Data_FY####_Q4.xlsx` | Temporary seasonal non-ag (landscaping, hospitality, etc.). |

The Q4 file is cumulative for the fiscal year. Real download hrefs carry a `_Q4`
suffix under `dol.gov/sites/dolgov/files/ETA/oflc/pdfs/`. Financials for public
employers come from their 10-K / earnings; live job postings from company job
boards (Greenhouse/Ashby public APIs).

## Reproduce

```bash
python3 -m venv .venv && ./.venv/bin/pip install openpyxl
# download the FY24/FY25 LCA, PERM, PW, H-2B xlsx into data/ (see table above)

# any employer's H-1B roles:
./.venv/bin/python scripts/filter_employer.py "acme corp" \
    data/out.csv data/LCA_FY2025.xlsx data/LCA_FY2024.xlsx

# any employer's green-card roles + recruitment red-flag fields:
./.venv/bin/python scripts/filter_perm.py "acme corp" \
    data/out_perm.csv data/PERM_FY2025.xlsx data/PERM_FY2024_newform.xlsx

# recover the prevailing-wage amount/level PERM omits (join PERM -> PW):
./.venv/bin/python scripts/join_perm_pw.py "acme corp" CO \
    --perm data/PERM_FY2025.xlsx data/PERM_FY2024_newform.xlsx \
    --pw   data/PW_FY2025.xlsx data/PW_FY2024.xlsx

# all roles seated in specific cities:
./.venv/bin/python scripts/filter_worksite.py CO "denver,boulder" \
    data/out_cities.csv data/LCA_FY2025.xlsx data/LCA_FY2024.xlsx

# every visa filing at one worksite ZIP, across programs:
./.venv/bin/python scripts/zip_lookup.py 80202
```

## Scripts

| Script | Does |
|--------|------|
| `filter_employer.py` | LCA (H-1B) filings for an employer (regex over name/DBA) |
| `filter_perm.py` | PERM filings for an employer, incl. recruitment red-flag fields (handles old/new form schema) |
| `filter_worksite.py` | LCA filings by worksite state + city list |
| `join_perm_pw.py` | Join PERM → PW to recover prevailing-wage amount + level |
| `zip_lookup.py` | All filings (LCA/PERM/H-2B) at a worksite ZIP |
| `h2b_colorado.py` | H-2B seasonal analysis (template; edit the state) |
| `correlate_postings.py` | Match LCA roles to live job-board postings + salary bands (template) |

## Notes / gotchas

- The Q4 file is the full fiscal year (cumulative). If a guessed URL 404s, grab the
  real `_Q4` href from the OFLC performance page.
- PERM **old form ≠ new form** schema (FY2024 ships both); `filter_perm.py` matches
  columns by name.
- PERM's new form has **no prevailing-wage amount** — join to the PW file on
  `JOB_OPP_PWD_NUMBER == PW.CASE_NUMBER`.
- The disclosure data only ever shows the **visa-sponsored** slice of an employer's
  workforce — which for some industries (e.g. meatpacking floor labor) is near zero.
