# Next steps — pick up here

_Last updated: 2026-07-21_

## Where we are

The **Charter case study is publish-ready** — a complete, primary-sourced,
honestly-framed story: floor-wage H-1B + engineered PERM recruitment, against
$4.3B free cash flow, with the actual Denver Post ad and wages matching the DOL
filings to the dollar. Ibotta is the clean counter-example. The data pipeline is
reusable on any employer.

**Solid (our own data):** LCA floor-wage (94%), PERM volume + recruitment
red-flags, primary-source ad, public financials, policy context.

**Still thin (caveated in the artifacts):**
- Per-employer "below median" leans on EPI's *national* FY2019 proxy — no
  statewide CO wage-level slice computed yet.
- PERM↔PW wage join only matched **26/113 (23%)** — most Charter PWD determination
  numbers predate the FY2024–25 PW files.
- "Could a citizen fill it" is inherently a judgment; we make no
  individual-displacement claim (and shouldn't).

## Decision pending

Four non-exclusive directions. Recommended order: **Publish first**, then layer on.

### 1. Publish / go live  *(recommended first)*
- Push this repo public on GitHub (methodology + scripts = the credibility anchor
  that lets journalists cite and verify).
- Ship the Charter case study as the flagship; statewide brief as context.
- Draft the first Substack post from the Charter material. Lead with the
  differentiators nobody else combines: **employer × financials**, **CO/local
  angle**, **honest non-partisan framing**.
- Keep the per-employer HTML "cards" as the shareable unit (one screenshot travels
  better than an essay).

### 2. Deepen the data
- **Download FY2023 PW** (`PW_Disclosure_Data_FY2023_Q4.xlsx`) and re-run
  `join_perm_pw.py` → lifts the 23% wage match toward full coverage (most Charter
  PWDs are 2023). This confirms whether the *green-card* wages floor-hug like the
  H-1B ones (preliminary: 73% of the matched 26 did).
- **Statewide CO wage-level slice** from the raw LCA `PW_WAGE_LEVEL` column →
  replaces the EPI national proxy with real Colorado numbers. Fixes the biggest
  caveat in the statewide brief.
- **Rank all CO employers** by "affordable + below-median" to auto-surface the next
  Charters instead of picking by hand.

### 3. Broaden the cases
- Run 2–3 more big CO filers through the same pipeline to show the pattern is
  systemic, not one company. Candidates: **Western Union**, **DISH / EchoStar**,
  **Comcast**, **Visa**. Each ~30 min with the existing scripts.

### 4. Outreach / collaborate
- **EPI / Ron Hira** (own the wage-level framework; would likely engage a rigorous
  data collaborator).
- **h1bdatawatch.com** (journalist-facing, no-code).
- **Local press** — Colorado Sun, Denverite, Denver Post — the local hook national
  desks ignore.
- **jobs.now** — the activist/job-seeker side; you'd be the complementary data side.

## Concrete open threads (small, ready to grab)

- **More primary-source ads.** Method proven: NewsBank "Denver Post Collection" →
  *Image* edition (2017–current) has the classified/recruitment ads. Access via a
  Colorado library card through the Marmot proxy. Download button →
  `~/Downloads` → move into `evidence/`. Peak Sundays still to grab (from
  `data/charter_denverpost_worksheet.csv`): 2023-08-13 (16 ads), 2023-11-12 (16),
  2023-11-05 (11), 2023-07-16 (15).
- **Scrape the worksheet dates** systematically for the full 54-Sunday ad set.
- **Embed the ad image** into the Charter artifact as a data-URI (currently the ad
  is quoted as text; the image lives in `evidence/`).

## Key facts to remember

- **Charter does NOT use antiquated mail-in.** Its PERM roles are *browseable* on
  jobs.spectrum.com (e.g. live req 2026-76226, "Principal Engineer II — Multiple
  Openings," same boilerplate "negotiations begin at $174,068.76", stacked
  10y/5y/2y tailored reqs). The charge is **tailored requirements + floor wage on
  a browseable posting**, not hidden jobs. Do not lean on the jobs.now mail-in
  framing for Charter.
- **Green-card revocation** for PERM sham is legally possible but rare and
  equitably fraught — the fraud is the employer's, not the worker's. Enforcement
  targets employers (debarment, DOL Project Firewall).
- **Recruitment reports** (why each U.S. applicant was rejected) are NOT public
  (not in disclosure data, FOIA-exempt). Only the published *ads* are recoverable.

## Data provenance / gotchas

- DOL disclosure files: Q4 = full FY (cumulative). Real hrefs have `_Q4` suffix;
  grab them from the performance page via the browser if a guessed URL 404s.
- PERM **old form ≠ new form** schema (FY2024 has both files); `filter_perm.py`
  handles it by matching columns by name.
- PERM new form has **no prevailing-wage amount** — must join to the PW file on
  `JOB_OPP_PWD_NUMBER == PW.CASE_NUMBER`.
- Aggregators (h1bgrader, myvisajobs) Cloudflare-block scripted fetches; the DOL
  primary files do not.
