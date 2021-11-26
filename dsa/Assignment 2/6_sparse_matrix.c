#include <stdio.h>
int main ()
{
    int a[100][100];
    int i, j, m, n;
    int c = 0;
 
    printf("Enter the order of the matix \n");
    scanf("%d %d", &m, &n);
    printf("Enter the elements of the matix \n");
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            scanf("%d", &a[i][j]);
            if (a[i][j] == 0)
            {
                ++c;
            }
        }
    }
    if (c > ((m * n) / 2))
    {
        printf("Sparse Matrix...\n");
    }
    else
        printf("Not a Sparse Matrix...\n");
	return 0;
}
