/*
Write a C program to insert an integer at nth position and also display the number of shifting operations.
*/

#include<stdio.h>
int main()
{
	int n,i,val,pos,cnt=0;
	printf("Enter number of elements : ");
	scanf("%d",&n);
	int a[n];
	printf("Enter values : ");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		printf("%d\t",a[i]);
	}
	printf("\nEnter value and position to insert : ");
	scanf("%d%d",&val,&pos);
	if(pos<1 || pos>n+1)
	 printf("\nOut of range...");
	else
	{
		n++;
		for(i=n-1;i>=pos-1;i--)
		{
			a[i]=a[i-1];
			cnt++;
		}
		a[pos-1]=val;
		printf("\n");
		for(i=0;i<n;i++)
		{
			printf("%d\t",a[i]);
		}
		printf("\nNumber of shift operation = %d",cnt-1);
	}
	return 0;
}
