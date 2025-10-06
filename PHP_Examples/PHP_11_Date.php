<!DOCTYPE html>
<html>
<body>

<?php
	// Setting the timezone to Athens in Greece
	date_default_timezone_set("Europe/Athens");
	
	echo "<h3>The date today is:</h3>";
	echo "<p>".date("Y/m/d")."<br>".date("Y.m.d")."<br>".date("Y-m-d")."<br>". date("l")."</p>";
	
	echo "<h3>The time right now is:</h3>";
	echo "<p>".date("h:i:sa")."</p>";

	echo "<h3>The date and time tomorrow will be:</h3>";
	$d=strtotime("tomorrow");
	echo "<p>".date("Y-m-d h:i:sa", $d)."</p>";

	echo "<h3>The date and time next Saturday will be:</h3>";
	$d=strtotime("next Saturday");
	echo "<p>".date("Y-m-d h:i:sa", $d)."</p>";

	echo "<h3>The date and time in 3 months will be:</h3>";
	$d=strtotime("+3 Months");
	echo "<p>".date("Y-m-d h:i:sa", $d)."</p>";
?>

</body>
</html>
