const fs = require('fs');
const path = 'D:/Projects/Multiplicative-Composition/BACKLOG.md';
let content = fs.readFileSync(path, 'utf-8');

// Add new DONE items after the first DONE line
const marker = '## DONE\n';
const newItems = `## DONE
- [x] Paper 1 retroactive Paper 4 cross-refs: 5 edits (additive default, V-Dem #8, institutional default, conclusion, bibitem) — 2026-07-07
- [x] Paper 3 retroactive Paper 4 cross-ref: institutional additive default + bibitem — 2026-07-07
`;

content = content.replace(marker, newItems);
fs.writeFileSync(path, content);
console.log('BACKLOG updated');
