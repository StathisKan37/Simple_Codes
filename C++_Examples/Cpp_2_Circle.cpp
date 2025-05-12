#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	// Defining the variables we will need
	float x, perimeter, area;
	// Defining a float constant with the pi number
	const float PI = 3.14159265358979;

	// Asking for the Radius of a circle
	cout << "Type the radius of a circle" << endl;
	cin >> x;

	// Calculating the perimeter and the area
	perimeter = 2 * PI * x;
	area = PI * x * x;

	// Printing the results
	cout << "\nPerimeter : " << perimeter;
	cout << "\n     Area : " << area << "\n\n";
	
	return 0;
}
