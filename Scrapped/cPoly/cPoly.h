#pragma once
#include "SFML\Graphics.hpp"
// cPoly.h
// A class that contains a list of convex polygons, cPoly is short for
// collideable polygons, and these polygons are flexible in the sense that if
// properly defined, can be convex, and will detect with high accuracy,
// collisions with other polygons

#define MIN 0
#define MAX 1

// Drawing variables
const sf::Color CENTROID_COLOR = sf::Color(255, 0, 255);
const float CENTROID_SIZE = 5.0f;
const sf::Vector2f CENTROID_OFFSET = sf::Vector2f(CENTROID_SIZE, CENTROID_SIZE);
const float DEG_TO_RAD = 3.14f/180.f;

class cPoly
{
// Variables
private:
	sf::ConvexShape* shapes;
	sf::Vector2f* centroids;
	sf::Vector2f* origCentroids;

	int size;

public:
	bool drawCentroids;

// Functions
private:
	void setCentroids();

public:
	// Static functions
	// Most of these functions are kept public because they can be reused
	// relatively easily, as cPolys are being build to be really versitile

	//Centroid functions
	static float triArea(const sf::Vector2f& A, const sf::Vector2f& B, const sf::Vector2f& C);
	static sf::Vector2f triCentroid(const sf::Vector2f& A, const sf::Vector2f& B, const sf::Vector2f& C);
	static sf::Vector2f centroid(const sf::ConvexShape& shape);
	
	// Linear Algebra Functions
	static sf::Vector2f normal (const sf::Vector2f& v1, const sf::Vector2f& v2);
	static sf::Vector2f* cPoly::getNormals(const sf::ConvexShape& poly);
	static float proj (const sf::Vector2f& A, const sf::Vector2f& P);
	static float projUnit(const sf::Vector2f& A, const sf::Vector2f& U);
	static sf::Vector2f unitVector(const sf::Vector2f& V);
	static float magnitude(const sf::Vector2f& V);
	static float dot(const sf::Vector2f& A, const sf::Vector2f& B);
	static float* generateProjs(const sf::ConvexShape& poly, const sf::Vector2f& P, const sf::Vector2f& centroid);

	static sf::Vector2f calcPointLoc (const sf::ConvexShape& poly, int pointNum);

	// Collision functions
	static bool collideConvex(const sf::ConvexShape& poly1, const sf::ConvexShape& poly2,
							  const sf::Vector2f& centroid1, const sf::Vector2f& centroid2);
	static bool collide (const cPoly& cPoly1, const cPoly& cPoly2);

	// Constructors
	cPoly(bool dCentr = false);
	cPoly(sf::ConvexShape& input, int inputSize, bool dCentr = false);
	cPoly(const cPoly &copy);

	// Mutators
	void setOrigin (const sf::Vector2f& origin);
	void move (const sf::Vector2f& offset);
	void setPosition (const sf::Vector2f& position);
	void rotate (const float angle);
	void setFillColor(const sf::Color &color);
	void draw(sf::RenderWindow& window) const;
	void setTexture	(const sf::Texture * texture);
};