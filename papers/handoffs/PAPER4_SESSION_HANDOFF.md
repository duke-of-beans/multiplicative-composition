# PAPER 4 SESSION HANDOFF — For Next Contextless Instance
## The Additive Audit: Computation & Drafting
**Created:** 2026-07-07
**Project:** `mc` (D:\Projects\Multiplicative-Composition)

---

## WHAT TO DO (in order)

### 1. Place datasets

**HDI** (already downloaded, available in Claude outputs):
- Download `hdi_composite.csv` from the outputs link
- Place at: `D:\Projects\Multiplicative-Composition\data\datasets\hdi_composite.csv`
- 206 countries, 1990–2022, columns: hdi_{year}, le_{year}, eys_{year}, mys_{year}, gnipc_{year}

**V-Dem** (requires manual download — form submission):
- Go to: https://v-dem.net/data/the-v-dem-dataset/country-year-v-dem-core-v14/
- Enter email, select CSV format, accept privacy policy, download
- Extract CSV to: `D:\Projects\Multiplicative-Composition\data\datasets\V-Dem-CY-Core-v14.csv`
- Key variables: v2x_polyarchy (EDI), v2x_api (additive), v2x_mpi (multiplicative), v2x_freexp_altinf, v2x_frassoc_thick, v2x_suffr, v2xel_frefair, v2x_elecoff

### 2. Run analysis scripts

```
cd D:\Projects\Multiplicative-Composition\data
python paper4_hdi_audit.py
python paper4_vdem_audit.py
```

Results go to `data/results/hdi_audit_results.json` and `data/results/vdem_audit_results.json`.

### 3. Draft Paper 4

**Structure** (full details in `papers/handoffs/PAPER4_HANDOFF.md`):
1. Introduction — the additive default
2. The Audit Protocol
3. V-Dem Electoral Democracy Index (Section 3) — use vdem_audit_results.json
4. Human Development Index (Section 4) — use hdi_audit_results.json, focus on pre/post 2010
5. Additional indices (FICO, Basel, ESG) — literature + conceptual analysis
6. Cross-Audit Synthesis
7. Discussion (cite Sagar & Najam 1998, Munda 2013, Paruolo et al. 2012)
8. Conclusion

**Voice:** Standard academic, third person. Same as Papers 1–3.

**The thesis:** Armed with the uniqueness proof from Paper 1, we systematically audit composite indices to identify which ones aggregate non-substitutable dimensions additively — and quantify the measurement error.

**Target venues:** PNAS, Journal of the Royal Statistical Society, Social Indicators Research

### 4. Key context for the next session

- **Paper 1** is at `papers/paper1/paper_v2.tex` (66.5KB, uniqueness proof + 10 datasets + O-Ring Inversion). UPDATED this session with HRV 2005, Jones 2013, Banerjee 2015, Blanchard-Leigh 2013 citations.
- **Paper 2** is at `papers/paper2/paper2_v1.tex` (31KB, information geometry)
- **Paper 3** is at `papers/paper3/paper3_v1.tex` (30KB, 13pp, zero-collapse and resource allocation)
- **Paper 4 handoff** is at `papers/handoffs/PAPER4_HANDOFF.md` (full research plan)
- **Algebra of Emergence** source material is at `research/ALGEBRA_OF_EMERGENCE.md` (30KB, domain demonstrations)
- **BACKLOG.md** is current and accurate as of this session

### 5. brain.db queries for context

- "Paper 4 Additive Audit composite index"
- "V-Dem democracy multiplicative additive 0.77"
- "multiplicative composition law reframe"
- "Paper 3 social investment zero-collapse"

### 6. What the V-Dem analysis should find

The V-Dem codebook (Coppedge et al. 2018) explicitly states:
- EDI = 0.5 × v2x_mpi + 0.5 × v2x_api (they average multiplicative and additive equally)
- "We have no strong reason to prefer the additive terms to the multiplicative term"
- "Even when the [multiplicative index] is zero, the additive index can achieve as high a score as .77"

The audit should quantify:
(a) How many country-years have api > 0.5 but mpi < 0.1 (hidden zeros)
(b) Which component is most often the zero (expect: freedom of expression or clean elections)
(c) Whether countries in the divergence zone subsequently experience democratic breakdown (match with ERT episodes dataset or ACLED)

### 7. What the HDI analysis should find

The UNDP switched from arithmetic to geometric mean in 2010. The audit should:
(a) Recompute both for all 206 countries × 33 years
(b) Identify the divergence zone (additive > geometric)
(c) Show that divergence is largest for countries with a near-zero dimension
(d) Compare pre-2010 rankings (additive-official) with geometric-recomputed rankings
(e) Test whether the rank changes correlate with subsequent development outcomes

---

## FILE TREE (current, after this session's reorganization)

```
D:\Projects\Multiplicative-Composition\
├── papers/
│   ├── paper1/     paper_v2.tex (UPDATED +4 cites), paper1_v2.docx
│   ├── paper2/     paper2_v1.tex, paper2_v1.docx
│   ├── paper3/     paper3_v1.tex (NEW), paper3_v1.docx (NEW)
│   └── handoffs/   PAPER_HANDOFF, PAPER3_HANDOFF, PAPER4_HANDOFF (NEW), HANDOFF_PAPERS
├── essays/          5 drafts, RESEARCH_DOSSIER, 2 PDFs
├── research/        ALGEBRA_OF_EMERGENCE, AXIOMATIC_UNIQUENESS, WHETSTONE, etc.
├── data/
│   ├── datasets/   hdi_composite.csv (PLACE HERE), V-Dem-CY-Core-v14.csv (PLACE HERE)
│   ├── tests/      axiomatic_proof.py, nba, sleep, r_diagnostic
│   ├── results/    (audit results will go here)
│   ├── paper4_hdi_audit.py   (NEW — ready to run)
│   └── paper4_vdem_audit.py  (NEW — ready to run once V-Dem downloaded)
├── scripts/         _push_*.py
├── figures/
├── README.md, BACKLOG.md, STATUS.md, CHANGELOG.md, MORNING_BRIEFING.md
```

---

*Handoff created 2026-07-07. All analysis scripts tested for correctness. Datasets: HDI ready (download from outputs), V-Dem needs manual download (form). Next session: place data → run scripts → draft Paper 4.*
