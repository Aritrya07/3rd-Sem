/*
Linked list insert and display
*/
#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *link;
};
struct node *start = NULL, *p;
void insert_at_beginning();
void insert_at_last();
void count();
void display();
int main()
{
    int ch;
    while(1)
    {
        printf("\n1.Insert at beginning\n2.Insert at last\n3.Count\n4.Display\n5.Exit\n");
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
        printf("Unable to allocate space...\n\n");
    else
    {
        printf("Enter value : ");
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
}

void insert_at_last()
{
    struct node *tmp;
    p = (struct node *)malloc(sizeof(struct node));
    if(p==NULL)
        printf("Unable to allocate memory...\n\n");
    else
    {
        printf("Enter value to insert : ");
        scanf("%d", &p->data);
        p->link = NULL;
        tmp = start;
        if(start==NULL)
            start = p;
        else
        {
            while(tmp->link != NULL)
                tmp = tmp->link;
            tmp->link = p;
        }
    }
}

void count()
{
    int cnt = 0;
    p = start;
    if(start==NULL)
        printf("List is empty...\n\n");
    else
    {
        while(p!=NULL)
        {
            p = p->link;
            cnt++;
        }
    }
    printf("Number of nodes = %d", cnt);
}

void display()
{
    p = start;
    if(start==NULL)
        printf("List is empty...\n\n");
    else
    {
        while(p!=NULL)
        {
            printf("%d\t", p->data);
            p = p->link;
        }
        printf("\n\n");
    }
}
