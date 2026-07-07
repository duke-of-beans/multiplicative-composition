/**
 * Paper 4: V-Dem Outcome Validation
 * Do countries in the "hidden zero" divergence zone (api > 0.5, mpi < 0.1)
 * subsequently experience democratic breakdown at higher rates?
 * 
 * Uses v2x_regime (Regimes of the World):
 *   0 = closed autocracy
 *   1 = electoral autocracy  
 *   2 = electoral democracy
 *   3 = liberal democracy
 * 
 * Method: For each country-year, check regime type 5 and 10 years later.
 * Compare breakdown rates for:
 *   Group A: "hidden zeros" (api > 0.5, mpi < 0.1)
 *   Group B: "agreement" (api > 0.5, mpi > 0.5) — both say democratic
 *   Group C: "agreement-low" (api < 0.3, mpi < 0.3) — both say autocratic
 */
const fs = require('fs');
const path = require('path');

const DATA_DIR = __dirname;
const DATASET = path.join(DATA_DIR, 'datasets', 'V-Dem-CY-Core-v16', 'V-Dem-CY-Core-v16.csv');
const RESULTS = path.join(DATA_DIR, 'results', 'vdem_outcome_validation.json');

function parseCSVLine(line) {
  const fields = [];
  let current = '';
  let inQuotes = false;
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (ch === '"') { inQuotes = !inQuotes; }
    else if (ch === ',' && !inQuotes) { fields.push(current.trim()); current = ''; }
    else { current += ch; }
  }
  fields.push(current.trim());
  return fields;
}

function safeFloat(val) {
  if (!val || val === '' || val === 'NA' || val === '.') return null;
  const n = parseFloat(val);
  return isNaN(n) ? null : n;
}

function run() {
  console.log('Loading V-Dem data for outcome validation...');
  const raw = fs.readFileSync(DATASET, 'utf-8');
  const lines = raw.split('\n').filter(l => l.trim());
  
  const header = parseCSVLine(lines[0]);
  const idx = {};
  for (const col of ['country_name','country_text_id','year','v2x_polyarchy','v2x_api','v2x_mpi',
                      'v2x_regime','v2x_regime_amb','v2x_freexp_altinf','v2x_frassoc_thick',
                      'v2x_suffr','v2xel_frefair','v2x_elecoff']) {
    const i = header.indexOf(col);
    if (i >= 0) idx[col] = i;
  }
  console.log('Columns found:', Object.keys(idx).join(', '));
  
  // Build lookup: country -> year -> {api, mpi, regime, ...}
  const data = {};
  for (let i = 1; i < lines.length; i++) {
    const f = parseCSVLine(lines[i]);
    const country = f[idx['country_name']] || '';
    const year = safeFloat(f[idx['year']]);
    const api = safeFloat(f[idx['v2x_api']]);
    const mpi = safeFloat(f[idx['v2x_mpi']]);
    const regime = safeFloat(f[idx['v2x_regime']]);
    
    if (!country || year === null) continue;
    if (!data[country]) data[country] = {};
    data[country][Math.round(year)] = {
      api, mpi, regime,
      elecoff: safeFloat(f[idx['v2x_elecoff']]),
      freexp: safeFloat(f[idx['v2x_freexp_altinf']]),
    };
  }
  
  console.log(`Built lookup for ${Object.keys(data).length} countries`);
  
  // For each country-year, classify into groups and check future outcomes
  const horizons = [5, 10];
  const results = { horizons: {}, group_sizes: {}, extreme_case_outcomes: [] };
  
  for (const h of horizons) {
    const groups = {
      hidden_zero: { n: 0, breakdown: 0, stayed_autocratic: 0, democratized: 0, no_future: 0 },
      agreement_dem: { n: 0, breakdown: 0, stayed_democratic: 0, no_future: 0 },
      agreement_low: { n: 0, breakdown: 0, stayed_autocratic: 0, democratized: 0, no_future: 0 },
    };
    
    for (const country of Object.keys(data)) {
      for (const yearStr of Object.keys(data[country])) {
        const year = parseInt(yearStr);
        const obs = data[country][year];
        if (obs.api === null || obs.mpi === null) continue;
        
        const futureYear = year + h;
        const future = data[country][futureYear];
        
        // Hidden zero: additive says democratic, multiplicative says zero
        if (obs.api > 0.5 && obs.mpi < 0.1) {
          groups.hidden_zero.n++;
          if (!future || future.regime === null) {
            groups.hidden_zero.no_future++;
          } else if (future.regime <= 1) {
            // Still autocratic (closed or electoral autocracy)
            groups.hidden_zero.stayed_autocratic++;
          } else if (future.regime >= 2) {
            // Democratized (electoral or liberal democracy)
            groups.hidden_zero.democratized++;
          }
        }
        
        // Agreement democratic: both say democratic
        if (obs.api > 0.5 && obs.mpi > 0.5) {
          groups.agreement_dem.n++;
          if (!future || future.regime === null) {
            groups.agreement_dem.no_future++;
          } else if (future.regime <= 1) {
            // Breakdown: was democratic by both measures, became autocratic
            groups.agreement_dem.breakdown++;
          } else {
            groups.agreement_dem.stayed_democratic++;
          }
        }
        
        // Agreement low: both say autocratic
        if (obs.api < 0.3 && obs.mpi < 0.3) {
          groups.agreement_low.n++;
          if (!future || future.regime === null) {
            groups.agreement_low.no_future++;
          } else if (future.regime >= 2) {
            groups.agreement_low.democratized++;
          } else {
            groups.agreement_low.stayed_autocratic++;
          }
        }
      }
    }
    
    // Compute rates (excluding no_future)
    const hz = groups.hidden_zero;
    const ad = groups.agreement_dem;
    const hzValid = hz.n - hz.no_future;
    const adValid = ad.n - ad.no_future;
    
    results.horizons[`${h}_year`] = {
      hidden_zero: {
        total: hz.n,
        with_future_data: hzValid,
        stayed_autocratic: hz.stayed_autocratic,
        democratized: hz.democratized,
        pct_stayed_autocratic: hzValid > 0 ? Math.round(1000 * hz.stayed_autocratic / hzValid) / 10 : null,
        pct_democratized: hzValid > 0 ? Math.round(1000 * hz.democratized / hzValid) / 10 : null,
      },
      agreement_democratic: {
        total: ad.n,
        with_future_data: adValid,
        breakdown: ad.breakdown,
        stayed_democratic: ad.stayed_democratic,
        pct_breakdown: adValid > 0 ? Math.round(1000 * ad.breakdown / adValid) / 10 : null,
        pct_stayed_democratic: adValid > 0 ? Math.round(1000 * ad.stayed_democratic / adValid) / 10 : null,
      },
      agreement_low: {
        total: groups.agreement_low.n,
        with_future_data: groups.agreement_low.n - groups.agreement_low.no_future,
      },
      key_comparison: {
        hidden_zero_autocratic_rate: hzValid > 0 ? Math.round(1000 * hz.stayed_autocratic / hzValid) / 10 : null,
        agreement_dem_breakdown_rate: adValid > 0 ? Math.round(1000 * ad.breakdown / adValid) / 10 : null,
        note: 'If hidden-zero countries remain autocratic at much higher rates than agreement-democratic countries break down, the multiplicative index is the better predictor.'
      }
    };
    
    console.log(`\n=== ${h}-YEAR HORIZON ===`);
    console.log(`Hidden zeros: ${hz.n} obs, ${hzValid} with future data`);
    console.log(`  Stayed autocratic: ${hz.stayed_autocratic} (${results.horizons[`${h}_year`].hidden_zero.pct_stayed_autocratic}%)`);
    console.log(`  Democratized: ${hz.democratized} (${results.horizons[`${h}_year`].hidden_zero.pct_democratized}%)`);
    console.log(`Agreement-dem: ${ad.n} obs, ${adValid} with future data`);
    console.log(`  Breakdown: ${ad.breakdown} (${results.horizons[`${h}_year`].agreement_democratic.pct_breakdown}%)`);
    console.log(`  Stayed democratic: ${ad.stayed_democratic} (${results.horizons[`${h}_year`].agreement_democratic.pct_stayed_democratic}%)`);
  }
  
  // Track specific extreme cases (Hong Kong, Japan occupation, etc.)
  const trackCases = [
    {country: 'Hong Kong', years: [1990, 1995, 2000, 2005, 2010, 2015, 2020]},
    {country: 'Japan', years: [1950, 1955, 1960]},
  ];
  
  for (const tc of trackCases) {
    const caseData = [];
    for (const y of tc.years) {
      const obs = data[tc.country]?.[y];
      if (obs) {
        caseData.push({
          year: y,
          api: obs.api, mpi: obs.mpi, regime: obs.regime,
          elecoff: obs.elecoff, freexp: obs.freexp
        });
      }
    }
    results.extreme_case_outcomes.push({ country: tc.country, trajectory: caseData });
  }
  
  fs.writeFileSync(RESULTS, JSON.stringify(results, null, 2));
  console.log(`\nResults saved to ${RESULTS}`);
}

run();
