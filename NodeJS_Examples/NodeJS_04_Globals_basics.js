// Printing the global dirname and filename
console.log("Directory name:", __dirname);
console.log("Directory name:", __filename);

// Including process module
const process = require('process');
// The process object represents the currently running application
console.log("Process ID:", process.pid);
console.log("Platform:", process.plaform);
console.log("Node.js Version:", process.version);
console.log("Node enviroment:", process.env.NODE_ENV);
