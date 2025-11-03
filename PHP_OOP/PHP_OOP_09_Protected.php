<?php
	class User{
		protected $my_name;
		public function __construct($my_name){
			$this->my_name = $my_name;}
	}
	class My_speech extends User{
		public function speak(){
			// The child class can use a protected property
			echo "My name is ".$this->my_name;}
	}
	
	$user_1 = new My_speech("David Bowman");
	// => My name is David Bowman
	$user_1->speak();
	
	// If we try to run this command:
	// echo $user_1->my_name;
	// It would return an error
?>
