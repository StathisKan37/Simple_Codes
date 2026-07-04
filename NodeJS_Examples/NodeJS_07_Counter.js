// Importing 'timers' module
const { setTimeout, setInterval, setImmediate } = require('timers');
// Setting the counter to 0
let count = 0;

// Starting an interval wich runs every 1000 milliseconds
const interval = setInterval(() => {
	// Printing a message and adding 1 to counter
	console.log(count +1);
	count++;

	// Stopping the interval when the counter reaches 5
	if (count==5){
		clearInterval(interval);
		console.log("Done");
	}
}, 1000)
