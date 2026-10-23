#include <stdio.h>

// Fibonacci recursive function
int fibonacci(int a){
	// Fibonacci of 0 is 0
	if (a==0){
		return 0;}
	// Fibonacci of 1 is 1
	else if (a==1){
		return 1;}
	// F(n) = F(n-1) + F(n-2)
	else{
		return (fibonacci(a-1)+fibonacci(a-2));
	}
}

int main (void){
	int a;
	// Asking for an integer
	printf("Type a number: ");
	scanf("%d",&a);
	
	// Printing the result
	printf ("Fibonacci of %d: %d\n", a, fibonacci(a));
	
	return 0;
}
