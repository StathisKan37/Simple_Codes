#include <stdio.h>
#include <stdlib.h>

int main (){
	
	// Aasking the number of numbers to print
	int *p,N;
	printf("How many numbers would you like to print? ");
	scanf("%d",&N);
	// Allocatibg dynamically the size of the array
	p=(int*)malloc(N*sizeof(int));

	int i;
	for (i=0;i<N;i++){
		p[i]=i+1;
	}
	
	// Printing each number
	for (i=0;i<N;i++){
		printf("\n%d",p[i]);
	}
	
	return 0;
}
