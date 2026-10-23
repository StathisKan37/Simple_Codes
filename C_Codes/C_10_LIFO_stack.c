#include <stdio.h>
#include <stdlib.h>

# define x 30

typedef struct node{
	int num;
	node *next;
}node;
node *head;

void add_stack(const node *p);
void show_stack();

int main () {
	int i;
	node n;
	
	for (i=0;i<x;i++){
		n.num=i;
		add_stack(&n);
	}
	
	show_stack();
}

void add_stack(const node *p){
	node *new_node;
	new_node=(node*)malloc(sizeof(node));
	*new_node=*p;
	new_node->next=head;
	head=new_node;
}

void show_stack(){
	node *p;
	p=head;
	while(p!=NULL){
		printf("%d\n",p->num);
		p=p->next;
	}
}
