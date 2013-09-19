using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;

namespace WFWF
{
    public partial class Wrestler : WrestlerInterface
    {
        /// <summary>
        /// Will initialize the dictionaries above, constructors will all check
        /// for initialization before running, and will throw errors if
        /// intialization does not work. init() will throw an error if it fails.
        /// </summary>
        public static bool init()
        {
            return isinit;
        }

        /// <summary>
        /// Accessors for the attribute, throws out errors if the attribute
        /// is non-existant, these errors are to help modders debug.
        /// </summary>
        /// <returns>
        /// Copy of the attribute belonging to the wrestler
        /// </returns>a
        public attribute getAttribute( String  key)
        {
            bool hasKey = __attributes.ContainsKey(key);
            Trace.Assert(hasKey, String.Format(
                "Tried getting an atrribute called {0}, but did not find it" +
                "is this mispelled? Try searching the files for this name and" +
                "see if it's supposed to be there", key));
            if (!hasKey)
            {
                throw new Exception("Tried getting attribute that did not exist.");
            }
            return __attributes[key];
        }
        /// <summary>
        /// Accessors for the general skill, throws out errors if the g. skill
        /// is non-existant, these errors are to help modders debug.
        /// </summary>
        /// <returns>
        /// Copy of the general skills belonging to the wrestler
        /// </returns>
        public experience getGeneralSkill( String  key)
        {
            bool hasKey = __generalSkills.ContainsKey(key);
            Trace.Assert(hasKey, String.Format(
                "Tried getting an general skill called {0}, but did not find it" +
                "is this mispelled? Try searching the files for this name and" +
                "see if it's supposed to be there", key));
            if (!hasKey)
            {
                throw new Exception("Tried getting general skill that did not exist.");
            }
            return __generalSkills[key];
        }
        /// <summary>
        /// Accessors for the wrestling skill, throws out errors if the w. skill
        /// is non-existant, these errors are to help modders debug.
        /// </summary>
        /// <returns>
        /// Copy of the wrestling skills belonging to the wrestler
        /// </returns>
        public experience getWrestlingSkill( String  key)
        {
            bool hasKey = __wrestlingSkills.ContainsKey(key);
            Trace.Assert(hasKey, String.Format(
                "Tried getting an wrestling skill called {0}, but did not find it" +
                "is this mispelled? Try searching the files for this name and" +
                "see if it's supposed to be there", key));
            if (!hasKey)
            {
                throw new Exception("Tried getting wrestling skill that did not exist.");
            }
            return __wrestlingSkills[key];
        }
        /// <summary>
        /// Accessors for the body parts, throws out errors if the b. part
        /// is non-existant, these errors are to help modders debug.
        /// </summary>
        /// <returns>
        /// Copy of the body parts belonging to the wrestler
        /// </returns>
        public bodypart getBodyPart( String  key)
        {
            bool hasKey = __wrestlingSkills.ContainsKey(key);
            Trace.Assert(hasKey, String.Format(
                "Tried getting an bodypart called {0}, but did not find it" +
                "is this mispelled? Try searching the files for this name and" +
                "see if it's supposed to be there", key));
            if (!hasKey)
            {
                throw new Exception("Tried getting bodypart that did not exist.");
            }
            return __bodyParts[key];
        }

        /// <summary>
        /// Adds exp to a general skill, defines the parameters through which
        /// the game is allowed to modify the experience and skills of the
        /// wrestler
        /// </summary>
        public void expGeneralSkill( String  name, byte experience)
        {
            bool hasKey = __generalSkills.ContainsKey(name);
            Trace.Assert(hasKey, String.Format(
                "Tried getting an general skill called {0}, but did not find it" +
                "is this mispelled? Try searching the files for this name and" +
                "see if it's supposed to be there", name));
            if (!hasKey)
            {
                throw new Exception("Tried getting genericskill that did not exist.");
            }
            __generalSkills[name].addExp(experience);
        }
        /// <TODO>
        /// Make it so skills are properly modifying by experience mods
        /// </TODO>
        /// <summary>
        /// Adds exp to a general skill, defines the parameters through which
        /// the game is allowed to modify the experience and skills of the
        /// wrestler
        /// </summary>
        public void expWrestlingSkill( String  name, byte experience)
        {
            bool hasKey = __wrestlingSkills.ContainsKey(name);
            Trace.Assert(hasKey, String.Format(
                "Tried getting an wrestling skill called {0}, but did not find it" +
                "is this mispelled? Try searching the files for this name and" +
                "see if it's supposed to be there", name));
            if (!hasKey)
            {
                throw new Exception("Tried getting wrestling that did not exist.");
            }
            __wrestlingSkills[name].addExp(experience);
        }
    }
}
