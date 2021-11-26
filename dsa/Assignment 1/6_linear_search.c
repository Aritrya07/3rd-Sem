/*
Write a C program to implement linear search (in both of successful and
unsuccessful modes) and also show the number of comparisons.
*/

#include<stdio.h>
int main()
{
	int i, n, a[100], cnt = 0, f = 0, val, pos;
	printf("Enter number of elements : ");
	scanf("%d", &n);
	printf("\nEnter numbers : ");
	for(i = 0; i < n; i++)
		scanf("%d", &a[i]);
	printf("Enter value to search : ");
	scanf("%d", &val);
	for(i = 0; i < n; i++)
	{
		cnt++;
		if(a[i] == val)
		{
			f = 1;
			pos = i + 1;
			break;
		}
	}
	if(f == 1)
	{
		printf("\nValue found in position %d", pos);
		printf("\nNumber of steps = %d", cnt);
	}
	else
		printf("\nValue not found...");
	return 0;
}
