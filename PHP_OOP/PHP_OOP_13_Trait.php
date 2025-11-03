<?php
	// Definign a trait with a method
	trait my_traits{
		public function my_greet($my_name){
			echo "My name is ".$my_name."<br>";}
	}
	
	class Human{
		// The class uses the trait
		use my_traits;
		public function __construct($my_name){
			$this->my_greet($my_name);}
	}
	
	// => My name is David Bowman
	$user_1 = new Human("David Bowman");
	// => My name is Frank Poole
	$user_2 = new Human("Frank Poole");
	// => My name is Heywood Floyd
	$user_3 = new Human("Heywood Floyd");
?>
