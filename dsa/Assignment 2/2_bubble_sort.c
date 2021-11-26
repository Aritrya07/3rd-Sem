#include<stdio.h>
#include<stdlib.h>

void bubble_sort(int *p, int n)
{
	int i, j, tmp;
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < n-i-1; j++)
		{
			if(*(p+j) > *(p+j+1))
			{
				tmp = *(p+j);
				*(p+j) = *(p+j+1);
				*(p+j+1) = tmp;
			}
		}
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

	bubble_sort(p, n);
	printf("Sorted array : ");
	display(p, n);
    return 0;
}
