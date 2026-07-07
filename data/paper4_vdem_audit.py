"""
Paper 4: The Additive Audit — V-Dem Electoral Democracy Index Analysis
======================================================================

PREREQUISITE: Manual download of V-Dem v14 Core dataset.
V-Dem requires form submission at:
  https://v-dem.net/data/the-v-dem-dataset/country-year-v-dem-core-v14/

Steps:
  1. Visit the URL above
  2. Enter email, select CSV format, accept privacy policy
  3. Download the ZIP file
  4. Extract the CSV to: data/datasets/V-Dem-CY-Core-v14.csv

Key V-Dem variables for the audit:
  v2x_polyarchy  — Electoral Democracy Index (EDI) — the one that averages mult+add
  v2x_api        — Additive Polyarchy Index
  v2x_mpi        — Multiplicative Polyarchy Index
  v2x_freexp_altinf — Freedom of Expression & Alt Info
  v2x_frassoc_thick  — Freedom of Association (thick)
  v2x_suffr      — Share of population with suffrage
  v2xel_frefair  — Clean elections
  v2x_elecoff    — Elected officials

The audit: recompute additive vs multiplicative EDI for all countries,
identify where they diverge, and test whether divergence predicts
democratic breakdown.

Usage:
    python paper4_vdem_audit.py

Output:
    data/results/vdem_audit_results.json
"""
import csv
import json
import math
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET = os.path.join(DATA_DIR, 'datasets', 'V-Dem-CY-Core-v16', 'V-Dem-CY-Core-v16.csv')
RESULTS = os.path.join(DATA_DIR, 'results', 'vdem_audit_results.json')


def safe_float(val):
    if val is None or str(val).strip() in ('', 'NA', '.'):
        return None
    try:
        return float(val)
    except (ValueError, TypeError):
        return None


def load_vdem():
    """Load V-Dem Core v14 dataset."""
    if not os.path.exists(DATASET):
        print(f"ERROR: V-Dem dataset not found at {DATASET}")
        print("Download from: https://v-dem.net/data/the-v-dem-dataset/country-year-v-dem-core-v14/")
        print("Extract CSV to the path above.")
        return None
    
    rows = []
    with open(DATASET, 'r', errors='replace') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def run_vdem_audit():
    """
    Core audit: compare v2x_api (additive) vs v2x_mpi (multiplicative) 
    vs v2x_polyarchy (V-Dem's 50/50 average of both).
    
    The key finding: how many country-years have v2x_api > 0.5 
    but v2x_mpi < 0.1? These are the "hidden zeros" — countries the 
    additive index calls democratic but the multiplicative index 
    identifies as having a collapsed dimension.
    """
    data = load_vdem()
    if data is None:
        return None
    
    print(f"Loaded {len(data)} country-year observations")
    
    # Check which columns exist
    sample = data[0]
    key_vars = ['v2x_polyarchy', 'v2x_api', 'v2x_mpi', 
                'v2x_freexp_altinf', 'v2x_frassoc_thick',
                'v2x_suffr', 'v2xel_frefair', 'v2x_elecoff',
                'country_name', 'year', 'COWcode']
    
    present = [v for v in key_vars if v in sample]
    missing = [v for v in key_vars if v not in sample]
    print(f"Present: {present}")
    if missing:
        print(f"Missing: {missing}")
    
    results = {
        'dataset': 'V-Dem v14 Core (Country-Year)',
        'n_observations': len(data),
        'variables_used': present,
        'divergence_cases': [],
        'by_decade': {},
        'extreme_cases': [],
    }
    
    # Analyze divergence between additive and multiplicative indices
    divergences = []
    
    for row in data:
        year = safe_float(row.get('year'))
        api = safe_float(row.get('v2x_api'))  # additive polyarchy
        mpi = safe_float(row.get('v2x_mpi'))  # multiplicative polyarchy
        edi = safe_float(row.get('v2x_polyarchy'))  # official EDI (average)
        country = row.get('country_name', row.get('country_text_id', ''))
        
        if all(v is not None for v in [year, api, mpi, edi]):
            gap = api - mpi
            
            entry = {
                'country': country,
                'year': int(year),
                'api_additive': round(api, 4),
                'mpi_multiplicative': round(mpi, 4),
                'edi_official': round(edi, 4),
                'gap': round(gap, 4),
            }
            
            # Add component scores if available
            for comp in ['v2x_freexp_altinf', 'v2x_frassoc_thick', 
                        'v2x_suffr', 'v2xel_frefair', 'v2x_elecoff']:
                val = safe_float(row.get(comp))
                if val is not None:
                    entry[comp] = round(val, 4)
            
            divergences.append(entry)
            
            # Flag extreme cases: additive says "democratic" but multiplicative says "zero"
            if api > 0.5 and mpi < 0.1:
                results['extreme_cases'].append(entry)
    
    # Sort extreme cases by gap
    results['extreme_cases'].sort(key=lambda x: x['gap'], reverse=True)
    
    # Decade analysis
    for decade_start in range(1900, 2030, 10):
        decade_data = [d for d in divergences 
                      if decade_start <= d['year'] < decade_start + 10]
        if decade_data:
            mean_gap = sum(d['gap'] for d in decade_data) / len(decade_data)
            max_gap = max(decade_data, key=lambda x: x['gap'])
            results['by_decade'][f"{decade_start}s"] = {
                'n_observations': len(decade_data),
                'mean_gap': round(mean_gap, 4),
                'max_gap_country': max_gap['country'],
                'max_gap_value': max_gap['gap'],
                'extreme_count': sum(1 for d in decade_data if d['gap'] > 0.3),
            }
    
    # Top 20 all-time divergences
    divergences.sort(key=lambda x: x['gap'], reverse=True)
    results['top_20_divergences'] = divergences[:20]
    
    # Summary statistics
    if divergences:
        gaps = [d['gap'] for d in divergences]
        results['summary'] = {
            'total_observations': len(divergences),
            'mean_gap': round(sum(gaps) / len(gaps), 4),
            'median_gap': round(sorted(gaps)[len(gaps)//2], 4),
            'max_gap': round(max(gaps), 4),
            'extreme_cases_count': len(results['extreme_cases']),
            'pct_gap_above_0_1': round(100 * sum(1 for g in gaps if g > 0.1) / len(gaps), 1),
            'pct_gap_above_0_3': round(100 * sum(1 for g in gaps if g > 0.3) / len(gaps), 1),
            'key_finding': (
                f"Of {len(divergences)} country-year observations, "
                f"{len(results['extreme_cases'])} have additive > 0.5 but multiplicative < 0.1 "
                f"(hidden zeros). The additive index systematically overstates democracy "
                f"for countries with a collapsed dimension."
            ),
        }
    
    # Save
    os.makedirs(os.path.dirname(RESULTS), exist_ok=True)
    with open(RESULTS, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to {RESULTS}")
    print(f"Extreme cases (api>0.5, mpi<0.1): {len(results['extreme_cases'])}")
    if results['extreme_cases']:
        print("Top 5:")
        for c in results['extreme_cases'][:5]:
            print(f"  {c['country']} ({c['year']}): add={c['api_additive']}, mult={c['mpi_multiplicative']}, gap={c['gap']}")
    
    return results


if __name__ == '__main__':
    run_vdem_audit()
