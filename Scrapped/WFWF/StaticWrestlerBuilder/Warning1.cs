using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace GameBuilder
{
    /// <summary>
    /// Class intended to provide a warning screen for users attempting to
    /// add a new attribute while wrestling skills exist, it's a pain to
    /// go back and change everything, so we'll just make sure users are
    /// starting from scratch if their intention is to add new attributes,
    /// I may add more functionality later, but right now, I don't feel
    /// like dealing with handling new attribute additions
    /// </summary>
    public partial class Warning1 : Form
    {
        public Warning1()
        {
            InitializeComponent();
        }

        /// <summary>
        /// Close the form
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
