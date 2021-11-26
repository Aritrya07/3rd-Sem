/*
Linked list insert, delete, display and reverse display
*/

#include<stdio.h>
#include<stdlib.h>

struct node
{
	int data;
	struct node *link;
} *start = NULL, *p;

void insert_at_beginning();
void insert_at_last();
void count();
void display();
void delete_at_end();
void print_reverse();
void sum_of_elements();

int main()
{
    int ch;
    while(1)
    {
        printf("\n1.Insert at beginning\n2.Insert at end\n3.Count\n4.Display\n5.Delete from end\n6.Reverse\n7.Sum\n8.Exit\n");
        printf("--------------------\n\n");
        printf("Enter your choice : ");
        scanf("%d", &ch);
        switch(ch)
		{
			case 1:
				insert_at_beginning();
				break;
			case 2:
				insert_at_last();
				break;
			case 3:
				count();
				break;
			case 4:
				display();
				break;
			case 5:
				delete_at_end();
				break;
			case 6:
				print_reverse();
				break;
			case 7:
				sum_of_elements();
				break;
			case 8:
				exit(1);
			default:
				printf("Wrong choice...\n\n");
		}
    }
    return 0;
}

void insert_at_beginning()
{
	p = (struct node *)malloc(sizeof(struct node));
	if(p==NULL)
	{
		printf("Not enough memory...");
		return;
	}
	printf("Enter data to input : ");
	scanf("%d", &p->data);
	p->link = NULL;
	if(start==NULL)
		start = p;
	else
	{
		p->link = start;
		start = p;
	}
}

void insert_at_last()
{
	struct node *tmp;
	p = (struct node *)malloc(sizeof(struct node));
	if(p==NULL)
	{
		printf("Not enough memory...\n");
		return;
	}
	printf("Enter data to input : ");
	scanf("%d", &p->data);
	p->link = NULL;
	if(start==NULL)
		start = p;
	else
	{
		tmp = start;
		while(tmp->link!=NULL)
			tmp = tmp->link;
		tmp->link = p;
	}
}

void count()
{
	int cnt = 1;
	p = start;
	while(p->link!=NULL)
	{
		p = p->link;
		cnt++;
	}
	printf("Number of nodes  = %d\n", cnt);
}

void display()
{
	if(start==NULL)
	{
		printf("List is empty...\n\n");
	}
	else
	{
		p = start;
		while(p!=NULL)
		{
			printf("%d\t", p->data);
			p = p->link;
		}
		printf("\n\n");
	}
}

void delete_at_end()
{
	struct node *tmp;
	if(start == NULL)
		printf("Underflow...\n\n");
	else if(start->link==NULL)
	{
		tmp = start;
		start = NULL;
		printf("Deleted item = %d\n\n", tmp->data);
		free(tmp);
	}
	else
	{
		p = start;
		while(p->link!=NULL)
		{
			tmp = p;
			p = p->link;
		}
		tmp->link=NULL;
		printf("Deleted item = %d\n\n", p->data);
		free(p);
	}
}

void print_reverse()
{
	struct node *tmp;
	if(start==NULL)
	{
		printf("List is empty...\n\n");
		return;
	}
	p = start;
	while(p->link!=NULL)
		p = p->link;
	while(p != start)
	{
		tmp = start;
		while(tmp->link!=p)
			tmp = tmp->link;
		printf("%d\t", p->data);
		p = tmp;
	}
	printf("%d\n\n", p->data);
}

void sum_of_elements()
{
	int sum = 0;
	if(start==NULL)
		printf("Empty list...\n\n");
	else
	{
		p = start;
		while(p!=NULL)
		{
			sum = sum + p->data;
			p = p->link;
		}
		printf("Sum = %d\n\n", sum);
	}
}
