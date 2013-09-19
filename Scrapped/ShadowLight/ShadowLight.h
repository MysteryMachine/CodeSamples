#pragma once
#include "MainGameModule.h"

class ShadowLightEngine : Engine
{
private:
	Module** modules;
	sf::RenderWindow window;

public:
	virtual void logic();
	virtual void graphics();

	ShadowLightEngine();

	virtual void run();
};