# HANDOFF: Three Papers for Multiplicative Composition
## Complete context for writing Papers 1, 2, and 3

**Created:** 2026-05-31
**Repo:** https://github.com/duke-of-beans/multiplicative-composition (PUBLIC)
**Research page:** https://davidkirsch.me/research

---

## PAPER 1: Multiplicative Composition of Independent Dimensions in Emergent Systems

### Status
Draft complete at `PAPER_DRAFT.md` in repo. 2,298 words, covers 8 domains + cliff-vs-slope + info geometry section. Needs voice pass and arXiv formatting.

### What needs to happen
1. **Voice pass:** Current draft is standard academic third-person passive. Should be rewritten in SCRVNR analytical mode or Tranche-style professional voice — technical precision, zero hand-holding, let data carry weight, controlled confidence. NOT casual essay voice (that's for the website). Professional but distinctly David Kirsch, not generic academic.
2. **arXiv formatting:** Convert to LaTeX. Standard article class, single-column. Include figures from `figures/` directory.
3. **Figure updates:** The 5 axiomatic proof figures need regeneration at publication DPI (300+). Run `axiomatic_proof.py`.
4. **NBA result update:** Current draft may reference simulated NBA. Update to real NBA data (210 team-seasons, TIE result — honest).
5. **CES ρ discussion:** Be honest about convergence issues. Lead with direct mult-vs-add comparison as primary finding. ρ as supporting diagnostic.

### Voice reference
Read `writing/the-natural-order-of-intelligence.html` on the website for the essay voice. Paper voice should be one register more formal — same precision, same confidence, less conversational. Think Tranche research page voice: declarative, data-first, no hedging except where intellectually required.

### Key files in repo
- `PAPER_DRAFT.md` — current draft (start here)
- `AXIOMATIC_UNIQUENESS.md` — full proof with honest assessment
- `INFORMATION_GEOMETRY.md` — info geometry outline (v1)
- `info_geometry_proof.py` — formal proof with numerical verification
- `rho_estimator_v2.py` — CES estimator (differential evolution)
- `figures/` — 5 figures from axiomatic proof
- All domain test scripts (`network_sync_test.py`, `signal_processing_test.py`, `ecosystem_test.py`, `worldbank_test.py`, `nba_real_test.py`)
- All results JSONs

### Target venue
arXiv preprint first (establishes priority). Then Physical Review E, Complexity, or similar.

### Dependencies
None — everything needed is in the repo.

---

## PAPER 2: Emergence as Information Volume on Statistical Manifolds

### Status
Derivation complete at `info_geometry_proof.py` and `INFORMATION_GEOMETRY.md`. Numerical verification recovers theoretical exponents to 3 decimal places. The key insight (capacity is additive, states are multiplicative, emergence counts states) is formalized.

### What needs to happen
1. **Paper 1 on arXiv first** — Paper 2 cites Paper 1 for the axiomatic proof and empirical results.
2. **Formal mathematical writing:** This paper needs to be written in the language of differential geometry and information theory. Definitions, Lemmas, Theorems, Proofs. More formal than Paper 1.
3. **The Step 3 argument needs sharpening:** The definition of emergence as volume density (√det g) is justified by uniqueness (only scalar satisfying reparameterization invariance + multiplicativity + zero-collapse). This uniqueness argument needs to be stated as a formal theorem with proof.
4. **The capacity-vs-states distinction** is the conceptual core. Shannon entropy = capacity = additive. Fisher volume = distinguishable states = multiplicative. These are different quantities. This distinction should be the paper's central contribution.
5. **Mathematician review:** The Riemannian geometry claims (diagonal Fisher metric for product manifolds, volume element formula) are standard results, but a reviewer will want them presented in proper differential geometry notation with citations to Amari (2016) and Ay et al. (2017).

### Key files
- `info_geometry_proof.py` — theorem statement, proof, numerical verification
- `info_geometry_proof_results.json` — verification results
- `INFORMATION_GEOMETRY.md` — earlier outline (less complete than proof.py)

### Target venue
IEEE Transactions on Information Theory, Journal of Mathematical Physics, or Entropy (MDPI). This is a math paper, not an empirical paper.

### Dependencies
- Paper 1 on arXiv (for citation)
- Ideally: review by someone with differential geometry background

---

## PAPER 3: Zero-Collapse and Resource Allocation in Multiplicative Systems

### Status
Foundation documented at `ESSAY_SOCIAL_INVESTMENT.md` and `HANDOFF_SOCIAL_ESSAY.md`. Three lenses (individual, government, society) fully outlined. No formal analysis started.

### What needs to happen
1. **Paper 1 on arXiv first** — Paper 3 cites Paper 1 for the mathematical framework.
2. **Real-world data analysis:**
   - Housing First longitudinal outcomes (HUD, Urban Institute)
   - Austerity vs stimulus natural experiment (Greece vs Iceland, 2008-2015, Eurostat/OECD data)
   - World Bank panel regression with country/year fixed effects (we have 162-country cross-section; need panel with temporal dimension)
   - Failed state economic trajectories (Venezuela, Zimbabwe — WGI × GDP timelines)
3. **Econometric methods:** This paper needs proper panel regression, not just Spearman correlations. Fixed effects, instrumental variables if possible. Needs to meet social science methodological standards.
4. **The social investment essay should publish first** — establishes the argument publicly in accessible form. Paper 3 formalizes it academically.

### Key files
- `HANDOFF_SOCIAL_ESSAY.md` — essay handoff (three lenses, research needs, voice)
- `ESSAY_SOCIAL_INVESTMENT.md` — essay foundation material
- `worldbank_test.py` + `worldbank_results.json` — 162-country cross-section
- `social_economic_tests.py` + `social_econ_results.json` — simulated tests (method validation)

### Target venue
PNAS, Nature Human Behaviour, Journal of Development Economics, or policy journal. This paper crosses disciplinary boundaries — needs a venue that welcomes that.

### Dependencies
- Paper 1 on arXiv
- Social investment essay published on website
- Housing First data (HUD)
- Eurostat austerity/stimulus data
- World Bank panel (temporal extension of existing cross-section)
- Possibly: collaboration with development economist for methodological credibility

---

## SEQUENCING

```
Paper 1 (main result)
  → arXiv preprint
    → Repo already public
      → Research page already updated
        ├─→ Paper 2 (info geometry) — can start immediately after Paper 1
        ├─→ Social investment essay — can start immediately after Paper 1  
        └─→ Paper 3 (social policy) — after essay + data collection
```

---

## FILE INDEX

All files in `D:\Projects\Multiplicative-Composition\` and mirrored at `https://github.com/duke-of-beans/multiplicative-composition`:

### Core documents
- `PAPER_DRAFT.md` — Paper 1 draft
- `AXIOMATIC_UNIQUENESS.md` — full proof
- `INFORMATION_GEOMETRY.md` — info geometry outline
- `ESSAY_SOCIAL_INVESTMENT.md` — essay foundation (three lenses)
- `HANDOFF_SOCIAL_ESSAY.md` — essay handoff doc
- `HANDOFF_PAPERS.md` — THIS FILE
- `STATUS.md` — project status + backlog
- `README.md` — public-facing repo description

### Code
- `axiomatic_proof.py` — proof figures
- `rho_estimator_v2.py` — CES estimator (differential evolution, all 3 sim domains)
- `network_sync_test.py` — domain 1 (simulated)
- `signal_processing_test.py` — domain 2 (simulated)
- `ecosystem_test.py` — domain 3 (simulated)
- `worldbank_test.py` — domain 6 (real-world, 162 countries)
- `nba_real_test.py` — domain 8 (real-world, 210 team-seasons)
- `social_economic_tests.py` — method validation (simulated)
- `info_geometry_proof.py` — info geometry theorem + numerical verification
- `info_geometry_step3.py` — Step 3 formalization
- `sleep_edf_test.py` — sleep data (circular test)
- `sleep_stage_test.py` — sleep data (non-circular, stage prediction)
- `r_diagnostic.py` — R measure saturation analysis
- `run_all.py` — unified reproduction script

### Results
- `rho_v2_results.json` — CES estimator v2 results
- `worldbank_results.json` — World Bank 162-country results
- `nba_real_results.json` — NBA 210 team-season results (from local machine)
- `signal_processing_results.json`
- `ecosystem_results.json`
- `network_sync_results.json`
- `real_network_results.json`
- `social_econ_results.json`
- `cliff_slope_results.json` — Sleep-EDF cliff-vs-slope
- `propofol_results.json` — Chennu propofol (20 subjects, moderate sedation)
- `propofol_all_results.json` — all 20 subjects processed
- `info_geometry_proof_results.json`
- `sleep_edf_rho_test.json`

### Figures
- `figures/01_zero_collapse.png`
- `figures/02_ces_family.png`
- `figures/03_isoquants.png`
- `figures/04_cliff_vs_slope.png`
- `figures/05_log_space_linearity.png`

### Infrastructure
- `requirements.txt`
- `LICENSE` (MIT)
- `.gitignore`

### HIRM cross-reference
- HIRM architectural reckoning appended to `D:\Projects\HIRM\STATUS.md`
- HIRM removed from website research page pending v2 rework
- Brain.db observation stored for auto-surfacing
