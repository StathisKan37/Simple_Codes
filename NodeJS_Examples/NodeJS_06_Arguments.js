// Run this code with two arguments:
// 1) Name
// 2) Age
// Example:
// $ node NodeJS_06_Arguments.js Heywood_floyd 43

// Including process module
const process = require('process');

// Printing the arguments
console.log("My name is", process.argv[2]);
console.log("I am", process.argv[3], "years old");
