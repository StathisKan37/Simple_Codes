#include <stdio.h>
#include <stdlib.h>

// The struct with the names:
typedef struct node{
	char name[30];
	node *next;
}node;
// This is the first node of the stack
node *head;

void add_stack(const node *p);
void pop(void);
void show_stack();
void copy_char(char x[30], char y[30]);

int main () {
	
	node n;
	copy_char("Walter_White",n.name);
	add_stack(&n);
	copy_char("Jesse_Pinkman",n.name);
	add_stack(&n);
	copy_char("Mike_Ehrmantraut",n.name);
	add_stack(&n);
	copy_char("Gustavo_Fring",n.name);
	add_stack(&n);
	copy_char("Saul_Goodman",n.name);
	add_stack(&n);
	copy_char("Lalo_Salamanca",n.name);
	add_stack(&n);
	
	
	int x=1;
	do{
		printf("-------LIFO Stack-------\n");
		printf("  1. Add a new name\n");
		printf("  2. Delete a name\n");
		printf("  3. View all names\n");
		printf("\n  0. Exit\n");
		printf("----------------------\n> ");
		scanf("%d",&x);
		
		system("cls");
		
		switch(x){
			case 1:
				printf("Type the new name: ");
				scanf("%s",&n.name);
				add_stack(&n);
				
			break;
			
			case 2:
				pop();
				printf("\n\n");
			break;
			
			case 3:
				show_stack();
				printf("\n\n");
			break;
			
			case 0:
				printf("Thanks for using this stack!\nMade by Stathis_Kanetakis\n\n");
			break;
			
			default:
				printf("Wrong Choice!\n\n");
			break;
		}
		
	}while(x!=0);
}

void add_stack(const node *p){
	node *new_node;
	new_node=(node*)malloc(sizeof(node));
	*new_node=*p;
	new_node->next=head;
	head=new_node;
}

void pop(void){
	
	node *p;
	int i;
	p=head->next;
	printf("%s deleted succesfully",head->name);
	free(head);
	head=p;
}

void show_stack(){
	node *p;
	p=head;
	while(p!=NULL){
		printf("%s\n",p->name);
		p=p->next;
	}
}

void copy_char(char x[30], char y[30]){
	int i;
	for(i=0;i<30;i++){
		y[i]=x[i];
	}
}
