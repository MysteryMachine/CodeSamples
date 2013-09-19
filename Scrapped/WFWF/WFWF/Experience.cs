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
        /// The experience struct is similar to the attribute struct, it wraps
        /// around several different bits of data and makes sure they are 
        /// initated within allowable conditions, and makes sure they're not
        /// changed in a way that is illogical, it also allows for the addition
        /// of exp to the structure, as the "safe" way to change things
        /// </summary>
        public partial struct experience : experienceInterface
        {
            // Constants
            private static byte expToLevel = 100;
            private static byte maxLevel = 100;

            // C# properties
            private byte __level;
            public byte level
            {
                get
                {
                    return __level;
                }
            }

            private byte __exp;
            public byte exp
            {
                get
                {
                    return __exp;
                }
            }

            /// <summary>
            /// Add exp to the current pool, if its higher than what one needs to
            /// level up, level up, if we're at max level, don't do anything
            /// </summary>
            public void addExp(byte total)
            {
                int newexp = __exp + total;
                if (newexp > expToLevel)
                {
                    if (__level < maxLevel)
                    {
                        __level++;
                        newexp -= expToLevel;
                    }

                    else
                    {
                        return;
                    }
                }

                Debug.Assert(newexp <= byte.MaxValue,
                    "Experience not properly handled, check addExp");
                Debug.Assert(__level < maxLevel,
                    "Wrestler's level changed above max, check addExp");

                __exp = (byte)newexp;
            }

            // Constructors
            public experience(byte initialLevel = 0)
            {
                bool check = initialLevel <= expToLevel;
                Trace.Assert(check, String.Format(
                    "Attempted to intialize an experience struct " +
                    "with an initial level that was too high. Level of {0} was" +
                    "asked for, but {1} is the max level. Check the file where" +
                    "starting conditions for wrestlers are defined and make sure" +
                    "no one has a level above the max.", initialLevel, maxLevel));

                if (!check)
                {
                    throw new Exception("Level too high to fit within rules.");
                }

                __exp = 0;
                __level = initialLevel;
            }
        }
    }
}