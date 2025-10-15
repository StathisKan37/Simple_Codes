<html>
<body>
<?php 
	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		// Printing the name
		if (!empty($_POST["name"])){
			echo "<h3>Hello! My name is ".$_POST["name"]."</h3>";}
		// Printing the email
		if (!empty($_POST["email"])){
			echo "<h3>Email address: ".$_POST["email"]."</h3>";}
		// Printing the age
		if (!(empty($_POST["age"]))) {
			echo "<h3>My age is ".$_POST["age"]."</h3>";}
		// Printing the comments
		if (!(empty($_POST["comment"]))) {
			echo "<p>".$_POST["comment"]."</p>";}
		// Printing the gender
		if (!(empty($_POST["gender"]))) {
			echo "<h3>Gender: ".$_POST["gender"]."</h3>";}
	}
?>
</body>
</html>
