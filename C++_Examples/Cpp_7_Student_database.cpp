#include <cstdlib>
#include <iostream>
using namespace std;

// Student database
int main (){
	// Defining the variables
	float g1=0, g2=0, g3=0;
	int a, b;
	string on11=" ";
	string on12=" ";
	string on21=" ";
	string on22=" ";
	string on31=" ";
	string on32=" ";

    // Showing the options
	cout<<"1. Name insert" << endl;
	cout<<"2. Change name" << endl;
	cout<<"3. Show database" << endl;
	cout<<"0. Exit" << endl;
	cout<<"________________" << endl;

	// Start a loop
	do{
        // Asking for an option
        cout << "Your option: ";
        cin >> a;

        // Name insert
        if (a==1){
            // Student 1
            cout << "\nStudent 1";
			cout << "\nFirst name: ";
			cin>>on11;
			cout<<"\nLast name: ";
			cin>>on12;
			cout<<"\nGrade: ";
			cin>>g1;
            // Student 2
            cout << "\nStudent 2";
			cout << "\nFirst name: ";
			cin>>on21;
			cout<<"\nLast name: ";
			cin>>on22;
			cout<<"\nGrade: ";
			cin>>g2;
            // Student 3
            cout << "\nStudent 3";
			cout << "\nFirst name: ";
			cin>>on31;
			cout<<"\nLast name: ";
			cin>>on32;
			cout<<"\nGrade: ";
			cin>>g3;
        }

		// Change name
        if (a==2){
            cout << "Which student are you changing? (1,2,3)" << endl;
            cin >> b;
            cout << "Type the first name, the last name and the grade" << endl;

            // For student 1
            if (b==1){
                cin >> on11;
				cin >> on12;
				cin >> g1;
            }

            //For student 2
            if (b==2){
                cin >> on21;
				cin >> on22;
				cin >> g2;
            }

            // For student 3
            if (b==3){
                cin >> on31;
				cin >> on32;
				cin >> g3;
            }
        }

        // Show database
        if (a==3){
            // Student 1
            cout<<"- Student 1 -" << endl;
			cout<<"First name: " << on11 << endl;
			cout<<"Last name : " << on12 << endl;
			cout<<"Grade     : " << g1 << endl;
            // Student 2
            cout<<"- Student 2 -" << endl;
			cout<<"First name: " << on21 << endl;
			cout<<"Last name : " << on22 << endl;
			cout<<"Grade     : " << g2 << endl;
            // Student 3
            cout<<"- Student 3 -" << endl;
			cout<<"First name: " << on31 << endl;
			cout<<"Last name : " << on32 << endl;
			cout<<"Grade     : " << g3 << endl;
        }
    // End of loop
    }while (a!=0);

	return 0;
}
