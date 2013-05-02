#include <iostream>
#include <math.h>
using namespace std;
/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

unsigned long long solve(unsigned int max)
{
	int root = sqrt((double)max) + 1;
	int square = root*root;
	bool * primes = new bool[square]();
	unsigned long long answer = 0;
	primes[0] = false;
	primes[1] = false;
	for (int i = 2; i < square; i++)
		primes[i] = true;

	for (int i = 2; i < root; i++)
		if(primes[i])
			for(int j = 2*i; j < square; j+=i)
				primes[j] = false;

	for(int i = 0; i < max; i++)
	{
		if(primes[i])
			answer+=i;
	}
	return answer;
}

void main ()
{
	cout << solve(2000000);
	while(cin);
}