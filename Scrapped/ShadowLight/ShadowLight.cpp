#include "ShadowLight.h"


// Logics all modules, should handle controls for things
// the will launch new modules and hand control over to
// certain modules
void ShadowLightEngine::logic()
{
	for(int i = 0; i < this->totalModules; i++)
	{
		this->modules[i]->logic(true);
	}
}

// Graphics all modules and displays and clears screens
void ShadowLightEngine::graphics()
{
	window.clear();

	for(int i = 0; i < totalModules; i++)
	{
		this->modules[i]->graphics();
	}

	window.display();
}

// Creates all modules and the screen
ShadowLightEngine::ShadowLightEngine() : window(sf::RenderWindow(sf::VideoMode(800, 600), "SFML works!"))
{
	this->modules = new Module*[TOTALMODULES];
	this->totalModules = TOTALMODULES;
	this->open = true;

	this->modules[ADDRESSMAINGAMEMODULE] =  new MainGameModule(window);
}

//While the window is open, execute graphics and logic
void ShadowLightEngine::run()
{
	window.setFramerateLimit(30);
	while(window.isOpen())
	{
		this->graphics();
		this->logic();
	}
}