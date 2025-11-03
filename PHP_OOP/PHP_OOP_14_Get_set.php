<?php
	class User{
		// Saving all dynamic properties
		private $my_data = [];
		
		// This magic method saves a property that doesn't exist
		public function __set($my_name, $given_name){
			$this->my_data[$my_name] = $given_name;}
		
		// This magic method reads a property that doesn't exist
		public function __get($my_name){
			return $this->my_data[$my_name] ?? null;}
	}
	
	
	$user_1 = new User();
	// Setting dynamic properties using __set()
	$user_1->first_name = "David";
	$user_1->last_name = "Bowman";
	$user_1->age = 30;
	
	// Printing the dynamic properties using __get()
	// => First name: David
	echo "First name: ".$user_1->first_name."<br>";
	// => Last name: Bowman
	echo "Last name: ".$user_1->last_name."<br>";
	// => Age: 30
	echo "Age: ".$user_1->age."<br>";
?>
