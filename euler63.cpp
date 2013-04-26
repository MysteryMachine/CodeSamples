#include <iostream>
#include <math.h>
using namespace std;

/*
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
*/

long int checkDigits (long int i){
	long int count = 0;
	for(count; i > 0; count++)
		i/=10;
	return count;
}

long int solve(){
	long int power = 1;
	long int count = 0;
	long int digitsInPower;
	int minCheck = 1;
	bool key = true;

	while(key)
	{
		for(int i = minCheck; i < 10 ; i++)
		{ 
			digitsInPower = power/(log((double)10)/log((double)i)) + 1;
			
			if(digitsInPower == power)
			{
				count++;
			}
			else if(digitsInPower > power)
				break;
		}

		power++;
		int check = 1 + power/(log(10.0)/log((double)minCheck));
		if(power > check)
			minCheck++;

		if (minCheck == 10)
		{
			key = false;
			break;
		}
	}

	return count;
}

void main (){
	cout << solve();
	while(cin);
}