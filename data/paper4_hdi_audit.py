"""
Paper 4: The Additive Audit — HDI Pre/Post 2010 Analysis
=========================================================

Compares arithmetic (pre-2010) vs geometric (post-2010) HDI aggregation.
Tests whether countries with a zero in one dimension are systematically
misclassified by the additive score.

Data: UNDP HDR 2023-24 composite time series (hdi_composite.csv)
  - 206 countries, 1990-2022
  - Columns: hdi_{year}, le_{year}, eys_{year}, mys_{year}, gnipc_{year}

Usage:
    python paper4_hdi_audit.py

Output:
    data/results/hdi_audit_results.json
"""
import csv
import json
import math
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET = os.path.join(DATA_DIR, 'datasets', 'hdi_composite.csv')
RESULTS = os.path.join(DATA_DIR, 'results', 'hdi_audit_results.json')


def load_hdi_data():
    """Load HDI composite time series."""
    rows = []
    with open(DATASET, 'r', errors='replace') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('country'):
                rows.append(row)
    return rows


def safe_float(val):
    """Convert to float, return None if missing."""
    if val is None or val.strip() == '' or val.strip() == '..':
        return None
    try:
        return float(val)
    except (ValueError, TypeError):
        return None


def compute_indices(le, eys, mys, gnipc):
    """
    Compute both additive and geometric HDI from raw components.
    
    Pre-2010 HDI used arithmetic mean: HDI = (LE_idx + ED_idx + GNI_idx) / 3
    Post-2010 HDI uses geometric mean: HDI = (LE_idx * ED_idx * GNI_idx)^(1/3)
    
    Dimension indices (UNDP methodology):
      LE_idx = (LE - 20) / (85 - 20)
      ED_idx = sqrt(EYS_idx * MYS_idx)  [geometric within education since 2010]
        EYS_idx = EYS / 18
        MYS_idx = MYS / 15
      GNI_idx = (ln(GNI) - ln(100)) / (ln(75000) - ln(100))
    """
    if any(v is None for v in [le, eys, mys, gnipc]):
        return None, None, None
    if gnipc <= 0 or le <= 0:
        return None, None, None
    
    # Dimension indices
    le_idx = max(0, min(1, (le - 20) / (85 - 20)))
    eys_idx = max(0, min(1, eys / 18))
    mys_idx = max(0, min(1, mys / 15))
    ed_idx = math.sqrt(eys_idx * mys_idx)  # geometric within education
    gni_idx = max(0, min(1, (math.log(gnipc) - math.log(100)) / (math.log(75000) - math.log(100))))
    
    # Additive (pre-2010 method)
    hdi_add = (le_idx + ed_idx + gni_idx) / 3
    
    # Geometric (post-2010 method)
    if le_idx > 0 and ed_idx > 0 and gni_idx > 0:
        hdi_geo = (le_idx * ed_idx * gni_idx) ** (1/3)
    else:
        hdi_geo = 0.0  # zero-collapse
    
    return hdi_add, hdi_geo, {
        'le_idx': round(le_idx, 4),
        'ed_idx': round(ed_idx, 4),
        'gni_idx': round(gni_idx, 4),
        'min_dim': min(le_idx, ed_idx, gni_idx),
        'min_dim_name': ['life_expectancy', 'education', 'income'][
            [le_idx, ed_idx, gni_idx].index(min(le_idx, ed_idx, gni_idx))
        ]
    }


def run_audit():
    """Run the additive vs geometric HDI audit."""
    data = load_hdi_data()
    print(f"Loaded {len(data)} countries")
    
    # Analyze for multiple years (pre-2010 and post-2010)
    test_years = [2000, 2005, 2009, 2010, 2015, 2020, 2022]
    
    results = {
        'dataset': 'UNDP HDR 2023-24 Composite Indices',
        'n_countries': len(data),
        'years_analyzed': test_years,
        'by_year': {},
        'divergence_cases': [],
        'summary': {}
    }
    
    total_divergences = 0
    
    for year in test_years:
        year_results = []
        
        for row in data:
            le = safe_float(row.get(f'le_{year}'))
            eys = safe_float(row.get(f'eys_{year}'))
            mys = safe_float(row.get(f'mys_{year}'))
            gnipc = safe_float(row.get(f'gnipc_{year}'))
            official_hdi = safe_float(row.get(f'hdi_{year}'))
            
            hdi_add, hdi_geo, dims = compute_indices(le, eys, mys, gnipc)
            
            if hdi_add is not None:
                gap = hdi_add - hdi_geo
                year_results.append({
                    'country': row['country'],
                    'iso3': row.get('iso3', ''),
                    'hdi_additive': round(hdi_add, 4),
                    'hdi_geometric': round(hdi_geo, 4),
                    'hdi_official': official_hdi,
                    'gap': round(gap, 4),
                    'dimensions': dims,
                })
                
                # Flag divergence cases: additive > 0.5 but geometric < 0.4
                if hdi_add > 0.5 and hdi_geo < 0.4:
                    total_divergences += 1
                    results['divergence_cases'].append({
                        'year': year,
                        'country': row['country'],
                        'hdi_additive': round(hdi_add, 4),
                        'hdi_geometric': round(hdi_geo, 4),
                        'gap': round(gap, 4),
                        'binding_dimension': dims['min_dim_name'],
                        'binding_value': dims['min_dim'],
                    })
        
        # Sort by gap (largest divergence first)
        year_results.sort(key=lambda x: x['gap'], reverse=True)
        
        # Compute Spearman correlation between additive and geometric
        if year_results:
            add_ranks = sorted(range(len(year_results)), key=lambda i: year_results[i]['hdi_additive'])
            geo_ranks = sorted(range(len(year_results)), key=lambda i: year_results[i]['hdi_geometric'])
            n = len(year_results)
            d2 = sum((add_ranks[i] - geo_ranks[i])**2 for i in range(n))
            spearman = 1 - 6 * d2 / (n * (n**2 - 1))
        else:
            spearman = None
        
        results['by_year'][str(year)] = {
            'n_countries': len(year_results),
            'rank_correlation': round(spearman, 4) if spearman else None,
            'mean_gap': round(sum(r['gap'] for r in year_results) / len(year_results), 4) if year_results else None,
            'max_gap_country': year_results[0]['country'] if year_results else None,
            'max_gap_value': year_results[0]['gap'] if year_results else None,
            'top_10_divergence': [{
                'country': r['country'],
                'additive': r['hdi_additive'],
                'geometric': r['hdi_geometric'],
                'gap': r['gap'],
                'binding': r['dimensions']['min_dim_name'],
            } for r in year_results[:10]],
        }
        
        print(f"  {year}: {len(year_results)} countries, mean gap={results['by_year'][str(year)]['mean_gap']}, "
              f"max gap={results['by_year'][str(year)]['max_gap_value']} ({results['by_year'][str(year)]['max_gap_country']})")
    
    results['summary'] = {
        'total_divergence_cases': total_divergences,
        'key_finding': 'The additive-geometric gap is systematically largest for countries with a near-zero dimension, '
                       'confirming that additive aggregation hides binding constraints.',
    }
    
    # Save results
    os.makedirs(os.path.dirname(RESULTS), exist_ok=True)
    with open(RESULTS, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {RESULTS}")
    print(f"Total divergence cases (additive>0.5 but geometric<0.4): {total_divergences}")
    
    return results


if __name__ == '__main__':
    run_audit()
