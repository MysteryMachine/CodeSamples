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
    /// Used to determine which part of the menu we are currently showing
    /// </summary>
    public enum choice { attribute, general, wrestling, body };

    /// <summary>
    /// Main form for the game builder application
    /// </summary>
    
    public partial class MainForm : Form
    {
        public String[] genericAttributes;
        public Dictionary<String, String> genericGeneralSkills;
        public Dictionary<String, Wrestler.modifier> genericWrestlingSkills;
        public String[] genericBodyParts;
        public choice formchoice;

        Attributes attWindow;
        BodyParts bdptWindow;
        GeneralSkills gnskWindow;
        WrestlingSkills wrskWindow;

        /// <summary>
        /// Constructor
        /// </summary>
        public MainForm()
        {
            this.genericAttributes = new String[0];
            this.genericGeneralSkills = new Dictionary<String,String>();
            this.genericWrestlingSkills = new Dictionary<String,Wrestler.modifier>();
            this.genericBodyParts = new String[0];
            this.formchoice = choice.attribute;
            this.attWindow = new Attributes(this);
            this.bdptWindow = new BodyParts(this);
            this.gnskWindow = new GeneralSkills(this);
            this.wrskWindow = new WrestlingSkills(this);
            
            InitializeComponent();

            this.attributes_Click(new object(), new EventArgs());
        }

        /// <summary>
        /// Called after menus are changed in some way, it merely calls
        /// the appropriate function to update everything
        /// </summary>
        public void repopListThings()
        {
            if (this.formchoice == choice.attribute)
            {
                this.attributes_Click(new object(), new EventArgs());
            }
            else if (this.formchoice == choice.body)
            {
                this.bparts_Click(new object(), new EventArgs());
            }
            else if (this.formchoice == choice.general)
            {
                this.gskills_Click(new object(), new EventArgs());
            }
            else if (this.formchoice == choice.wrestling)
            {
                this.wskills_Click(new object(), new EventArgs());
            }
            else
            {
                throw new Exception("Tried to repopulate list, but no attribute was found");
            }
            
        }

        /// <summary>
        /// Displays all the attributes in the side menu, after clearing out
        /// the items
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void attributes_Click(object sender, EventArgs e)
        {
            this.listthings.Items.Clear();
            if (genericAttributes.Length != 0)
            {
                foreach ( String  att in genericAttributes)
                {
                    this.listthings.Items.Add(att);
                }
            }

            this.formchoice = choice.attribute;

            this.attributesButton.FlatStyle = FlatStyle.Flat;
            this.bpartsButton.FlatStyle = FlatStyle.Standard;
            this.gskillsButton.FlatStyle = FlatStyle.Standard;
            this.wskillsButton.FlatStyle = FlatStyle.Standard;
        }

        /// <summary>
        /// Displays all the general skills in the side menu, after clearing out
        /// the items
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void gskills_Click(object sender, EventArgs e)
        {
            this.listthings.Items.Clear();
            if (this.genericGeneralSkills.Count != 0)
            {
                foreach ( String  skills in this.genericGeneralSkills.Keys)
                {
                    this.listthings.Items.Add(skills);
                }
            }

            this.formchoice = choice.general;

            this.attributesButton.FlatStyle = FlatStyle.Standard;
            this.bpartsButton.FlatStyle = FlatStyle.Standard;
            this.gskillsButton.FlatStyle = FlatStyle.Flat;
            this.wskillsButton.FlatStyle = FlatStyle.Standard;
        }

        /// <summary>
        /// Displays all the wrestling skills in the side menu, after clearing out
        /// the items
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void wskills_Click(object sender, EventArgs e)
        {
            this.listthings.Items.Clear();
            if (this.genericWrestlingSkills.Count != 0)
            {
                foreach ( String  skills in this.genericWrestlingSkills.Keys)
                {
                    this.listthings.Items.Add(skills);
                }
            }

            this.formchoice = choice.wrestling;

            this.attributesButton.FlatStyle = FlatStyle.Standard;
            this.bpartsButton.FlatStyle = FlatStyle.Standard;
            this.gskillsButton.FlatStyle = FlatStyle.Standard;
            this.wskillsButton.FlatStyle = FlatStyle.Flat;
        }


        /// <summary>
        /// Displays all the body parts in the side menu, after clearing out
        /// the items
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void bparts_Click(object sender, EventArgs e)
        {
            this.listthings.Items.Clear();
            if (genericBodyParts.Length != 0)
            {
                foreach ( String  att in genericBodyParts)
                {
                    this.listthings.Items.Add(att);
                }
            }

            this.formchoice = choice.body;

            this.attributesButton.FlatStyle = FlatStyle.Standard;
            this.bpartsButton.FlatStyle = FlatStyle.Flat;
            this.gskillsButton.FlatStyle = FlatStyle.Standard;
            this.wskillsButton.FlatStyle = FlatStyle.Standard;
        }

        /// <summary>
        /// Checks to see what menu we are on, then calls the appropriate function
        /// for that menu, using the function meant to be used for adding new items
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void add_Click(object sender, EventArgs e)
        {
            if (this.formchoice == choice.attribute)
            {
                this.attWindow.openWindow();
            }

            else if (this.formchoice == choice.body)
            {
                this.bdptWindow.openWindow();
            }

            else if (this.formchoice == choice.general)
            {
                this.gnskWindow.openWindow();
            }

            else if (this.formchoice == choice.wrestling)
            {
                this.wrskWindow.openWindow();
            }

            else
            {
                throw new Exception("Somehow the mainform does not have a choice to use?");
            }
        }


        /// <summary>
        /// Searches a string array for a value, and returns its index
        /// </summary>
        /// <param name="val">Value to search for</param>
        /// <param name="list">String array to use</param>
        /// <returns></returns>
        public int getID( String  val, ref  String [] list)
        {
            int retval = -1;

            for (int i = 0; i < list.Length; i++)
            {
                if (list[i] == val)
                {
                    retval = i;
                }
            }

            return retval;
        }

        /// <summary>
        /// Figures out what menu we're in, then calls the appropriate
        /// edit function for what is highlighted in listhtings
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void edit_Click(object sender, EventArgs e)
        {
            if (this.listthings.Text == "")
            {
                return;
            }
            else if (this.formchoice == choice.attribute)
            {
                this.attWindow.openWindow(this.getID(this.listthings.Text, ref this.genericAttributes));
            }

            else if (this.formchoice == choice.body)
            {
                this.bdptWindow.openWindow(this.getID(listthings.Text, ref this.genericBodyParts));
            }

            else if (this.formchoice == choice.general)
            {
                this.gnskWindow.openWindow(this.listthings.Text);
            }

            else if (this.formchoice == choice.wrestling)
            {
                this.wrskWindow.openWindow(this.listthings.Text);
            }

            else
            {
                throw new Exception("Somehow the mainform does not have a choice to use?");
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            new SaveLoad(this).ShowDialog();
        }

        private void delete_Click(object sender, EventArgs e)
        {
            if (this.formchoice == choice.attribute)
            {
                this.attWindow.Delete(this.listthings.SelectedIndex);
            }

            else if (this.formchoice == choice.body)
            {
                this.bdptWindow.Delete(this.listthings.SelectedIndex);
            }

            else if (this.formchoice == choice.general)
            {
                this.gnskWindow.Delete(this.listthings.Text);
            }

            else if (this.formchoice == choice.wrestling)
            {
                this.wrskWindow.Delete(this.listthings.Text);
            }

            this.repopListThings();
        }
    }
}
