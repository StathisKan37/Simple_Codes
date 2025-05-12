#include <cstdlib>
#include <iostream>
using namespace std;

int main(){
    // Defining 2 integers
	int a, i=0;

    // Starting a loop
	do {
        // Asking for the password
        cout<<"Password: ";
		cin>>a;
		cout<<"\n";
		i=i+1;

    // The loop ends after 3 tries or when the password is right
    }while (a!=999 && i<=2);

    // If the password is wrong you are locked!
    if (a!=999){
		cout<<"Locked!!!"<<"\n";}
    // If the password is right you are welcome!
	else{
		cout<<"Welcome ..."<<"\n";}

	return 0;}
