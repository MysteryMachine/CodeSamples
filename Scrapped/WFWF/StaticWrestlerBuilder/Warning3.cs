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
    /// The warning displayed if the user attempts to edit a general skill name
    /// or delete it while it is being used inside a wrestlingskill
    /// </summary>
    public partial class Warning3 : Form
    {
        public Warning3()
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
