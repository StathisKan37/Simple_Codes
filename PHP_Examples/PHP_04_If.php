<!DOCTYPE html>
<html>
<body>
<?php
	// Getting the current hour in 24-hour format (00–23)
	$t = date("H");
	// Printing the current hour to the page
	echo "<p>The hour (of the server) is " . $t ."</p>";

	// Checking the hour and display a different message
	if ($t < "10"){
		echo "<p>Have a good morning!</p>";}
	elseif ($t < "20"){
		echo "<p>Have a good day!</p>";}
	else{
		echo "<p>Have a good night!</p>";}
?>
</body>
</html>
