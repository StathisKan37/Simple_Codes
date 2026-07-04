// Importing 2 methods from fs module
// 1. readFileSync
// 2. writeFileSync
const {readFileSync, writeFileSync} = require('fs');

// Loading 2 .txt files
const test_1_txt = readFileSync('./Other_files/Test_1.txt', 'utf8');
const test_2_txt = readFileSync('./Other_files/Test_2.txt', 'utf8');

// Creating  a new .txt file
writeFileSync(
	'./Other_files/New_text.txt',
	`Text file 1:\n${test_1_txt}\n\nText file 2:\n${test_2_txt}`
);
