using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using WFWF;

namespace WrestlerBuilder
{
    public partial class WrestlerBuilder : Form
    {
        public Dictionary<String, Wrestler.attribute> attributes;
        public Dictionary<String, Wrestler.experience> generalSkills;
        public Dictionary<String, Wrestler.experience> wrestlingSkills;
        public Dictionary<String, Wrestler.bodypart> bodyParts;

        public WrestlerBuilder()
        {
            InitializeComponent();
        }

        private void Close_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
