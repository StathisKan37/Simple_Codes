<html>
<body>

<?php
	// The file 'PHP_Hello_print.php' exists
	include 'Other_files/PHP_Hello_print.php';
	echo "<p>Name: ".$myname."</p>";
	
	// The file 'noFileExists.php' doesn't exist
	// So nothing will be printed
	require 'Other_files/noFileExists.php';
	echo "<p>Name: ".$myname."</p>";
?>

</body>
</html>
