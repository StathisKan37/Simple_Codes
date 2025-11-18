<?php
	class User{
		// Creating an invoke method
		public function __invoke($my_name){
			return "My name is ".$my_name."<br>";}
	}
	
	$user_1 = new User();
	
	// Calling the variable $user_1 as a method
	// => My name is David Bowman
	echo $user_1("David Bowman");
	// => My name is Frank Poole
	echo $user_1("Frank Poole");
	// => My name is Heywood Floyd
	echo $user_1("Heywood Floyd");	
?>
