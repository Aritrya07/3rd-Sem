#include<stdio.h>
#include<stdlib.h>

void selection_sort(int *p, int n)
{
	int i, j, min, tmp;
	for(i = 0; i < n-1; i++)
	{
		min = i;
		for(j = i+1; j < n; j++)
		{
			if(*(p+min) > *(p+j))
				min = j;
		}
		if(i != min)
		{
			tmp = *(p+i);
			*(p+i) = *(p+min);
			*(p+min) = tmp;
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

	selection_sort(p, n);
	printf("Sorted array : ");
	display(p, n);
    return 0;
}
