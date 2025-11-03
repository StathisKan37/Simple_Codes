<?php
	// The parent class
	class Human_speech{
		public function speak(){
			echo "I am a human<br>";}
	}
	// The child class
	class Android_speech extends Human_speech{
		public function speak(){
			echo "I am an android<br>";}
	}
	
	// Creating an object of the parent class
	$David_Bowman = new Human_speech();
	// Calling the function of the parent
	// => I am a human
	$David_Bowman->speak();
	
	// Creating an object of the child class
	$HAL_9000 = new Android_speech();
	// Calling the function of the child
	// => I am an android
	$HAL_9000->speak();
?>
