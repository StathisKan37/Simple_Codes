<?php
	interface User_interface{
		// Defining the names of the methods
		public function my_greet($my_name);
		public function my_speech();
	}
	// These classes must use all of the methods of the 'User_interface'
	// Otherwise it will give an error
	class Human implements User_interface{
		public function my_greet($my_name){
			echo "My name is ".$my_name."<br>";}
		public function my_speech(){
			echo "I am a human <br>";}
	}
	class Android implements User_interface{
		public function my_greet($my_name){
			echo "My name is ".$my_name."<br>";}
		public function my_speech(){
			echo "I am an android <br>";}
	}
	
	$user_1 = new Human();
	// => My name is David Bowman
	$user_1->my_greet("David Bowman");
	// => I am a human
	$user_1->my_speech();
	
	$user_2 = new Android();
	// => My name is HAL 9000
	$user_2->my_greet("HAL 9000");
	// => I am an android
	$user_2->my_speech();
?>
