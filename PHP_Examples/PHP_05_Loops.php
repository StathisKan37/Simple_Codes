<!DOCTYPE html>
<html>
<body>
<?php
	$i = 1;
	echo '<p>While loop:</p>';
	while ($i < 6){
		echo '<p>'.$i.'</p>';
		$i++;}

	$i = 1;
	echo '<p>Do while loop:</p>';
	do{
		echo '<p>'.$i.'</p>';
		$i++;
	}while ($i < 6);
	
	echo '<p>For loop:</p>';
	for ($x = 1; $x <= 5; $x++) {
		echo '<p>'.$x.'</p>';}

?>
</body>
</html>
