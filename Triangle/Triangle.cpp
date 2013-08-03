#include "Triangle.h"

// Loads our file into an array
void TriangleSolution::load()
{
	const int arrSize = 10;
	char* arr = new char[arrSize];
	unsigned int position = 0;
	for(int i = 1; i <= MAXLEVEL; i++)
	{
		for(int j = 1; j <= i; j++)
		{
			// Inside a row, the delim is the space
			file.getline(arr, arrSize, ' ');
			this->triangle[position] = Node(toInt(arr), i);
			position++;
		}
		// Next line
		file.getline(arr, arrSize);
	}

	file.close();
}

// Just toss out the highest number found into the file
// and save that
void TriangleSolution::save()
{
	outfile << this->currentMax;
	outfile.flush();
	outfile.close();
}

// A play on Dijkstra's algorithm, this probably could be solved
// about as easily with a binary tree, but the set up involved
// and the dealing with pointers will probably offset any benefits of
// the binary tree's speed
void TriangleSolution::solve()
{
	int size = this->triangle.size();
	this->triangle[0].distance = this->triangle[0].value;
	unsigned int leftId, rightId, temp;
	for(int i = 0; i < size; i++)
	{
		// If we're not on the max level
		if(this->triangle[i].level < MAXLEVEL)
		{
			// Check to see if the distance from the 0th node to this 
			//next left and right node is the largers when we go through this path
			leftId = this->triangle[i].getLeftId(i);
			temp = this->triangle[i].distance + this->triangle[leftId].value;

			if(temp > this->triangle[leftId].distance)
			{
				this->triangle[leftId].distance = temp;
			}

			rightId = this->triangle[i].getRightId(i);
			temp = this->triangle[i].distance + this->triangle[rightId].value;

			if(temp > this->triangle[rightId].distance)
			{
				this->triangle[rightId].distance = temp;
			}
		}
		// If we're at the bottom, check to see if it has
		// been the greatest sum
		else if(this->triangle[i].distance > this->currentMax)
		{
			this->currentMax = this->triangle[i].distance;
		}
	} 

	save();
}

// Entry point
void main()
{
	TriangleSolution().solve();
}