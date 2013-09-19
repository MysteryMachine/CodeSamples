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
    /// If a generalskill exists that uses an attribute that is about to be deleted or edited,
    /// </summary>
    public partial class Warning2 : Form
    {
        public Warning2()
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
