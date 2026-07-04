// Including os module
const os = require('os');

// Printing information of the operating systems
console.log("Platform:", os.platform());
console.log("OS Version:", os.release());
console.log("CPU architectue:", os.arch());
console.log("CPU cores:", os.cpus().length);
console.log("First CPU:", os.cpus()[0].model);
console.log("Uptime:", os.uptime());
console.log("Total memory:", os.totalmem());
console.log("Free memory:", os.freemem());
console.log("Platform:", os.platform());

// Printing information about user
console.log("Username:", os.userInfo().username);
console.log("Home directory:", os.userInfo().homedir);
