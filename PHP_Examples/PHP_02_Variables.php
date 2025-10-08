<!DOCTYPE html>
<html>
<body>
<?php
	// Saving an integer
	$var_int = 37;
	// Saving a float
	$var_float = 3.14159;
	// Saving a string
	$var_str = 'Stathis';
	// Saving a boolean
	$var_bool = True;
	// Saving an array
	$var_array = [1,2,3,4];
	// Saving a Null
	$var_null = NULL;
	
	// Printing the integers
	echo '<h3>Integer: '. $var_int .'</h3>';
	echo '<h3>Float: '. $var_float .'</h3>';
	echo '<h3>String: '. $var_str .'</h3>';
	echo '<h3>Boolean: '. ($var_bool ? 'True' : 'False') .'</h3>';
	echo '<h3>Array: '. implode(", ", $var_array) .'</h3>';
	echo '<h3>Null: '. (is_null($var_null) ? 'NULL' : $var_null) .'</h3>';
?>
</body>
</html>
