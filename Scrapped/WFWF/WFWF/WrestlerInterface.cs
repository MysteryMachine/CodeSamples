using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace WFWF
{
    public enum rating { D = 1, C, B, A};
    public static class ratingConvert
    {
        public static string ConvertToStr(rating rate)
        {
            if(rate == rating.D)
            {
                return "D";
            }

            else if(rate == rating.C)
            {
                return "C";
            }

            else if (rate == rating.B)
            {
                return "B";
            }

            else if (rate == rating.A)
            {
                return "A";
            }

            else
            {
                return "";
            }
        }

        public static rating ConvertToRating (char rate)
        {
            if (rate == 'D')
            {
                return rating.D;
            }

            else if (rate == 'C')
            {
                return rating.C;
            }

            else if (rate == 'B')
            {
                return rating.B;
            }

            else if (rate == 'A')
            {
                return rating.A;
            }

            else
            {
                throw new Exception("This string isn't good for conversion");
            }
        }
    }
    interface modifierInterface
    {
        rating[] minAtt { get; }
        rating[] maxAtt { get; }
        String [] skillMods { get; }
    }

    interface attributeInterface
    {
        rating aptitude { get; }
    }
    interface experienceInterface
    {
        byte level { get; }

        byte exp { get; }
        void addExp(byte total);
    }
    interface bodypartInterface
    {
        rating damage { get; }
        rating beauty { get; }
        void hurt();
        void heal(bool hospital = false);
    }

    interface WrestlerInterface
    {
        Wrestler.attribute getAttribute( String  key);
        Wrestler.experience getGeneralSkill( String  key);
        Wrestler.experience getWrestlingSkill( String  key);
        Wrestler.bodypart getBodyPart( String  key);
        String name { get; }

        void expGeneralSkill( String  key, byte val);
        void expWrestlingSkill( String  key, byte val);
    }

    /// <summary>
    /// Used to define a wrestler in game, several static fields of data
    /// are kept within the class after loading it from files so that wrestlers
    /// can be copied into other wrestlers, along with keeping the data required
    /// to do things with the skills
    /// </summary>
    public partial class Wrestler : WrestlerInterface
    {
        /// <remarks>
        /// Static dictionaries that will be copied for wrestlers
        /// Generic attributes are strings that will be referenced in
        /// the dictionaries keys in the other skills, as of now they don't
        /// need to hold information statically
        /// </remarks>
        private static String[] genericAttributes;
        /// <remarks>
        /// General skills are a dictionary, with the key being the name of the
        /// and the value being an attribute
        /// </remarks>
        private static Dictionary<String, String> genericGeneralSkills;
        /// <remarks>
        /// Contains all the static information for leveling up a skill, the
        /// String key is the name of the skill, the modifier holds all the
        /// experience modifier information
        /// </remarks>
        private static Dictionary<String, modifier> genericWrestlingSkills;
        /// <remarks>
        /// An array that holds the dictionary values for the body parts,
        /// we don't need to hold any information statically as of yet
        /// </remarks>
        private static String [] genericBodyParts;

        /// <remarks>
        /// The personal skill and attribute dictionaries for wrestlers
        /// </remarks>
        private Dictionary<String, attribute> __attributes;
        private Dictionary<String, experience> __generalSkills;
        private Dictionary<String, experience> __wrestlingSkills;
        private Dictionary<String, bodypart> __bodyParts;

        private static bool isinit = false;
    }
}
