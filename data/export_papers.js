const fs = require('fs');
const path = require('path');
const base = 'D:/Projects/Multiplicative-Composition/papers';
const files = {
  paper1: path.join(base, 'paper1/paper_v2.tex'),
  paper2: path.join(base, 'paper2/paper2_v1.tex'),
  paper3: path.join(base, 'paper3/paper3_v1.tex'),
  paper4: path.join(base, 'paper4/paper4_v1.tex')
};
const out = {};
for (const [key, filepath] of Object.entries(files)) {
  try {
    const content = fs.readFileSync(filepath, 'utf-8');
    // Base64 encode to avoid JSON escaping issues
    out[key] = Buffer.from(content).toString('base64');
    console.log(`${key}: ${content.length} bytes`);
  } catch (e) {
    console.log(`${key}: ERROR - ${e.message}`);
  }
}
fs.writeFileSync('D:/Projects/Multiplicative-Composition/data/results/all_papers_b64.json', JSON.stringify(out));
console.log('Written to all_papers_b64.json');
