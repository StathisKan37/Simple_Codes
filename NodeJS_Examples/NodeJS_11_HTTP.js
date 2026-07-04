// Importing the http module
const http = require('http');

// Creating a server
// req: Incoming request object
// res: Response object
const server = http.createServer((req,res) =>{
	// http://localhost:5000
    if (req.url === '/') {
        return res.end('<h1>Welcome to the homepage</h1>');
    }
	// http://localhost:5000/about
    if (req.url === '/about') {
        return res.end('Here is our history');
    }
	// Other URLs
    res.end('Wrong url');
});

// Starting the server on port 5000
// Displaying the message: 'Server is running on port 5000'
server.listen(5000, () => {console.log('Server is running on port 5000');});

// Type in the browser the following link
// http://localhost:5000
