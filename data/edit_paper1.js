/**
 * Paper 1 retroactive edits for Paper 4 cross-references.
 * 5 surgical find-and-replace operations.
 */
const fs = require('fs');
const path = 'D:/Projects/Multiplicative-Composition/papers/paper1/paper_v2.tex';

// Backup first
fs.copyFileSync(path, path.replace('.tex', '_pre_p4_edits.tex'));

let content = fs.readFileSync(path, 'utf-8');
let edits = 0;

// EDIT 1: Line ~105 - After "0.77" in persistence of additive default
// Find: "A country with zero press freedom is rated 77\% democratic by the additive half of their index."
// Insert after preceding sentence about 0.77
const edit1_find = "A country with zero press freedom is rated 77\\% democratic by the additive half of their index.";
const edit1_replace = "A systematic audit of 26,954 V-Dem country-year observations reveals that this is not an isolated case: 2,586 observations (9.6\\%) have additive scores above 0.5 while the multiplicative score is below 0.1, and predictive validation using subsequent regime outcomes confirms these countries remain autocratic 91\\% of the time within five years \\cite{kirsch2026audit}. A country with zero press freedom is rated 77\\% democratic by the additive half of their index.";
if (content.includes(edit1_find)) {
  content = content.replace(edit1_find, edit1_replace);
  edits++;
  console.log('Edit 1: Inserted Paper 4 quantified evidence in additive default section');
} else {
  console.log('Edit 1: MARKER NOT FOUND');
}

// EDIT 2: Line ~326 - V-Dem derivation #8
// Find: "The present paper provides that reason."
// Replace with: adds companion audit reference
const edit2_find = "The present paper provides that reason.";
const edit2_replace = "The present paper provides the formal reason; the companion audit \\cite{kirsch2026audit} provides the empirical validation: across 26,954 country-year observations, the multiplicative index correctly predicts regime type while the additive index systematically misclassifies.";
if (content.includes(edit2_find)) {
  content = content.replace(edit2_find, edit2_replace);
  edits++;
  console.log('Edit 2: Updated V-Dem derivation #8 with companion audit reference');
} else {
  console.log('Edit 2: MARKER NOT FOUND');
}

// EDIT 3: Line ~513 - institutional additive default
// Find: "a country with zero press freedom scores 0.77 on democracy; a drug"
// Insert Paper 4 citation after "0.77 on democracy"
const edit3_find = "a country with zero press freedom scores 0.77 on democracy;";
const edit3_replace = "a country with zero press freedom scores 0.77 on democracy \\cite{kirsch2026audit};";
if (content.includes(edit3_find)) {
  content = content.replace(edit3_find, edit3_replace);
  edits++;
  console.log('Edit 3: Added citation in institutional additive default');
} else {
  console.log('Edit 3: MARKER NOT FOUND');
}

// EDIT 4: Conclusion - "systematic audit" future work -> now done
// Find: "the systematic audit of existing additive indices across policy domains---identifying which composite metrics are currently making the composition error described here, and quantifying the consequences."
const edit4_find = "the systematic audit of existing additive indices across policy domains---identifying which composite metrics are currently making the composition error described here, and quantifying the consequences.";
const edit4_replace = "the systematic audit of existing additive indices across policy domains. A companion paper \\cite{kirsch2026audit} initiates this program, auditing V-Dem and the HDI and demonstrating a 9.6\\% hidden-zero rate in the world's most comprehensive democracy dataset.";
if (content.includes(edit4_find)) {
  content = content.replace(edit4_find, edit4_replace);
  edits++;
  console.log('Edit 4: Updated conclusion future work -> now done');
} else {
  console.log('Edit 4: MARKER NOT FOUND');
}

// EDIT 5: Add bibliography entry before \end{thebibliography}
const edit5_find = "\\end{thebibliography}";
const edit5_replace = `\\bibitem{kirsch2026audit}
Kirsch, D. (2026). The additive audit: Systematic measurement error from additive aggregation of non-substitutable dimensions. \\textit{Working paper}.

\\end{thebibliography}`;
if (content.includes(edit5_find)) {
  content = content.replace(edit5_find, edit5_replace);
  edits++;
  console.log('Edit 5: Added Paper 4 bibliography entry');
} else {
  console.log('Edit 5: MARKER NOT FOUND');
}

fs.writeFileSync(path, content);
console.log(`\nTotal edits applied: ${edits}/5`);
console.log(`File written: ${path}`);
