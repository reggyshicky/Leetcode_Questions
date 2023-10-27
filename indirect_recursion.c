//Write a program to print numbers from 1 to 10 in such a way 
//that when the number is odd, add 1 and when the number is
//even, subtract 1. Expected output 2,1,4,3,6,5,8,7,10,9
# include <stdio.h>
# include <stdlib.h>

void odd();
void even();
int n = 1;

void odd()
{
	if (n <= 10)
	{
		printf("%d ", n+1);
		n++;
		even();
	}
	return;
}

void even()
{
	if (n <= 10)
	{
		printf("%d ", n-1);
		n++;
		odd();
	}
	return;
}

int main()
{
	odd();
	printf("\n");
	return (0);
	/*we calling odd() because the 1st number we encounter 
	 *is 1 and is an odd number, therefore we first have to
	 *to call the odd function in order to handle that no. 
	*/ 
}
