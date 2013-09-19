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
        /// The modifier struct holds a list of minimum attribute rating required
        /// to train a skill at a normal level, and the maximum attribute level
        /// with which training bonuses are confered above the minimum. It 
        /// holds a String that determines what gen skills are used for
        /// giving bonuses to wrestling skill training, of course, this is only
        /// used for wrestling skills.
        /// </summary>
        public partial struct modifier : modifierInterface
        {
            // Constants
            private static String NOSKILL = "NOSK";

            // C# properties
            private rating[] __minAtt;
            public rating[] minAtt
            {
                get
                {
                    return __minAtt;
                }
                set
                {
                    __minAtt = value;
                }
            }

            private rating[] __maxAtt;
            public rating[] maxAtt
            {
                get
                {
                    return __maxAtt;
                }

                set
                {
                    __maxAtt = value;
                }
            }

            private String[] __skillMods;
            public String[] skillMods
            {
                get
                {
                    return __skillMods;
                }

                set
                {
                    __skillMods = value;
                }
            }

            // Constructors
            public modifier(rating[] in_minAtt, rating[] in_maxAtt, 
                 ref String[] in_skillMods)
            {
                if (in_maxAtt == null || in_minAtt == null || in_skillMods == null)
                {
                    throw new Exception("Attribute array null.");
                }

                bool size_match = in_minAtt.Length == in_maxAtt.Length;

                Trace.Assert(size_match, String.Format(
                    "Error, got two in attribute arrays with" +
                    "different sizes, {0} is the first  String , {1} is the " +
                    "second  String ", in_minAtt, in_maxAtt));
                if (!size_match)
                {
                    throw new Exception("Size mismatch in skills, typo exists.");
                }

                __minAtt = in_minAtt;
                __maxAtt = in_maxAtt;
                __skillMods = in_skillMods;
            }
        }
    }
}