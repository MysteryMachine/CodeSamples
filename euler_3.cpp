#include <math.h>
#include <vector>
#include <iostream>
using namespace std;
/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

int solve(unsigned long long num)
{
	unsigned long long myNum = num;
	bool isPrime;
	vector<unsigned long long> primes;
	unsigned long long iterator = 4;
	primes.push_back(2);
	primes.push_back(3);

	while(iterator <= myNum)
	{
		isPrime = true;
		for(int i = 0; i < primes.size(); i++)
		{
			if(iterator%primes[i] == 0)
			{
				isPrime = false;
				break;
			}
		}

		if(isPrime)
		{
			primes.push_back(iterator);
			while(myNum%iterator == 0)
			{
				cout << iterator << ' ' << myNum << endl;
				if(iterator == myNum)
					return iterator;
				myNum/=iterator;
			}
		}

		iterator++;
	}

	return 0;
}

void main()
{
	unsigned long long i;
	cout << solve(600851475143);
	while(cin>>i);
}