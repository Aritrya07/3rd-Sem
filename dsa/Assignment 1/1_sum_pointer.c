/*
Write a C program to take n elements from user and display the sum elements using pointer.
*/

#include<stdio.h>
int main()
{
	int a[100], n, i, *p, s = 0;
	printf("Enter number of elements : ");
	scanf("%d", &n);
	printf("Enter elements : ");
	for(i = 0; i < n; i++)
		scanf("%d", &a[i]);
	p = a;
	for(i = 0; i < n; i++)
	{
		s = s + (*p);
		p++;
	}
	printf("Sum = %d", s);
	return 0;
}
