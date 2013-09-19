#include "SFML\Graphics.hpp"
#include "cPoly.h"
#include <math.h>
#include <iostream>

// Iterates through all convex shapes in the list and calls the function that
// calculates the centroid for that function, then updates that centroid
void cPoly::setCentroids()
{
	for (int i = 0; i < size; i++)
	{
		centroids[i] = centroid(shapes[i]);
	}
}

// The formulas below are relatively simple, with proofs for them up on the internet
float cPoly::triArea(const sf::Vector2f &A, const sf::Vector2f &B, const sf::Vector2f &C)
{
	return (float)std::abs(0.5*(A.x*(B.y - C.y) + B.x*(C.y - A.y) + C.x*(A.y - B.y)));
}

sf::Vector2f cPoly::triCentroid(const sf::Vector2f &A, const sf::Vector2f &B, const sf::Vector2f &C)
{
	return sf::Vector2f((A.x + B.x + C.x)/3.0f, (A.y + B.y + C.y)/3.0f);
}

// Not a very difficult algorithm, it will take the first point in the shape, and 
// iterate through all other successive two points that make all the triangles that
// compose the shape, it will sum the centroid*area of each triangle, and 
// seperately sum the area of the triangles, it will return
// sum(centroid*area)/sum(area)
// While iterating through all triangles, point B should always be the point 
// immediately clockwise or counterclockwise to point A, depending on which
// direction the shape was defined
sf::Vector2f cPoly::centroid(const sf::ConvexShape &shape)
{
	// Declare variables
	sf::Vector2f* A;
	sf::Vector2f* B; 
	sf::Vector2f* C;

	sf::Vector2f areaXCentroidSum;
	float areaSum;
	float area;

	// Define initial conditions
	A = &shape.getPoint(0);

	areaSum = 0;

	// Loop through all possible point Bs
	for (int i = 1; i < (shape.getPointCount()-1); i++)
	{
		B = &shape.getPoint(i);
		C = &shape.getPoint(i+1);

		area = triArea(*A, *B, *C);

		areaSum += area;
		areaXCentroidSum += area*triCentroid(*A, *B, *C);
	}

	return areaXCentroidSum/areaSum;
}

// Returns a vector going through the origin
// Takes a line defined by two seperate vectors
sf::Vector2f cPoly::normal (const sf::Vector2f &v1, const sf::Vector2f &v2)
{
	float x = v2.x - v1.x;
	float y = v2.y - v1.y;

	return sf::Vector2f(-y, x);
}

sf::Vector2f* cPoly::getNormals(const sf::ConvexShape &poly)
{
	int count = poly.getPointCount();
	sf::Vector2f* vectors = new sf::Vector2f[count];
	sf::Vector2f point1;
	sf::Vector2f point2;
	for (int i = 0; i < count; i++)
	{
		int j = i + 1;
		if (j == count)
			j = 0;
		point1 = calcPointLoc(poly, i);
		point2 = calcPointLoc(poly, j);

		vectors[i] = normal(point1, point2);
	}

	return vectors;
}

// Returns a projection of A on P
float cPoly::proj (const sf::Vector2f &A, const sf::Vector2f &P)
{
	return dot(A, P)/magnitude(P);
}

float cPoly::projUnit(const sf::Vector2f& A, const sf::Vector2f& U)
{
	return dot(A, U);
}

// The next three functions are simple vector operations
// This finds the unit vector in the same direction as V
sf::Vector2f cPoly::unitVector(const sf::Vector2f &V)
{
	float mag = magnitude(V);
	if(mag == 0)
		return sf::Vector2f(0, 0);
	return sf::Vector2f(V.x/mag, V.y/mag);
}

// Finds the magnitude of V
float cPoly::magnitude(const sf::Vector2f &V)
{
	return (float)std::sqrt(dot(V, V));
}

// Finds the dot product of A and B
float cPoly::dot(const sf::Vector2f &A, const sf::Vector2f &B)
{
	return A.x*B.x + A.y*B.y;
}

// Generate an array with the values of the projections of vector created
// by extending a line from the centroid to a point in the polygon and
// a vector P (in this case, P will be a vector normal to a face of one of
// the tested polygons), C is the centroid of the polygon
// Return a size two array, with the max value found in position 1, the min
// at position 0
float* cPoly::generateProjs(const sf::ConvexShape& poly, const sf::Vector2f &P, const sf::Vector2f& centroid)
{
	sf::Vector2f U = unitVector(P);
	int count = poly.getPointCount();
	//return the highest and lowest value in a size 2 array
	float* projs = new float[2];
	projs[0] = 1000000; //arbitrary large number, projections won't get this big in our system
	projs[1] = 0;
	float check;
	for(int i = 1; i < count; i++)
	{
		sf::Vector2f vec = calcPointLoc(poly, i);
		check = std::abs(projUnit(vec - centroid, U));
		if (check < projs[MIN])
			projs[MIN] = check;
		if (check > projs[MAX])
			projs[MAX] = check;
	}

	return projs;
}

// Gets the absolute position of a point on the screen
// TO-DO: I'm reduntantly using the formula for rotating a point around a point
// here, I should move the functionality into its own function and call that in
// these two, as of now, it doesn't directly translate, because my centroids
// don't store their original position in the same way as sf::shapes do
// On a side note, I wish these things were kept within sf::shape so I didn't need
// to apply a long algorithm to get it out 
sf::Vector2f cPoly::calcPointLoc (const sf::ConvexShape& poly, int pointIndex)
{
	sf::Vector2f point = poly.getPoint(pointIndex);
	sf::Vector2f origin = poly.getOrigin();
	sf::Vector2f position = poly.getPosition();

	float totalAngle = poly.getRotation();

	float s = std::sin(totalAngle*DEG_TO_RAD);
	float c = std::cos(totalAngle*DEG_TO_RAD);

	point.x = point.x - origin.x;
	point.y = point.y - origin.y;

	sf::Vector2f change = sf::Vector2f(point.x * c - point.y *s, point.x * s + point.y *c);
	point.x = change.x + position.x;
	point.y = change.y + position.y;

	sf::Vector2f test = point;

	return test;
}

// Utilizes the Seperating Axis Theorem, the basic way this works is we check to see
// if a line can be drawn between two shapes by checking the distance of the shapes
bool cPoly::collideConvex(const sf::ConvexShape& poly1, const sf::ConvexShape& poly2,
						  const sf::Vector2f& centroid1, const sf::Vector2f& centroid2)
{
	// We first general normals for each face of the polygon
	sf::Vector2f* p1Normals = getNormals(poly1);
	sf::Vector2f* p2Normals = getNormals(poly2);

	// The lists of projections
	float* P1;
	float* P2;

	// We assume collision occurs, and stop when evidence otherwise is shown
	// This algorithm is at its slowest when everything is colliding, if one
	// axis does not register collision, collision has not occurred
	bool hasCollided = false;
	bool hasNotCollidedOnce = true;
	// check all the normals of the first polygon, if collision occurs,
	// program is essentially done

	for (int i1 = 0; i1 < poly1.getPointCount() && hasNotCollidedOnce; i1++)
	{
		P1 = generateProjs(poly1, p1Normals[i1], centroid1);
		P2 = generateProjs(poly2, p1Normals[i1], centroid2);

		if(P1[MAX] < P2[MIN] || P2[MAX] < P1[MIN])
			hasNotCollidedOnce = false;
	}

	//
	for (int i2 = 0; i2 < poly2.getPointCount() && hasNotCollidedOnce; i2++)
	{
		P1 = generateProjs(poly1, p2Normals[i2], centroid1);
		P2 = generateProjs(poly2, p2Normals[i2], centroid2);

		if(P1[MAX] < P2[MIN] || P2[MAX] < P1[MIN])
			hasNotCollidedOnce = false;
	}

	if(hasNotCollidedOnce)
		hasCollided = true;

	return hasCollided;
}

// Calls collideConvex on all polygons that might collide
bool cPoly::collide(const cPoly& cPoly1, const cPoly& cPoly2)
{
	bool hasCollided = false;
	// Test every convexpoly in cpoly1 against every convexpoly in cpoly2
	// if collision is detected, stop checking and just return true
	// otherwise, if collision is not detected, return false
	for(int i = 0; i < cPoly1.size && !hasCollided; i++)
	{
		for(int j = 0; j < cPoly2.size && !hasCollided; j++)
		{
			hasCollided = collideConvex(cPoly1.shapes[i], cPoly2.shapes[j], cPoly1.centroids[i], cPoly2.centroids[j]);
		}
	}

	return hasCollided;
}

// Default constructor, creates small triangle, used to bypass crashing or checking
// for triangle size all the time
cPoly::cPoly(bool dCentr)
{
	size = 1;

	shapes = new sf::ConvexShape[size];
	centroids = new sf::Vector2f[size];

	shapes[0].setPointCount(3);
	shapes[0].setPoint(0, sf::Vector2f(12.5, 0));
	shapes[0].setPoint(1, sf::Vector2f(25, 25));
	shapes[0].setPoint(2, sf::Vector2f(0, 25));

	drawCentroids = dCentr;
	setCentroids();
	origCentroids = new sf::Vector2f[size];
	for(int i = 0; i < size; i++)
		origCentroids[i] = sf::Vector2f(centroids[i]);
}

// cPoly constructor, takes the address of an array of shapes, and the size of
// that array, with the assumption that both inputs are valid, ie, that all
// the input shapes work and that the size matches. Also, considering this class
// is designed to be used in making contiguous concave shapes, it is also
// assumed that the user adequately linked the shapes, correct shapes should
// also contain at least one shape, the only way I check for this is with the
// size variable
cPoly::cPoly(sf::ConvexShape& input, int inputSize, bool dCentr)
{
	if (inputSize > 0)
	{
		shapes = &input;
		size = inputSize;
	}

	// Default behavior if invalid size is given, but this is the only check done
	else
	{
		size = 1;

		shapes = new sf::ConvexShape[size];
	
		shapes[0].setPointCount(3);
		shapes[0].setPoint(0, sf::Vector2f(12.5, 0));
		shapes[0].setPoint(1, sf::Vector2f(25, 25));
		shapes[0].setPoint(2, sf::Vector2f(0, 25));	
	}

	drawCentroids = dCentr;
	centroids = new sf::Vector2f[size];
	setCentroids();
	origCentroids = new sf::Vector2f[size];
	for(int i = 0; i < size; i++)
		origCentroids[i] = sf::Vector2f(centroids[i]);
}

// cPoly copy constructor
cPoly::cPoly(const cPoly &copy)
{
	size = copy.size;

	shapes = new sf::ConvexShape[size];
	for(int i = 0; i < size; i++)	
		shapes[i] = sf::ConvexShape(copy.shapes[i]);
	
	drawCentroids = copy.drawCentroids;
	centroids = new sf::Vector2f[size];
	for(int i = 0; i < size; i++)
		centroids[i] = sf::Vector2f(centroids[i]);;
	origCentroids = new sf::Vector2f[size];
	for(int i = 0; i < size; i++)
		origCentroids[i] = sf::Vector2f(centroids[i]);;
}

// The next few functions are simple, they copy the functionality in ConvexShape,
// but with an array of shapes, iterrating through each
// and applying the proper function, and then updating the centroid of the shape
void cPoly::setOrigin (const sf::Vector2f& origin)
{
	for(int i = 0; i < size; i++)
	{
		sf::Vector2f originalOrigin = shapes[i].getOrigin();
		shapes[i].setOrigin(origin);
		centroids[i] -= shapes[i].getOrigin() - originalOrigin;
	}
}

void cPoly::move (const sf::Vector2f& offset)
{
	for(int i = 0; i < size; i++)
	{
		shapes[i].move(offset);
		centroids[i] += offset;
	}
}

void cPoly::setPosition (const sf::Vector2f& position)
{
	for(int i = 0; i < size; i++)
	{
		sf::Vector2f originalPosition = shapes[i].getPosition();
		centroids[i] += shapes[i].getPosition() - originalPosition;
		shapes[i].setPosition(position);
	}
}

// Rotation is more complex, first we use the approriate formula to create
// rotation then we calculate the rotation of a point around a point, using
// know linear algebra algorithms
void cPoly::rotate (const float angle)
{
	// first rotate the shapes correctly to calc s and c
	for(int i = 0; i < size; i++)
	{
		shapes[i].rotate(angle);

		float totalAngle = shapes[i].getRotation();

		float s = std::sin(totalAngle*DEG_TO_RAD);
		float c = std::cos(totalAngle*DEG_TO_RAD);

		sf::Vector2f origin = shapes[i].getOrigin();
		sf::Vector2f position = shapes[i].getPosition();
		centroids[i].x = origCentroids[i].x - origin.x;
		centroids[i].y = origCentroids[i].y - origin.y;

		sf::Vector2f change = sf::Vector2f(centroids[i].x * c - centroids[i].y *s, centroids[i].x * s + centroids[i].y *c);
		centroids[i].x = change.x + position.x;
		centroids[i].y = change.y + position.y;
	}
}

void cPoly::setFillColor(const sf::Color &color)
{
	for(int i = 0; i<size; i++)
		shapes[i].setFillColor(color);
}

// Iterates through each shape and tells the screen to draw it
void cPoly::draw(sf::RenderWindow& window) const
{
	if (size > 0)
	{
		for(int i = 0; i < size; i++)
		{
			window.draw(shapes[i]);
			if (drawCentroids)
			{
				sf::CircleShape center = sf::CircleShape(CENTROID_SIZE);
				center.setFillColor(CENTROID_COLOR);
				// Offsetting is required because cicles are not drawn at center
				center.move(centroids[i] - CENTROID_OFFSET);
				window.draw(center);
			}
		}	
	}
}

void cPoly::setTexture (const sf::Texture * texture)
{
	for(int i = 0; i < size; i++)
	{
		shapes[i].setTexture(texture, true);
	}
}