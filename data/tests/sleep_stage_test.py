"""
NON-CIRCULAR TEST: Does multiplicative composition predict
independently-labeled sleep stages better than additive?

Target: Sleep stage labels (scored by human experts, NOT computed from EEG)
Predictors: Phi, R_theory, D_eff (EEG-derived components)
Question: Is Phi*R*D a better predictor of stage than a1*Phi + a2*R + a3*D?

This breaks the circularity because stages are an EXTERNAL ground truth.
"""
import pandas as pd
import numpy as np
import glob, os, json
from scipy.stats import spearmanr, pearsonr, f_oneway
from scipy.optimize import minimize
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, cohen_kappa_score
from sklearn.model_selection import cross_val_score
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# 1. LOAD DATA
# ============================================================
batch_dir = r"D:\Projects\HIRM\Empirical\Results\Sleep_EDF_Batch"
files = sorted([f for f in glob.glob(os.path.join(batch_dir, "S[0-9]*_R*.csv"))])
print(f"Loading {len(files)} batch files...")

frames = []
for f in files:
    df = pd.read_csv(f)
    if 'subject' not in df.columns:
        df['subject'] = int(os.path.basename(f).split('_')[0][1:])
        df['recording'] = int(os.path.basename(f).split('_')[1][1])
    frames.append(df)

data = pd.concat(frames, ignore_index=True)

# Map stages to ordinal consciousness level
stage_map = {
    'Sleep stage W': 5,
    'Sleep stage R': 4,
    'Sleep stage 1': 3,
    'Sleep stage 2': 2,
    'Sleep stage 3': 1,
    'Sleep stage 4': 0,
}
data['stage_level'] = data['stage'].map(stage_map)
data = data.dropna(subset=['stage_level'])
data['stage_level'] = data['stage_level'].astype(int)

print(f"Total valid epochs: {len(data)}")
print(f"Stage distribution:")
for s in ['Sleep stage W','Sleep stage R','Sleep stage 1','Sleep stage 2','Sleep stage 3','Sleep stage 4']:
    n = len(data[data['stage']==s])
    print(f"  {s:20s} n={n:6d} ({100*n/len(data):.1f}%)")

Phi = data['Phi'].values
R = data['R_theory'].values
D = data['D_eff'].values
Y = data['stage_level'].values

# ============================================================
# 2. COMPOSE PREDICTORS
# ============================================================
# Multiplicative: C_mult = Phi * R * D (the HIRM claim)
C_mult = Phi * R * D

# Additive: C_add = best linear combination (fitted to stages)
# We'll also test: geometric mean, harmonic mean, min

C_geom = np.power(Phi * R * D, 1/3)  # geometric mean
C_min = np.minimum(np.minimum(Phi, R), D)  # Leontief

# For additive, fit weights to maximize correlation with stages
def neg_corr_add(params):
    a1, a2, a3 = params
    pred = a1*Phi + a2*R + a3*D
    return -spearmanr(pred, Y)[0]

res = minimize(neg_corr_add, [1, 1, 1], method='Nelder-Mead')
C_add_opt = res.x[0]*Phi + res.x[1]*R + res.x[2]*D
print(f"\nOptimal additive weights: a1={res.x[0]:.3f}, a2={res.x[1]:.3f}, a3={res.x[2]:.3f}")

# Simple equal-weight additive
C_add_eq = Phi + R + D

# ============================================================
# 3. CORRELATION WITH STAGE LABELS
# ============================================================
print("\n" + "="*60)
print("TEST 1: SPEARMAN CORRELATION WITH SLEEP STAGE")
print("="*60)
print("(higher = better predictor of consciousness level)")

compositions = {
    'Multiplicative (Phi*R*D)': C_mult,
    'Geometric mean': C_geom,
    'Additive (equal weights)': C_add_eq,
    'Additive (optimized weights)': C_add_opt,
    'Min (Leontief)': C_min,
    'Phi alone': Phi,
    'R alone': R,
    'D alone': D,
}

results = {}
for name, vals in compositions.items():
    rho_s, p = spearmanr(vals, Y)
    r_p, _ = pearsonr(vals, Y)
    results[name] = {'spearman': rho_s, 'pearson': r_p}
    print(f"  {name:35s}  rho={rho_s:.4f}  r={r_p:.4f}")

# ============================================================
# 4. CLASSIFICATION ACCURACY
# ============================================================
print("\n" + "="*60)
print("TEST 2: CLASSIFICATION ACCURACY (5-fold CV)")
print("="*60)
print("(can each composition distinguish sleep stages?)")

scaler = StandardScaler()

for name, vals in [('Multiplicative', C_mult), ('Additive (opt)', C_add_opt),
                    ('Phi alone', Phi), ('Components (3 features)', None)]:
    if vals is not None:
        X = scaler.fit_transform(vals.reshape(-1, 1))
    else:
        X = scaler.fit_transform(np.column_stack([Phi, R, D]))

    clf = LogisticRegression(max_iter=1000, multi_class='multinomial', random_state=42)
    scores = cross_val_score(clf, X, Y, cv=5, scoring='accuracy')
    kappa_scores = []
    for train_idx, test_idx in [(np.ones(len(Y), dtype=bool), np.ones(len(Y), dtype=bool))]:
        clf.fit(X, Y)
        pred = clf.predict(X)
        kappa_scores.append(cohen_kappa_score(Y, pred))

    print(f"  {name:30s}  acc={scores.mean():.4f} (+/-{scores.std():.4f})  kappa={kappa_scores[0]:.4f}")

# ============================================================
# 5. STAGE SEPARATION (EFFECT SIZE)
# ============================================================
print("\n" + "="*60)
print("TEST 3: STAGE SEPARATION (Cohen's d between adjacent stages)")
print("="*60)

def cohens_d(a, b):
    na, nb = len(a), len(b)
    pooled_std = np.sqrt(((na-1)*np.std(a,ddof=1)**2 + (nb-1)*np.std(b,ddof=1)**2) / (na+nb-2))
    return (np.mean(a) - np.mean(b)) / pooled_std if pooled_std > 0 else 0

stage_pairs = [('Sleep stage W','Sleep stage 1'), ('Sleep stage 1','Sleep stage 2'),
               ('Sleep stage 2','Sleep stage 3'), ('Sleep stage 3','Sleep stage 4')]

print(f"  {'Transition':25s} {'Multiplicative':>14s} {'Additive(opt)':>14s} {'Phi alone':>14s}")
for s1, s2 in stage_pairs:
    mask1 = data['stage'] == s1
    mask2 = data['stage'] == s2
    d_mult = cohens_d(C_mult[mask1], C_mult[mask2])
    d_add = cohens_d(C_add_opt[mask1], C_add_opt[mask2])
    d_phi = cohens_d(Phi[mask1], Phi[mask2])
    label = f"{s1.split()[-1]}->{s2.split()[-1]}"
    print(f"  {label:25s} {d_mult:14.3f} {d_add:14.3f} {d_phi:14.3f}")

# ============================================================
# 6. CES RHO ESTIMATION (against stage labels)
# ============================================================
print("\n" + "="*60)
print("TEST 4: CES RHO ESTIMATION (fitted to stage labels)")
print("="*60)

def ces_pred(params, Phi, R, D):
    rho, a1, a2, a3, k, b = params
    if abs(rho) < 1e-6:
        composed = k * np.power(Phi, abs(a1)) * np.power(R, abs(a2)) * np.power(D, abs(a3))
    else:
        inner = abs(a1)*np.power(Phi, rho) + abs(a2)*np.power(R, rho) + abs(a3)*np.power(D, rho)
        inner = np.maximum(inner, 1e-10)
        composed = k * np.power(inner, 1.0/rho)
    return composed + b

def loss_stage_ces(params):
    try:
        pred = ces_pred(params, Phi, R, D)
        return -spearmanr(pred, Y)[0]
    except:
        return 0

# Search over rho values
print("  Scanning rho from -2 to 2...")
best_rho = None
best_corr = -1
rho_scan = {}

for rho_test in np.linspace(-2, 2, 41):
    res = minimize(loss_stage_ces, [rho_test, 0.5, 0.5, 0.5, 1.0, 0.0],
                   method='Nelder-Mead', options={'maxiter': 5000})
    corr = -res.fun
    rho_scan[float(rho_test)] = float(corr)
    if corr > best_corr:
        best_corr = corr
        best_rho = res.x[0]

print(f"  Best rho: {best_rho:.4f} (Spearman = {best_corr:.4f})")

if abs(best_rho) < 0.3:
    verdict = "MULTIPLICATIVE SUPPORTED (rho near 0)"
elif best_rho > 0.7:
    verdict = "ADDITIVE SUPPORTED (rho near 1)"
elif best_rho < -0.5:
    verdict = "COMPLEMENTARY/MIN SUPPORTED (rho << 0)"
else:
    verdict = f"INTERMEDIATE (rho = {best_rho:.3f})"
print(f"  VERDICT: {verdict}")

# ============================================================
# 7. THE DECISIVE COMPARISON
# ============================================================
print("\n" + "="*60)
print("SUMMARY: MULTIPLICATIVE vs ADDITIVE vs COMPONENTS")
print("="*60)

r_mult = spearmanr(C_mult, Y)[0]
r_add = spearmanr(C_add_opt, Y)[0]
r_phi = spearmanr(Phi, Y)[0]
r_3feat = spearmanr(C_mult, Y)[0]  # placeholder

print(f"  Spearman with stage labels:")
print(f"    Multiplicative (Phi*R*D):     {r_mult:.4f}")
print(f"    Additive (optimized):         {r_add:.4f}")
print(f"    Phi alone:                    {r_phi:.4f}")
print(f"    CES (best rho={best_rho:.3f}):       {best_corr:.4f}")
print()

if r_mult > r_add and r_mult > r_phi:
    print("  >>> MULTIPLICATIVE WINS: best single-number predictor of sleep stage")
elif r_add > r_mult:
    print("  >>> ADDITIVE WINS: linear combination predicts stages better")
elif r_phi > r_mult:
    print("  >>> PHI ALONE WINS: multiplication adds no value over the best component")

improvement = (r_mult - r_add) / r_add * 100
print(f"  >>> Multiplicative vs additive: {improvement:+.2f}% difference in correlation")

# Save full results
output = {
    'n_epochs': len(data),
    'correlations': {k: {'spearman': float(v['spearman']), 'pearson': float(v['pearson'])}
                     for k, v in results.items()},
    'ces_rho_best': float(best_rho),
    'ces_best_corr': float(best_corr),
    'rho_scan': rho_scan,
    'additive_weights': [float(x) for x in res.x[:3]] if hasattr(res, 'x') else None,
    'verdict': verdict,
}
outpath = r"D:\Projects\Multiplicative-Composition\sleep_stage_prediction_test.json"
with open(outpath, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nFull results saved: {outpath}")
