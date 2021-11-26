// Write a C program to remove characters (from a string) located at odd positions.

#include<stdio.h>
#include<string.h>
int main()
{
	char s[100];
	int l, i, c = 0;
	printf("Enter string : ");
	scanf("%s", &s);
	l = strlen(s);
	for(i = 0; i < l; i++)
	{
		if(i%2==0)
		{
			s[c] = s[i+1];
			c++;
		}
	}
	s[c] = '\0';
	printf("%s", s);
	return 0;
}
