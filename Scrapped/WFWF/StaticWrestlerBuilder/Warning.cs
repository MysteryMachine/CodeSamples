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
    /// Warning displayed when users try to sumbit an incomplete form
    /// </summary>
    public partial class Warning : Form
    {
        public Warning()
        {
            InitializeComponent();
        }
        /// <summary>
        /// Closes this form
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
