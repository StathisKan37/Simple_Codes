#include <iostream>
#include <cstdlib>
using namespace std;
int main (void)
{
    // Defining a float and a string
	double a;
	string b;

	cout<<"Type the length and the units of measurement"<<endl;
	cout<<"Available units:";
	cout<<" Picometres: pm"<<endl;
	cout<<"Micrometres: um"<<endl;
	cout<<" Nanometres: nm"<<endl;
	cout<<" Milimetres: mm"<<endl;
	cout<<"Centimetres: cm"<<endl;
	cout<<" Decimetres: dm"<<endl;
	cout<<"     Metres: m"<<endl;
	cout<<" Decametres: Dm"<<endl;
	cout<<"Hectometres: Hm"<<endl;
	cout<<" Kilometres: Km"<<endl;
	cout<<" Megametres: Mm"<<endl;
	cout<<" Gigametres: Gm"<<endl;
	cout<<" Terametres: Tm"<<endl;

    do{
    // Asking for the langth and the units of measurement
	cin>>a>>b;

	// From picometres to metres
	if(b=="pm"){
        cout<<"Picometres to metres"<<endl;
		a=a/(1000*1000*1000*1000);}

	// From nanometres to metres
	if(b=="nm"){
        cout<<"Nanometres to metres"<<endl;
		a=a/(1000*1000*1000);}

	// From micrometres to metres
	if(b=="um"){
        cout<<"Micrometres to metres"<<endl;
		a=a/(1000*1000);}

	// From milimetres to metres
	if(b=="mm"){
        cout<<"Milimetres to metres"<<endl;
		a=a/1000;}

	// From centimetres to metres
	if(b=="cm"){
        cout<<"Centimetres to metres"<<endl;
		a=a/100;}

	// From decimetres to metres
	if(b=="dm"){
        cout<<"Decimetres to metres"<<endl;
		a=a/10;}

	// From metres to metres
	if(b=="m"){
        cout<<"Metres to metres"<<endl;
		a=a;}

	// From decametres to metres
	if(b=="Dm"){
        cout<<"Decametres to metres"<<endl;
		a=a*10;}

	// From hectometres to metres
	if(b=="Hm"){
        cout<<"Hectometres to metres"<<endl;
		a=a*1000*1000;}

	// From kilometres to metres
	if(b=="Km"){
        cout<<"Kilometres to metres"<<endl;
		a=a*1000;}

	// From megametres to metres
	if(b=="Mm"){
        cout<<"Megametres to metres"<<endl;
		a=a*1000*1000;}

	// From gigametres to metres
	if(b=="Gm"){
        cout<<"Gigametres to metres"<<endl;
		a=a*1000*1000*1000;}

	// From terametres to metres
	if(b=="Tm"){
        cout<<"Terametres to metres"<<endl;
		a=a*1000*1000*1000*1000;}

    // Printing the result
	cout<<"Lenght: "<<a<<" m\n\n";

	// When the user types '999' the loop ends
	}while (a!=999);

	return 0;
}
