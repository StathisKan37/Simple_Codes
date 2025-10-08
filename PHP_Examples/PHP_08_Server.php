<!DOCTYPE html>
<html>
<body>

<?php
	// Filename of the currently executing script:
	echo $_SERVER['PHP_SELF'];
	echo "<br>";
	// Version of the Common Gateway Interface (CGI):
	echo $_SERVER['GATEWAY_INTERFACE'];
	echo "<br>";
	// IP address of the host server
	echo $_SERVER['SERVER_ADDR'];
	echo "<br>";
	// Server’s host name:
	echo $_SERVER['SERVER_NAME'];
	echo "<br>";
	// Server identification
	echo $_SERVER['SERVER_SOFTWARE'];
	echo "<br>";
	// Host header:
	echo $_SERVER['HTTP_HOST'];
	echo "<br>";
	// The complete URL of the current page:
	echo $_SERVER['HTTP_REFERER'];
	echo "<br>";
	// Browser’s user agent
	echo $_SERVER['HTTP_USER_AGENT'];
	echo "<br>";
	// Path of the current script
	echo $_SERVER['SCRIPT_NAME'];
?>

</body>
</html>
