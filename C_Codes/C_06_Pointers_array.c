#include <stdio.h>
#include <stdlib.h>

// Defining a constant with name 'x'
#define x 20

int main(){	
	printf("Pointers:");
	// Defining an Array, a variable and a pointer
	int A[x],i;
	int *p;
	
	// Starting a loop
	for (i=0;i<x;i++){
		// Saving an integer in an Array's cell
		A[i]=i;
		// Saving in the pointer the address of that cell
		p=&A[i];
		// Printing them
		printf("\n%3d : %d",*(A+i),p);
	}
	
	return 0;
}
