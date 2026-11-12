"""
unit_invariance_checks.py -- machine checks for research/UNIT_INVARIANCE_THEOREM.md

Each check prints PASS/FAIL. Exit code 1 if any check fails.

 C1  The harmonic mean H(x,y) = 2xy/(x+y) satisfies Paper 1's Axioms 1-4
     (zero-collapse, continuity, strict monotonicity, homogeneity) ...
 C2  ... and is NOT of the form k x^a y^b (log H has a non-zero mixed partial).
 C3  CES with rho < 0 is zero-collapsing and homogeneous for a range of rho;
     CES with rho > 0 is not zero-collapsing.
 C4  Unit invariance f(l1 x1, l2 x2) = phi(l1, l2) f(x1, x2):
     holds for the power law, fails for the harmonic mean and for min().
 C5  Ordinal unit invariance (rankings survive a change of units):
     holds for the power law, fails for the harmonic mean.
 C6  Theorem 1 direction: random continuous solutions of the multiplicative
     equation F(l*x) = F(l) F(x) built from power laws only; a perturbed
     non-power function violates it. (Sanity check, not a proof.)
 C7  Marginal inversion: d f / d x_i = alpha_i f / x_i is INCREASING in x_i
     when alpha_i > 1, so "steepest when x_i is smallest" is false in general;
     the ratio of marginals (alpha_i/x_i)/(alpha_j/x_j) is the robust statement.
 C8  Zero-collapse survives across the rho <= 0 family: the marginal product of
     the scarcest input, as a share of total marginal product, rises as rho falls.
"""
import sys

import numpy as np
import sympy as sp

ok = True


def report(tag, cond, msg):
    global ok
    ok &= bool(cond)
    print(f"{'PASS' if cond else 'FAIL'}  {tag}  {msg}")


x, y, lam, l1, l2 = sp.symbols("x y lambda l1 l2", positive=True)
H = 2 * x * y / (x + y)

# C1
report("C1a", sp.limit(H, x, 0, "+") == 0 and sp.limit(H, y, 0, "+") == 0, "harmonic mean: zero-collapse")
report("C1b", sp.simplify(sp.diff(H, x) - 2 * y**2 / (x + y) ** 2) == 0, "harmonic mean: dH/dx = 2y^2/(x+y)^2 > 0")
report("C1c", sp.simplify(H.subs({x: lam * x, y: lam * y}, simultaneous=True) - lam * H) == 0,
       "harmonic mean: homogeneous of degree 1")
# C2: k x^a y^b  <=>  d^2 log f / dlogx dlogy = 0
u, v = sp.symbols("u v", real=True)
logH = sp.log(H.subs({x: sp.exp(u), y: sp.exp(v)}))
mixed = sp.simplify(sp.diff(logH, u, v))
report("C2", mixed != 0, f"harmonic mean is not a power law: mixed log-partial = {mixed}")

# C3
rng = np.random.default_rng(7)


def ces(X, a, rho):
    return (a * X**rho).sum(axis=-1) ** (1 / rho)


X = rng.uniform(0.5, 5, (2000, 3))
a = np.array([0.2, 0.3, 0.5])
good = True
for rho in [-0.1, -0.5, -1, -3]:
    Xz = X.copy()
    Xz[:, 0] = 1e-12
    good &= ces(Xz, a, rho).max() < 1e-3
    good &= np.allclose(ces(3.7 * X, a, rho), 3.7 * ces(X, a, rho))
report("C3a", good, "CES rho<0: output -> 0 as any input -> 0, and homogeneous of degree 1")
Xz = X.copy()
Xz[:, 0] = 1e-12
report("C3b", ces(Xz, a, 0.5).min() > 0.1, "CES rho>0: output stays positive when an input is zero")

# C4
P = x ** sp.Rational(3, 10) * y ** sp.Rational(7, 10)
rP = sp.simplify(P.subs({x: l1 * x, y: l2 * y}, simultaneous=True) / P)
rH = sp.simplify(H.subs({x: l1 * x, y: l2 * y}, simultaneous=True) / H)
report("C4a", not (rP.free_symbols & {x, y}), f"power law: f(l.x)/f(x) = {rP} (free of x, y)")
report("C4b", bool(rH.free_symbols & {x, y}), f"harmonic mean: f(l.x)/f(x) = {rH} (depends on x, y)")
mn = lambda p, q: np.minimum(p, q)
report("C4c", not np.isclose(mn(2 * 1.0, 3.0) / mn(1.0, 3.0), mn(2 * 5.0, 3.0) / mn(5.0, 3.0)),
       "min(): rescaling one input changes output by a state-dependent factor")

# C5: ranking of two systems must not depend on the unit of dimension 1
A, B = (1.0, 9.0), (3.0, 2.5)
hm = lambda p, q: 2 * p * q / (p + q)
pw = lambda p, q: p**0.3 * q**0.7
flip_h = (hm(*A) > hm(*B)) != (hm(100 * A[0], A[1]) > hm(100 * B[0], B[1]))
flip_p = False
for c in np.logspace(-4, 4, 200):
    flip_p |= (pw(*A) > pw(*B)) != (pw(c * A[0], A[1]) > pw(c * B[0], B[1]))
report("C5a", flip_h, f"harmonic mean: A>B is {hm(*A) > hm(*B)} in one unit, "
                     f"{hm(100*A[0], A[1]) > hm(100*B[0], B[1])} after rescaling dimension 1 by 100")
report("C5b", not flip_p, "power law: ranking of A vs B unchanged under 200 unit changes")

# C6
al = rng.uniform(0.1, 2, 4)
F = lambda Z: np.prod(Z**al, axis=-1)
Z1, Z2 = rng.uniform(0.2, 5, (500, 4)), rng.uniform(0.2, 5, (500, 4))
G = lambda Z: F(Z) * (1 + 0.05 * np.sin(Z[..., 0]))
report("C6a", np.allclose(F(Z1 * Z2), F(Z1) * F(Z2)), "power law satisfies F(l.x) = F(l)F(x)")
report("C6b", not np.allclose(G(Z1 * Z2), G(Z1) * G(Z2)), "perturbed non-power function violates it")

# C7
al_i = sp.symbols("alpha_i", positive=True)
k, c = sp.symbols("k c", positive=True)
f = k * x**al_i * c                      # c = product of the other dimensions
d2 = sp.simplify(sp.diff(f, x, 2))       # sign of d/dx (df/dx)
report("C7a", sp.simplify(d2.subs(al_i, 2)) > 0, "alpha_i = 2: df/dx_i increases with x_i (not steepest at the bottom)")
report("C7b", sp.simplify(d2.subs(al_i, sp.Rational(1, 2))).is_negative, "alpha_i = 1/2: df/dx_i decreases with x_i")
a1, a2 = sp.symbols("a1 a2", positive=True)
f2 = k * x**a1 * y**a2
ratio = sp.simplify(sp.diff(f2, x) / sp.diff(f2, y))
report("C7c", sp.simplify(ratio - (a1 / x) / (a2 / y)) == 0, f"ratio of marginals = {ratio} = (a1/x)/(a2/y) for every a1, a2")

# C8
xs = np.array([0.2, 1.0, 1.0])
w = np.array([1 / 3, 1 / 3, 1 / 3])
shares = []
for rho in [1.0, 0.5, 1e-9, -0.5, -1.0, -3.0]:
    mp = w * xs ** (rho - 1)             # marginal products up to a common factor
    shares.append(mp[0] / mp.sum())
report("C8", all(np.diff(shares) > 0) and abs(shares[0] - 1 / 3) < 1e-9,
       "share of marginal product at the scarcest input by rho [1, .5, 0, -.5, -1, -3]: "
       + ", ".join(f"{s:.2f}" for s in shares))

sys.exit(0 if ok else 1)
