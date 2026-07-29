/**
 * Paper 3 retroactive edit for Paper 4 cross-reference.
 * 1 surgical insertion in institutional additive default section.
 */
const fs = require('fs');
const path = 'D:/Projects/Multiplicative-Composition/papers/paper3/paper3_v1.tex';

fs.copyFileSync(path, path.replace('.tex', '_pre_p4_edits.tex'));

let content = fs.readFileSync(path, 'utf-8');
let edits = 0;

// EDIT 1: Institutional Additive Default section
// Find: "In each case, the multiplicative model predicts suboptimal outcomes when any dimension is near zero, and the evidence confirms."
// Add Paper 4 evidence after
const edit1_find = "In each case, the multiplicative model predicts suboptimal outcomes when any dimension is near zero, and the evidence confirms.";
const edit1_replace = "In each case, the multiplicative model predicts suboptimal outcomes when any dimension is near zero, and the evidence confirms. A systematic audit of composite indices \\cite{kirsch2026audit} quantifies this pattern: in the V-Dem democracy dataset, 9.6\\% of country-year observations are classified as ``democratic'' by the additive index despite having a collapsed dimension, and these countries remain autocratic 91\\% of the time---the additive default does not merely misallocate resources, it misdiagnoses the system.";
if (content.includes(edit1_find)) {
  content = content.replace(edit1_find, edit1_replace);
  edits++;
  console.log('Edit 1: Added Paper 4 evidence in institutional additive default');
} else {
  console.log('Edit 1: MARKER NOT FOUND');
}

// EDIT 2: Add bibliography entry
const edit2_find = "\\end{thebibliography}";
const edit2_replace = `\\bibitem{kirsch2026audit}
Kirsch, D. (2026). The additive audit: Systematic measurement error from additive aggregation of non-substitutable dimensions. \\textit{Working paper}.

\\end{thebibliography}`;
if (content.includes(edit2_find)) {
  content = content.replace(edit2_find, edit2_replace);
  edits++;
  console.log('Edit 2: Added Paper 4 bibliography entry');
} else {
  console.log('Edit 2: MARKER NOT FOUND');
}

fs.writeFileSync(path, content);

// Verify
const verify = fs.readFileSync(path, 'utf-8');
const result = {
  edits_applied: edits,
  refs: (verify.match(/kirsch2026audit/g) || []).length,
  size: verify.length
};
fs.writeFileSync('D:/Projects/Multiplicative-Composition/data/results/edit3_verify.json', JSON.stringify(result, null, 2));
