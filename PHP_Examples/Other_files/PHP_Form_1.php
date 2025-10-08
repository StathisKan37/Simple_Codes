<html>
<body>
<?php 
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["name"])) {
    echo "<h3>Name is required</h3>";
  } else {
    echo "<h3>Hello! My name is ".$_POST["name"]."</h3>";
  }
}
?>
</body>
</html>
