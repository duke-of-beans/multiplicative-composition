import pandas as pd, glob, os, numpy as np
batch = r"D:\Projects\HIRM\Empirical\Results\Sleep_EDF_Batch"
files = sorted([f for f in glob.glob(os.path.join(batch, "S[0-9]*_R*.csv"))])
data = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
stages = ['Sleep stage W','Sleep stage R','Sleep stage 1','Sleep stage 2','Sleep stage 3','Sleep stage 4']

print("R_obs by stage:")
for s in stages:
    d = data[data.stage==s].R_obs
    print(f"  {s:20s}  mean={d.mean():.4f}  std={d.std():.4f}  min={d.min():.4f}  max={d.max():.4f}")

print(f"\nGlobal R_obs range: {data.R_obs.min():.4f} to {data.R_obs.max():.4f}")
print(f"R_obs > 0.95: {(data.R_obs>0.95).mean()*100:.1f}%")
print(f"R_obs > 0.90: {(data.R_obs>0.90).mean()*100:.1f}%")
print(f"R_obs > 0.80: {(data.R_obs>0.80).mean()*100:.1f}%")

# Dynamic range comparison
print("\nDynamic range comparison (max-min within each stage):")
for s in stages:
    d = data[data.stage==s]
    print(f"  {s:20s}  Phi: {d.Phi.max()-d.Phi.min():.2f}  R_obs: {d.R_obs.max()-d.R_obs.min():.4f}  D: {d.D_eff.max()-d.D_eff.min():.4f}")

# What R_obs SHOULD look like: wake vs N4 effect size
from scipy.stats import mannwhitneyu
for col in ['Phi','R_obs','D_eff']:
    wake = data[data.stage=='Sleep stage W'][col]
    n4 = data[data.stage=='Sleep stage 4'][col]
    u, p = mannwhitneyu(wake, n4)
    d_cohen = (wake.mean()-n4.mean()) / np.sqrt((wake.std()**2+n4.std()**2)/2)
    print(f"\nWake vs N4 for {col}: Cohen's d = {d_cohen:.3f}, p = {p:.2e}")
