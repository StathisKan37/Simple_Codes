#include <stdio.h>
#include <stdlib.h>

int main(){
	
	// Saving and prinitng a string
	char text[]="The republic will be reorganised into the first... galactric... empire!";
	printf("%s \n",text);
	
	// Saving the string in a pointer and printing it
	char *str= text;
	int i;
	for (i=0;i<sizeof(text);i++){
		printf("%c",str[i]);
	}
	
	printf("\n");
	
	for (i=0;i<sizeof(text);i++){
		printf("%c",*(text+i));
	}
	
	return 0;
}
