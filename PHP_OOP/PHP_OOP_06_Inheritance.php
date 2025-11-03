<?php
	// This class is the parent
	class Bank_account{
		// Private property
		private $my_balance;
		
		// This method returns the balance of the account
		public function get_balance(){
			return $this->my_balance;}
		
		// This method adds/removes money from the balance
		public function deposit($amount){
			$this->my_balance += $amount;
			return $this;}
	}

	// This class is the child
	class Saving_account extends Bank_account{
		private $interest_rate;

		// This method saves the interest rate
		public function set_interest_rate($interest_rate){
			$this->interest_rate = $interest_rate;}
		
		// This method adds the interest to the balance
		public function add_interest(){
			// Calculating the interest
			$interest = $this->interest_rate * $this->get_balance();
			// Depositing the interest to the balance
			$this->deposit($interest);}
	}

	// Creating a new object
	$account_1 = new Saving_account();
	
	// Adding 100 to the account
	$account_1->deposit(100);
	
	// Setting the interest rate
	$account_1->set_interest_rate(0.5);
	$account_1->add_interest();
	
	// => 150
	echo $account_1->get_balance();
?>
