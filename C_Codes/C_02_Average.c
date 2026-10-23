#include <stdio.h>
#include <math.h>

int main(void){
	int a, i;
	float x, m[100], y=0, z;
	printf("Average measurements:\n");
	printf("How many measurements will you type?\n");
	
	// Asking for the number of measurments
	do{
		printf("They must be more than 0 and less than 100:\n");
		scanf("%d",&a);
	// Asking again if the input is invalid
	}while(a<=0 || a>100);
	
	// Asking for the measurements
	printf("Type your measurements: \n");
	for(i=0; i<a;i++){
		scanf("%f",&x);
		// Saving the measurements in the array 'm'
		m[i] = x;
		// Saving the sum of measurements in variable 'y'
		y = y + x;
	}
	
	// Calculating the average of the measurements
	y = y/a;
	
	// Calculating the standard deviation
	z=0;
	for(i=0; i<a;i++){
		x=m[i]-y;
		z=z+pow(x,2);
	}
	z=z/(a-1);
	z=sqrt(z);
	
	printf("The average is: %f + %f\n",y,z);
	
	return 0;
}
