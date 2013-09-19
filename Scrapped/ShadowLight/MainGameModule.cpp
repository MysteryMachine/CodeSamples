#include "MainGameModule.h"

// Creates the main game module
MainGameModule::MainGameModule(sf::RenderWindow& inWindow) : window(inWindow)
{
	// This process is maybe not needed
	location = ADDRESSMAINGAMEMODULE;
	id = ADDRESSMAINGAMEMODULE;

	// Loads the map and player entities
	entities = new cPolyEntity*[10];
	entitySpace = 10;
	totalEntities = new int(2);

	MapEntity* map = new MapEntity(TEST, entities, totalEntities, (float)window.getSize().x, (float)window.getSize().y);
	
	entities[ADDRESSPLAYERENTITY] = new PlayerEntity(*map, (float)window.getSize().x, (float)window.getSize().y);
	entities[ADDRESSPLAYERENTITY]->id = ADDRESSPLAYERENTITY;
	entities[ADDRESSMAPENTITY] = map;
	entities[ADDRESSMAPENTITY]->id = ADDRESSMAPENTITY;

	*totalEntities = 2;

	// Set ids
	for(unsigned int i = *this->totalEntities; i < entitySpace; i ++)
	{
		entities[i] = new cPolyEntity();
		entities[i]->id = i;
	}
}

// Calls the draw function on all entities
void MainGameModule::graphics()
{
	for(int i = 0; i < *totalEntities; i++)
	{
		entities[i]->draw(window);
	}
}

// should eventually handle module level controls, right now just ticks
// all entities
// TODO: Change map movement to happen here
void MainGameModule::logic(bool hasControls)
{
	for(int i = 0; i < *totalEntities; i++)
	{
		entities[i]->tick(hasControls, window);
	}
}