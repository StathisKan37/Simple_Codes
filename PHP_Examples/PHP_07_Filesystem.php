<!DOCTYPE html>
<html>
<body>
<?php
	// Cheching if a file named 'PHP_File_text.txt' exists
	if (file_exists('Other_files/PHP_File_text.txt')){
		echo '<p>The file exists</p>';
		echo '<p>And the size of th file is '.filesize('Other_files/PHP_File_text.txt').' bytes</p>';}
	else{
		echo '<p>The file does not exists</p>';}
	
	// Opening the Text_file.txt
	$file = fopen('Other_files/PHP_File_text.txt', 'r');
	// Printing every line of the Text_file.txt
	while (($line = fgets($file)) != false){
		echo $line.'<br>';}
?>
</body>
</html>
