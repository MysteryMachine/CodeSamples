#include <vector>
#include <iostream>
using namespace std;
/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

vector<int> getPrimes (int max)
{
	vector<int> primes;
	primes.push_back(2);
	for (int i = 3; i <=max; i++)
	{
		bool isPrime = true;
		for(int j = 0; j < primes.size();  j++)
		{
			if(i%primes[j] == 0)
			{
				isPrime = false;
			}
		}

		if(isPrime)
		{
			primes.push_back(i);
		}
	}

	return primes;
}

int * factor(vector<int> &primes, int num)
{
	int * primeCount = new int[primes.size()];
	for (int i = 0; i < primes.size(); i++)
	{
		primeCount[i] = 0;
	}

	for (int i = 0; i < primes.size(); i++)
	{
		while(num%primes[i] == 0)
		{
			num/=primes[i];
			primeCount[i]++;
		}
	}

	return primeCount;
}

unsigned int solveBad(int max)
{
	vector<int> primes = getPrimes(max);
	int * primeCount = new int[primes.size()];
	for (int i = 0; i < primes.size(); i++)
	{
		primeCount[i] = 0;
	}
	unsigned int result = 1;

	for (int i = 2; i <= max; i++)
	{
		int * primesToCheck = factor(primes, i);
		for(int j = 0; j < primes.size(); j++)
			if(primesToCheck[j] > primeCount[j])
				primeCount[j] = primesToCheck[j];
	}

	for(int i = 0; i < primes.size(); i++)
	{
		for(int j = 0; j < primeCount[i]; j++)
		{
			result *= primes[i];
		}
	}
	return result;
}

unsigned int solve(int max)
{
	vector<int> primes = getPrimes(max);
	unsigned int result = 1;

	for (int i = 0; i < primes.size(); i++)
	{
		int primeToPower = 1;
		while(true)
			if(primeToPower*primes[i] <= max)
				primeToPower *= primes[i];
			else
				break;

		result *= primeToPower;
	}

	return result;
}

void main ()
{
	cout << solve(20) << endl << solveBad(20);
	while(cin);
}