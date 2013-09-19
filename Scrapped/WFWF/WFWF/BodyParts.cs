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
        /// Keeps track of the health and physical attractiveness of a body part
        /// while also providing functions that help heal or hurt the wrestlers
        /// </summary>
        public partial struct bodypart : bodypartInterface
        {
            // Consts
            private static int baseChance = 75;
            private static Random rand = new Random();

            // C# Properties
            private rating __damage;
            public rating damage
            {
                get
                {
                    return __damage;
                }
            }
            private rating __beauty;
            public rating beauty
            {
                get
                {
                    return __beauty;
                }
            }

            // Constructors
            public bodypart(rating in_beauty = rating.D)
            {
                __damage = rating.D;
                __beauty = in_beauty;
            }

            /// <summary>
            /// Simple function that determine randomly wether a wrestler is
            /// seriously hurt or not upon being hurt in an opportunity
            /// </summary>
            /// <remarks>
            /// TODO: Improve formulas for randomly being hurt
            /// </remarks>
            public void hurt()
            {
                if (__damage != rating.A)
                {
                    int chance = (100 - baseChance) * ((int)__damage - 1);
                    if (chance > rand.Next(100))
                    {
                        __damage++;
                    }
                }
            }

            /// <summary>
            /// Simple function that determine randomly wether a wrestler is
            /// healed or not upon being given the opportunity to try and heal
            /// </summary>
            /// <remarks>
            /// TODO: Improve formulas for randomly being healed
            /// </remarks>
            public void heal(bool hospital = false)
            {
                if (__damage != rating.D)
                {
                    int chance = baseChance / (int)__damage;
                    if (hospital)
                    {
                        chance *= 2;
                    }

                    if (chance > rand.Next(100) && __damage != rating.D)
                    {
                        __damage--;
                    }
                }
            }
        }
    }
}