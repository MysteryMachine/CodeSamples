#include <iostream>

int recursiveSolve(int n, int m)
{
	if(n == 1)
		return 10 - m;
	else
	{
		int sum = 0;
		for(int i = m; m < 10; m++)
			sum += foo(n-1, i);
		return sum;
	}
}

int solve(int i)
{
	int solution = 2*recursiveSolve(i, 0);
}