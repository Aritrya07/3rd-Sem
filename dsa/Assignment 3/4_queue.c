// Write a C program to implement Linear Queue(using array).

#include<stdio.h>   
#include<stdlib.h>  
#define maxsize 5  
void insert();  
void delete();  
void display();  
int front = -1, rear = -1;  
int queue[maxsize];  
void main ()  
{  
    int choice;   
    while(choice != 4)   
    {       
        printf("\n1.EN-QUEUE\n2.DE-QUEUE\n3.DISPLAY\n4.EXIT\n");  
        printf("\nEnter your choice : ");  
        scanf("%d",&choice);  
        switch(choice)  
        {  
            case 1:  
            	insert();  
            	break;  
            case 2:  
            	delete();  
            	break;  
            case 3:  
            	display();  
            	break;  
            case 4:  
            	exit(0);  
            	break;  
            default:   
            	printf("\nEnter valid choice...\n");  
        }  
    }  
}  
void insert()  
{
	int item;
    printf("\nEnter the element : ");  
    scanf("\n%d",&item);
    if(rear == maxsize-1)  
    {  
        printf("\nOVERFLOW\n");  
        return;  
    }  
    if(front == -1 && rear == -1)  
    {  
        front = 0;  
        rear = 0;  
    }  
    else   
    {  
        rear = rear+1;  
    }  
    queue[rear] = item;  
}  
void delete()  
{  
    int item;   
    if (front == -1 || front > rear)  
    {  
        printf("\nUNDERFLOW\n");  
        return;  
              
    }  
    else  
    {  
        item = queue[front];  
        if(front == rear)  
        {  
            front = -1;  
            rear = -1 ;  
        }  
        else   
        {  
            front = front + 1;  
        }  
        printf("\nvalue deleted ");  
    }      
}
     
void display()  
{  
    int i;  
    if(rear == -1)  
    {  
        printf("\nEmpty queue\n");  
    }  
    else  
    {    
        for(i=front;i<=rear;i++)  
        {  
            printf("\n%d\t",queue[i]);  
        }
        printf("\n");
    }
}
