<?php
	class My_name{
		
		// Defining a private property
		private $name;
		
		// A method that saves the given name in the property '$name'
		public function set_name($given_name){
			$this->name = $given_name;
		}
		
		// A method that returns the name
		public function get_name(){
			return $this->name;
		}
	}
	
	// Creating some objects
	$name_1 = new My_name();
	$name_2 = new My_name();
	$name_3 = new My_name();
	
	// Setting the names
	$name_1->set_name('David Bowman');
	$name_2->set_name('Frank Poole');
	$name_3->set_name('Heywood Floyd');
	
	// Printing the names
	echo $name_1->get_name();
	echo '<br>';
	echo $name_2->get_name();
	echo '<br>';
	echo $name_3->get_name();
?>
