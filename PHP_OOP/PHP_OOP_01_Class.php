<?php
	class Bank_account{
		
		// Defining two public properties
		public $my_account;
		public $my_balance;
		
		// Defining a method
		public function deposit($amount){
			$this->my_balance += $amount;
		}
	}
	// Creating an object from the 'Bank_account()' class
	$new_account = new Bank_account();
	
	// Setting the 2 properties
	$new_account->my_account = "GR-12345";
	$new_account->my_balance = 100;
	
	echo "The account ".$new_account->my_account." has ".$new_account->my_balance." euros<br>";
	
	// Using the method 'deposit()'
	$new_account->deposit(-25);
	
	echo "Now it has ".$new_account->my_balance." euros";
	
?>
