---
title: "The Company Made $4.3 Billion. It Paid Its Engineers the Legal Minimum."
subtitle: "Charter Communications is Colorado's largest H-1B sponsor. Public data shows it pays the exact prevailing-wage floor on 94% of its Colorado roles — then certifies to the government that no qualified American was available."
date: 2026-07-21
tags: [h1b, perm, colorado, labor, charter, data]
status: draft
---

On Sunday, August 6, 2023, on page 4 of the Denver Post's Business section, wedged
between ads for child care and a Garage Sale, ran this:

> **Charter Communications, Inc.** in Greenwood Village, CO seeks Principal
> Engineer I (mult openings) to be resp for eng actvties that mintain & enhance
> the compny's telcommunications & signl procssing hrdware, SW, & elctrical sys …
> negotiations bgn at **$121,222/yr.** Ref. code 2023-18518.

Telegraphic, abbreviated, easy to skim past. It was one of at least nineteen
Charter recruitment ads in that single Sunday edition. And that $121,222 figure is
not a number Charter picked. It is the **prevailing wage** — the legal *minimum*
the U.S. Department of Labor allows an employer to pay a foreign worker for that
job, in that place, at that experience level.

Charter offered the minimum. Not a dollar more. And it does this almost every
time.

## The pattern, not the anecdote

I pulled the Department of Labor's public disclosure data — every H-1B and
green-card filing, employer by employer — and filtered it to Charter's Colorado
worksites for fiscal years 2024 and 2025. (The code and data are linked at the
bottom; anyone can re-run it.)

Charter is **Colorado's #1 H-1B sponsor.** Across those two years it filed **134
H-1B roles** in the state, almost all at one Greenwood Village hub. Here is what
the wages look like against the legal floor:

- **126 of 134 (94%)** were paid *within half a percent* of the prevailing wage.
- The **median premium over the floor was 0.0%.**
- Charter almost never pays an H-1B worker a cent above the minimum the rules
  permit.

These aren't call-center jobs. They're Principal Engineers, Network Engineers,
Software Engineers — the roles that supposedly justify reaching abroad for scarce
talent. A third of the ones with a wage level assigned sit *below* the local
median wage for the occupation.

## Then it makes them permanent

The H-1B is temporary. To keep a worker, an employer sponsors a **green card**
through a process called PERM — and PERM comes with a catch the H-1B doesn't. The
employer must **test the U.S. labor market** and certify to the government that it
found *no able, willing, qualified American* for the job.

That Denver Post ad? It's the labor-market test. Charter is legally required to
advertise the role, and if a qualified American applies, it must hire them instead
of proceeding with the sponsorship.

In FY2024–25, Charter filed **113 green-card labor certifications** for Colorado
roles. Two things stand out in the data:

- **71%** carried job requirements that **exceed the normal level** for the
  occupation — an unusual stack of specific skills and exact year-counts that
  narrows the qualified pool. (Legal, if justified by "business necessity." Also
  the recognized way to write a job description that fits one particular person.)
- **40** were filed atop an **attested layoff** in the same area and occupation —
  certifying "no American available" in a labor market where Charter had recently
  cut jobs.

And the wage on these permanent roles? The same floor. When I joined the filings
to the government's prevailing-wage file, the green-card roles hugged the minimum
just like the H-1B ones.

## Here's the part that makes it a choice

The standard defense is: *it's legal, and $121,000 isn't a low salary.* Both true.
So let me show you why neither settles it.

Charter Communications, fiscal year 2024:

| | |
|---|---|
| Revenue | **$55.1 billion** |
| Net income | **$5.1 billion** |
| Free cash flow | **$4.3 billion** |
| Gross margin | 86% |

Paying every one of its 134 Colorado H-1B roles **20% above the floor** would cost
roughly **$3.5 million a year** — less than **one-tenth of one percent** of Charter's
free cash flow. For a company generating $4.3 billion in cash, sourcing talent at
market rates instead of the legal minimum is a rounding error.

So the floor wage isn't a constraint. It's a **decision.** The company can
trivially afford to pay more, or to widen its net to recruit locally at a
competitive wage. It chooses the minimum, at volume, and certifies that no
American was available.

## What this is — and what it isn't

I want to be precise, because this subject rewards precision and punishes hype.

**This is legal.** Paying the prevailing wage is compliant. Writing demanding job
requirements is compliant. Running newspaper ads is *required.* Nothing here is an
accusation of fraud.

**It is not a story about the workers.** The visa holders didn't write the rules
or the job descriptions. The public data contains no worker names, and it
shouldn't. The subject is the **employer's process**, not any individual.

**Wage level is a proxy, not proof.** A floor wage strongly suggests a role is
routine and cost-driven rather than a genuine scarcity — but it can't prove that
any specific American was passed over. I'm showing you a pattern, not a verdict.

And to be fair to Charter on one point: its green-card roles *are* listed on its
normal careers site — they're findable, not hidden in a PO box. The engineering
isn't concealment. It's the **tailored requirements and the floor wage** on a
posting anyone can read.

## The control group

If floor-wage sponsorship were just "how tech hiring works," every profitable
company would do it. They don't.

I ran the same analysis on **Ibotta**, a profitable Denver tech company (it IPO'd
in 2024). Ibotta filed **four** H-1B roles in two years — two of them the same
position — and paid them at its own published market rates. Every one of its
current engineering openings is in Denver. A rich company that simply doesn't lean
on the program.

The difference between Ibotta and Charter isn't affordability. Both can pay
whatever they want. The difference is what they *do* with that freedom.

## Why it matters now

There's a bill in the Senate right now — the H-1B & L-1 Visa Reform Act of 2025 —
written to close exactly this loophole by requiring employers to pay the higher of
the prevailing wage or the local median. It has five sponsors and neither of
Colorado's senators, in the state with the sharpest floor-wage hub in this
analysis.

I think the wage floor is the most honest, least partisan lens on the H-1B debate.
It isn't about whether immigration is good or bad. It's about whether the biggest,
richest employers are using a public program to hire specialized talent — or to
hold labor costs at the legal minimum because the rules let them.

The data says, for Charter in Colorado, it's the second one.

---

**How I know this.** Everything above comes from public U.S. Department of Labor
disclosure data (H-1B/LCA, PERM, and prevailing-wage files), Charter's own SEC
filings and earnings, and the Denver Post archive. The full methodology, the
scripts, and the reproducible pipeline are here:
**github.com/reagent/h1b-colorado**. Re-run it, check my math, or point it at your
own employer.

*This is the first in a series analyzing how Colorado employers use the H-1B and
green-card programs. Next: how to read the data yourself — and check any company
in ten minutes. If you have a lead on an employer worth a look, reply to this
email.*

*[ Subscribe ] to get the next one.*
