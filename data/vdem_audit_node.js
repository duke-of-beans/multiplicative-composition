/**
 * Paper 4: The Additive Audit — V-Dem Electoral Democracy Index Analysis
 * Node.js version for execution on Windows where Python is unavailable.
 * 
 * Reads V-Dem v16 Core dataset, compares additive (v2x_api) vs 
 * multiplicative (v2x_mpi) polyarchy indices.
 */
const fs = require('fs');
const path = require('path');

const DATA_DIR = __dirname;
const DATASET = path.join(DATA_DIR, 'datasets', 'V-Dem-CY-Core-v16', 'V-Dem-CY-Core-v16.csv');
const RESULTS = path.join(DATA_DIR, 'results', 'vdem_audit_results.json');

function parseCSVLine(line) {
  const fields = [];
  let current = '';
  let inQuotes = false;
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (ch === '"') {
      inQuotes = !inQuotes;
    } else if (ch === ',' && !inQuotes) {
      fields.push(current.trim());
      current = '';
    } else {
      current += ch;
    }
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
  console.log('Reading V-Dem dataset...');
  if (!fs.existsSync(DATASET)) {
    console.error('Dataset not found:', DATASET);
    process.exit(1);
  }
  
  const raw = fs.readFileSync(DATASET, 'utf-8');
  const lines = raw.split('\n').filter(l => l.trim());
  console.log(`Total lines: ${lines.length}`);
  
  // Parse header
  const header = parseCSVLine(lines[0]);
  const colIdx = {};
  const needed = ['country_name', 'country_text_id', 'year', 'COWcode',
    'v2x_polyarchy', 'v2x_api', 'v2x_mpi',
    'v2x_freexp_altinf', 'v2x_frassoc_thick', 'v2x_suffr', 
    'v2xel_frefair', 'v2x_elecoff'];
  
  for (const col of needed) {
    const idx = header.indexOf(col);
    if (idx >= 0) colIdx[col] = idx;
  }
  console.log('Found columns:', Object.keys(colIdx).join(', '));
  
  const results = {
    dataset: 'V-Dem v16 Core (Country-Year)',
    n_observations: lines.length - 1,
    variables_used: Object.keys(colIdx),
    extreme_cases: [],
    by_decade: {},
    top_20_divergences: [],
    summary: {}
  };
  
  const divergences = [];
  let processed = 0;
  
  for (let i = 1; i < lines.length; i++) {
    const fields = parseCSVLine(lines[i]);
    const country = fields[colIdx['country_name']] || '';
    const year = safeFloat(fields[colIdx['year']]);
    const api = safeFloat(fields[colIdx['v2x_api']]);
    const mpi = safeFloat(fields[colIdx['v2x_mpi']]);
    const edi = safeFloat(fields[colIdx['v2x_polyarchy']]);
    
    if (year === null || api === null || mpi === null || edi === null) continue;
    
    processed++;
    const gap = api - mpi;
    
    const entry = {
      country,
      year: Math.round(year),
      api_additive: Math.round(api * 10000) / 10000,
      mpi_multiplicative: Math.round(mpi * 10000) / 10000,
      edi_official: Math.round(edi * 10000) / 10000,
      gap: Math.round(gap * 10000) / 10000
    };
    
    // Add component scores
    for (const comp of ['v2x_freexp_altinf', 'v2x_frassoc_thick', 
                         'v2x_suffr', 'v2xel_frefair', 'v2x_elecoff']) {
      if (colIdx[comp] !== undefined) {
        const val = safeFloat(fields[colIdx[comp]]);
        if (val !== null) entry[comp] = Math.round(val * 10000) / 10000;
      }
    }
    
    divergences.push(entry);
    
    // Extreme cases: additive says "democratic" but multiplicative says "zero"
    if (api > 0.5 && mpi < 0.1) {
      results.extreme_cases.push(entry);
    }
  }
  
  console.log(`Processed ${processed} valid observations`);
  
  // Sort extreme cases
  results.extreme_cases.sort((a, b) => b.gap - a.gap);
  
  // Decade analysis
  for (let decade = 1780; decade <= 2020; decade += 10) {
    const decadeData = divergences.filter(d => d.year >= decade && d.year < decade + 10);
    if (decadeData.length > 0) {
      const meanGap = decadeData.reduce((s, d) => s + d.gap, 0) / decadeData.length;
      const maxEntry = decadeData.reduce((max, d) => d.gap > max.gap ? d : max, decadeData[0]);
      results.by_decade[`${decade}s`] = {
        n_observations: decadeData.length,
        mean_gap: Math.round(meanGap * 10000) / 10000,
        max_gap_country: maxEntry.country,
        max_gap_value: maxEntry.gap,
        extreme_count: decadeData.filter(d => d.gap > 0.3).length
      };
    }
  }
  
  // Top 20 divergences
  divergences.sort((a, b) => b.gap - a.gap);
  results.top_20_divergences = divergences.slice(0, 20);
  
  // Summary
  const gaps = divergences.map(d => d.gap);
  gaps.sort((a, b) => a - b);
  results.summary = {
    total_observations: divergences.length,
    mean_gap: Math.round(gaps.reduce((s, g) => s + g, 0) / gaps.length * 10000) / 10000,
    median_gap: Math.round(gaps[Math.floor(gaps.length / 2)] * 10000) / 10000,
    max_gap: Math.round(Math.max(...gaps) * 10000) / 10000,
    extreme_cases_count: results.extreme_cases.length,
    pct_gap_above_0_1: Math.round(1000 * gaps.filter(g => g > 0.1).length / gaps.length) / 10,
    pct_gap_above_0_3: Math.round(1000 * gaps.filter(g => g > 0.3).length / gaps.length) / 10,
    key_finding: `Of ${divergences.length} country-year observations, ` +
      `${results.extreme_cases.length} have additive > 0.5 but multiplicative < 0.1 ` +
      `(hidden zeros). The additive index systematically overstates democracy ` +
      `for countries with a collapsed dimension.`
  };
  
  // Save
  fs.mkdirSync(path.dirname(RESULTS), { recursive: true });
  fs.writeFileSync(RESULTS, JSON.stringify(results, null, 2));
  
  console.log(`\nResults saved to ${RESULTS}`);
  console.log(`Extreme cases (api>0.5, mpi<0.1): ${results.extreme_cases.length}`);
  if (results.extreme_cases.length > 0) {
    console.log('Top 10:');
    for (const c of results.extreme_cases.slice(0, 10)) {
      console.log(`  ${c.country} (${c.year}): add=${c.api_additive}, mult=${c.mpi_multiplicative}, gap=${c.gap}`);
    }
  }
  console.log(`\nMean gap: ${results.summary.mean_gap}`);
  console.log(`Max gap: ${results.summary.max_gap}`);
  console.log(`% with gap > 0.1: ${results.summary.pct_gap_above_0_1}%`);
  console.log(`% with gap > 0.3: ${results.summary.pct_gap_above_0_3}%`);
}

run();
