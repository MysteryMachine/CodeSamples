#ifndef SALOMAOBECKERTRIANGLESOLUTION
#define SALOMAOBECKERTRIANGLESOLUTION

#include <fstream>
#include <vector>
#include <math.h>
using namespace std;

const unsigned int MAXLEVEL = 100;

// Contains all the information regarding each node
// It would be easy to repurpose this class into a
// binary tree to solve the problem in a slightly
// different way
class Node
{
public:
// Public vars
	unsigned int value;
	unsigned int distance;
	unsigned int level;
// Public functions
	// Constructors
	Node(): value(0), distance(0), level(0){};
	Node(unsigned int v, unsigned int l): value(v), distance(0), level(l){};
	
	// Public functions
	int getLeftId(unsigned int thisId) { return thisId + level; };
	int getRightId(unsigned int thisId) { return thisId + level + 1; };
};

class TriangleSolution
{
private:
// Private vars
	// Loading
	fstream file;
	ofstream outfile;
	
	// My solutions flattens the triangle into a line and
	// uses the properties of triangular numbers to figure
	// out where the next adjacent location is, I considered
	// using a binary tree to solve this problem, but loading
	// into the tree felt cumbersome, and would probably be
	// slower than quickly loading into an array and using
	// some quick math to find out where we're going next
	vector<Node> triangle;
	unsigned int currentMax;
	
// Private functions
	void load();
	void save();

	// Converts a character array of characters
	// to an integer
	static unsigned int toInt(char* arr)
	{
		string str = string(arr);
		unsigned int retval = 0;
		unsigned int power = 1;
		for(int i = str.length() - 1; i >= 0; i--)
		{
			retval += power*((unsigned int)(str[i] - '0'));
			power *= 10;
		}
		
		return retval;
	};

public:
// Public functions
	// Constructors
	TriangleSolution(): triangle(),
		file("triangle.txt"), outfile("output.txt", ofstream::trunc), currentMax(0)
	{ 
		int sum = 0;
		for(int i = 1; i <= 100; i++)
		{
			sum += i;
		}
		this->triangle.resize(sum);
		this->load(); 
	};

	// Functions
	void solve();
};
#endif