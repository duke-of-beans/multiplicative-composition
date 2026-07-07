# Zero-Collapse and Resource Allocation in Multiplicative Systems

**David Kirsch**

Working Paper — June 2026

---

## Abstract

Where should a society invest its marginal dollar? This paper presents a mathematical framework that answers the question directly. When independent dimensions of human or economic capacity compose multiplicatively rather than additively, the marginal return on investment in any dimension is inversely proportional to that dimension's current value. The lowest dimension always yields the highest return. This property, which we term *marginal inversion*, follows from the calculus of the multiplicative form and requires no economic theory beyond the composition structure itself. A second property, *zero-collapse*, predicts that any dimension reaching zero eliminates the product entirely, producing cliff-like rather than proportional decline. We validate the framework empirically across three scales: individual outcomes (Housing First programs, N=950 RCT), national crisis response (Greece/Iceland and US/UK natural experiments), and societal collapse (Venezuela and Zimbabwe governance trajectories using World Bank WGI data). A 162-country cross-sectional analysis using World Bank indicators confirms multiplicative composition of national output, with fitted exponents placing human capital (0.79), infrastructure (0.50), and health (0.42) as the operative dimensions. We then examine the framework's implications for the historical debate between supply-side and demand-side economic policy, finding that fifty years of tax-cut data across eighteen OECD nations shows no statistically significant growth effect from top-end investment, while randomized trials of bottom-end investment produce fiscal multipliers of 2.5–4.3×. The multiplicative framework predicts both findings: the derivative is flat at high values and steep at low values. Current US fiscal policy (P.L. 119-21) simultaneously reduces the lowest dimensions (Medicaid, SNAP) while subsidizing the highest (top-bracket tax relief), an allocation the framework identifies as provably suboptimal.

---

## 1. Introduction

The question of where public investment produces the greatest return has been debated for decades without mathematical resolution. Supply-side economics argues that reducing taxes on capital formation and high earners generates growth that distributes broadly. Demand-side economics argues that direct investment in lower-income populations generates higher multiplier effects. Both sides marshal empirical evidence. Neither offers a mathematical proof of optimality.

This paper provides one.

The argument rests on a structural property of how independent dimensions compose. If a person's capacity to function depends on housing, healthcare, education, financial stability, and social connection, and if these dimensions compose multiplicatively, then the marginal return on investment in any single dimension scales as the inverse of that dimension's value. This is not an assumption about human behavior or market dynamics. It is a consequence of the composition function.

The multiplicative form is not arbitrary. Kirsch (2026) proves that given five axioms — zero-collapse (absence of any dimension produces zero output), continuity, strict monotonicity, scale consistency, and dimensional independence — the multiplicative power-law form is the unique valid composition function. No additive alternative satisfies these constraints. The proof follows Aczél's (1966) functional equations framework and has been validated empirically across eight domains including neural dynamics, network synchronization, ecosystem resilience, and macroeconomic output.

This paper applies two properties of the multiplicative form to questions of social and economic policy. Section 2 develops the mathematical framework. Section 3 presents empirical validation at three scales. Section 4 examines the marginal inversion property against the supply-side/demand-side debate. Section 5 applies the framework to current US fiscal policy. Section 6 discusses limitations and falsification criteria.

## 2. Mathematical Framework

### 2.1 The Multiplicative Composition Form

Let x₁, x₂, ..., xₙ ∈ ℝ₊ represent n independently measurable dimensions of a system. Define the emergent output E as a function of these dimensions:

**E = k · ∏ᵢ xᵢ^αᵢ**

where k > 0 is a scaling constant and αᵢ > 0 are dimension-specific exponents with Σαᵢ = κ for some fixed degree of homogeneity κ > 0.

Kirsch (2026) proves this form is uniquely determined by five axioms: (A1) if any xᵢ = 0, then E = 0; (A2) E is continuous on ℝ₊ⁿ; (A3) ∂E/∂xᵢ > 0 for all i when all xⱼ > 0; (A4) E(λx) = λᵏE(x) for fixed k; (A5) E is separable, i.e., the contribution of each dimension depends only on its own value. The proof proceeds by log-transformation: under homogeneity and separability, log E is linear in each log xᵢ, yielding the power-law product form upon exponentiation. This result is a special case of Aczél's (1966) characterization of continuous multiplicative homomorphisms on ℝ₊ⁿ.

### 2.2 Zero-Collapse

From (A1) directly: if any dimension xⱼ = 0, then E = k · 0^αⱼ · ∏ᵢ≠ⱼ xᵢ^αᵢ = 0, regardless of the values of all other dimensions.

This property distinguishes the multiplicative form from the additive form f = Σ wᵢxᵢ, where zeroing one dimension reduces output by only that dimension's weighted contribution. Under multiplicative composition, the loss is total. The system does not degrade proportionally; it collapses.

The empirical signature of zero-collapse is disproportionate decline. If output depends on four dimensions and one reaches zero, the additive model predicts a decline of approximately 25% (one-quarter of the weighted sum). The multiplicative model predicts a decline approaching 100%. The magnitude of observed decline therefore discriminates between the two composition structures.

### 2.3 Marginal Inversion

The partial derivative of E with respect to any dimension xᵢ is:

**∂E/∂xᵢ = αᵢ · E / xᵢ**

The marginal return on investment in dimension xᵢ is inversely proportional to xᵢ. As xᵢ approaches zero, the derivative diverges. As xᵢ grows large, the derivative approaches zero. The return is highest where the dimension is lowest.

This result has a direct policy interpretation. Given a fixed budget to allocate across dimensions, the allocation that maximizes total output invests most heavily in the dimension with the lowest current value. The optimal allocation is always bottom-up. This follows from the convexity of the objective in log-space: log E = log k + Σ αᵢ log xᵢ is concave in the allocations, and the maximum of a concave function subject to a budget constraint is achieved at the corner where marginal returns are equalized — which, given the 1/xᵢ structure, requires investing most in the smallest xᵢ.

This property, which we term *marginal inversion*, holds for any multiplicative system regardless of the specific values of αᵢ. It requires no assumptions about market structure, individual behavior, or institutional design. It is a structural consequence of how the dimensions compose.

### 2.4 Relationship to Existing Frameworks

The multiplicative form is not new to economics. Cobb and Douglas (1928) proposed Y = A · L^α · K^β for aggregate production, and the Penn World Tables continue to use this structure. Hausmann, Rodrik, and Velasco (2005) articulated the "binding constraints" framework for growth diagnostics, arguing that the most binding constraint should receive priority investment — a heuristic statement of marginal inversion.

What is new is the uniqueness proof. Cobb-Douglas was proposed as a convenient functional form. Binding constraints were stated as a diagnostic heuristic. The axiomatic proof establishes that given reasonable constraints on how independent dimensions compose, the multiplicative form is not a choice among alternatives. It is the only form that survives.

The information-geometric derivation (Kirsch, 2026b) provides a second, independent foundation. The volume element of the Fisher information metric on a product manifold of independent parameters is √(det g(θ)) = ∏ᵢ √gᵢᵢ(θᵢ), which is structurally identical to the multiplicative composition form. This connects the result to the natural geometry of probability distributions: the multiplicative form measures distinguishable structure in observation space, not total information capacity. The two derivations — axiomatic and geometric — converge on the same functional form from different starting points.

## 3. Empirical Evidence Across Three Scales

The multiplicative framework generates two testable predictions: (1) interventions addressing the lowest dimension produce disproportionately large returns, and (2) collapse of any single dimension produces disproportionate — not proportional — decline in output. We evaluate these predictions at three scales: the individual, the national, and the societal.

### 3.1 Individual Scale: Housing First

The Housing First approach to homelessness provides the clearest test of zero-collapse at the individual level. If a person's functional capacity composes multiplicatively from housing, healthcare, education, employment, and social connection, then a person with zero housing should receive zero return from investment in any other dimension. The conventional "treatment first" model, which provides job training, clinical services, and other supports contingent on sobriety or program compliance, implicitly assumes additive composition — that each service adds independent value regardless of housing status.

The data resolves this. The CDC Community Preventive Services Task Force conducted a systematic review of 26 studies and found that Housing First programs increase housing stability, reduce homelessness, and improve quality of life, with a cost-benefit ratio of $1.44 returned per $1.00 invested (CDC/CPSTF, 2023). The Canadian At Home/Chez Soi trial, a multi-site randomized controlled experiment (N=950, five cities, 2009–2011), found that Housing First with Assertive Community Treatment achieved 73% housing stability at 12 months versus 31% for treatment-as-usual, with 69% of program costs offset by reductions in emergency services, shelter use, and hospitalization (Aubry et al., 2020).

Finland's national implementation provides the population-level result. Following adoption of Housing First as national policy in 2008, long-term homelessness declined 68% over fourteen years, at a total investment of approximately €270 million. Finland is the only European Union member state in which homelessness has declined during this period (Pathfinders, 2024).

These outcomes are consistent with multiplicative composition and inconsistent with the additive model. Under additive composition, treatment-first programs should produce returns proportional to the services provided, regardless of housing status. They do not. The return is approximately zero until housing is addressed, then positive once it is — the signature of a binding zero in a multiplicative product.

### 3.2 National Scale: Crisis Response

The 2008–2010 financial crisis generated a natural experiment in fiscal policy. Countries facing similar shocks chose opposite allocations: some invested in the lowest dimensions (safety nets, employment support, consumer protection), while others cut them (austerity programs targeting social spending, healthcare, and public services). The multiplicative framework predicts the former should recover faster.

**Greece and Iceland.** Both economies collapsed in 2008. Greece, under troika-imposed austerity, cut social spending, pensions, healthcare, and public employment. GDP fell 26% over five years; unemployment peaked at 28%; youth unemployment reached 58%; the debt-to-GDP ratio — the stated target of austerity — rose from 130% to 180% (Eurostat; Danchev, 2024). Iceland let its banks fail, protected domestic depositors, prosecuted 29 bankers, and invested in its social safety net while allowing the króna to devalue. GDP returned to pre-crisis levels by 2015; unemployment fell to 3.8%; IMF loans were repaid ahead of schedule (Wharton, 2018; Oxford Academic, 2022). The country that invested in its lowest dimensions recovered. The country that cut them did not.

**United States and United Kingdom.** The US passed the American Recovery and Reinvestment Act (ARRA), an $836 billion stimulus targeting unemployment compensation, state fiscal relief, infrastructure, and food assistance. The Congressional Budget Office estimated ARRA raised GDP by 0.7–4.1% and created up to 2.8 million full-time-equivalent jobs at peak effect (CBO, 2015). The UK pursued austerity under the Cameron government: real capital spending fell 31.9% between 2009/10 and 2012/13 (Institute for Government). Emergency food parcel distribution rose from approximately 60,000 to 2.89 million (Trussell Trust/House of Commons Library, 2025). After fourteen years, government debt rose from 65% to 98% of GDP.

Blanchard and Leigh (2013) demonstrated that the IMF's own forecasting models had underestimated the fiscal multiplier, assuming 0.5 when the actual multiplier was 0.9–1.7. Cutting the lowest dimensions cost approximately twice what the models predicted. The error was structural: the models assumed additive composition, where removing one dollar of government spending removes one dollar of output. A multiplicative system amplifies the removal.

### 3.3 Societal Scale: Failed States

The zero-collapse property predicts that if a single dimension of societal capacity reaches zero, total output collapses regardless of the strength of other dimensions. Venezuela and Zimbabwe provide the test.

**Venezuela.** OPEC's 2025 Annual Statistical Bulletin records Venezuelan proven oil reserves at approximately 303 billion barrels — roughly 18% of the global total, the largest national endowment on record. GDP peaked at $372.6 billion in 2012. By 2020, it had fallen approximately 88%, a contraction deeper than the US Great Depression and exceeding Syria's wartime decline (IMF; Institute of International Finance, 2019). Per capita income fell from $12,607 to $1,509. The resource endowment did not change. What collapsed was institutional quality: World Bank Worldwide Governance Indicators show Rule of Law declining from −0.76 (1998) to −2.35 (2020), and Transparency International's Corruption Perceptions Index falling from 28 to 10 (2001–2024), placing Venezuela among the three lowest-ranked countries globally.

**Zimbabwe.** Following the land-reform program beginning in 2000, food production fell approximately 60% over a decade. Hyperinflation peaked at 79.6 billion percent per month in November 2008, with prices doubling approximately every 24 hours (Hanke and Kwok, 2009). GDP per capita declined from $1,640 to $661 (1998–2008), reaching levels last observed in 1952. The World Bank's Rule of Law indicator fell to the 1st percentile globally by 2008.

In both cases, substantial dimensions survived — oil reserves, arable land, human capital, physical infrastructure. One dimension (institutional trust/governance) approached zero. An additive model predicts that the loss of one of four dimensions should reduce output by approximately 25%. Observed decline was 78–90%. This ratio — observed decline three to four times greater than additive prediction — is the empirical signature of zero-collapse in a multiplicative system.

### 3.4 Cross-Country Validation

To test multiplicative composition at the macroeconomic level, we regressed GDP output on three independently measured dimensions — human capital index, infrastructure quality, and health outcomes — across 162 countries using World Bank data (Kirsch, 2026). The multiplicative model achieved a Spearman rank correlation of 0.953, with fitted exponents of 0.79 (human capital), 0.50 (infrastructure), and 0.42 (health). The additive model achieved 0.951.

The exponent ordering is itself informative. Health carries the lowest exponent (0.42), which under the marginal inversion property means it contributes the steepest marginal return at low values. This is consistent with the development economics literature finding that health interventions in low-income countries produce disproportionately large returns (Bloom et al., 2004; Jamison et al., 2013).

## 4. Marginal Inversion and the Supply-Side Question

The marginal inversion property generates a specific, testable prediction about fiscal policy. If societal output composes multiplicatively, then investment in dimensions that are already large produces returns near zero, while investment in dimensions near zero produces large returns. Supply-side economics, which directs tax relief and deregulation toward high-income earners and capital holders, invests in the highest dimensions. The multiplicative framework predicts this should produce negligible returns.

### 4.1 Evidence on Top-End Investment

Hope and Limberg (2022) constructed a latent indicator of taxes on the rich and identified 30 instances of major tax cuts across 18 OECD countries from 1965 to 2015. Their findings: tax cuts for the rich produced no statistically significant effect on real GDP per capita and no effect on unemployment. The only measurable outcome was higher income concentration in the top 1%. The study, published in *Socio-Economic Review* after an initial working paper release in 2020, represents the largest cross-national analysis of supply-side tax policy to date.

Hungerford (2012) examined US top marginal tax rates from 1945 to 2010 for the Congressional Research Service. When the top rate exceeded 90% in the 1950s, real GDP growth averaged 4.2%. When it fell to 35% in the 2000s, growth averaged 1.7%. The analysis found no association between top-rate reductions and saving, investment, or productivity growth, but found a statistically significant association with rising top-income concentration (top 0.1% income share rising from 4.2% to 12.3%).

Ostry, Berg, and Tsangarides (2014), in an IMF Staff Discussion Note authorized by Olivier Blanchard, concluded that the equity-efficiency trade-off is "largely illusory." Lower net inequality was robustly associated with faster and more durable growth, and redistribution was generally growth-neutral or growth-positive. Only in extreme cases was there evidence of growth-reducing redistribution.

The state of Kansas provides a controlled demonstration. Governor Brownback implemented what he described as a "real live experiment" in supply-side economics beginning in 2012: the top income tax rate was cut by approximately 30%, and pass-through business income was taxed at zero. Over the following four years, Kansas real GDP grew 3.8% against approximately 7% nationally. State revenue collapsed, bond ratings were cut, and education and infrastructure funding were reduced. In June 2017, a Republican-controlled legislature repealed the tax cuts over the governor's veto (Gale, 2017; CBPP; Tax Policy Center).

The multiplicative framework predicts these findings. When xᵢ is large, ∂E/∂xᵢ ≈ 0. Investment at the top of the distribution invests where the derivative is flattest. The predicted return is negligible, and the observed return is negligible.

### 4.2 Evidence on Bottom-End Investment

Egger, Haushofer, Miguel, Niehaus, and Walker (2022) studied unconditional cash transfers of approximately $1,000 to over 10,500 poor households across 653 randomized villages in rural Kenya — a fiscal transfer exceeding 15% of local GDP. The authors estimated a local fiscal multiplier of 2.5 (expenditure approach) to 2.7 (income approach), with large positive spillovers to non-recipient households and enterprises and minimal price inflation. Published in *Econometrica*, this remains the largest randomized evaluation of cash transfer general equilibrium effects.

Banerjee, Duflo, and collaborators (2015) tested the BRAC "graduation" model across six countries (Ethiopia, Ghana, Honduras, India, Pakistan, Peru) in a randomized trial with approximately 11,000 households. The model provides a simultaneous, multi-dimensional intervention: productive asset transfer, consumption support, skills training, regular coaching, savings facilitation, and health services. Returns ranged from 133% (Ghana) to 433% (India), with effects persisting and growing at seven-year follow-up. The multi-dimensional package outperformed single-component interventions tested within the same trial — an empirical confirmation that addressing multiple low dimensions simultaneously (the multiplicative strategy) outperforms addressing them individually (the additive strategy).

Chetty, Hendren, and Katz (2016) re-analyzed the Moving to Opportunity experiment using tax records for approximately 4,600 families across five US cities. Children who moved to lower-poverty neighborhoods before age 13 earned $3,477 more per year as adults (31% above the control mean of $11,270), attended college at higher rates, and had lower rates of single parenthood. Returns were largest for children starting from the lowest baseline and at the youngest ages — the empirical signature of marginal inversion.

### 4.3 The Juxtaposition

Placed in direct comparison: fifty years of top-end tax cuts across eighteen countries produce zero measurable growth. Six randomized trials of bottom-end investment produce multipliers of 2.5× to 4.3×. The multiplicative framework predicts both findings from the same structural property: the derivative is flat at high values and steep at low values. Top-end investment operates where ∂E/∂xᵢ ≈ 0. Bottom-end investment operates where ∂E/∂xᵢ is maximal. The question of where to invest is resolved by the composition structure, not by ideological preference.

## 5. Current Application: US Fiscal Policy (2025)

The One Big Beautiful Bill Act (P.L. 119-21), signed into law on July 4, 2025, provides a real-time application of the framework. The law reduces Medicaid funding by approximately $911 billion to $1.02 trillion and SNAP funding by approximately $186 billion over ten years (CBO, July 2025). Simultaneously, it makes permanent the 2017 individual income tax reductions, raises the estate and gift tax exemption to $15 million, and restores 100% bonus depreciation for business investment.

The Congressional Budget Office's distributional analysis (August 11, 2025) found that the law reduces resources for the bottom income decile by 3.1% while increasing resources for the top decile by 2.7%. The Tax Policy Center estimated that nearly 60% of the law's tax benefits accrue to households in the top income quintile, with the top 1% (incomes averaging approximately $2.7 million) receiving an average net tax reduction of $66,000.

In the language of the multiplicative framework, this law cuts the lowest dimensions (health coverage, food security) while subsidizing the highest (top-bracket income, corporate profitability, intergenerational wealth transfer). The marginal inversion property predicts this is the least efficient allocation available: it invests where the derivative is flattest and divests from where it is steepest.

Early indicators are consistent with the framework's predictions. The HUD 2024 Annual Homelessness Assessment Report recorded 771,480 people experiencing homelessness, an 18% increase and the highest count since data collection began in 2007. Child poverty had already doubled from 5.2% to 12.4% following the expiration of the expanded Child Tax Credit in 2022, the largest single-year increase in the Supplemental Poverty Measure on record (Census Bureau, 2023). In November 2025, SNAP funding lapsed for the first time in the program's history during a government shutdown, leaving approximately 42 million recipients without benefits (NPR; CNBC, 2025).

The institutional trust dimension, which the zero-collapse property identifies as the most dangerous to lose, is trending downward across multiple independent indices. The V-Dem Institute downgraded the United States from "liberal democracy" to "electoral democracy" for the first time in over fifty years (Lindberg et al., *Democratization*, 2025). Freedom House recorded the US at 81/100, its lowest score since the current methodology began in 2002 (*Freedom in the World*, 2026). The Economist Intelligence Unit's Democracy Index fell to 7.65, the lowest since the index was created in 2006.

None of these indicators individually constitutes a zero. But the multiplicative model's prediction is not that collapse is imminent — it is that the marginal cost of further reductions in these dimensions is accelerating, and that the return on investment in restoring them is correspondingly high.


## 6. Limitations and Falsification

Several limitations warrant explicit statement.

First, the cross-country analysis (Section 3.4) is cross-sectional, not panel. The 162-country result demonstrates that GDP output is well-described by a multiplicative function of human capital, infrastructure, and health, but does not establish the temporal dynamics of investment reallocation. A panel analysis with country and year fixed effects, using time-varying dimension measures, would strengthen the causal interpretation. This extension is planned.

Second, the CES elasticity parameter ρ, estimated across multiple domains using differential evolution and basin-hopping optimization, does not converge to zero in any domain (estimated range: −0.28 to +0.38). The pure multiplicative form (ρ = 0) is therefore an approximation. In every domain tested, the multiplicative model outperforms the additive model on both loss metrics and rank correlation, but the exact composition lies on a CES continuum between multiplicative and complementary forms. The marginal inversion result holds qualitatively for all ρ < 1 (i.e., for all forms more complementary than additive), but the quantitative sharpness of the inversion depends on ρ.

Third, the Housing First, austerity, and failed-state evidence is observational. The At Home/Chez Soi trial is the exception (randomized, controlled), but the Greece/Iceland and US/UK comparisons are natural experiments with confounds: the countries differ in monetary regime, currency sovereignty, eurozone membership, and labor market structure. The direction of the results is consistent across all comparisons, but the precise magnitude attributable to fiscal allocation is not identified.

Fourth, the policy application (Section 5) projects forward from early indicators. The Medicaid work requirements enacted in P.L. 119-21 take effect January 1, 2027. The full effect of the law's spending reductions will unfold over a decade. The framework predicts cliff-like deterioration as dimensions approach zero; whether the enacted reductions are sufficient to trigger this threshold is an empirical question that cannot yet be answered.

**Falsification criteria.** The thesis would be weakened by any of the following: (a) a high-quality randomized trial demonstrating that single-dimension interventions match the returns of the BRAC multi-dimensional package, contradicting the multiplicative advantage; (b) a credible cross-national study finding statistically significant GDP growth from top-end tax cuts after controlling for the covariates in Hope and Limberg (2022); (c) a case in which a country's institutional quality fell to the bottom decile of WGI scores without producing disproportionate output decline; or (d) implementation of the OBBBA Medicaid provisions resulting in coverage losses substantially below CBO's projected 5.3 million. To our knowledge, none of these currently exists in the published literature.


## 7. Conclusion

The mathematics of multiplicative composition resolves the resource allocation question without recourse to economic theory, political philosophy, or moral argument. When independent dimensions compose multiplicatively, the marginal return is highest where the dimension is lowest. Investment at the bottom is not a compassionate alternative to investment at the top. It is the mathematically optimal allocation. The compassionate allocation and the efficient allocation are structurally identical.

This result reframes the supply-side/demand-side debate. For decades, the question has been treated as ideological: should we prioritize growth (supply-side) or equity (demand-side)? The multiplicative framework dissolves the dichotomy. The growth-maximizing allocation and the equity-maximizing allocation are the same allocation, because the steepest part of the growth curve is at the bottom of the distribution. Fifty years of cross-national data on top-end investment and six randomized trials of bottom-end investment confirm this empirically.

The zero-collapse property adds urgency. Systems that lose a single dimension do not degrade gradually. They fall off a cliff. Venezuela's 303 billion barrels of oil and Zimbabwe's agricultural base and educated workforce were not sufficient to prevent collapse once institutional trust reached the bottom percentile. The multiplicative model predicts this outcome; the additive model does not.

Current US fiscal policy (P.L. 119-21) simultaneously reduces the lowest dimensions of the most vulnerable populations while concentrating resources in the highest dimensions of the most advantaged. The framework developed in this paper identifies this as a provably suboptimal allocation — not as a matter of values, but of structure.

---

## References

Aczél, J. (1966). *Lectures on Functional Equations and Their Applications*. Academic Press.

Aubry, T., et al. (2020). Cost-effectiveness of Housing First with Assertive Community Treatment. *Psychiatric Services*, 71(12). DOI: 10.1176/appi.ps.202000029.

Banerjee, A., Duflo, E., et al. (2015). A multifaceted program causes lasting progress for the very poor: Evidence from six countries. *Science*, 348(6236), 1260799. DOI: 10.1126/science.1260799.

Blanchard, O. and Leigh, D. (2013). Growth forecast errors and fiscal multipliers. IMF Working Paper 13/1.

Bloom, D., Canning, D., and Sevilla, J. (2004). The effect of health on economic growth: A production function approach. *World Development*, 32(1), 1–13.

Centers for Disease Control and Prevention, Community Preventive Services Task Force (2023). Housing First programs: Systematic review. CDC/CPSTF.

Chetty, R., Hendren, N., and Katz, L.F. (2016). The effects of exposure to better neighborhoods on children: New evidence from the Moving to Opportunity experiment. *American Economic Review*, 106(4), 855–902. DOI: 10.1257/aer.20150572.

Cobb, C.W. and Douglas, P.H. (1928). A theory of production. *American Economic Review*, 18(1), 139–165.

Congressional Budget Office (2015). Estimated impact of the American Recovery and Reinvestment Act on employment and economic output. CBO Publications 25005, 25075, 49958.

Congressional Budget Office (2025). Distributional analysis of the One Big Beautiful Bill Act (P.L. 119-21). August 11, 2025.

Danchev, S. (2024). Equally poorer: Inequality and the Greek debt crisis. *Fiscal Studies*.

Egger, D., Haushofer, J., Miguel, E., Niehaus, P., and Walker, M. (2022). General equilibrium effects of cash transfers: Experimental evidence from Kenya. *Econometrica*, 90(6), 2603–2643. DOI: 10.3982/ECTA17945.

Gale, W.G. (2017). The Kansas tax cut experiment. Brookings Institution.

Hanke, S. and Kwok, A. (2009). On the measurement of Zimbabwe's hyperinflation. *Cato Journal*, 29(2), 353–364.

Hausmann, R., Rodrik, D., and Velasco, A. (2005). Growth diagnostics. John F. Kennedy School of Government, Harvard University.

Hope, D. and Limberg, J. (2022). The economic consequences of major tax cuts for the rich. *Socio-Economic Review*, 20(2), 539–559. DOI: 10.1093/ser/mwab061.

Hungerford, T.L. (2012). Taxes and the economy: An economic analysis of the top tax rates since 1945. Congressional Research Service Report R42729.

Jamison, D.T., et al. (2013). Global health 2035: A world converging within a generation. *The Lancet*, 382(9908), 1898–1955.

Kirsch, D. (2026). Multiplicative composition of independent dimensions in emergent systems. Working paper. Available at: https://davidkirsch.me/research.

Kirsch, D. (2026b). Emergence as information volume on statistical manifolds. Working paper.

Lindberg, S., et al. (2025). State of the world 2024: 25 years of autocratization. *Democratization*, 32.

OPEC (2025). Annual Statistical Bulletin 2025.

Ostry, J.D., Berg, A., and Tsangarides, C.G. (2014). Redistribution, inequality, and growth. IMF Staff Discussion Note 14/02.

Pathfinders (2024). Housing First policy: Finland.

U.S. Census Bureau (2023). Supplemental Poverty Measure: 2022.

U.S. Department of Housing and Urban Development (2024). Annual Homelessness Assessment Report to Congress, Part 1.

World Bank. Worldwide Governance Indicators. https://info.worldbank.org/governance/wgi/.

---

*Corresponding author: david@davidkirsch.me*
*Working paper. Comments welcome.*
