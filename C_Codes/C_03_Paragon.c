#include <stdio.h>

// Paragon recursive function
int paragon(int x){
	if(x==1){
		return 1;}
	else {
		x=x*paragon(x-1);}
}

int main (void){
	int x;
	// Asking for an integer
	printf("Type an integer: ");
	scanf("%d", &x);
	
	// Printing the result
	printf("Paragon of %d: %d\n", x, paragon(x));
	
	return 0;
}
