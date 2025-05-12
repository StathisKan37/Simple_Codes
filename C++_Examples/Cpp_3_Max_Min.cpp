#include <iostream>
#include <cstdlib>
using namespace std;

int main (void){
	// Defining an array and 3 variables
	int a[4], i, max, min;
	
	cout << "Type 5 integers" << endl;
	// Starting 5 loop
	for (i=0; i<=4; i++){
		// Scanning 5 integers
		cout<<i+1<<") ";
		cin>>a[i];}

	// Setting the first value of the array as maximum and minimum
	max=a[0];
	min=a[0];

	for (i=1; i<=4; i++){
		// Searching for the maximum integer
		if(max<a[i]){
			max=a[i];}

		// Searching for the minimum integer
		if(min>a[i]){
			min=a[i];}
	}
	
	// Printing the results
	cout<<"Maximum: "<<max<<"\n";
	cout<<"Minimum: "<<min<<"\n";
	return 0;}
