<?php
	class User{
		public function __call($function_name, $arguments){
			echo "Running ".$function_name." function...<br>";
			echo "My name is ".$arguments[0]." and my age is ".$arguments[1]."<br>";}
		
		public static function __callStatic($function_name, $arguments){
			echo "My name is ".$arguments[0]."<br>";}
		
	}
	
	$user_1 = new User();
	// When the method doesn't exists, the magic method __call() is called
	// => Running my_speech function...
	// => My name is David Bowman and my age is 30
	$user_1->my_speech("David Bowman", 30);
	
	// When the static method doesn't exists,
	// the magic method __callStatic() is called
	// => My name is HAL 9000
	User::my_speech("HAL 9000");
?>
