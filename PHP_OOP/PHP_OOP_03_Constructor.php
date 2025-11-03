<?php
	class My_name{
		
		// Constructor method
		public function __construct(){
			echo 'An object is created successfully<br>';
		}
		
		// Destruction method
		public function __destruct(){
			echo 'The object is deleted successfully<br>';
		}
	}
	
	// By creating an object, the construct function is
	// called automatically
	$name = new My_name();
	
	// By deleting the object, the construct function is
	// called automatically
	unset($name);
?>
