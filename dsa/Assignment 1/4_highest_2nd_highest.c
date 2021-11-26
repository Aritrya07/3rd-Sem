/*
Write a C program to show highest and second highest element from a set of integers.
*/

#include<stdio.h>
int main()
{
	int a[100];
	int n,i,j,m,c,cnt=0;
	printf("Enter number of elements : ");
	scanf("%d",&n);
	printf("Enter values : ");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	for(i=0;i<n;i++)
	{
		for(j=0;j<n-i-1;j++)
		{
			if(a[j]>a[j+1])
			{
				c=a[j+1];
				a[j+1]=a[j];
				a[j]=c;
			}
		}
	}
	printf("\nHighest element = %d\t2nd highest element = %d",a[n-1],a[n-2]);
	return 0;
}
