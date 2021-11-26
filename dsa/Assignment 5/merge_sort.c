#include<stdio.h>
#define MAX 100
void merge_sort(int arr[], int low, int up);
void merge(int arr[], int temp[], int low1, int up1, int low2, int up2);
void copy(int arr[], int temp[], int low, int up);

int main()
{
    int a[MAX], i, n;
    printf("Enter number of elements : ");
    scanf("%d", &n);
    printf("Enter elements of array : ");
    for(i = 0; i < n; i++)
        scanf("%d", &a[i]);
    merge_sort(a, 0, n-1);
    printf("Sorted array -\n");
    for(i = 0; i < n; i++)
        printf("%d\t", a[i]);
    printf("\n");
    return 0;
}

void merge_sort(int arr[], int low, int up)
{
    int mid, temp[MAX];
    if(low < up)
    {
        mid = (low + up) / 2;
        merge_sort(arr, low, mid);
        merge_sort(arr, mid+1, up);
        merge(arr, temp, low, mid, mid+1, up);
        copy(arr, temp, low, up);
    }
}

void merge(int arr[], int temp[], int low1, int up1, int low2, int up2)
{
    int i, j, k;
    i = low1;
    j = low2;
    k = low1;
    while((i<=up1) && (j<=up2))
    {
        if(arr[i]<arr[j])
            temp[k++] = arr[i++];
        else
            temp[k++] = arr[j++];
    }
    while(i<=up1)
        temp[k++] = arr[i++];
    while(j<=up2)
        temp[k++] = arr[j++];
}

void copy(int arr[], int temp[], int low, int up)
{
    int i;
    for(i = low; i <= up; i++)
        arr[i] = temp[i];
}