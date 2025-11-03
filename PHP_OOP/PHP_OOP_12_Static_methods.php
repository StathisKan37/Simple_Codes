<?php
	class My_speech {
		public static function human($my_name){
			return "My name is ".$my_name.". I am a human<br>";}
		public static function android($my_name){
			return "My name is ".$my_name.". I am an android<br>";}
	}
	
	// Calling the functions of class My_speech(), without creating objects
	
	// => My name is David Bowman. I am a human
	echo My_speech::human("David Bowman");
	// => My name is Frank Poole. I am a human
	echo My_speech::human("Frank Poole");
	// => My name is Heywood Floyd. I am a human
	echo My_speech::human("Heywood Floyd");
	// => My name is HAL 9000. I am an android
	echo My_speech::android("HAL 9000");
?>
