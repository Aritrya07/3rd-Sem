#include<stdio.h>
#include<stdlib.h>

int binary_search(int *p, int n, int val, int *c)
{
    int low = 0, high = n - 1, mid;
    
    while(low <= high)
    {
        mid = (low + high) / 2;
        *c = *c + 1;
		if(*(p + mid) < val)
            low = mid + 1;
        else if(*(p+mid) > val)
            high = mid - 1;
        else
            return mid;
    }
    return -1;
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
    
    printf("Enter value to search : ");
    scanf("%d", &val);
    
    index = binary_search(p, n, val, &com);
    
    if(index == -1)
        printf("%d not found...\nNo. of comparisions = %d", val, com);
    else
        printf("%d found at position %d\nNo. of comparisions = %d", val, index + 1, com);
    
    return 0;
}
