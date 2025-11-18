<?php
	namespace Human;
	// The following classes belong to 'Human' namespace
	class User{
		public function my_speech($my_name){
			echo "My name is ".$my_name."<br>";
			echo "I am a human<br>";}
	}

	namespace Android;
	// The following classes belong to 'Android' namespace
	class User{
		public function my_speech($my_name){
			echo "My name is ".$my_name."<br>";
			echo "I am an android<br>";}
	}
	
	$user_1 = new \Human\User();
	// => My name is David Bowman
	// => I am a human
	$user_1->my_speech("David Bowman");
	$user_2 = new \Android\User();
	// => My name is HAL 9000
	// => I am an android
	$user_2->my_speech("HAL 9000");
?>
