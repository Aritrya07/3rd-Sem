#include<stdio.h>
void quick(int arr[], int low, int up);
int partition(int arr[], int low, int up);

int main()
{
    int a[100], i, n;
    printf("Enter number of elements : ");
    scanf("%d", &n);
    printf("Enter elements of array : ");
    for(i = 0; i < n; i++)
        scanf("%d", &a[i]);
    quick(a, 0, n-1);
    printf("Sorted array -\n");
    for(i = 0; i < n; i++)
        printf("%d\t", a[i]);
    printf("\n");
    return 0;
}

void quick(int arr[], int low, int up)
{
    int pivloc;
    if(low>=up)
        return;
    pivloc = partition(arr, low, up);
    quick(arr, low, pivloc-1);
    quick(arr, pivloc+1, up);
}

int partition(int arr[], int low, int up)
{
    int temp, i, j, pivot;
    i = low+1;
    j = up;
    pivot = arr[low];
    while(i <= j)
    {
        while((arr[i] < pivot) && (i < up))
            i++;
        while(arr[j] > pivot)
            j--;
        if(i < j)
        {
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
        else
            i++;
    }
    arr[low] = arr[j];
    arr[j] = pivot;
    return j;
}
