<?php
	class Bank_account{
		private $my_balance;

		// Saving the parameter of the class in the private property '$my_balance'
		public function __construct($my_balance){
		$this->my_balance = $my_balance;}
		
		// Returning the balance
		public function get_balance(){
			return $this->my_balance;}
		
		// Depositing the balance
		public function deposit($amount){
			$this->my_balance += $amount;
			return $this;}
	}

	class SavingAccount extends Bank_account{
		private $interest_rate;
		
		public function __construct($my_balance, $interest_rate){
			// Calling the constructor of the parent
			parent::__construct($my_balance);
			// Saving the interest rate
			$this->interest_rate = $interest_rate;}
		
		// Calculating and depositing the interest
		public function add_interest(){
			$interest = $this->interest_rate * $this->get_balance();
			$this->deposit($interest);}
	}

	// Creating a new object with:
	// $my_balance = 100
	// $interest_rate = 0.5
	$account_1 = new SavingAccount(100, 0.5);
	// Adding the interest
	$account_1->add_interest();
	// => 150
	echo $account_1->get_balance();
?>
