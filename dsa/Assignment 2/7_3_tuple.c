#include<stdio.h>
#define srow 50
#define mrow 20
#define mcolumn 20

/*Begin of main*/
int main()
{
	int mat[mrow][mcolumn],sparse[srow][3];
	int i,j,nzero=0,mr,mc,sr,s;

	printf("Enter number of rows : ");
	scanf("%d",&mr);
	printf("Enter number of columns : ");
	scanf("%d",&mc);

	for(i=0;i<mr;i++)
	{
		for(j=0;j<mc;j++)
		{
			printf("Enter element : ",i+1,j+1);
			scanf("%d",&mat[i][j]);
		}
	}
	
	printf("Entered matrix is : \n");
	for(i=0;i<mr;i++)
	{
		for(j=0;j<mc;j++)
		{
			printf("%6d",mat[i][j]);
			if(mat[i][j]!=0)
				nzero++;
		}
	printf("\n");
	}

	sr=nzero+1;
	s=0;
	
	for(i=0;i<mr;i++)
		for(j=0;j<mc;j++)
		{
			if(mat[i][j]!=0)
			{
				sparse[s][0]=i+1;
				sparse[s][1]=j+1;
				sparse[s][2]=mat[i][j];
				s++;
			}
	}
	for(i=0;i<s;i++)
	{
		for(j=0;j<3;j++)
			printf("%d\t",sparse[i][j]);
		printf("\n");
	}
	return 0;
}
