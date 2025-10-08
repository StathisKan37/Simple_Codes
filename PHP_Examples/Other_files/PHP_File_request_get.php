<?php
	// Check if GET parameters exist
	if (isset($_GET["name"]) && isset($_GET["age"])){
		// Saving the parameters in variables
		$name = $_GET["name"];
		$age = $_GET["age"];
		// Printing the result
		echo "Hello, my name is $name and I am $age years old.";}
	else {
		echo "No GET parameters received.";
	}
?>
