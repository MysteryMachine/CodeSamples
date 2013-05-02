#include <math.h>
#include <iostream>
#include <string>
using namespace std;
/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

string toString(int num)
{
	string result = string();
	char index = '0';
	while(num)
	{
		result.push_back(((char)(num%10)+index));
		num/=10;
	}

	return result;
}

string reverseString(string str)
{
	string newStr = string();
	for (int i = str.size()-1; i >= 0; i--)
	{
		newStr.append(str.substr(i, 1));
	}

	return newStr;
}

bool checkPalindrome(int i)
{
	if(toString(i) == reverseString(toString(i)))
	{
		return true;
	}

	return false;
}

int solve(double digits)
{
	int ans = 0, min = pow(10, digits - 1), max = pow(10, digits);
	for(int i = min; i < max; i++)
		for(int j = min; j < max; j++)
			if(checkPalindrome(i*j) && i*j > ans)
				ans = i*j;
	return ans;
}

void main()
{ 
	cout <<  solve(3);
	while(cin);
}