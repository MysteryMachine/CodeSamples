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
    public partial class WrestlingSkills : Form
    {
        bool change;
        String [] starr = new  String [1] { "\t" };
        rating[] stmod1 = new rating[1]{rating.D};
        rating[] stmod2 = new rating[1] { rating.D };
        MainForm main;
        String workingKey;
        Wrestler.modifier workingMod;
        public WrestlingSkills(MainForm mf)
        {
            this.main = mf;
            this.change = false;
            this.InitializeComponent();
        }

        public void openWindow( String  key)
        {
            this.workingKey = key;
            this.workingMod = main.genericWrestlingSkills[key];
            this.populateMenus();
            this.ShowDialog();
        }

        public void openWindow()
        {
            this.workingKey = "";
            this.workingMod = new Wrestler.modifier(
                this.stmod1, this.stmod2, ref this.starr);
            rating[] newRats1 = new rating[main.genericAttributes.Length];
            rating[] newRats2 = new rating[main.genericAttributes.Length];
            for (int i = 0; i < newRats1.Length; i++ )
            {
                newRats1[i] = rating.D;
                newRats2[i] = rating.D;
            }
            this.workingMod.minAtt = newRats1
                ;
            this.workingMod.maxAtt = newRats2;
            this.populateMenus();
            this.ShowDialog();
        }

        private void populateMenus()
        {
            this.mintext.Text = "";
            this.maxtext.Text = "";

            this.attlist.Items.Clear();
            foreach ( String  att in main.genericAttributes)
            {
                this.attlist.Items.Add(att);
            }

            this.gensklist.Items.Clear();
            foreach ( String  skill in main.genericGeneralSkills.Keys)
            {
                this.gensklist.Items.Add(skill);
            }

            this.name.Text = this.workingKey;

            if (this.workingKey != "")
            {
                foreach ( string  skill in this.workingMod.skillMods)
                {
                    for (int i = 0; i < gensklist.Items.Count; i++)
                    {
                        if (String.Equals(skill, gensklist.Items[i]))
                        {
                            this.gensklist.SetItemChecked(i, true);
                        }
                    }
                }
            }


        }

        private void cancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void sumbit_Click(object sender, EventArgs e)
        {
            if (this.name.Text == "" || this.workingMod.skillMods.Length == 0)
            {
                new Warning().ShowDialog();
            }
            else
            {
                if (this.workingKey != "")
                {
                    main.genericWrestlingSkills.Remove(this.workingKey);
                    main.genericWrestlingSkills.Add(this.name.Text, this.workingMod);
                }
                else
                {
                    main.genericWrestlingSkills.Add(this.name.Text, this.workingMod);
                }
                main.repopListThings();
                this.Close();
            }
        }

        private void attlist_SelectedIndexChanged(object sender, EventArgs e)
        {
            this.change = false;
            this.mintext.Text = ratingConvert.ConvertToStr(this.workingMod.minAtt[attlist.SelectedIndex]);
            this.maxtext.Text = ratingConvert.ConvertToStr(this.workingMod.maxAtt[attlist.SelectedIndex]);
            this.change = true;
        }

        private void mintext_TextChanged(object sender, EventArgs e)
        {
            if (!this.change)
            {
                return;
            }
            if (this.mintext.Text.Length > 0 && (this.mintext.Text[0] != 'C' && this.mintext.Text[0] != 'B' &&
                this.mintext.Text[0] != 'A' && this.mintext.Text[0] != 'D'))
            {
                this.mintext.Text = "";
            }
            if (this.mintext.Text.Length == 1)
            {
                this.workingMod.minAtt[this.attlist.SelectedIndex] = ratingConvert.ConvertToRating(this.mintext.Text[0]);
                if (this.workingMod.maxAtt[this.attlist.SelectedIndex] < this.workingMod.minAtt[this.attlist.SelectedIndex])
                {
                    this.workingMod.maxAtt[this.attlist.SelectedIndex] = this.workingMod.minAtt[this.attlist.SelectedIndex];
                    this.maxtext.Text = this.mintext.Text;
                }
            }
        }

        private void maxtext_TextChanged(object sender, EventArgs e)
        {
            if (!this.change)
            {
                return;
            }
            if (this.maxtext.Text.Length > 0 && (this.maxtext.Text[0] != 'C' && this.maxtext.Text[0] != 'B' &&
                this.maxtext.Text[0] != 'A' && this.maxtext.Text[0] != 'D'))
            {
                this.maxtext.Text = "";
            }
            if (this.maxtext.Text.Length == 1)
            {
                this.workingMod.maxAtt[this.attlist.SelectedIndex] = ratingConvert.ConvertToRating(this.maxtext.Text[0]);
                if (this.workingMod.maxAtt[this.attlist.SelectedIndex] < this.workingMod.minAtt[this.attlist.SelectedIndex])
                {
                    this.workingMod.maxAtt[this.attlist.SelectedIndex] = this.workingMod.minAtt[this.attlist.SelectedIndex];
                    this.maxtext.Text = this.mintext.Text;
                }
            }
        }

        private void gensklist_OnItemCheck(object sender, EventArgs e)
        {
            CheckedListBox sent = (CheckedListBox)sender;
            ItemCheckEventArgs args = (ItemCheckEventArgs)e;
            String[] newstrarr;
            if (this.workingMod.skillMods[0] == "\t")
            {
                newstrarr = new String[1];
                newstrarr[0] = sent.Text; 
                this.workingMod.skillMods = newstrarr;
                return;
            }
            else if(args.NewValue == CheckState.Unchecked 
                && this.workingMod.skillMods.Length == 1)
            {
                newstrarr = new String[1];
                newstrarr[0] = "\t";
                this.workingMod.skillMods = newstrarr;
                return;
            }
            else if (args.NewValue == CheckState.Checked)
            {
                newstrarr = new String[this.workingMod.skillMods.Length + 1];
                newstrarr[this.workingMod.skillMods.Length] = sent.Text;
            }

            else
            {
                newstrarr = new String[this.workingMod.skillMods.Length - 1];
            }
            int i = 0;
            foreach (string str in this.workingMod.skillMods)
            {
                if (i == args.Index && args.NewValue == CheckState.Unchecked)
                {
                }
                else
                {
                    newstrarr[i] = str;
                    i++;
                }
            }

            this.workingMod.skillMods = newstrarr;
        }

        public void Delete(string str)
        {
            main.genericWrestlingSkills.Remove(str);
        }
    }
}
