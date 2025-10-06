<!DOCTYPE html>
<html>
<body>
<?php
	// Printing the PI number
	echo '<p>PI number: '.pi().'</p>';
	// Printing the minimum and maximum
	echo '<p>Minimum: '.min(0, 150, 30, 20, -8, -200).'</p>';
	echo '<p>Maximum: '.max(0, 150, 30, 20, -8, -200).'</p>';
	// Printing the absolute value
	echo '<p>Absolute value: '.abs(-6.7).'</p>';
	// Printing the square root
	echo '<p>Square root: '.sqrt(64).'</p>';
	// Printing rounded floats
	echo '<p>Rounded float: '.round(1.49).'</p>';
	// Printing an random integer between 10 and 100
	echo '<p>Random integer: '.rand(10, 100).'</p>';
?>
</body>
</html>
