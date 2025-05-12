#include<iostream>
#include<cstdlib>
using namespace std;

int main (void){

    // Defining some integers
	int x, d500, d200, d100, d50, d20, d10, d5, d2, d1;

	cout<<"How much money do you have?"<<endl;
	cin>>x;


	// Calculating the number of 5 hundreds
	d500=x/500;
	x=x-d500*500;

	// Calculating the number of 2 hundreds
	d200=x/200;
	x=x-d200*200;

	//  Calculating the number of one hundreds
	d100=x/100;
	x=x-d100*100;

	// Calculating the number of fifties
	d50=x/50;
	x=x-d50*50;

	// Calculating the number of twenties
	d20=x/20;
	x=x-d20*20;

	// Calculating the number of tens
	d10=x/10;
	x=x-d10*10;

	// Calculating the number of fives
	d5=x/5;
	x=x-d5*5;

	// Calculating the number of twos
	d2=x/2;
	x=x-d2*2;

	// Calculating the number of ones
	d1=x/1;
	x=x-d1*1;

	// Prinitng the changes
	if (d500!=0) {cout<<d500<<" x 500 euros"<<endl;}
	if (d200!=0) {cout<<d200<<" x 200 euros"<<endl;}
	if (d100!=0) {cout<<d100<<" x 100 euros"<<endl;}
	if (d50!=0) {cout<<d50<<" x 50 euros"<<endl;}
	if (d20!=0) {cout<<d20<<" x 20 euros"<<endl;}
	if (d10!=0) {cout<<d10<<" x 10 euros"<<endl;}
	if (d5!=0) {cout<<d5<<" x 5 euros"<<endl;}
	if (d2!=0) {cout<<d2<<" x 2 euros"<<endl;}
	if (d1!=0) {cout<<d1<<" x 1 euros"<<endl;}

	return 0;
}
