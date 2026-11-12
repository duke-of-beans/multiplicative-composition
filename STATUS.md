# Multiplicative-Composition — STATUS
**Last Updated:** 2026-11-12

## Current State
Paper 1 v2 is ON HOLD for submission (2026-11-12; previously SUBMISSION-READY as of 2026-07-10). Papers 2-4 at v1.

**New (2026-11-12):** Axiom review found the uniqueness proof assumes the product form (Axiom 5) and that the harmonic mean, every CES with rho < 0 and min() satisfy Axioms 1-4 without being power laws. Replacement: one unit-invariance axiom in place of Axioms 4 and 5, from which the product, zero-collapse and separability are derived. Zero-collapsing compositions form a line (rho <= 0); MC is its only unit-free point. Note: research/UNIT_INVARIANCE_THEOREM.md. Checks: data/tests/unit_invariance_checks.py (17 pass). rho estimated with intervals on 4 public datasets (data/results/rho_profile_results.json): concrete -0.30, abalone -0.015, California housing +0.53, Penn World Table +0.43. The concrete power-law fit has negative exponents on water and both aggregates. Paper 1 not yet edited.

**New (2026-08-09):** THIRD EMPIRICAL VALIDATION of MC hidden-zero structure — operational system, not dataset. POSTCOG action-safety engine tested multiplicative vs additive scoring against 139 real AUTONOMIC sprints (17 aborted, 122 completed). Results: multiplicative caught 17/17 aborts (100%) vs additive 16/17 (94.1%). Discrimination gap: multiplicative separates aborted from completed by 0.100 vs additive 0.067 — 49% better. Additive average = 0.785 (dangerously close to auto-approve), multiplicative average = 0.329 (properly conservative). Additive averaging dilutes risk dimensions; multiplicative doesn't allow it. Three independent validations now: V-Dem (governance, 2,586 hidden zeros), HDI (development, education binding), POSTCOG (operational action-safety, 139 sprints). Code at D:\Projects\POSTCOG\tests\mc-prediction.test.ts.

**New (2026-07-16):** RF/Smith Chart convergent derivation identified. Friis equation is MC with domain-specific dimensions. Three new backlog items for RF, complex-valued axioms, cross-domain tool transfer.

## Author Standard
All academic work and citations: **David E. Kirsch**. arXiv endorsement code 4EWXUO (Pitz & Ferraz).

## Papers
| Paper | Title | Status | File |
|-------|-------|--------|------|
| 1 | Axiomatic Characterization of Multiplicative Aggregation: On Zero-Collapse and the O-Ring Inversion | v2 ON HOLD: section 2 axioms to be revised (research/UNIT_INVARIANCE_THEOREM.md section 7) | papers/paper1/paper_v2.tex |
| 2 | Emergence as Information Volume on Statistical Manifolds | v1 draft | papers/paper2/paper2_v1.tex |
| 3 | Zero-Collapse and Resource Allocation | v1 draft | papers/paper3/paper3_v1.tex |
| 4 | The Additive Audit | v1 draft | papers/paper4/paper4_v1.tex |

## Empirical Validations (3 domains, same structural prediction)
| Domain | Dataset | Key Result |
|--------|---------|------------|
| Governance | V-Dem v16 (26,954 obs) | 2,586 hidden zeros (9.6%), 91.1% stayed autocratic at 5yr |
| Development | HDI (206 countries × 7yr) | Education binding 100%, mean gap 0.007 |
| **Operational** | **POSTCOG/AUTONOMIC (139 sprints)** | **100% vs 94.1% abort detection, 49% better discrimination** |

## Endorsement (P0)
- Code: 4EWXUO, target econ.TH
- Thomas Pitz — thomas.pitz@hochschule-rhein-waal.de
- Vinicius Ferraz — vinicius@singularity.inc

## Blockers
- Paper 1 section 2 revision to the unit-invariance axiom (blocks submission)
- Read Luce 1959, Aczel-Roberts-Rosenbaum 1986, Ebert-Welsch 2004, Tsui-Weymark 1997 before citing
- Endorsement email send
- WHETSTONE full-abstract pass
