"""
rho_profile_test.py -- where on the zero-collapse line does each dataset sit?

Fits the N-input CES family in log space

    log y = b0 + nu * (1/rho) * log( sum_i a_i * z_i^rho ),   sum a_i = 1, a_i > 0

with z_i = x_i / geometric_mean(x_i) (normalised CES, so the weights a_i are
unit-free), and reports rho-hat with a bootstrap 95% interval.

    rho -> 0     multiplicative power law (Cobb-Douglas, the MC form)
    rho  < 0     zero-collapsing, MORE bottlenecked than MC (rho -> -inf is min())
    0 < rho <= 1 substitutable, no zero-collapse (rho = 1 is additive)

The rho -> 0 neighbourhood is evaluated with the exact second-order series
(weighted mean + rho/2 * weighted variance of logs), so the estimator is stable
at rho = 0. This replaces the unstable NLS described in Paper 1 section 4.4.

Also reports, per dataset: log-space R^2 at rho = 0 and at rho-hat, Spearman for
the multiplicative, CES and additive-in-levels fits, and a joint F-test of all
pairwise imbalance terms (L_i - L_j)^2 added to the log-linear model (the
N-input Kmenta test: under exact MC every such coefficient is zero).

Usage:  python rho_profile_test.py <data_dir> <out_json>
Data (public copies; not committed to this repo):
  concrete.csv  UCI Concrete Compressive Strength (Yeh 1998)
  abalone.csv   UCI Abalone (headerless)
  housing.csv   California Housing (Pace & Barry 1997)
  pwt10.01.rda  Penn World Table 10.01 (CRAN package pwt10)
"""
import json
import sys
import warnings

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.optimize import least_squares
from scipy.special import logsumexp, softmax
from scipy.stats import spearmanr

warnings.filterwarnings("ignore")
RNG = np.random.default_rng(20261112)
RHO_LO, RHO_HI = -8.0, 3.0


def ces_log(L, theta, rho):
    """(1/rho) * log sum a_i exp(rho L_i); exact series near rho = 0."""
    a = softmax(theta)
    if abs(rho) < 1e-3:
        m = L @ a
        v = (L ** 2) @ a - m ** 2
        return m + 0.5 * rho * v
    return logsumexp(rho * L + np.log(a), axis=1) / rho


def fit_ces(L, ly, rho_fixed=None, starts=None):
    n, k = L.shape
    X = np.column_stack([np.ones(n), L])

    def unpack(p):
        if rho_fixed is None:
            return p[:k], p[k], p[k + 1], p[k + 2]
        return p[:k], rho_fixed, p[k], p[k + 1]

    def resid(p):
        th, rho, nu, b0 = unpack(p)
        return b0 + nu * ces_log(L, th, rho) - ly

    # start from the Cobb-Douglas OLS solution
    b = np.linalg.lstsq(X, ly, rcond=None)[0]
    al = np.clip(b[1:], 1e-3, None)
    nu0 = al.sum()
    th0 = np.log(al / nu0)
    if starts is None:
        starts = [0.0, -1.0, 0.5, -3.0] if rho_fixed is None else [None]
    best = None
    for s in starts:
        if rho_fixed is None:
            p0 = np.concatenate([th0, [s, nu0, b[0]]])
            lo = np.concatenate([np.full(k, -30.0), [RHO_LO, -np.inf, -np.inf]])
            hi = np.concatenate([np.full(k, 30.0), [RHO_HI, np.inf, np.inf]])
        else:
            p0 = np.concatenate([th0, [nu0, b[0]]])
            lo = np.concatenate([np.full(k, -30.0), [-np.inf, -np.inf]])
            hi = np.concatenate([np.full(k, 30.0), [np.inf, np.inf]])
        try:
            r = least_squares(resid, p0, bounds=(lo, hi), method="trf", max_nfev=400)
        except Exception:
            continue
        if best is None or r.cost < best.cost:
            best = r
    th, rho, nu, b0 = unpack(best.x)
    return dict(rho=float(rho), nu=float(nu), b0=float(b0), a=softmax(th).tolist(),
                sse=float(2 * best.cost), pred=b0 + nu * ces_log(L, th, rho))


def r2(y, p):
    return float(1 - ((y - p) ** 2).sum() / ((y - y.mean()) ** 2).sum())


def analyse(name, df, ycol, xcols, cluster=None, n_boot=200, note=""):
    df = df[[ycol] + xcols + ([cluster] if cluster else [])].dropna()
    df = df[(df[[ycol] + xcols] > 0).all(axis=1)].reset_index(drop=True)
    y = df[ycol].to_numpy(float)
    X = df[xcols].to_numpy(float)
    ly = np.log(y)
    L = np.log(X)
    L = L - L.mean(axis=0)                      # divide by geometric means
    n, k = L.shape
    # Orientation: CES weights are positive, so an input that LOWERS the output
    # (e.g. water in concrete) enters as its reciprocal. Signs come from the
    # unconstrained log-linear (power-law) fit, which is then the rho = 0 member.
    b_ols = np.linalg.lstsq(np.column_stack([np.ones(n), L]), ly, rcond=None)[0][1:]
    sign = np.where(b_ols >= 0, 1.0, -1.0)
    L = L * sign

    cd = fit_ces(L, ly, rho_fixed=0.0)
    ces = fit_ces(L, ly)
    add = sm.OLS(y, sm.add_constant(X)).fit()

    # N-input Kmenta: joint test of pairwise imbalance terms
    pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]
    Z = np.column_stack([(L[:, i] - L[:, j]) ** 2 for i, j in pairs])
    Xu = sm.add_constant(np.column_stack([L, Z]))
    kw = {}
    if cluster:
        kw = dict(cov_type="cluster", cov_kwds={"groups": pd.factorize(df[cluster])[0]})
    else:
        kw = dict(cov_type="HC1")
    mu = sm.OLS(ly, Xu).fit(**kw)
    R = np.zeros((len(pairs), Xu.shape[1]))
    for r_i in range(len(pairs)):
        R[r_i, 1 + k + r_i] = 1.0
    wald = mu.wald_test(R, scalar=True, use_f=True)

    # bootstrap interval for rho (cluster bootstrap if clustered)
    boots = []
    if cluster:
        groups = df.groupby(cluster).indices
        keys = list(groups.keys())
    for _ in range(n_boot):
        if cluster:
            pick = RNG.choice(len(keys), len(keys))
            idx = np.concatenate([groups[keys[g]] for g in pick])
        else:
            idx = RNG.integers(0, n, n)
        try:
            boots.append(fit_ces(L[idx], ly[idx], starts=[ces["rho"], 0.0])["rho"])
        except Exception:
            pass
    boots = np.array(boots)
    lo, hi = np.percentile(boots, [2.5, 97.5])

    if hi < 0:
        verdict = "rho < 0: zero-collapsing, more bottlenecked than MC"
    elif lo > 0:
        verdict = "rho > 0: partly substitutable (between MC and additive)"
    else:
        verdict = "rho = 0 not rejected: consistent with MC"
    out = dict(
        dataset=name, n=int(n), output=ycol, dimensions=xcols, note=note,
        entered_as_reciprocal=[c for c, sg in zip(xcols, sign) if sg < 0],
        powerlaw_exponents_unconstrained={c: round(float(b), 3) for c, b in zip(xcols, b_ols)},
        rho_hat=round(ces["rho"], 3), rho_ci95=[round(float(lo), 3), round(float(hi), 3)],
        rho_at_bound=bool(ces["rho"] <= RHO_LO + 1e-6 or ces["rho"] >= RHO_HI - 1e-6),
        boot_reps=int(len(boots)), clustered_by=cluster,
        ces_weights={c: round(a, 3) for c, a in zip(xcols, ces["a"])},
        r2_log_mc=round(r2(ly, cd["pred"]), 4), r2_log_ces=round(r2(ly, ces["pred"]), 4),
        r2_log_translog_pairs=round(float(mu.rsquared), 4),
        spearman_mc=round(float(spearmanr(cd["pred"], y)[0]), 4),
        spearman_ces=round(float(spearmanr(ces["pred"], y)[0]), 4),
        spearman_additive=round(float(spearmanr(add.fittedvalues, y)[0]), 4),
        imbalance_F=round(float(wald.statistic), 2), imbalance_p=float(wald.pvalue),
        verdict=verdict,
    )
    print(json.dumps(out, indent=1))
    return out


def main(data_dir, out_json):
    res = []

    c = pd.read_csv(f"{data_dir}/concrete.csv")
    res.append(analyse("Concrete strength (5 always-present ingredients)", c, "strength",
                       ["cement", "water", "coarseagg", "fineagg", "age"],
                       note="slag, ash, superplastic are zero in many rows with positive "
                            "strength, so they are not zero-collapse dimensions and are omitted"))
    c["binder"] = c["cement"] + c["slag"] + c["ash"]
    res.append(analyse("Concrete strength (binder = cement+slag+ash)", c, "strength",
                       ["binder", "water", "coarseagg", "fineagg", "age"],
                       note="cementitious materials pooled additively as substitutes"))

    a = pd.read_csv(f"{data_dir}/abalone.csv", header=None,
                    names=["sex", "length", "diameter", "height", "whole_w", "shucked_w",
                           "viscera_w", "shell_w", "rings"])
    res.append(analyse("Abalone age (rings)", a, "rings",
                       ["length", "diameter", "height", "whole_w", "shucked_w", "viscera_w", "shell_w"],
                       note="dimensions are strongly collinear size measures"))

    h = pd.read_csv(f"{data_dir}/housing.csv")
    h["rooms_per_hh"] = h["total_rooms"] / h["households"]
    h["bedrooms_per_hh"] = h["total_bedrooms"] / h["households"]
    h["occupancy"] = h["population"] / h["households"]
    res.append(analyse("California housing value", h, "median_house_value",
                       ["median_income", "housing_median_age", "rooms_per_hh",
                        "bedrooms_per_hh", "population", "occupancy"],
                       note="positive-valued features only; Paper 1's exact feature list is "
                            "not in the repo, so this is a reconstruction"))

    import pyreadr
    p = list(pyreadr.read_r(f"{data_dir}/pwt10.01.rda").values())[0]
    p["country"] = p["country"].astype(str)
    res.append(analyse("Penn World Table (output, capital, labour)", p, "rgdpo", ["cn", "emp"],
                       cluster="country", note="pooled country-years, PWT 10.01"))
    p["hc_emp"] = p["hc"] * p["emp"]
    res.append(analyse("Penn World Table (capital, human-capital-adjusted labour)", p, "rgdpo",
                       ["cn", "hc_emp"], cluster="country", note="pooled country-years, PWT 10.01"))

    with open(out_json, "w") as f:
        json.dump(dict(generated="2026-11-12", method=__doc__.strip().split("\n\n")[1], results=res), f, indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
