// Salomao Becker
// Juggle Fest Problem
#include "JuggleFest.h"

// Constructor
JuggleFest::JuggleFest(): circuits(circuitsTotal), jugglers(jugglersTotal),
#ifdef TEST
	file("input-ez.txt"),
	outfile("output-ez.txt", fstream::trunc)
#else
	file("input.txt"),
	outfile("output.txt", fstream::trunc)
#endif
{
	// Allocating memory
	for(int i = 0; i < jugglersTotal; i++)
	{
		this->jugglers[i] = new Juggler(i);
	}
	for(int i = 0; i < circuitsTotal; i++)
	{
		for(unsigned int j = 0; j < jugglersPerCircuit; j++)
		{
			this->circuits[i].assignedJugglers[j] = new Juggler();
		}
	}

	// Loading
	this->load();
}

// A tiny function for making sure we load things in the right
// order, it also obsfucates more from the constructor, and is
// therefore nice and easy to use
void JuggleFest::load()
{
		this->loadCircuits();
		this->loadJugglers();
}

// Loads Circuits
void JuggleFest::loadCircuits()
{
	const unsigned int lineSize = 500;
	char* line = new char[lineSize];
	for(int i = 0; i < circuitsTotal; i ++)
	{
		// Skips to before the value of H
		this->file.getline(line, lineSize, ':');
		// Reads this value
		this->file.getline(line, lineSize, ' ');

		this->circuits[i].skills.h = toInt(line);

		// Skips to before the value of E
		file.getline(line, lineSize, ':');
		// Reads this value
		file.getline(line, lineSize, ' ');

		this->circuits[i].skills.e = toInt(line);

		// Skips to before the value of P
		this->file.getline(line, lineSize, ':');
		// Reads this value
		this->file.getline(line, lineSize);

		this->circuits[i].skills.p = toInt(line);
	}
}

// Loads Jugglers
void JuggleFest::loadJugglers()
{
	const unsigned int lineSize = 500;
	char* line = new char[lineSize];
	for(int i = 0; i < jugglersTotal; i++)
	{
		// Loading the skill values is the same deal as for circuits
		this->file.getline(line, lineSize, ':');
		this->file.getline(line, lineSize, ' ');

		jugglers[i]->skills.h = toInt(line);

		this->file.getline(line, lineSize, ':');
		this->file.getline(line, lineSize, ' ');

		this->jugglers[i]->skills.e = toInt(line);

		this->file.getline(line, lineSize, ':');
		this->file.getline(line, lineSize, ' ');

		this->jugglers[i]->skills.p = toInt(line);

		// Loading preferences
		for(unsigned int j = 0; j < preferencesPerJuggler; j++)
		{
			this->file.getline(line, lineSize, 'C');
			// Things are now being delimed via commas
			if(j < preferencesPerJuggler - 1)
			{
				this->file.getline(line, lineSize, ',');
			}
			// Except at the end of the line, where we use the default
			// new line delim of getline
			else
			{
				this->file.getline(line, lineSize);
			}
			// Load in the ID of the circuit the juggler prefers,
			// and calculate his/her scores
			this->jugglers[i]->preferences[j].circuitId = toInt(line);
			this->jugglers[i]->preferences[j].circuitScore = 
				dotSkills(this->jugglers[i]->skills, 
				this->circuits[this->jugglers[i]->preferences[j].circuitId].skills);
		}
	}

	file.close();
}

// Try to insert jugglers into their preferred circuits, where j is the juggler number, 
// if insert reports that a juggler was removed from a circuit
// by returning the preference level in which the juggler was inserted, go to the next one
// and try to reinsert, this algorithm converges to a max of 1888 circuits filled in with
// people who want to be in there versus 1885 when I just kept force adding people
// until I converged, I think force adding was maybe a little faster, but I figured
// having more people be in the event they wanted was the better solution
void JuggleFest::solve()
{	
	int lastPreferenceLevelOfDisplacedJuggler;
	for(int currentPreferenceCheckLevel = 0; 
		currentPreferenceCheckLevel < preferencesPerJuggler; 
		currentPreferenceCheckLevel++)
	{
		lastPreferenceLevelOfDisplacedJuggler = -1;

		for(int j = 0; j < jugglersTotal; j++)
		{
			if(!this->jugglers[j]->isAssigned)
			{
				 lastPreferenceLevelOfDisplacedJuggler = insert(
					this->circuits[jugglers[j]->preferences[currentPreferenceCheckLevel].circuitId].assignedJugglers,
					this->jugglers[j], currentPreferenceCheckLevel,
					this->jugglers[j]->preferences[currentPreferenceCheckLevel].circuitId);
			}
			// If a juggler was removed from a circuit he was in and we have moved forward enough
			// not to check to see if he can fit into some circuits, go back
			if(lastPreferenceLevelOfDisplacedJuggler >= 0 && 
				lastPreferenceLevelOfDisplacedJuggler < currentPreferenceCheckLevel)
			{ 
					currentPreferenceCheckLevel = lastPreferenceLevelOfDisplacedJuggler;
					// This break ensures we work on high priority stuff first, rather
					// than redoubling our efforts
					break;
			}
		}
	}

	// What remains are only people who are not skilled enough to get into
	// any of the circuits they want, so just distribute them wherever
	int j = 0;
	for(int i = 0; i < circuitsTotal; i++)
	{
		for(int k = 0; k < jugglersPerCircuit; k++)
		{
			// A dummy at the end implies the event isn't full
			// No need to reset j, we don't need to try to add already added jugglers
			for( ; j < jugglersTotal && this->circuits[i].assignedJugglers[k]->dummy; j++)
			{
				if(!jugglers[j]->isAssigned)
				{
					this->circuits[i].assignedJugglers[k] = jugglers[j];
					jugglers[j]->isAssigned = true;
				}
			}
		}
	}

	this->save();
}

// Tries to insert a juggler into an already full array of jugglers,
// based on his or her skill, returns the preference level for this circuit
// of the potentially ousted last place juggler so we can check tell the
// solve function to retry adding jugglers on that level again
int JuggleFest::insert(vector<Juggler*>& circuitJugglers, Juggler*& insert, 
	const unsigned int insertRank, const unsigned int circuitId)
{
	bool assigned = false;
	// This is the preference level of a potentially removed juggler for this
	// particular circuit
	int removedPref = -1;
	for(int i = 0; i < jugglersPerCircuit && !assigned; i++)
	{
		// If this guy has a higher score than anyone, insert him into
		// the event, or if it's just a placeholder, insert also
		if(circuitJugglers[i]->dummy || insert->preferences[insertRank].circuitScore > 
			circuitJugglers[i]->preferences[circuitJugglers[i]->assignedRank].circuitScore)
		{
			// Unassign the last rank, move everything over one, add in the
			// new juggler,
			if(!circuitJugglers[jugglersPerCircuit - 1]->dummy)
			{
				removedPref = circuitJugglers[i]->assignedRank;
			}
			circuitJugglers[jugglersPerCircuit - 1]->assignedRank = -1;
			circuitJugglers[jugglersPerCircuit - 1]->isAssigned = false;

			for(int j = jugglersPerCircuit - 1; j > i; j--)
			{
				circuitJugglers[j] = circuitJugglers[j-1];
			}

			insert->assignedRank = insertRank;
			insert->isAssigned = true;
			circuitJugglers[i] = insert;

			assigned = true;
		}
	}

	return removedPref;
}

// Very simple function meant to save everything in the desired format
void JuggleFest::save()
{
#ifdef DEBUG
	// Quick sanity checking
	int cmissingCount = 0;
	int jmissingCount = 0;
	// Checks to see if all circuits are populated
	bool solved = true;
	for(int i = 0; i < circuitsTotal; i++)
	{
		// If a circuit 
		if(circuits[i].assignedJugglers[jugglersPerCircuit - 1]->dummy)
		{
			cmissingCount++;
			solved = false;
		}
	}

	// Checks to see if all jugglers are assigned
	jmissingCount = 0;
	for(int i = 0; i < jugglersTotal; i++)
	{
		if(!jugglers[i]->isAssigned)
		{
			jmissingCount++;
			solved = false;
		}
	}


	if(solved)
	{
#endif
		for(int i = circuitsTotal - 1; i >= 0; i--)
		{
			this->outfile << 'C' << i << ' ';
			for(int j = 0; j < jugglersPerCircuit; j++)
			{
				this->outfile << 'J' << this->circuits[i].assignedJugglers[j]->id << ' ';
				for(int k = 0; k < preferencesPerJuggler; k++)
				{
					this->outfile << 'C' << this->circuits[i].assignedJugglers[j]->preferences[k].circuitId;
					this->outfile << ':' << this->circuits[i].assignedJugglers[j]->preferences[k].circuitScore << ' ';
				}
			}
			this->outfile << endl;
		}

#ifdef DEBUG
	}

	else
	{
		this->outfile << cmissingCount << " circuits are missing people." << endl;
		this->outfile << jmissingCount << " jugglers unassigned";
	}
#endif

	this->outfile.flush();
	this->outfile.close();

#ifdef DEBUG
#ifndef TEST
	// Saves the email address for me
	unsigned int sum = 0;
	for(int i = 0; i < jugglersPerCircuit; i++)
	{
		sum += this->circuits[1970].assignedJugglers[i]->id;
	}

	this->outfile.open("email.txt", ofstream::trunc);
	this->outfile << sum << "@yodle.com";
#endif
#endif
}

// Entry point
void main()
{
	JuggleFest().solve();
};