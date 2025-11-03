<?php
	abstract class User_abstract{
		protected $my_name;
		public function __construct($my_name){
			$this->my_name = $my_name;}
		
		public function my_greet(){
			echo "My name is ".$this->my_name."<br>";}
	}
	
	class Human extends User_abstract{
		public function my_speech(){
			echo "I am a human<br>";}
	}
	
	class Android extends User_abstract{
		public function my_speech(){
			echo "I am an android<br>";}
	}
	
	$user_1 = new Human("David Bowman");
	// => My name is David Bowman
	$user_1->my_greet();
	// => I am a human
	$user_1->my_speech();
	
	$user_2 = new Android("HAL 9000");
	// => My name is HAL 9000
	$user_2->my_greet();
	// => I am an android
	$user_2->my_speech();
	
	// We cannot create an object from an abstract class
	// The following comand would return an error:
	// $user_3 = new User("Frank Poole")
?>
