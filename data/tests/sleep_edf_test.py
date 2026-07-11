import pandas as pd
import numpy as np
import json, glob, os

# Load all batch CSVs
batch_dir = r"D:\Projects\HIRM\Empirical\Results\Sleep_EDF_Batch"
files = sorted([f for f in glob.glob(os.path.join(batch_dir, "S[0-9]*_R*.csv"))])
print(f"Found {len(files)} batch files")

frames = []
for f in files:
    df = pd.read_csv(f)
    if 'subject' not in df.columns:
        df['subject'] = int(os.path.basename(f).split('_')[0][1:])
        df['recording'] = int(os.path.basename(f).split('_')[1][1])
    frames.append(df)

data = pd.concat(frames, ignore_index=True)
print(f"Total epochs: {len(data)}")
print(f"Columns: {list(data.columns)}")
print(f"Stages: {data['stage'].value_counts().to_dict()}")

# Map stages to consciousness level
stage_order = {
    'Sleep stage W': 5,  # Wake - highest
    'Sleep stage R': 4,  # REM
    'Sleep stage 1': 3,  # N1
    'Sleep stage 2': 2,  # N2
    'Sleep stage 3': 1,  # N3
    'Sleep stage 4': 0,  # N4 - lowest
}
data['stage_level'] = data['stage'].map(stage_order)
data = data.dropna(subset=['stage_level'])

# Aggregate by stage
stage_stats = data.groupby('stage').agg({
    'C': ['mean', 'std', 'median'],
    'Phi': ['mean', 'std', 'median'],
    'R_theory': ['mean', 'std', 'median'],
    'D_eff': ['mean', 'std', 'median'],
    'stage_level': 'first'
}).round(4)

print("\n=== STAGE MEANS ===")
for stage in ['Sleep stage W', 'Sleep stage R', 'Sleep stage 1', 'Sleep stage 2', 'Sleep stage 3', 'Sleep stage 4']:
    if stage in data['stage'].values:
        s = data[data['stage']==stage]
        print(f"  {stage:20s}  C={s['C'].mean():8.2f}  Phi={s['Phi'].mean():8.2f}  R={s['R_theory'].mean():6.3f}  D={s['D_eff'].mean():6.3f}  n={len(s)}")

# THE CLIFF TEST: How does C degrade as we go W -> N1 -> N2 -> N3 -> N4?
print("\n=== CLIFF VS SLOPE TEST ===")
stages_ordered = ['Sleep stage W', 'Sleep stage 1', 'Sleep stage 2', 'Sleep stage 3', 'Sleep stage 4']
C_means = [data[data['stage']==s]['C'].mean() for s in stages_ordered if s in data['stage'].values]
Phi_means = [data[data['stage']==s]['Phi'].mean() for s in stages_ordered if s in data['stage'].values]
R_means = [data[data['stage']==s]['R_theory'].mean() for s in stages_ordered if s in data['stage'].values]
D_means = [data[data['stage']==s]['D_eff'].mean() for s in stages_ordered if s in data['stage'].values]

# Normalize to Wake=1
C_norm = [c/C_means[0] for c in C_means]
Phi_norm = [p/Phi_means[0] for p in Phi_means]
R_norm = [r/R_means[0] for r in R_means]
D_norm = [d/D_means[0] for d in D_means]

print("  Normalized (Wake=1.0):")
for i, stage in enumerate([s for s in stages_ordered if s in data['stage'].values]):
    print(f"    {stage:20s}  C={C_norm[i]:.3f}  Phi={Phi_norm[i]:.3f}  R={R_norm[i]:.3f}  D={D_norm[i]:.3f}")

# Check for cliff: ratio of consecutive drops
print("\n  Drop ratios (>1 means accelerating = cliff):")
for i in range(1, len(C_norm)):
    drop = C_norm[i-1] - C_norm[i]
    prev_drop = C_norm[i-2] - C_norm[i-1] if i >= 2 else drop
    ratio = drop / prev_drop if prev_drop > 0.001 else float('inf')
    print(f"    Step {i}: C drops {drop:.3f} (ratio vs prev: {ratio:.2f})")

# CES rho estimation
print("\n=== CES RHO ESTIMATION ===")
from scipy.optimize import minimize

Phi_all = data['Phi'].values
R_all = data['R_theory'].values
D_all = data['D_eff'].values
C_all = data['C'].values

# Filter valid data
mask = (Phi_all > 0.01) & (R_all > 0.01) & (D_all > 0.01) & (C_all > 0.01)
Phi_v, R_v, D_v, C_v = Phi_all[mask], R_all[mask], D_all[mask], C_all[mask]
print(f"  Valid epochs: {mask.sum()} / {len(mask)}")

def ces_3d(params, Phi, R, D):
    rho, a1, a2, a3, k = params
    if abs(rho) < 1e-6:
        return k * np.power(Phi, a1) * np.power(R, a2) * np.power(D, a3)
    return k * np.power(a1*np.power(Phi, rho) + a2*np.power(R, rho) + a3*np.power(D, rho), 1.0/rho)

def loss_ces(params):
    try:
        pred = ces_3d(params, Phi_v, R_v, D_v)
        return np.mean((np.log(pred + 1e-6) - np.log(C_v + 1e-6))**2)
    except:
        return 1e10

# Test multiplicative fit (rho=0)
def loss_mult(params):
    a1, a2, a3, k = params
    pred = k * np.power(Phi_v, a1) * np.power(R_v, a2) * np.power(D_v, a3)
    return np.mean((np.log(pred + 1e-6) - np.log(C_v + 1e-6))**2)

# Test additive fit
def loss_add(params):
    a1, a2, a3 = params
    pred = a1*Phi_v + a2*R_v + a3*D_v
    pred = np.maximum(pred, 1e-6)
    return np.mean((np.log(pred + 1e-6) - np.log(C_v + 1e-6))**2)

# Fit multiplicative
res_mult = minimize(loss_mult, [1, 1, 1, 1], method='Nelder-Mead', options={'maxiter': 10000})
print(f"  Multiplicative fit (rho=0): loss={res_mult.fun:.6f}")
print(f"    params: a1={res_mult.x[0]:.3f}, a2={res_mult.x[1]:.3f}, a3={res_mult.x[2]:.3f}, k={res_mult.x[3]:.3f}")

# Fit additive
res_add = minimize(loss_add, [1, 1, 1], method='Nelder-Mead', options={'maxiter': 10000})
print(f"  Additive fit (rho=1): loss={res_add.fun:.6f}")
print(f"    params: a1={res_add.x[0]:.3f}, a2={res_add.x[1]:.3f}, a3={res_add.x[2]:.3f}")

# Fit CES with free rho
res_ces = minimize(loss_ces, [0.5, 0.3, 0.3, 0.3, 1], method='Nelder-Mead', options={'maxiter': 20000})
print(f"  CES fit (free rho): loss={res_ces.fun:.6f}")
print(f"    rho={res_ces.x[0]:.4f}")

if res_ces.x[0] < 0.1:
    print(f"\n  >>> RESULT: rho={res_ces.x[0]:.4f} ≈ 0 → MULTIPLICATIVE FORM VALIDATED")
elif res_ces.x[0] > 0.5:
    print(f"\n  >>> RESULT: rho={res_ces.x[0]:.4f} → ADDITIVE-LEANING")
else:
    print(f"\n  >>> RESULT: rho={res_ces.x[0]:.4f} → INTERMEDIATE")

ratio = res_add.fun / res_mult.fun
print(f"\n  Multiplicative vs Additive loss ratio: {ratio:.2f}x")
if ratio > 1.5:
    print("  >>> Multiplicative SUBSTANTIALLY outperforms additive")
elif ratio > 1.1:
    print("  >>> Multiplicative moderately outperforms additive")
else:
    print("  >>> Forms are comparable")

# Save results
results = {
    'total_epochs': len(data),
    'valid_epochs': int(mask.sum()),
    'multiplicative_loss': float(res_mult.fun),
    'additive_loss': float(res_add.fun),
    'ces_loss': float(res_ces.fun),
    'ces_rho': float(res_ces.x[0]),
    'loss_ratio': float(ratio),
    'stage_means': {s: {'C': float(data[data['stage']==s]['C'].mean()),
                        'Phi': float(data[data['stage']==s]['Phi'].mean()),
                        'R': float(data[data['stage']==s]['R_theory'].mean()),
                        'D': float(data[data['stage']==s]['D_eff'].mean()),
                        'n': int(len(data[data['stage']==s]))}
                    for s in data['stage'].unique()}
}
with open(r"D:\Projects\Multiplicative-Composition\sleep_edf_rho_test.json", 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to D:\\Projects\\Multiplicative-Composition\\sleep_edf_rho_test.json")
