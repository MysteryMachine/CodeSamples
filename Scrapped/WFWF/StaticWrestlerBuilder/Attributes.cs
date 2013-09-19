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
    /// This class is used for the attribute editing and adding form
    /// </summary>
    public partial class Attributes : Form
    {
        MainForm main;
        String[] newArr;
        int workid;
        bool edit;
        public Attributes(MainForm mf)
        {
            this.main = mf;
            this.InitializeComponent();
        }

        /// <summary>
        /// For editing an attribute, opens the dialog window that lets one do that
        /// </summary>
        /// <param name="att">The reference to the attribute name we're editing</param>
        public void openWindow(int id)
        {
            this.edit = true;
            this.workid = id;
            this.input.Text = main.genericAttributes[id];
            this.ShowDialog();
        }

        /// <summary>
        /// For adding a new attribute, opens the dialog after resizing the attribute array
        /// to one longer, giving the last space to the new attribute.
        /// </summary>
        /// <param name="addarr">The attribute array</param>
        public void openWindow()
        {
            this.edit = false;
            this.input.Text = "";
            this.newArr = new String[main.genericAttributes.Length + 1];
            int n = 0;
            foreach (String i in main.genericAttributes)
            {
                this.newArr[n] = i;
                n++;
            }
            //main.genericAttributes = this.newArr;
            this.workid = this.newArr.Length - 1;
            this.ShowDialog();
        }

        private void cancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        /// <summary>
        /// Function called when the user clicks the submit button, it makes
        /// sure any conditions required for validating this are met, then 
        /// updates the form
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void sumbit_Click(object sender, EventArgs e)
        {
            // If the form is incomplete, display Warning
            if (this.input.Text == "")
            {
                new Warning().ShowDialog();
            }

            else
            {
                // If we're editing the name of this attribute, but its being
                // used in a general skill, display this
                if (this.edit && this.usedInOther())
                {
                    new Warning2().ShowDialog();
                }
                // If that's not the case, but any number of generic wrestling
                // exist, display warning1 
                else if (!this.edit && main.genericWrestlingSkills.Count > 0)
                {
                    new Warning1().ShowDialog();
                }
                // Otherwise, validate the form and update the main variables
                else
                {
                    if (!this.edit)
                    {
                        main.genericAttributes = newArr;
                    }
                    main.genericAttributes[workid] = (String)this.input.Text;
                    main.repopListThings();
                    this.Close();
                }
            }
        }
        /// <summary>
        /// Checks to see if the attribuet exists in a general skill
        /// </summary>
        /// <returns>
        /// Returns true if the attribute we're working with exists
        /// a general skill
        /// </returns>
        private bool usedInOther()
        {
            bool retval = false;

            String strToFind = main.genericAttributes[this.workid];
            String[] keys = main.genericGeneralSkills.Keys.ToArray();
            for (int i = 0; i < main.genericGeneralSkills.Count && !retval; i++)
            {
                if (main.genericGeneralSkills[keys[i]] == strToFind)
                {
                    retval = true;
                }
            }
            return retval;
        }

        public void Delete(int id)
        {
            this.workid = id;
            // If we're editing the name of this attribute, but its being
            // used in a general skill, display this
            if (this.edit && this.usedInOther())
            {
                new Warning2().ShowDialog();
            }
            // If that's not the case, but any number of generic wrestling
            // exist, display warning1 
            else if (!this.edit && main.genericWrestlingSkills.Count > 0)
            {
                new Warning1().ShowDialog();
            }
            else
            {
                String[] newArr = new String[main.genericAttributes.Length - 1];
                int offset = 0;
                for (int i = 0; i < main.genericAttributes.Length; i++)
                {
                    if (i == id)
                    {
                        offset = -1;
                        continue;
                    }
                    else
                    {
                        newArr[i + offset] = main.genericAttributes[i];
                    }
                }

                main.genericAttributes = newArr;
            }
        }
    }
}
