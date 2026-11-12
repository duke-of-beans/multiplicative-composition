# Unit Invariance: a stronger uniqueness theorem for Multiplicative Composition

**Created:** 2026-11-12
**Order:** wo-20261112-3f1beed8 (theorem), wo-20261112-5e0c58d1 (rho tests)
**Status:** Theorem 1 proven here. Theorem 2 and Proposition 3 are classical results stated with proof sketches; each needs a full written proof or a checked citation before it goes into a paper. Empirical section covers 4 of the 8 primary datasets.
**Machine checks:** `python3 data/tests/unit_invariance_checks.py` (17 checks, all pass on 2026-11-12)
**Affects:** Paper 1 v2 sections 1, 2, 3.4 (genealogy), 4 (method, 4.4 CES) and 5 (O-Ring inversion). Paper 1 is on HOLD for submission until section 2 is revised.

Every claim below carries one of: **[PROVEN]** proof is in this note, **[CHECKED]** verified by the script, **[CLASSICAL]** known result, citation to be read before use, **[MEASURED]** from `data/results/rho_profile_results.json`.

---

## 1. What is wrong with the proof in Paper 1 v2

**1.1 Axiom 5 assumes the product.** [PROVEN by reading the text] Axiom 5 states `f(x) = prod g_i(x_i)`. The multiplicative structure is an input to the theorem. What the theorem then shows is narrower: if `f` is already a product of one-variable functions and is homogeneous, each factor is a power function. A reviewer will say the product was assumed, and they will be right.

**1.2 "There is no third option" is false as stated.** [CHECKED C1, C2, C3] The harmonic mean

    H(x, y) = 2xy / (x + y)

is zero-collapsing, continuous, strictly increasing in both arguments and homogeneous of degree 1. It satisfies Axioms 1 to 4. It is not a power law. The same is true of every CES function with rho < 0 and of min(). So "if a dimension cannot be compensated, multiply" skips a whole family of non-substitutable, zero-collapsing compositions that are not multiplication.

**1.3 The paper misstates what excludes CES.** [CHECKED C3] Section 2.4 says dropping homogeneity "opens the full CES family". CES is homogeneous of degree 1. Homogeneity does not exclude it. In the current proof only Axiom 5 excludes it, which is the axiom that assumes the answer.

**1.4 The marginal inversion is misstated.** [CHECKED C7] "Because df/dx_i = alpha_i f / x_i is a decreasing function of x_i" is only true when alpha_i < 1. Since f contains x_i^alpha_i, df/dx_i is proportional to x_i^(alpha_i - 1), which rises with x_i when alpha_i > 1. The statement that survives for every exponent is about the ratio between dimensions (section 4.3).

**1.5 The genealogy mixes two different laws.** Sprengel and Liebig's Law of the Minimum is min(x_1, ..., x_n), the rho -> -infinity end of the family. It is zero-collapsing but it is not a product. Series reliability, Cobb-Douglas and Kremer's O-Ring are products. Counting Liebig as an independent derivation of the power law is wrong; it is an independent discovery of zero-collapse.

---

## 2. The fix: one axiom in place of two

Independent dimensions have independent units. Cement is in kilograms, curing time in days. Nothing fixes the exchange rate between a kilogram and a day, so a law that composes them cannot depend on it.

Paper 1's Axiom 4 scales every dimension by the same factor lambda. That operation only has a meaning when the dimensions already share a unit, which is the opposite of what "independent dimensions" says. The right invariance is one scale factor per dimension.

**Setup.** f maps positive reals^N to positive reals.

**Axiom U (Unit invariance).** For every lambda = (lambda_1, ..., lambda_N) with all lambda_i > 0 there is a number phi(lambda) > 0 such that for all x

    f(lambda_1 x_1, ..., lambda_N x_N) = phi(lambda) * f(x_1, ..., x_N).

In words: changing the unit of any dimension changes the unit of the output and nothing else.

**Axiom C (Continuity).** f is continuous. (Monotonicity in each variable, or measurability, would also do; any of them rules out the pathological Cauchy solutions.)

**Axiom N (Necessity).** f is strictly increasing in each x_i.

### Theorem 1 (strong form) [PROVEN]

If f satisfies U and C then

    f(x) = k * prod x_i^alpha_i     for some k > 0 and real alpha_i.

If f also satisfies N then every alpha_i > 0, and f extends continuously to the boundary with f = 0 whenever any x_i = 0.

**Proof.** Put x = (1, ..., 1) in U: f(lambda) = phi(lambda) f(1). So phi = f / f(1). Substituting back, with F = f / f(1):

    F(lambda_1 x_1, ..., lambda_N x_N) = F(lambda) F(x)   for all lambda, x.

This is the multiplicative Cauchy equation in N variables. Hold all coordinates but the i-th at 1 and write h_i(t) = F(1, ..., t, ..., 1). Then h_i(st) = h_i(s) h_i(t), h_i is continuous and positive, so h_i(t) = t^alpha_i (Aczel 1966, the same step Paper 1 already uses). Writing x as the coordinate-wise product of (x_1, 1, ..., 1), (1, x_2, 1, ..., 1), ... and applying the equation N - 1 times gives F(x) = prod h_i(x_i) = prod x_i^alpha_i. So f = k prod x_i^alpha_i with k = f(1).

Under N, f increasing in x_i forces alpha_i > 0, and then x_i -> 0 sends f -> 0. QED.

### What changed

| Paper 1 v2 | This note |
|---|---|
| 5 axioms | 3 axioms |
| Product form assumed (Axiom 5) | Product form derived |
| Zero-collapse stated as axiom, shown redundant | Zero-collapse is a theorem: it follows from necessity |
| Common-scale homogeneity (needs a shared unit) | Per-dimension unit invariance (needs no shared unit) |
| Harmonic mean, CES rho<0, min() all satisfy Axioms 1-4 | All three fail Axiom U [CHECKED C4] |
| Homogeneity of degree alpha assumed | Derived, with alpha = sum of alpha_i |

Separability also stops being an assumption. "The contribution of x_i does not depend on x_j" is a consequence of the power law, not a premise.

### Theorem 2 (ordinal form) [CLASSICAL, proof sketch]

Many composite scores are only used to rank. The weaker requirement is that rankings survive a change of units:

**Axiom U-ord.** f(x) >= f(y) if and only if f(lambda * x) >= f(lambda * y), for every lambda.

**Claim.** U-ord, C and N hold if and only if f(x) = psi(prod x_i^alpha_i) for a strictly increasing continuous psi and alpha_i > 0.

*Sketch.* In log coordinates U-ord says the ordering induced by f on R^N is invariant under every translation. A continuous, strictly monotone, translation-invariant weak order on R^N has parallel hyperplanes as indifference sets, so it is represented by a linear functional sum alpha_i log x_i. This is the ratio-scale social welfare ordering result (Tsui and Weymark 1997) and the basis of Ebert and Welsch (2004). The harmonic mean fails it: there are pairs A, B whose ranking flips when one dimension is re-expressed in different units [CHECKED C5].

This is the form to use in Paper 4. An index built by adding or averaging dimensions with different units produces rankings that depend on the units chosen. Only the weighted geometric form does not.

---

## 3. The map: zero-collapse is a line, MC is a point on it

**Proposition 3** [CLASSICAL, needs written proof for general weights and degree]. Suppose f is continuous, strictly increasing, homothetic, and additively separable in the general sense f(x) = h(sum g_i(x_i)). Then f is a monotone transform of the CES family

    (sum a_i x_i^rho)^(1/rho),  rho != 0,      or      prod x_i^a_i  (the rho -> 0 limit).

This is Bergson's theorem (1936); for the symmetric mean case it is Hardy, Littlewood and Polya, Theorem 84. Zero-collapse then holds exactly when rho <= 0 [CHECKED C3].

So the family of zero-collapsing compositions is a line indexed by rho:

    rho = 1        additive. Perfect substitutes. No zero-collapse.
    0 < rho < 1    partly substitutable. No zero-collapse.
    rho = 0        MULTIPLICATIVE (MC). Zero-collapse. The only unit-free member.
    rho < 0        zero-collapse, tighter bottleneck than MC (harmonic mean at rho = -1).
    rho -> -inf    min(). Liebig's Law of the Minimum. Pure bottleneck.

**The improved statement of the law.** Non-substitutability does not single out multiplication. Non-substitutability plus the absence of a common unit does. Every other zero-collapsing composition adds its terms before it does anything else, and you can only add quantities that share a unit.

That is a sharper claim than "multiply, do not add", and it tells you when MC is *not* the right zero-collapse model: when the dimensions genuinely share a unit (probabilities, shares of one budget, the same nutrient from different sources), the whole rho <= 0 line is open and rho has to be estimated.

---

## 4. What survives, what changes

**4.1 The audits survive unchanged.** The hidden-zero results (V-Dem, HDI, POSTCOG) test additive scoring against zero-collapsing scoring. They hold for every rho <= 0, not just rho = 0.

**4.2 Boundary of Theorem 1: bounded index scores.** V-Dem components and HDI sub-indices live on [0, 1] with a fixed top. They are not ratio scales with a free unit, so Axiom U is not automatically granted for them. For those domains the theorem does not pick the product over the harmonic mean or min(); the case for the product there has to rest on Paper 2 or on data. This should be said in the paper.

**4.3 The marginal inversion, corrected.** For the power law

    (df/dx_i) / (df/dx_j) = (alpha_i / x_i) / (alpha_j / x_j)      [CHECKED C7]

for every choice of exponents. With equal unit costs, the best dimension to invest in is the one with the largest alpha_i / x_i: the weakest relative to its weight. That is the binding-constraint principle, and it is exact. "df/dx_i is steepest when x_i is smallest" should be removed.

**4.4 The inversion gets stronger down the line.** With equal weights and one input at 0.2 against two at 1.0, the scarce input's share of total marginal product is 0.33 at rho = 1, 0.71 at rho = 0, 0.93 at rho = -1, 1.00 at rho = -3 [CHECKED C8]. Paper 3's allocation argument does not depend on rho being exactly 0. It holds on the whole zero-collapse side and tightens as rho falls.

**4.5 Negative exponents.** Theorem 1 without Axiom N gives real exponents. alpha_i > 0 is a necessary dimension (zero-collapse). alpha_i < 0 is an inhibitor. The fitted "multiplicative model" in several of Paper 1's datasets contains negative exponents (section 5), which means those fits are power laws but are not all-dimensions-necessary laws. The paper currently presents them as the second while fitting the first.

---

## 5. Where the data sits on the line [MEASURED]

Method: fit the CES family in log space with inputs normalised by their geometric means, estimate rho with a bootstrap 95% interval (200 resamples; clustered by country for Penn World Table). The rho -> 0 neighbourhood uses the exact series, so the estimator is stable at 0; on synthetic data with true rho of -1.0, -0.3, 0.0, 0.5 it returned -1.007, -0.297, -0.010, 0.497. Inputs with a negative power-law exponent enter as reciprocals. Script: `data/tests/rho_profile_test.py`.

| Dataset | n | rho-hat | 95% interval | Side of the line |
|---|---|---|---|---|
| Concrete strength, 5 always-present ingredients | 1,030 | -0.30 | -0.35 to -0.22 | zero-collapse, slightly tighter than MC |
| Concrete strength, cement+slag+ash pooled as binder | 1,030 | -0.20 | -0.26 to -0.15 | zero-collapse, slightly tighter than MC |
| Abalone age | 4,175 | -0.015 | -0.023 to -0.005 | at MC for practical purposes |
| California housing value | 20,433 | +0.53 | +0.47 to +0.58 | partly substitutable |
| Penn World Table: output on capital, labour | 9,479 | +0.43 | +0.24 to +0.62 | partly substitutable |
| Penn World Table: capital, human-capital-adjusted labour | 8,201 | +0.69 | +0.48 to +0.96 | partly substitutable |

**Findings.**

1. **Replication.** The unconstrained power-law fit on the five always-present concrete ingredients gives Spearman 0.885, the figure in Paper 1 Table 1 (additive 0.770, also matching).

2. **The flagship fit has negative exponents.** In that concrete model the exponents are cement +0.49, age +0.29, water -2.29, coarse aggregate -1.62, fine aggregate -1.59. Three of five "dimensions" lower strength as they rise. The fitted law says zero water gives infinite strength, the opposite of zero-collapse. What the data supports is a power law in ratios (strength rises with cement relative to water and to aggregate, which is Abrams' water-cement law). Pooling the cementitious materials into one binder dimension removes most of this (only water stays negative, at -0.12) and fits better: Spearman 0.907.

3. **Three ingredients are not zero-collapse dimensions at all.** Slag, fly ash and superplasticizer are zero in many rows where strength is positive.

4. **The Spearman comparison in Paper 1 does not measure what it claims.** Housing and Penn World Table both show the multiplicative model ahead of or tied with the additive one on Spearman, while rho is clearly positive in both: the data is on the substitutable side. The comparison pits a log-space fit against a levels fit, so it mixes the composition question with the error structure. rho with an interval answers the composition question directly. Recommend replacing Table 1's Delta column with rho-hat and its interval.

5. **Exact MC is rejected everywhere at these sample sizes** by the joint test on pairwise imbalance terms (all p < 1e-5), as any exact functional form will be with thousands of observations. Effect sizes are small: adding all pairwise terms raises log-space R-squared by 0.055 (concrete), 0.023 (abalone), 0.041 (housing), 0.003 (PWT).

6. **Penn World Table matches the paper's own scope condition.** Capital and labour substitute; MC is not expected to hold and does not. This is pooled country-year data with no productivity or fixed-effect controls, so the number itself should not be quoted as an elasticity estimate.

**Not covered:** Agriculture (n=53), Infrastructure to GDP (160), Child Survival (240), HDI Components (66). They come from the World Bank API, which is not reachable from the cloud session, and the raw files are not in this repo. Clinical EEG and Network Sync need the files on G7.

**Scorecard on these four datasets:** one sits on the zero-collapse side near MC, one at MC, two on the substitutable side. That is weaker than "seven of eight" and more defensible, because each row now has an interval and a direction.

---

## 6. Prior art to read before revising Paper 1

Axiom U belongs to the "meaningfulness" tradition in measurement theory. The theorem is not new mathematics; the application to emergence, the zero-collapse reading, the audit and the allocation result are the contribution. Existence of each item below was confirmed on 2026-11-12; the exact theorem statements have not been read.

- Luce, R. D. (1959). On the possible psychophysical laws. *Psychological Review*. Ratio scale in, ratio scale out implies a power function.
- Aczel, J., Roberts, F. S., Rosenbaum, Z. (1986). On scientific laws without dimensional constants. *J. Math. Anal. Appl.* doi:10.1016/0022-247X(86)90162-9. The several-variable version, with and without independent admissible transformations.
- Ebert, U., Welsch, H. (2004). Meaningful environmental indices: a social choice approach. *J. Environmental Economics and Management* 47(2), 270-283. Applies the idea to composite indices; closest prior art to Paper 4.
- Tsui, K.-Y., Weymark, J. (1997). Social welfare orderings for ratio-scale measurable utilities. Source for Theorem 2.
- Bridgman, P. W. (1922). *Dimensional Analysis*. The physics ancestor: derived quantities are products of powers.
- Bergson (Burk), A. (1936). Source for Proposition 3. Not yet confirmed; from memory.

Paper 1 currently positions itself against Luce (1965). Luce (1959) and Aczel-Roberts-Rosenbaum (1986) are closer and must be cited.

---

## 7. Changes required in Paper 1 v2

1. Section 2: replace Axioms 4 and 5 with Axiom U; restate the theorem as Theorem 1 above; move zero-collapse from axiom to corollary.
2. Section 2.4: delete "dropping homogeneity opens the CES family". Replace with section 3 of this note.
3. Abstract and section 1: replace "there is no third option" with the unit-free statement.
4. Section 3: add Luce 1959, Aczel-Roberts-Rosenbaum 1986, Ebert-Welsch 2004. Reclassify Sprengel-Liebig as a discovery of zero-collapse (rho -> -infinity), not of the product.
5. Section 4: report rho with intervals; disclose negative exponents; state how zeros in inputs were handled.
6. Section 4.4: replace the unstable-estimator paragraph with the normalised CES method.
7. Section 5 and abstract: restate the marginal inversion as the ratio alpha_i / x_i.
8. Section 6: add the bounded-index boundary (4.2).

## 8. Open

- Full proofs or checked citations for Theorem 2 and Proposition 3.
- rho on the four World Bank datasets and the two G7 datasets.
- Fisher-volume link (Paper 2): the volume element transforms by a product of per-coordinate factors under per-coordinate reparameterisation, which is Axiom U. Worth one paragraph in Paper 2 if it holds up.
- Whether Axiom U can be argued for bounded indices via an odds or log transform.
