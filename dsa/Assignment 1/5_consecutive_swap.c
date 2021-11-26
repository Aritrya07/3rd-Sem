/*
Write a C program to swap two consecutive elements.
*/

#include<stdio.h>
int swap(int *p, int n)
{
	int i, tmp;
	for(i = 0; i < n/2 ; i++)
	{
		tmp = *p;
		*p = *(p+1);
		*(p+1) = tmp;
		p+=2;
	}
	return p;
}
int main()
{
	int a[100], n, i, *p;
	printf("Enter number of elements : ");
	scanf("%d", &n);
	printf("Enter elements : ");
	for(i = 0; i < n; i++)
		scanf("%d", &a[i]);
	if(n % 2 == 0)
	 p = swap(a, n);
	else
	 p = swap(a, n-1);
	for(i = 0; i < n ; i++)
		printf("%d\t", a[i]);
	return 0;
}
