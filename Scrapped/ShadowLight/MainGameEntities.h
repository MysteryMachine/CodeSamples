#pragma once
#include "../Demos/cPoly/cPoly.h"
#include "../Engine/engine.h"
#include "MainGameAddresses.h"
#include "MapFilePaths.h"
#include <vector>

#define DELIM_ITEM ';'
#define DELIM_OBJ ' '

#define TOLERANCE_MOVEMENT 1.0f
//Foward declarations

class string;

typedef enum collisionType
{
	NOCOLLISION, STANDARD, SLOW, DAMAGE, FALL
};

typedef enum polyType
{
	FULL, UL, UR, DL, DR 
};

class terrainArgs
{
public:
	cPoly poly;
	char tType;
	collisionType cType;
	terrainArgs(){};
	terrainArgs(polyType ptype, char ttype, sf::Texture** textures, 
				int i, int j, int tileSize)
	{
		tType = ttype;
		sf::ConvexShape* shape = new sf::ConvexShape[1];
		if(ptype == FULL)
		{
			shape[0].setPointCount(4);
			shape[0].setPoint(0, sf::Vector2f((float)0, (float)0));
			shape[0].setPoint(1, sf::Vector2f((float)tileSize, (float)0));
			shape[0].setPoint(2, sf::Vector2f((float)tileSize, (float)tileSize));
			shape[0].setPoint(3, sf::Vector2f((float)0, (float)tileSize));
		}
		else if(ptype == UR)
		{
			shape[0].setPointCount(3);
			shape[0].setPoint(0, sf::Vector2f((float)0, (float)0));
			shape[0].setPoint(1, sf::Vector2f((float)tileSize, (float)0));
			shape[0].setPoint(2, sf::Vector2f((float)tileSize, (float)tileSize));
		}
		else if(ptype == UL)
		{
			shape[0].setPointCount(3);
			shape[0].setPoint(0, sf::Vector2f((float)0, (float)0));
			shape[0].setPoint(1, sf::Vector2f((float)tileSize, (float)0));
			shape[0].setPoint(2, sf::Vector2f((float)0, (float)tileSize));
		}
		else if(ptype == DR)
		{
			shape[0].setPointCount(3);
			shape[0].setPoint(0, sf::Vector2f((float)0, (float)tileSize));
			shape[0].setPoint(1, sf::Vector2f((float)tileSize,(float) 0));
			shape[0].setPoint(2, sf::Vector2f((float)tileSize, (float)tileSize));
		}
		else if(ptype == DL)
		{
			shape[0].setPointCount(3);
			shape[0].setPoint(0, sf::Vector2f((float)0, (float)0));
			shape[0].setPoint(1, sf::Vector2f((float)0, (float)tileSize));
			shape[0].setPoint(2, sf::Vector2f((float)tileSize, (float)tileSize));
		}

		poly = cPoly(*shape, 1);
		poly.move(sf::Vector2f((float)i*tileSize, (float)j*tileSize));
		if(tType == 'G')
		{
			cType = NOCOLLISION;
			poly.setTexture(textures[GRASS]);
		}
		else if(tType == 'R')
		{
			cType = STANDARD;
			poly.setTexture(textures[ROCK]);
		}
	};
};

// Any entity that needs to be used on a map must inheret this instead of the
// entity, so that the cPoly of the entity exists for collisions.
// TO DO: Add sprites
class cPolyEntity : public Entity
{
public:
	cPoly collisionPoly;
	collisionType cType;
	int speed;
	sf::Vector2f direction;
	virtual void draw(sf::RenderWindow& win){};
	virtual void tick(bool hasControls, sf::RenderWindow& window){};
	sf::Vector2f position;
	cPolyEntity():position(sf::Vector2f(-10000, -10000)){};
};

// Entity responsible for handling collision and actually moving 
// the other cPolyEntities
class MapEntity: public cPolyEntity
{
private:
	cPolyEntity** entities;
	terrainArgs** map;
	int mapSize;
	float tileSize;
	sf::Vector2f destination;
	sf::Vector2f winCenter;
	int* totalEntities;
	sf::Vector2f movement;
	sf::Texture** textures;

	void handle_click(sf::Event events, sf::RenderWindow& window);
	void handle_move(sf::Event events, sf::RenderWindow& window);
	void moveEntities();
	void checkMapCollisions(sf::RenderWindow& window);
	void loadTextures();

public:
	virtual void tick(bool hasControls, sf::RenderWindow& window);
	virtual void draw(sf::RenderWindow& win);
	MapEntity(const char* path, cPolyEntity** ents, int* totalEnts, float winX, float winY);
	MapEntity(){};
};

// Handles certain controls, holds player information, still does not do much quite yet
class PlayerEntity : public cPolyEntity
{
private:
	MapEntity map;
	sf::Vector2f center;

public:
	virtual void tick(bool hasControls, sf::RenderWindow& window);
	virtual void draw(sf::RenderWindow& win);
	PlayerEntity(MapEntity& refMap, float  winX, float  winY);
};

