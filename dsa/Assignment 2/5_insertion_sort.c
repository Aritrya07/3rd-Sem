#include<stdio.h>
#include<stdlib.h>

void insertion_sort(int *p, int n)
{
	int i, j, k;
	for(i = 1; i < n; i++)
	{
		k = *(p+i);
		for(j = i-1; j >= 0 && k < *(p+j); j--)
			*(p+j+1) = *(p+j);
		*(p+j+1) = k;
		printf("Ater pass %d\n", i+1);
		display(p, n);
	}
}

void display(int *p, int n)
{
	int i;
	for(i = 0; i < n; i++)
		printf("%d\t", *(p+i));
	printf("\n\n");
}

int main()
{
    int *p, n, i, val, index, com = 0;

    printf("Enter number of elements : ");
    scanf("%d", &n);

    p = (int *)malloc(n * sizeof(int));
    if(p == NULL)
    {
        printf("Memory not available...");
        exit(0);
    }
    
    printf("Enter elements : ");
    for(i = 0; i < n; i++)
        scanf("%d", p+i);

	insertion_sort(p, n);
	printf("Sorted array : ");
	display(p, n);
    return 0;
}
