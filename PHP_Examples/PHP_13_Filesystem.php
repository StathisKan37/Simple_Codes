<!DOCTYPE html>
<html>
<body>
<?php
	// Creating a new file in the directory
	$php_file = fopen('Other_files/PHP_File_text.txt', 'w');
	
	// Writing content to the file
	fwrite($php_file, "hello world!");
	
	// Printing the size of the file
	echo filesize('Other_files/PHP_File_text.txt');
	
	// Adding content to the file
	$php_file = fopen('Other_files/PHP_File_text.txt', 'a');
	fwrite($php_file, "\nHello World!");
	fwrite($php_file, "\nHELLO WORLD!");
	
	// Printing again the size of the file
	clearstatcache();
	echo '<br>';
	echo filesize('Other_files/PHP_File_text.txt');
	
	// Printing the content of the file if the file exists
	if (file_exists('Other_files/PHP_File_text.txt')){
		$php_file = fopen('Other_files/PHP_File_text.txt', 'r');
		while (($line = fgets($php_file)) != false){
			echo '<br>'.$line;}}
	else{
		echo '<br>File does not exist';}
	
	// Closing the file
	fclose('Other_files/PHP_File_text.txt');
?>
</body>
</html>
