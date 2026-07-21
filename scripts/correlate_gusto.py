#!/usr/bin/env python3
"""Correlate Gusto LCA filings (FY24-25) with current Greenhouse job postings.

For each LCA role, find the closest live posting by title-token overlap, then
compare the LCA offered wage against the posting's salary band and against the
LCA prevailing wage. No PII involved — this shows whether the sponsored role
maps to a real advertised opening and how pay lines up.
"""
import csv
import html
import json
import re
from difflib import SequenceMatcher

LCA = "data/gusto.csv"
GH = "data/gusto_greenhouse.json"

STOP = set("the a an of and for to at in on with & , - / senior sr staff principal "
           "ii iii iv i lead".split())


def toks(s):
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return {w for w in s.split() if w and w not in STOP}


def bands(content):
    t = re.sub(r"<[^>]+>", " ", html.unescape(content or ""))
    nums = [int(x.replace(",", "")) for x in re.findall(r"\$\s?(\d{2,3},\d{3})", t)]
    nums = [n for n in nums if 40000 <= n <= 600000]
    return (min(nums), max(nums)) if nums else None


def load_postings():
    d = json.load(open(GH))
    out = []
    for jb in d["jobs"]:
        out.append({
            "title": jb["title"].strip(),
            "locs": [l.strip() for l in (jb.get("location", {}).get("name") or "").split(";")],
            "band": bands(jb.get("content", "")),
            "tok": toks(jb["title"]),
        })
    return out


def best_match(lca_title, postings):
    lt = toks(lca_title)
    best, bscore = None, 0.0
    for p in postings:
        if not p["tok"]:
            continue
        jac = len(lt & p["tok"]) / len(lt | p["tok"])
        seq = SequenceMatcher(None, lca_title.lower(), p["title"].lower()).ratio()
        score = 0.7 * jac + 0.3 * seq
        if score > bscore:
            best, bscore = p, score
    return best, bscore


def money(x):
    try:
        return f"${float(x):,.0f}"
    except (TypeError, ValueError):
        return str(x)


def main():
    postings = load_postings()
    rows = list(csv.DictReader(open(LCA)))
    print(f"LCA filings: {len(rows)}   |   live postings: {len(postings)}\n")
    hdr = f"{'LCA role (FY / level / worksite)':52} {'offered':>10} {'prevail':>9} | {'best live posting':40} {'posted band':>21} {'match':>5}"
    print(hdr)
    print("-" * len(hdr))
    for r in sorted(rows, key=lambda x: (x["WORKSITE_STATE"], x["JOB_TITLE"])):
        m, sc = best_match(r["JOB_TITLE"], postings)
        band = ""
        flag = ""
        if m and m["band"]:
            lo, hi = m["band"]
            band = f"{money(lo)}-{money(hi)}"
            try:
                off = float(r["WAGE_RATE_OF_PAY_FROM"])
                if off > hi:
                    flag = "↑>band"
                elif off < lo:
                    flag = "↓<band"
                else:
                    flag = "in-band"
            except ValueError:
                pass
        lca_label = f"FY{r['FISCAL_YEAR'][2:]} L{r['PW_WAGE_LEVEL']:<3} {r['JOB_TITLE'][:30]:30} {r['WORKSITE_CITY'][:8]:8},{r['WORKSITE_STATE']}"
        post_label = (m["title"][:38] if m else "— none —")
        print(f"{lca_label:52} {money(r['WAGE_RATE_OF_PAY_FROM']):>10} {money(r['PREVAILING_WAGE']):>9} | {post_label:40} {band:>21} {sc*100:>4.0f}% {flag}")


if __name__ == "__main__":
    main()
