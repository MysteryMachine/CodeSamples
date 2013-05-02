#include <iostream>
using namespace std;

int solve(int n)
{
	int solutions = 0;
	int eval;
	for  (int a = n+1; a < 2*n; a++)
	{
		for(int i = 1; ; i++)
		{
			eval = i+1/i*a;
			if(eval == n)
			{
				solutions++;
				break;
			}

			else if(eval > n)
			{
				break;
			}
		}
	}

	return solutions;
}

void main()
{
	cout << solve(2);
	while(cin);
}