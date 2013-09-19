#include "MainGameEntities.h"
#include <fstream>
#include <string>
#include <iostream>
#include <assert.h>

// Load textures and the map from a specified path, build the polies required
MapEntity::MapEntity(const char* path, cPolyEntity** ents, int* totalEnts, float winX, float winY)
{
	loadTextures();

	// Load map from file
	winCenter = sf::Vector2f(winX/2, winY/2);
	totalEntities = totalEnts;

	tileSize = 50;

	entities = ents;
	terrainArgs** read;
	//Used to to convert a 2 digit char into an int
	char* sizeInChar = new char[2]; 
	int size;
	std::fstream file(path);
	if(file.is_open())
	{
		if(file.good())
		{
			file.getline(sizeInChar, 3);
		}

		// Convert to the size of the array into an integer
		size = 10*((int)sizeInChar[0] - (int)'0');
		size += (int)sizeInChar[1] - (int)'0';

		// Set up the square terrainArgs array that will hold the loaded info
		read = new terrainArgs*[size];
		for (int i = 0; i < size; i++)
			read[i] = new terrainArgs[size];

		char* charToRead = new char;

		// FILE SPECIFICATIONS:
		// The file will contain several items separated by whatever is defined
		// by DELIM_OBJ in levelModule.h, and the fields within the object
		// are seperated by DELIM_ITEM. Order is height, slopex, slopey, type
		while(file.good())
		{
			for(int i = 0; i < size; i++)
			{
				for(int j = 0; j < size; j++)
				{
					polyType ptype = FULL;

					file.read(charToRead, 1);

					if(charToRead == "Q")
						ptype = UR;

					else if(charToRead == "E")
						ptype = UL;

					else if(charToRead == "Z")
						ptype = DR;

					else if(charToRead == "C")
						ptype = DL;
					
					file.read(charToRead, 1);
					file.read(charToRead, 1);

					read[i][j] = terrainArgs(ptype, *charToRead, textures, i, j, tileSize);

					// Go to next obj
					file.read(charToRead, 1);

#ifdef LVLMOD_PRINTOUTS
					std::cout << read[i][j].height << " ";
#endif
				}

#ifdef LVLMOD_PRINTOUTS
					std::cout << std::endl;
#endif
			}
		}
		file.close();

		map = read;
		mapSize = size;
	}
}

// Player movement is kept on the map because the map is what will keep track of all
// collisions, and movement moves the position of everything on the map, anything that
// isn't the player will need to request the map's permission to move before actually
// moving around
void MapEntity::tick(bool hasControls, sf::RenderWindow& window)
{
	sf::Event events;
	while(hasControls && window.pollEvent(events))
	{
		if(events.MouseButtonPressed)
		{
			handle_click(events, window);
		}
	}
	
	checkMapCollisions(window);

	moveEntities();
	
}

// Take the set in location to where the center of the map (the player) should move
// to, then apply the same movement to everything, thus moving the camera
void MapEntity::moveEntities()
{
	// Moves all non-playercollision polies
	for(unsigned int i = 0; i < *totalEntities; i++)
	{
		if(i != ADDRESSPLAYERENTITY && movement.x != 0 && movement.y != 0)
		{
			entities[i]->collisionPoly.move(movement);
			entities[i]->position -= movement;
		}	
	}

	// Moves map tiles
	for(int i = 0; i < mapSize; i++)
	{
		for(int j = 0; j < mapSize; j++)
		{
			map[i][j].poly.move(movement);
		}
	}

	
	// Updates player position
	entities[ADDRESSPLAYERENTITY]->position-=movement;

	// Checks to see if w'ere done moving
	// If not, reduce the destination (movement is always opposite of teh destination, so we add)
	if(destination.x*destination.x + destination.y*destination.y > entities[ADDRESSPLAYERENTITY]->speed*entities[ADDRESSPLAYERENTITY]->speed) 
	{
		destination = destination + movement;
	}
	// Otherwise, if there's a > 0 but < speed amount of moving to be done, we just move that
	else if(destination.x + destination.y != 0)
	{
		movement = -destination;
		destination = sf::Vector2f(0, 0);
	}
	// If we're at the destiniation (dest = 0), just stop moving
	else
	{
		movement = sf::Vector2f(0, 0);
	}
}

// Check the collisions of all entities with all map polies
void MapEntity::checkMapCollisions(sf::RenderWindow& window)
{
	for(int k = ADDRESSPLAYERENTITY; k < *this->totalEntities; k++)
	{
		// Create a copy poly and move it to where it'll be next turn
		cPoly checkPoly;
		checkPoly = cPoly(entities[k]->collisionPoly);
		checkPoly.setFillColor(sf::Color(255, 255, 255));
		checkPoly.draw(window);
		// If it's not the player, move using speed
		if(k != ADDRESSPLAYERENTITY)
			checkPoly.move(sf::Vector2f(entities[k]->direction.x * entities[k]->speed,
				entities[k]->direction.y * entities[k]->speed));
		// If it is, use the map's movement variable (since it is the player's speed)
		else if(k == ADDRESSPLAYERENTITY)
			checkPoly.move(sf::Vector2f(-movement.x, -movement.y));

		for(int i = 0; i < mapSize; i++)
		{
				for(int j = 0; j < mapSize; j++)
			{
				// To save speed, only check tiles that are 2*tilesize away (so 2 tiles)
				if(((entities[k]->position.x + 2*this->tileSize) > this->tileSize*i &&
					(entities[k]->position.x - 2*this->tileSize) < this->tileSize*i) 
						&&
					((entities[k]->position.y + 2*this->tileSize) > this->tileSize*j &&
					(entities[k]->position.y - 2*this->tileSize) < this->tileSize*j))
				{
					// If we collide
					if(cPoly().collide(checkPoly, map[i][j].poly) )
					{
						// Standard collision stops any future movement
						if(map[i][j].cType == STANDARD)
						{
							// Uses camera movement if the player collides
							if(k == ADDRESSPLAYERENTITY)
							{
								movement = sf::Vector2f(0,0);
								destination = sf::Vector2f(0,0);
							}
							// Uses speed of the entity if it is an entity
							else
							{
								entities[k]->direction = sf::Vector2f(0,0);
							}
						}
					}
				}
			}
		}
	}
}

// Simple function that loads texture files, addresses found in main
// game addresses file
void MapEntity::loadTextures()
{
	textures = new sf::Texture*[TOTALTILES];
	for(int i = 0; i < TOTALTILES; i++)
	{
		textures[i] = new sf::Texture();
	}
	textures[GRASS]->loadFromFile(GRASSFILE);
	textures[ROCK]->loadFromFile(ROCKFILE);
}

// Loops to all entities and draws it
void MapEntity::draw(sf::RenderWindow& win)
{
	for(int i = 0; i < mapSize; i++)
	{
		for(int j = 0; j < mapSize; j++)
		{
			map[i][j].poly.draw(win);
		}
	}
}

// Handles clicks on the map
void MapEntity::handle_click(sf::Event events, sf::RenderWindow& window)
{
	// If it's a right click
	if(sf::Mouse::isButtonPressed(sf::Mouse::Right))
	{
		// set destination (defined as the position of the screen where the origin is defined as the center of the screen) 
		sf::Vector2f mousePos = sf::Vector2f((float)sf::Mouse::getPosition(window).x, (float)sf::Mouse::getPosition(window).y);
		destination = sf::Vector2f((float)mousePos.x - winCenter.x, (float)mousePos.y - winCenter.y);
		// determine direction via taking a unit vector, determine the movement using player speed
		direction = cPoly().unitVector(destination);
		movement = sf::Vector2f(-direction.x*(entities[ADDRESSPLAYERENTITY]->speed), -direction.y*entities[ADDRESSPLAYERENTITY]->speed);
	
	}
}

PlayerEntity::PlayerEntity(MapEntity& refMap, float winX, float winY)
{
	cPolyEntity::cPolyEntity();
	speed = 5;

	// Create Player poly
	sf::ConvexShape* shape = new sf::ConvexShape[1];
	/*shape[0].setPointCount(6);
	shape->setPoint(0, sf::Vector2f(12.5, 0));
	shape->setPoint(1, sf::Vector2f(37.5, 0));
	shape->setPoint(2, sf::Vector2f(50, 21.6));
	shape->setPoint(3, sf::Vector2f(37.5, 42.2));
	shape->setPoint(4, sf::Vector2f(12.5, 42.2));
	shape->setPoint(5, sf::Vector2f(0, 21.6));*/
	shape[0].setPointCount(4);
	shape->setPoint(0, sf::Vector2f(0, 0));
	shape->setPoint(1, sf::Vector2f(0, 25));
	shape->setPoint(2, sf::Vector2f(25, 25));
	shape->setPoint(3, sf::Vector2f(25, 0));
	collisionPoly = cPoly(*shape, 1);
	// Center the player on the screen
	collisionPoly.setOrigin(collisionPoly.centroid(*shape));
	center = sf::Vector2f(winX/2, winY/2);
	collisionPoly.setPosition(center);
	position = sf::Vector2f(winX/2, winY/2);

	collisionPoly.setFillColor(sf::Color(255, 0, 255));
	
	cType = STANDARD;
}

void PlayerEntity::tick(bool hasControls, sf::RenderWindow& window)
{
	// currently not needed
}

// Draws the player
void PlayerEntity::draw(sf::RenderWindow& win)
{
	collisionPoly.draw(win);
}