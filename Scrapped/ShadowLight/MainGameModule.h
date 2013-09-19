#pragma once
#include "MainGameEntities.h"

// Handles any module level controls and runs things
// Note: It actually makes more sense to probably add
// certain movement functionaities and movement control checking
// to this level by itself...maybe change that for the future
class MainGameModule : public Module
{
private:
	int location;
	
	// Personal variables
	sf::RenderWindow& window;
	
	cPolyEntity** entities;

	sf::Vector2f destination;

public:
	bool permission_mouse;

	virtual void logic(bool hasControls);
	virtual void graphics();
	MainGameModule(sf::RenderWindow& inWindow);
};

