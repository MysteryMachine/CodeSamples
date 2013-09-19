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
        /// The attribute struct wraps around and aptitude, keeping it constant
        /// and giving defined conditions for what is a valid rating, it's maybe
        /// overly complicated for now, but if attributes become more complicated
        /// it will be easy to improve upon
        /// </summary>
        public partial struct attribute : attributeInterface
        {
            // C# properties
            private rating __aptitude;
            public rating aptitude
            {
                get
                {
                    return __aptitude;
                }
            }

            // Constructor
            public attribute(rating attRating = rating.D)
            {
                __aptitude = attRating;
            }
        }
    }
}