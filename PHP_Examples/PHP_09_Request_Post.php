<!DOCTYPE html>
<html>
<body>

<!-- Definning the form and button -->
<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
	My name: <input type="text" name="fname">
	<input type="submit">
</form>

<?php
	// Check if the request method is POST
	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		// Collecting the value of input field
		$name = $_POST['fname'];
		// Printing the name (if exists)
		if (empty($name)) {
			echo "Name is empty";
		}
		else{
			echo $name;
		}
	}
?>

</body>
</html>
