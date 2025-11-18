<?php
	class User{
		private $my_name;
		private $my_age;
		
		public function __construct($my_name, $my_age) {
			$this->my_name = $my_name;
			$this->my_age = $my_age;}
		
		public function __toString(){
			return "User: {$this->my_name}, Age: {$this->my_age}";}
	}
	
	$user_1 = new User("David Bowman", 30);
	// This command calls the magic method __toString()
	// And the result of the function is printed
	// => User: David Bowman, Age: 30
	echo $user_1;
?>
