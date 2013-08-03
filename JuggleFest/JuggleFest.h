// Salomao Becker
// Juggle Fest Problem
#ifndef SALOMAOBECKERJUGGLEFEST
#define SALOMAOBECKERJUGGLEFEST
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

// When test is defined, we test the smaller sample file provided
#ifdef TEST
const unsigned int circuitsTotal = 3;
const unsigned int jugglersTotal = 12;
const unsigned int jugglersPerCircuit = jugglersTotal/circuitsTotal;
const unsigned int preferencesPerJuggler = 3;
#else
const unsigned int circuitsTotal = 2000;
const unsigned int jugglersTotal = 12000;
const unsigned int jugglersPerCircuit = jugglersTotal/circuitsTotal;
const unsigned int preferencesPerJuggler = 10;
#endif


// Structs to be used

// Keeping a standard way to hold skills makes finding
// the dot product really neat and simple
class Skills
{
public:
// Public vars
	unsigned int h;
	unsigned int e;
	unsigned int p;

// Constructor
	Skills(): h(0), e(0), p(0){};
};

// Contains the id of the prefered circuit and the juggler's
// score in it
class Preference
{
public:
// Public vars
	unsigned int circuitScore;
	unsigned int circuitId;

// Constructor
	Preference(): circuitScore(0), circuitId(0){};
};


// This holds information relevant to jugglers
class Juggler
{
public:
// Public vars
	int id;
	bool dummy;
	Skills skills;
	vector<Preference> preferences;
	bool isAssigned;
	int assignedRank;

// Constructor
	// Dummy constructor
	Juggler(): skills(), isAssigned(false), assignedRank(-1), 
		dummy(true), preferences(preferencesPerJuggler), id(-1){};
	// Juggler constructor
		Juggler(unsigned int ID): skills(), isAssigned(false), assignedRank(-1), 
		dummy(false), preferences(preferencesPerJuggler), id(ID){};
};

// This holds information relevant to circuits
class Circuit
{
public:
// Public vars
	Skills skills;
	vector<Juggler*> assignedJugglers;

// Constructor
	Circuit(): skills(), assignedJugglers(jugglersPerCircuit)
	{
		for(int i = 0; i < jugglersPerCircuit; i++)
		{
			assignedJugglers[i] = new Juggler();
		}
	};
};

class JuggleFest
{
private:
// Variables
	// Files
	fstream file;
	ofstream outfile;

	// Vector arrays
	vector<Circuit> circuits;
	vector<Juggler*> jugglers;


// Short private static functions
	// Converts a character array of characters
	// to an integer
	static unsigned int toInt(char* arr)
	{
		string str = string(arr);
		unsigned int retval = 0;
		unsigned int power = 1;
		for(int i = str.length() - 1; i >= 0; i--)
		{
			retval += power*((unsigned int)(str[i] - '0'));
			power *= 10;
		}
		
		return retval;
	};
	
	// Returns the dot product of the skill values
	static unsigned int dotSkills(Skills a, Skills b)
	{
		return a.e*b.e + a.h*b.h + a.p*b.p;
	};
	
// Private functions
	void load() ;
	void loadCircuits();
	void loadJugglers();
	static int insert(vector<Juggler*>& circuitJugglers, Juggler*& insert, 
		const unsigned int insertRank, const unsigned int circuitId);
	void save();
	
public:
// Public functions
	JuggleFest();
	void solve();
};
#endif