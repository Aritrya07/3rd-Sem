// Write a C program to find out common elements from two arrays given by user.

#include<stdio.h>
void input(int *p, int *n, int x)
{
	int i;
	printf("Enter number of elements of array%d : ", x);
	scanf("%d", n);
	printf("Enter elements of array%d : ", x);
	for(i = 0; i < *n ; i++)
		scanf("%d", p+i);
}
void common(int *a, int *b, int n, int m)
{
	int i, j, f = 0;
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < m; j++)
		{
			if(*(a+i)==*(b+j))
			{
				printf("%d\t", *(a+i));
				f = 1;
			}
		}
	}
	if(f==0)
		printf("No common elements...");
}
int main()
{
	int a[100], b[100], i, n, m;
	input(a, &n, 1);
	input(b, &m, 2);
	common(a, b, n, m);
	return 0;
}
