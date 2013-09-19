// Application that demonstrates the basecPoly.cpp file's functionality
// Allows the creation of convex shapes via left clicking, pressing enter to 
// finish, the rotating of shapes by r and t keys and the click dragging of 
// shapes, with shapes turning red if they're colliding, being green if they're 
// not
#include "SFML\Graphics.hpp"
#include <iostream>
#include "cPoly.h"

int main()
{
	// Code here is currently just a playground for testing functionality
	
    sf::RenderWindow window(sf::VideoMode(800, 600), "basecPolyDemo");
	window.setFramerateLimit(30);

	// Define cPoly
	cPoly poly1;
	cPoly poly2;
	cPoly poly;

	sf::ConvexShape* shapes1 = new sf::ConvexShape[2];
	sf::ConvexShape* shapes2 = new sf::ConvexShape[2];
	sf::ConvexShape* shape = new sf::ConvexShape[1];
	shape[0].setPointCount(6);
	shape->setPoint(0, sf::Vector2f(12.5, 0));
	shape->setPoint(1, sf::Vector2f(37.5, 0));
	shape->setPoint(2, sf::Vector2f(50, 21.6));
	shape->setPoint(3, sf::Vector2f(37.5, 42.2));
	shape->setPoint(4, sf::Vector2f(12.5, 42.2));
	shape->setPoint(5, sf::Vector2f(0, 21.6));

	shapes1[0].setPointCount(4);
	shapes1[0].setPoint(0, sf::Vector2f(0, 0));
	shapes1[0].setPoint(1, sf::Vector2f(100, 0));
	shapes1[0].setPoint(2, sf::Vector2f(100, 100));
	shapes1[0].setPoint(3, sf::Vector2f(0, 100));
		  
	shapes1[1].setPointCount(3);
	shapes1[1].setPoint(0, sf::Vector2f(100, 25));
	shapes1[1].setPoint(1, sf::Vector2f(150, 50));
	shapes1[1].setPoint(2, sf::Vector2f(100, 75));
		  
	shapes2[0].setPointCount(4);
	shapes2[0].setPoint(0, sf::Vector2f(0, 0));
	shapes2[0].setPoint(1, sf::Vector2f(100, 0));
	shapes2[0].setPoint(2, sf::Vector2f(100, 100));
	shapes2[0].setPoint(3, sf::Vector2f(0, 100));
		  
	shapes2[1].setPointCount(3);
	shapes2[1].setPoint(0, sf::Vector2f(100, 25));
	shapes2[1].setPoint(1, sf::Vector2f(150, 50));
	shapes2[1].setPoint(2, sf::Vector2f(100, 75));

	poly1 = cPoly(*shapes1, 1);
	poly1.setOrigin(poly.centroid(*shapes1));

	poly2 = cPoly(*shapes2, 2);
	poly2.setOrigin(sf::Vector2f(-100.f, -100.f));
	
	poly = cPoly(*shape, 1);
	poly.setOrigin(poly.centroid(*shape));

	poly1.move(sf::Vector2f(400, 300));
	poly2.move(sf::Vector2f(400, 300));
	poly.move(sf::Vector2f(340, 320));

	bool unpause = true;
	int count = 0;
	// Main loop, runs while the window is unclosed
    while (window.isOpen())
    {
		// Event handling
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
			if (event.type == sf::Event::MouseButtonPressed)
			{
				unpause = !unpause;
			}
        }

		if(unpause)
		{
			//poly1.rotate(1.f);
			//poly.rotate(1.5f);
			//if((count/38)%2 == 0)
				//poly.move(sf::Vector2f(4, 4));
			//else
				//poly.move(sf::Vector2f(-4, -4));
			//count++;
		}

		if (cPoly::collide(poly1, poly))
		{
			poly1.setFillColor(sf::Color(255, 0, 0));
			poly.setFillColor(sf::Color(255, 0, 0));
		}

		else
		{
			poly1.setFillColor(sf::Color(0, 255, 0));
			poly.setFillColor(sf::Color(0, 255, 0));
		}
			
		// Drawing
        window.clear();
		poly1.draw(window);
		poly.draw(window);
        window.display();
    }

    return 0;
}