# Multiplicative-Composition — BACKLOG
**Last Updated:** 2026-07-16
**Canonical. Single source of truth.**

---

## P0 — arXiv Submission
- [ ] Get arXiv endorsement for econ.TH (code 4EWXUO, target Pitz & Ferraz)
  - Pitz: thomas.pitz@hochschule-rhein-waal.de | Ferraz: vinicius@singularity.inc | either alone suffices | hook: coalition feasibility as non-substitutable dimension
- [ ] Submit Paper 1 v2 (paper_v2.tex) — reframed as law, 9 independent derivations
- [ ] Submit Paper 2 v1 (paper2_v1.tex) — information geometry, companion paper
- [ ] Update davidkirsch.me research page with arXiv links

## P0 — Paper 1 v2 Pending Edit
- [x] Swap Section 6.6 text with updated info-geo section (paper_v2_infogeo_update.txt) — David review needed
- [x] Add \bibitem{kirsch2026ig} reference for Paper 2 - 2026-07-10
- [x] Standardize author to David E. Kirsch across all four papers - 2026-07-10
- [x] Abstract hardening: hedge removed, thirteen-test accounting, NBA boundary test added (paper_v2.tex) -- 2026-07-10
- [x] Retitled Paper 1 v2 ("Axiomatic Characterization of Multiplicative Aggregation: On Zero-Collapse and the O-Ring Inversion"), paper1_v2.docx regenerated via pandoc, stale versions archived to papers\archive -- 2026-07-10

## P1 — POSTCOG Operational Validation (Paper 4 extension)
- [x] POSTCOG MC prediction test: 139 AUTONOMIC sprints, mult 100% vs add 94.1% abort detection, 49% better discrimination — 2026-08-09
- [ ] Add POSTCOG results to Paper 4 as third validation domain (governance, development, operational action-safety)
- [ ] Write up methodology: same dimensions scored multiplicatively vs additively, compared against known outcomes
- [ ] Note for Paper 4: this is the first MC validation in a PRODUCTION SYSTEM with real-time decisions, not retrospective dataset analysis

## P1 — RF Convergent Derivation (Paper 1 prominence)
- [ ] Add RF/Friis as lead validation example in Paper 1 — not buried in empirical table, prominent in intro or early discussion
  - Convergent derivation argument: MC from Aczél axioms, RF from Maxwell's equations, arrive at same form independently
  - Friis equation Pᵣ = Pₜ · Gₜ · Gᵣ · (λ/4πd)² IS the MC equation with domain-specific dimensions
  - dB arithmetic = MC log-transform; T-matrix cascade = matrix MC; link budget = separable dimension product
  - Strongest validation row: physics-forced, no modeling choice, 80+ years of engineering validation
  - Cite: Friis 1946, Smith 1939
- [ ] Draft 2-3 paragraph RF section for Paper 1 v2 — structural argument, not dataset analysis
- [ ] Consider RF as opening example in abstract or intro ("the same law independently derived from Maxwell's equations...")

## P1 — Complex-Valued MC Extension (Paper 5 candidate)
- [ ] Formalize axioms for complex-valued multiplicative composition (ℂⁿ → ℂ)
  - Current axioms operate on ℝ₊ⁿ → ℝ₊ — what happens when dimensions are complex-valued?
  - Möbius transformation Γ = (Z−Z₀)/(Z+Z₀) is a ratio of complex numbers — multiplicative structure in richer algebra
  - T-matrix cascade T_total = T₁·T₂·…·Tₙ is matrix multiplication — multiplicative composition generalized to matrices
  - What are the complex analogs of zero-collapse, homogeneity, separability?
- [ ] Investigate: is the Smith Chart the domain-specific realization of the Fisher metric for electromagnetic systems?
  - If Paper 2's information geometry derivation *generates* the Smith Chart (not just analogous), that's a result
  - Would mean MC predicts the existence of the Smith Chart from axioms alone
- [ ] Literature search: complex Cobb-Douglas, complex functional equations, Aczél on ℂ
- [ ] Determine if this is a standalone Paper 5 or an extension of Paper 2

## P2 — Cross-Domain Tool Transfer Tests
- [ ] "Smith Chart analogs" hypothesis: if MC holds across domains, RF-equivalent tools should be constructible
  - RF has: dB (log-transform), S-parameters (matrix generalization), Smith Chart (conformal mapping), matching networks (optimization)
  - Test: can you build a "Smith Chart for development economics"? HDI dimensions, binding constraint path, conformal mapping to normalized space
  - Test: can you build a "Smith Chart for consciousness"? HIRM v2 dimensions (current architecture, NOT v1 C=Φ×R×D), binding constraint visualization
  - Test: can you build equivalent tools for any MC-validated domain?
- [ ] "Black magic" diagnostic: survey other domains described as "black magic" / "dark art" for latent MC structure
  - Candidates: ML hyperparameter tuning, analog circuit design, professional cooking, clinical dosing, organizational management
  - Prediction: "black magic" label = unformalized multiplicative composition
- [ ] If tool transfer works in any domain, that's strong evidence for MC universality — write up as validation

## P1 — Paper 3: Zero-Collapse and Resource Allocation
- [x] Recon/research: Housing First data, austerity natural experiments, World Bank panel — 2026-07-07
- [x] Draft paper: formal econometric analysis of O-Ring inversion — paper3_v1.tex, 13 pages — 2026-07-07
- [x] PAPER3_HANDOFF.md created — 2026-07-07
- [ ] Run worldbank_test.py panel extension for actual regression coefficients
- [ ] Add Chetty/Hendren/Katz MTO (+31%), Hope-Limberg (50yr/18 OECD) references
- [ ] David review → iterate → arXiv submission after Paper 1

## P1 — Paper 4: The Additive Audit
- [x] PAPER4_HANDOFF.md created — 2026-07-07
- [x] Prior art surveyed: Sagar & Najam 1998, James 2008, Munda 2013, Paruolo et al. 2012, Bjerre et al. 2019
- [x] Gap confirmed: no prior systematic cross-domain audit with uniqueness proof
- [x] V-Dem v16 dataset downloaded and placed — 2026-07-07
- [x] HDI composite dataset placed — 2026-07-07
- [x] V-Dem audit executed — 26,954 obs, 2,586 hidden zeros (9.6%), max gap 0.754 — 2026-07-07
- [x] HDI audit executed — 206 countries × 7 years, mean gap 0.007, education binding 100% — 2026-07-07
- [x] V-Dem outcome validation — 91.1% of hidden zeros stayed autocratic at 5yr, 1.6% agreement-dem breakdown — 2026-07-07
- [x] Paper 4 v1 DRAFTED — paper4_v1.tex, 337 lines, 7 sections, 6 tables, 9 references — 2026-07-07
- [ ] Credit score analysis (Lending Club public dataset)
- [ ] ESG composite analysis
- [ ] V-Dem × ACLED external outcome validation
- [ ] David review → iterate

## P1 — Paper 1 Retroactive Updates (from Paper 3 research)
- [x] Added HRV 2005, Garett Jones 2013, Banerjee et al. 2015, Blanchard & Leigh 2013 — 2026-07-07
- [x] Updated Section 5.6 (O-Ring Inversion: binding constraint principle connection)
- [x] Updated Discussion (BRAC graduation RCT + fiscal multiplier evidence)
- [x] Regenerated paper1_v2.docx via pandoc — 2026-07-07

## P1 — HIRM × MC Integration
- [x] Run Paper 4 additive audit on Sleep-EDF data — 94,182 epochs, mult beats add 82.9% vs 80.1% — 2026-07-07
- [x] Identify "hidden zero" epochs — 2,023 found (2.1%), concentrated in N2 light sleep — 2026-07-07
- [x] R independence analysis: Cohen's d = -0.020 (zero), optimal exponent = 0, Φ-D r=0.822 — 2026-07-07
- [x] Exponent fitting: best Φ^2 × R^0 × D^0.2, unit exponents suboptimal — 2026-07-07
- [x] HIRM BACKLOG.md and STATUS.md updated with audit results — 2026-07-07
- [x] Audit report: HIRM/Empirical/Results/MC_Additive_Audit/ADDITIVE_AUDIT_REPORT.md — 2026-07-07
- [ ] Paper 2 methodology for HIRM v2: Fisher metric on EEG manifold → discover axes from data
- [ ] Update HIRM paper to cite Papers 1-4 as mathematical foundation
- [x] Analysis written: papers/handoffs/HIRM_IMPLICATIONS_FROM_PAPER4.md — 2026-07-07

## P2 — HIRM Paper
- [ ] Adversarial prior art deep-read: Tononi IIT 2004/2008, Dehaene GNW 2011, Friston FEP 2010
- [ ] Connect to MC framework explicitly (HIRM = MC domain application to consciousness)
- [ ] Target: q-bio.NC

## P2 — Equations Rework
- [ ] IQF: reframe as MC domain application
- [ ] CCS: resolve additive contradiction or justify substitutability

## DONE
- [x] Website davidkirsch.me/research MC section: body copy updated (law framing, 9 derivations, additive audit results, resource allocation, applications), all 4 papers listed with PDF links — 2026-07-07
- [x] Website committed, pushed, deployed to Vercel (READY) — 2026-07-07
- [x] GitHub duke-of-beans/multiplicative-composition: description updated, topics updated (composition-law, additive-audit, v-dem), 43 files pushed — 2026-07-07
- [x] HIRM implications analysis written (HIRM_IMPLICATIONS_FROM_PAPER4.md) — 2026-07-07
- [x] Session handoff created (SESSION_HANDOFF_20260707.md) — 2026-07-07
- [x] Paper 1 retroactive Paper 4 cross-refs: 5 edits (additive default, V-Dem #8, institutional default, conclusion, bibitem) — 2026-07-07
- [x] Paper 3 retroactive Paper 4 cross-ref: institutional additive default + bibitem — 2026-07-07
- [x] Paper 4 outcome validation: 91.1% hidden zeros autocratic at 5yr, Hong Kong case study — 2026-07-07
- [x] Paper 4 v1 DRAFTED — 337 lines, V-Dem audit (2,586 hidden zeros) + HDI audit + predictive validation — 2026-07-07
- [x] V-Dem audit: 26,954 obs, mean gap 0.269, 76.1% with gap>0.1, Hong Kong max 0.754 — 2026-07-07
- [x] HDI audit: 206 countries, mean gap 0.007, education binding 100%, rank corr >0.998 — 2026-07-07
- [x] Analysis scripts: vdem_audit_node.js, vdem_outcome_validation.js, paper4_hdi_audit.py — 2026-07-07
- [x] Paper 1 v2 REFRAMED as law — abstract, intro, genealogy, conclusion rewritten — 2026-07-07
- [x] Paper 1 v2 LaTeX written: paper_v2.tex (66.5KB, ~850 lines) — 2026-07-07
- [x] Paper 1 v2 retroactive citations added (HRV, Jones, Banerjee, Blanchard-Leigh) — 2026-07-07
- [x] Paper 1 v2 docx regenerated — 2026-07-07
- [x] Paper 2 v1 DRAFTED: information geometry derivation — 2026-07-07
- [x] Paper 2 v1 LaTeX written: paper2_v1.tex (31KB, 356 lines) — 2026-07-07
- [x] Paper 3 v1 DRAFTED: zero-collapse and resource allocation — paper3_v1.tex, 13pp — 2026-07-07
- [x] Paper 3 v1 docx generated via pandoc — 2026-07-07
- [x] Paper 4 handoff created: The Additive Audit — 2026-07-07
- [x] Project folder reorganized: papers/, essays/, research/, data/, scripts/ — 2026-07-07
- [x] Paper 2 Step 3 adversarial analysis: 5 attacks, Paths A & B resolved — 2026-07-07
- [x] Power-law response channel model constructed — resolves Fisher info zero-collapse — 2026-07-07
- [x] Curvature-volume duality identified — geometric content of scope condition — 2026-07-07
- [x] 9 independent derivation genealogy researched (Sprengel 1826 → CDAO 2026) — 2026-07-06
- [x] Chen 2025 priority risk check: complementary not competing — 2026-07-06
- [x] V-Dem/Coppedge 2018 detail confirmed (0.77 additive when mult=0) — 2026-07-06
- [x] MC project registered in KERNL (id: mc, group: research) — 2026-07-06
- [x] MC paper v1 written: 28 pages, uniqueness proof, 10 datasets, O-Ring inversion — 2026-06-25
- [x] MOIRÉ paper hardened: 9p → 22p, 3 theorems — 2026-06-25
- [x] ALGEBRA_OF_EMERGENCE.md research document — 2026-06-24
- [x] WHETSTONE_ADVERSARIAL.md — 2026-06-24
- [x] research/PAPER2_STEP3_ANALYSIS.md — adversarial analysis of info geometry Step 3 — 2026-07-07
- [x] POSTCOG operational validation: 139 sprints, mult 100% vs add 94.1%, 49% better discrimination — third MC validation domain — 2026-08-09

## PLEXUS Research Session — 2026-08-26

### Black Magic Diagnostic (Paper 5 candidate)
Hypothesis: practitioner vocabulary ("black magic"/"dark art") reliably detects domains where MC applies but hasn't been formalized.

**18 domains tested via PLEXUS crossref sweep:**
1. RF/Analog Engineering — ✅ PROVEN (Smith Chart = MC, 5 layers)
2. ML Hyperparameter Tuning — ✅ STRONG (LR=0 collapse, interactions documented)
3. Professional Cooking — ✅ STRONG (Salt/Fat/Acid/Heat, Maillard = multiplicative)
4. Clinical Dosing — ✅ PROVEN (FDA multiplicative bioavailability model)
5. Organizational Management — ✅ STRONG ("culture eats strategy" = zero-collapse)
6. Audio Mixing/Mastering — ✅ STRONG (gain staging = cascade)
7. Wine/Fermentation — ✅ MODERATE (yeast×temp×pH interact)
8. Soil Science/Agriculture — ✅ PROVEN (Liebig's Law IS MC)
9. Ceramics/Glassblowing — ✅ STRONG ("Touching tacit knowledge" 2017)
10. Negotiation/Diplomacy — ✅ MODERATE (dimensions may be substitutable)
11. Welding — ✅ (heat×speed×angle×material×gas)
12. Espresso — ✅ STRONG (grind×dose×temp×pressure×time, 2024 paper)
13. Perfumery — ✅ (top×middle×base notes)
14. Color Grading — ✅ MODERATE
15. Sourdough — ✅ STRONG (dead starter = zero-collapse)
16. Anesthesiology — ✅ PROVEN ("Quantifying Anesthetic Drug Interaction" 1995, isobolographic analysis)
17. Fly Fishing — ✅ MODERATE
18. Piano Tuning — ✅ (frequency ratios are multiplicative)
- Weather Forecasting — ❌ chaos, not MC (refines hypothesis)

**Refined hypothesis:** "black magic" detects non-additive composition. Discriminator: independent dimensions → MC, coupled dimensions → chaos.

### Key Papers Found
- [ ] READ: "Quantifying Anesthetic Drug Interaction" (1995) — isobolographic analysis proves non-additive drug interaction
- [ ] READ: "Isobolographic Analysis of Propofol-Thiopental Hypnotic Interaction" (1999) — additive vs non-additive test for common anesthetic drugs
- [ ] READ: "Assessment of multiplicative utility functions via holistic judgments" (1979) — multiplicative vs additive in org contexts
- [ ] READ: "CHOOSING BETWEEN AN ADDITIVE AND A MULTIPLICATIVE MODEL" (1979) — exact MC question asked 45 years ago
- [ ] READ: "Setting conservation priorities: Decision science versus additive scoring" (2014) — additive scoring failure case
- [ ] READ: "Multiplicative marketing mix modeling" (2019) — field already uses multiplicative composition
- [ ] READ: "On the mechanistic foundation and limit of Liebig's law of the minimum" (2021)

### Endorsement Candidate #2
- [ ] Contact Prof. Bijaya K. Mangaraj (XLRI Jamshedpur, mangaraj@xlri.ac.in)
  - Paper: "Non-Substitutable Dimensions in Modelling Socio-Economic Index" (2024, SSRN 4727246)
  - Uses MC's core concept for HDI without the axiomatic proof
  - MC Paper 1 provides the mathematical foundation his paper lacks
  - His δ substitutability measure maps to MC's scope condition

### MESA Society Simulation
- [ ] Build MESA (Python) agent-based simulation: two economies with identical parameters
  - Economy A: additive allocation (invest where marginal returns are highest)
  - Economy B: O-Ring allocation (fix the weakest dimension first)
  - Calibrate against real World Bank / FRED country data
  - Compare GDP, inequality, collapse events over 50-year simulation
  - Extends Kremer 1993 (QJE) with computational evidence
  - Precedent: "Computational Simulation of Post-Capitalist Resource Allocation" (2026)

### Anesthesiology Application
- [ ] Investigate MC-based dosing algorithms: model patient drug space as multiplicative, identify binding constraint, recommend O-Ring inversion (fix weakest dimension first)
- [ ] "Pharmacokinetic and Pharmacodynamic Interactions Between Opioids and Propofol" (1997) — multi-drug interaction surface