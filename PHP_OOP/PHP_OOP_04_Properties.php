<?php
	class Bank_account{
		
		// Defining a float property
		public float $my_balance;
		
		// Saving the parameter of the class in the
		// property $my_balance
		public function __construct(float $my_balance){
			$this->my_balance = $my_balance;
		}
	}
	
	// Creating an object with parameter
	$new_account = new Bank_account(125.25);
	// => Your balance is 125.5
	echo 'Your balance is '.$new_account->my_balance;
?>
