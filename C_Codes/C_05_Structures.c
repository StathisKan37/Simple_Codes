#include <stdio.h>
#include <stdlib.h>

// Defining the structure 'Movie'
struct Movie{
	char name[25];
	int year;
	float rate;
};

void copy_char(char x[25], char y[25]);

int main (void){
	
	// Creating new structures
	struct Movie iv;
	copy_char("A new hope",iv.name);
	iv.year=1977;
	iv.rate=8.6;
	
	struct Movie v;
	copy_char("The empire strikes back",v.name);
	v.year=1980;
	v.rate=8.7;
	
	struct Movie vi;
	copy_char("Return of the jedi",vi.name);
	vi.year=1983;
	vi.rate=8.3;
	
	struct Movie i;
	copy_char("The phantom menace",i.name);
	i.year=1999;
	i.rate=6.5;
	
	struct Movie ii;
	copy_char("Attack of the clones",ii.name);
	ii.year=2002;
	ii.rate=6.6;
	
	struct Movie iii;
	copy_char("Revenge of the Sith",iii.name);
	iii.year=2005;
	iii.rate=7.6;
	
	struct Movie vii;
	copy_char("The force awakens",vii.name);
	vii.year=2015;
	vii.rate=7.8;
	
	struct Movie viii;
	copy_char("The Last Jedi",viii.name);
	viii.year=2017;
	viii.rate=6.9;
	
	struct Movie xi;
	copy_char("Rise of the Skywalker",xi.name);
	xi.year=2019;
	xi.rate=6.5;
	
	// Printing the result
	printf("         -Movie Title-         Year   IMDb rate\n");
	printf("  -------------------------- -------- ---------\n");
	printf(" |%25s | %5d  |   %2.1f   |\n",iv.name,iv.year,iv.rate);
	printf(" |%25s | %5d  |   %2.1f   |\n",v.name,v.year,v.rate);
	printf(" |%25s | %5d  |   %2.1f   |\n",vi.name,vi.year,vi.rate);
	printf(" |%25s | %5d  |   %2.1f   |\n",i.name,i.year,i.rate);
	printf(" |%25s | %5d  |   %2.1f   |\n",ii.name,ii.year,ii.rate);
	printf(" |%25s | %5d  |   %2.1f   |\n",iii.name,iii.year,iii.rate);
	printf(" |%25s | %5d  |   %2.1f   |\n",vii.name,vii.year,vii.rate);
	printf(" |%25s | %5d  |   %2.1f   |\n",viii.name,viii.year,viii.rate);
	printf(" |%25s | %5d  |   %2.1f   |\n",xi.name,xi.year,xi.rate);
	printf("  -------------------------- -------- ---------\n");
	
	return 0;
}

// Copiyng the string x (source) into y (destination), character by character
void copy_char(char x[25], char y[25]){
	int i;
	for (i=0;i<30;i++){
		y[i]=x[i];
	}
}
