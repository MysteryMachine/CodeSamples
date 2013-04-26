#include <iostream>
#include <math.h>
using namespace std;
/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

int solve (int num)
{
	// Algorithm uses the sieve of eratosthenes and
	// the prime number theorem to maximize runtime
	// and space efficiency. 

	// Calculate space required with Prime Number Theorem, using
	// a little more space than the theorem requires to ensure prime
	// number is found
	int space = (int)(2*((double)num)*(log((double)num)));

	// Find root of the number and square it to avoid problems
	// due to rounding, work with this new square number, initialize
	// the boolean array with trues, assuming initially that all numbers
	// are prime
	int root = sqrt((double)space) + 1;
	int workNum = root*root;
	bool * arr = new bool[workNum + 1];
	for(int i = 2; i < workNum; i++)
		arr[i] = true;
	arr[0] = false;
	arr[1] = false;

	// Apply the sieve of eratosthenes
	int nextFalse;
	for(int i = 2; i <= root; i++)
	{
		if (!arr[i])
			continue;
		nextFalse = i*2;
		while (nextFalse < workNum)
		{
			arr[nextFalse] = false;
			nextFalse += i;
		}
	}
	
	// Go through the list, counting the primes
	// and stop when you hit the num-th prime
	int primeCount = 0;
	int count = 0;
	while(primeCount != num)
	{
		count++;
		if(arr[count])
			primeCount++;
	}

	return count;	
}

void main()
{
	cout << solve(10001);
	while(cin);
}