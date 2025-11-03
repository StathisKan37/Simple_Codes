<?php
	class User{
		// Defining a readonly property
		public readonly string $username;
		
		// Setting the name method
		public function set_name(string $username){
			$this->username = $username;}
	}
	
	// A new object with the property 'David Bowman'
	$user_1 = new User();
	$user_1->set_name('David Bowman');
	
	// => David Bowman
	echo $user_1->username;
	
	// The following command wouldn't change the name
	// $user_1->set_name('Frank Poole');
?>
