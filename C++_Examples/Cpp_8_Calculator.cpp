#include <cstdlib>
#include <iostream>
// cmath: Includes a library for mathematical functions
#include <cmath>

// Defining the functions
double doub_add(double x1, double x2);
double doub_sub(double x1, double x2);
double doub_mul(double x1, double x2);
double doub_div(double x1, double x2);
double doub_root(double x);
double doub_pow(double x);

using namespace std;

int main(void){
	// Definining two double variables
	double a, b;

	// Asking two values from the user
	cout<<"A = ";cin>>a;
	cout<<"B = ";cin>>b;

	// Printing the results from each function
	cout<<"-----------------------\n";
    cout<<"      Addition: A + B = "<<doub_add(a,b)<<"\n";
    cout<<"  Substraction: A - B = "<<doub_sub(a,b)<<"\n";
    cout<<"Multiplication: A * B = "<<doub_mul(a,b)<<"\n";
    cout<<"      Division: A / B = "<<doub_div(a,b)<<"\n";
	cout<<"-----------------------\n";
    cout<<"Square root of A: "<<doub_root(a)<<"\n";
    cout<<"Square root of B: "<<doub_root(b)<<"\n";
    cout<<"-----------------------\n";
    cout<<"A in the power of 2: "<<doub_pow(a)<<"\n";
    cout<<"B in the power of 2: "<<doub_pow(b)<<"\n";
    return 0;
	}

    // Adding the double variables
	double doub_add (double x1, double x2){
		return x1+x2;}

    // Substracting the double variables
	double doub_sub (double x1, double x2){
		return x1-x2;}

    // Multiplying the double variables
	double doub_mul (double x1, double x2){
		return x1*x2;}

    // Dividing the double variables
	double doub_div (double x1, double x2){
		return x1/x2;}

    // Square root of a double variable
	double doub_root (double x){
		return sqrt(x);}
	
	// Power of 2 of a double variable
	double doub_pow(double x){
		return x*x;}
