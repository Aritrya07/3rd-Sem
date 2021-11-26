#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define MAX 50

void push(long int symbol);
long int pop();
int isEmpty();
long int eval_post();

char postfix[MAX];
long int stack[MAX];
int top;

int main()
{
	long int value;
	top = -1;
	printf("Enter postfix : ");
	scanf("%s", &postfix);
	value = eval_post();
	printf("Value of expression : %ld\n", value);
	return 0;
}

void push(long int symbol)
{
	if(top>MAX)
	{
		printf("Stack Overflow...\n");
		exit(1);
	}
	stack[++top] = symbol;
}

long int pop()
{
	if(isEmpty())
	{
		printf("Stack Underflow...\n");
		exit(1);
	}
	return (stack[top--]);
}

int isEmpty()
{
	if(top==-1)
		return 1;
	else
		return 0;
}

long int eval_post()
{
	long int a, b, temp, result;
	unsigned int i;
	for(i = 0; i<strlen(postfix); i++)
	{
		if(postfix[i]<='9' && postfix[i]>='0')
			push(postfix[i] - '0');
		else
		{
			a = pop();
			b = pop();
			switch(postfix[i])
			{
				case '+':
					temp = b + a;
					break;
				case '-':
					temp = b - a;
					break;
				case '*':
					temp = b * a;
					break;
				case '/':
					temp = b / a;
					break;
				case '^':
					temp = pow(b, a);
					break;
			}
			push(temp);
		}
	}
	result = pop();
	return result;
}
