/*
Write a C program to delete an integer at nth position and also display the number
of shifting operations.
*/

#include <stdio.h>
int main()
{
    int i,size,pos,cnt=0;
    printf("Enter size of the array : ");
    scanf("%d",&size);
    int arr[size];
    printf("Enter elements in array : ");
    for(i=0;i<size;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("Enter the element position to delete : ");
    scanf("%d",&pos);
	if(pos<0 || pos>size)
     printf("Invalid position! Please enter position between 1 to %d",size);
    else
    {
    	printf("\nDeleted element : %d\n",arr[pos-1]);
        for(i=pos-1;i<size-1;i++)
        {
            arr[i] = arr[i + 1];
            cnt++;
        }
        size--;
        for(i=0;i<size;i++)
        {
            printf("%d\t",arr[i]);
        }
        printf("\nShift = %d",cnt);
    }
    return 0;
}
