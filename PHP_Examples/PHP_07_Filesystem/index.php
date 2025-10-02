<!DOCTYPE html>
<html>
<body>
<?php
	// Cheching if a file named 'Text_file.txt' exists
	if (file_exists('Text_file.txt')){
		echo '<p>The file exists</p>';
		echo '<p>And the size of th file is '.filesize('Text_file.txt').' bytes</p>';}
	else{
		echo '<p>The file does not exists</p>';}
	
	// Opening the Text_file.txt
	$file = fopen('Text_file.txt', 'r');
	// Printing every line of the Text_file.txt
	while (($line = fgets($file)) != false){
		echo $line.'<br>';}
?>
</body>
</html>
