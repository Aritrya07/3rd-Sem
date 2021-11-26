// Write a C program to perform push, pop, display operation for a stack(using array).

#include <stdio.h>
#include <stdlib.h>

void push(int *s, int item, int n, int *top)
{
	if(*top == n-1)
		printf("Stack overflown...\n");
	else
	{
		++(*top);
		*(s+*top) = item;
	}
}

void pop(int *s, int *top)
{
	if(*top == -1)
		printf("Stack underflow...\n");
	else
	{
		printf("Deleted item : %d\n", *(s+*top));
		--(*top);
	}
}

void display(int *s, int top)
{
  	int i;
  	if(top == -1)
  		printf("Stack is empty...\n");
  	else
  	{
  		printf("Stack: ");
  		for(i = 0; i <= top; i++)
    		printf("\t%d", *(s+i));
  	}
  	printf("\n");
}

int main()
{
	int c, val, n, top = -1;
  	printf("Enter size of stack : ");
  	scanf("%d", &n);
  	int s[n];
    
  	while(1)
  	{
		printf("1.PUSH\n2.POP\n3.DISPLAY\n4.EXIT\n");
  		printf("Enter your choice : ");
  		scanf("%d", &c);
  		switch(c)
  		{
   			case 1: printf("Enter value to push : ");
   					scanf("%d", &val);
   					push(s, val, n, &top);
   				break;
   			case 2: pop(s, &top);
   				break;
   			case 3: display(s, top);
   				break;
   			case 4: exit(0);
   			default: printf("Wrong Choice...\n");
  		}
  	}
  	return 0;
}
