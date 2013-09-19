using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using WFWF;

namespace GameBuilder
{
    /// <summary>
    /// Form for editing general skills
    /// </summary>
    public partial class GeneralSkills : Form
    {
        String workingKey;
        bool edit;
        MainForm main;
        /// <summary>
        /// Constructor
        /// </summary>
        /// <param name="mf"></param>
        public GeneralSkills(MainForm mf)
        {
            main = mf;
            InitializeComponent();
        }
        /// <summary>
        /// Opens the window for editing an existing general skill
        /// </summary>
        /// <param name="key"></param>
        public void openWindow( String  key)
        {
            this.edit = true;
            this.workingKey = key;
            this.populateMenus();
            this.ShowDialog();
        }
        /// <summary>
        /// Opens the window after populating the menus, this version
        /// is for new general skills
        /// </summary>
        public void openWindow()
        {
            this.edit = false;
            this.workingKey = "";
            this.textBox.Text = workingKey;
            this.populateMenus();
            this.ShowDialog();
        }
        /// <summary>
        /// Populates the menus in the generic skill page
        /// </summary>
        private void populateMenus()
        {
            this.textBox.Text = this.workingKey;
            this.attlist.Items.Clear();
            foreach ( String  attribute in main.genericAttributes)
            {
                this.attlist.Items.Add(attribute);
            }
            if (this.workingKey != "")
            {
                this.selectedatt.Text = main.genericGeneralSkills[this.workingKey];
            }
            else
            {
                this.selectedatt.Text = "";
            }
        }
        /// <summary>
        /// Closes the screen
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void cancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }
        /// <summary>
        /// Checks to see if we are able to submit
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void sumbit_Click(object sender, EventArgs e)
        {
            // If incomplete form, go here
            if (this.textBox.Text == "" || this.selectedatt.Text == "")
            {
                new Warning().ShowDialog();
            }
            // If this is in a wrestling skill and we're trying to change it
            else if(this.edit && this.textBox.Text != this.workingKey && this.inWSkill())
            {
                new Warning3().ShowDialog();
            }
            else
            {
                // If we're editing
                if (this.edit)
                {
                    // Readd if we've changed the name
                    if (this.textBox.Text != this.workingKey)
                    {
                        main.genericGeneralSkills.Remove(workingKey);
                        main.genericGeneralSkills.Add(this.textBox.Text, this.selectedatt.Text);
                    }
                    // Otherwise change the value in the dict
                    else
                    {
                        main.genericGeneralSkills[workingKey] = this.selectedatt.Text;
                    }
                }
                // If not, just striaght add it
                else
                {
                    main.genericGeneralSkills.Add((String)this.textBox.Text, (String)this.selectedatt.Text);
                }

                main.repopListThings();
                this.Close();
            }
        }
        /// <summary>
        /// Checks to see if the general skill is being used in a wrestling skill
        /// </summary>
        /// <returns></returns>
        private bool inWSkill()
        {
            bool retval = false;
            String[] keys = main.genericWrestlingSkills.Keys.ToArray();
            for (int i = 0; i < main.genericWrestlingSkills.Count && !retval; i++)
            {
                foreach (String str in main.genericWrestlingSkills[keys[i]].skillMods)
                {
                    if (str == this.workingKey)
                    {
                        retval = true;
                    }
                }
            }

            return retval;
        }
        /// <summary>
        /// Updates the attribute we're using upon click
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void attlist_SelectedIndexChanged(object sender, EventArgs e)
        {
            this.selectedatt.Text = this.attlist.Text;
        }

        public void Delete(string str)
        {
            this.workingKey = str;
            if(this.inWSkill())
            {
                new Warning3().ShowDialog();
            }
            else
            {
                main.genericGeneralSkills.Remove(str);
            }
        }
    }
}
