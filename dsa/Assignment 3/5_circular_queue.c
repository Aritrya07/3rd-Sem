// Write a C program to implement Circular Queue(using array).

#include <stdio.h>
#include <stdlib.h>

void enqueue(int *s, int item, int n, int *top)
{
	if(*top == n-1)
		printf("Queue overflown...\n");
	else
	{
		++(*top);
		*(s+*top) = item;
	}
}

void dequeue(int *s, int *top, int start)
{
	int i;
	if(*top == -1)
		printf("Queue underflow...\n");
	else
	{
		printf("De-queue item : %d\n", *(s+start));
		for(i = 0; i < *top; i++)
		{
			*(s+i) = *(s+i+1);
		}
		--(*top);
	}
}

void display(int *s, int top)
{
  	int i;
  	if(top == -1)
  		printf("Queue is empty...\n");
  	else
  	{
  		printf("Queue: ");
  		for(i = 0; i <= top; i++)
    		printf("\t%d", *(s+i));
  	}
  	printf("\n");
}

int main()
{
	int ch, c, val, n, top = -1, start = 0;
  	printf("Enter size of queue : ");
  	scanf("%d", &n);
  	int q[n];
    
  	while(1)
  	{
		printf("1.EN-QUEUE\n2.DE-QUEUE\n3.DISPLAY\n4.EXIT\n");
  		printf("Enter your choice : ");
  		scanf("%d", &c);
  		switch(c)
  		{
   			case 1: printf("Enter value to enqueue : ");
   					scanf("%d", &val);
   					enqueue(q, val, n, &top);
   				break;
   			case 2: dequeue(q, &top, start);
   				break;
   			case 3: display(q, top);
   				break;
   			case 4: exit(0);
   			default: printf("Wrong Choice...\n");
  		}
  	}
  	return 0;
}
