"""NBA Real Data via nba_api package"""
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "nba_api", "-q"])

from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd, numpy as np, json
from scipy.optimize import differential_evolution
from scipy.stats import spearmanr

print("Fetching NBA team stats...")
seasons = ['2023-24','2022-23','2021-22','2020-21','2019-20','2018-19','2017-18']
all_teams = []

for season in seasons:
    try:
        stats = leaguedashteamstats.LeagueDashTeamStats(season=season, per_mode_detailed='PerGame')
        df = stats.get_data_frames()[0]
        df['SEASON'] = season
        all_teams.append(df)
        print(f"  {season}: {len(df)} teams")
    except Exception as e:
        print(f"  {season}: {e}")

if not all_teams:
    print("No data retrieved")
    exit()

data = pd.concat(all_teams, ignore_index=True)
print(f"\nTotal: {len(data)} team-seasons")

# Dimensions:
# x1 = Offensive efficiency proxy: (PTS + AST) / TOV — points and assists per turnover
# x2 = Defensive efficiency proxy: (STL + BLK + DREB) / OPP_FGM (not available, use STL+BLK)
# x3 = Team cohesion: AST / FGM — what fraction of baskets are assisted

x1 = (data['PTS'] + data['AST']) / np.maximum(data['TOV'], 1)  # offensive quality
x2 = (data['STL'] + data['BLK'] + data['DREB']) / 10  # defensive presence (normalized)
x3 = data['AST'] / np.maximum(data['FGM'], 1)  # cohesion (assist rate)
y = data['W_PCT']

mask = (x1>0)&(x2>0)&(x3>0)&(y>0)
x1,x2,x3,y = x1[mask].values,x2[mask].values,x3[mask].values,y[mask].values
x1n,x2n,x3n,yn = x1/x1.max(),x2/x2.max(),x3/x3.max(),y

def loss_m(p):
    pred=p[3]*np.power(x1n,p[0])*np.power(x2n,p[1])*np.power(x3n,p[2])
    return np.mean((np.log(np.maximum(pred,1e-12))-np.log(np.maximum(yn,1e-12)))**2)
def loss_a(p):
    pred=p[0]*x1n+p[1]*x2n+p[2]*x3n+p[3]
    return np.mean((np.log(np.maximum(pred,1e-12))-np.log(np.maximum(yn,1e-12)))**2)

rm=differential_evolution(loss_m,[(-3,8),(-3,8),(-3,8),(1e-4,50)],maxiter=3000,seed=42,tol=1e-12,polish=True)
ra=differential_evolution(loss_a,[(-10,10),(-10,10),(-10,10),(-2,2)],maxiter=3000,seed=42,tol=1e-12,polish=True)
pm=rm.x[3]*np.power(x1n,rm.x[0])*np.power(x2n,rm.x[1])*np.power(x3n,rm.x[2])
pa=ra.x[0]*x1n+ra.x[1]*x2n+ra.x[2]*x3n+ra.x[3]
sm,_=spearmanr(pm,yn);sa,_=spearmanr(pa,yn)
ratio=ra.fun/rm.fun

print(f"\n{'='*60}")
print(f"NBA REAL DATA: Offense x Defense x Cohesion -> Win%")
print(f"{'='*60}")
print(f"  N = {len(y)} team-seasons")
print(f"  Mult: loss={rm.fun:.6f} Spearman={sm:.4f}")
print(f"    exp: offense={rm.x[0]:.3f}, defense={rm.x[1]:.3f}, cohesion={rm.x[2]:.3f}")
print(f"  Add:  loss={ra.fun:.6f} Spearman={sa:.4f}")
print(f"  Ratio: {ratio:.2f}x -> {'MULT' if ratio>1.1 else 'ADD' if ratio<0.9 else 'TIE'}")

json.dump({'domain':'NBA Real Data','n':int(len(y)),'mult_spearman':float(sm),
           'add_spearman':float(sa),'ratio':float(ratio),'real_world':True,
           'exponents':{'offense':float(rm.x[0]),'defense':float(rm.x[1]),'cohesion':float(rm.x[2])}},
          open(r'D:\Projects\Multiplicative-Composition\nba_real_results.json','w'),indent=2)
print("Saved.")
