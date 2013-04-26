#include <iostream>
/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

int getSum(int num, int top)
{
	do
	{
		top--;
	} while(top%num);

	return (num+top)*top/(2*num);
}

int slowSum(int num, int top)
{
	int i = 0, sum = 0;
	while(true)
	{
		i+=num;
		if (i >= top)
			break;
		sum+=i;
	}

	return sum;
}

void main ()
{
	int terminate;
	std::cout << getSum(3, 1000) + getSum(5, 1000) - getSum(15, 1000);
	while(std::cin >> terminate){}
}