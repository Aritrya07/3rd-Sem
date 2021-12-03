/*
Linked list insert at beginning, insert at last, insert at a position, delete from end, delete from a postion, display and reverse display(using recursion)
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
void insert_pos();
void count();
void display();
void delete_at_end();
void print_reverse(struct node *);
void sum_of_elements();
void delete_pos();

int main()
{
    int ch;
    while(1)
    {
        printf("\n1.Insert at beginning\n2.Insert at end\n3.Insert at position\n4.Count\n5.Display\n6.Delete from end\n7.Delete at position\n8.Reverse\n9.Sum\n10.Exit\n");
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
				insert_pos();
				break;
			case 4:
				count();
				break;
			case 5:
				display();
				break;
			case 6:
				delete_at_end();
				break;
			case 7:
				delete_pos();
				break;
			case 8:
				if(start==NULL)
					printf("List is empty...\n\n");
				else
				{
					print_reverse(start);
					printf("\n\n");
				}
				break;
			case 9:
				sum_of_elements();
				break;
			case 10:
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

void print_reverse(struct node *tmp)
{
	if(tmp!=NULL)
	{
		print_reverse(tmp->link);
		printf("%d\t", tmp->data);
	}
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

void delete_pos()
{
	int pos, i;
	struct node *tmp;
	tmp = start;
	if(start==NULL)
	{
		printf("List underflow...\n\n");
		return;
	}
	printf("Enter postion : ");
	scanf("%d", &pos);
	if(pos==1)
	{
		printf("Deleted item = %d\n\n", tmp->data);
		start = tmp->link;
		free(tmp);
	}
	else
	{
		for(i=2;i<=pos;i++)
		{
			if(tmp==NULL)
			{
				printf("Invalid position...\n\n");
				return;
			}
			tmp = tmp->link;
		}
		p = start;
		while(p->link!=tmp)
			p = p->link;
		printf("Deleted item = %d\n\n", tmp->data);
		p->link = tmp->link;
		free(tmp);
	}
}

void insert_pos()
{
	int pos, i;
	struct node *tmp;
	tmp = start;
	p = (struct node *)malloc(sizeof(struct node));
	if(p==NULL)
	{
		printf("Not enough memory...\n\n");
		return;
	}
	printf("Enter position : ");
	scanf("%d", &pos);
	printf("Enter value to insert : ");
	scanf("%d", &p->data);
	p->link = NULL;
	if(pos==1)
	{
		p->link = start;
		start = p;
	}
	else
	{
		for(i=2;i<pos;i++)
		{
			if(tmp==NULL)
			{
				printf("Invalid position...\n\n");
				return;
			}
			tmp = tmp->link;
		}
		p->link = tmp->link;
		tmp->link = p;
	}
}
