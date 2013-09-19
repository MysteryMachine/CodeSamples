using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Runtime.Serialization;
using System.Text;
using System.Windows.Forms;
using System.Xml;
using WFWF;

namespace GameBuilder
{
    public partial class SaveLoad : Form
    {
        MainForm parent;

        StreamReader reader;
        StreamWriter writer;
        
        string attPath;
        string genskPath;
        string wrskPath;
        string bdpPath;
        string folder;

        char gensksep1;
        
        char wrsksep1;
        char wrsksep2;

        public SaveLoad(MainForm par)
        {
            this.parent = par;

            this.folder = "generic";

            this.attPath = this.folder + "/attributes.txt";
            this.genskPath = this.folder + "/generalskills.txt";
            this.wrskPath = this.folder + "/wrestlingskills.txt";
            this.bdpPath = this.folder + "/bodyparts.txt";

            this.gensksep1 = '\t';
            this.wrsksep1 = '\t';
            this.wrsksep2 = '?';

            this.InitializeComponent();
        }

        private void Cancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void closewithoutsaving_Click(object sender, EventArgs e)
        {
            this.Close();
            parent.Close();
        }
        /// <TODO>
        /// Split every subroutine in its own function to lower the cyclomatic 
        /// complexity of this function
        /// </TODO>
        /// <summary>
        /// 
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void closeandsave_Click(object sender, EventArgs e)
        {
            if(!Directory.Exists(this.folder))
            {
                Directory.CreateDirectory(folder);
            }
            try
            {
                this.writer = new StreamWriter(this.attPath);
                foreach (string str in parent.genericAttributes)
                {
                    this.writer.WriteLine(str);
                }
                this.writer.Close();

                this.writer = new StreamWriter(this.bdpPath);
                foreach (string str in parent.genericBodyParts)
                {
                    this.writer.WriteLine(str);
                }
                this.writer.Close();

                this.writer = new StreamWriter(this.genskPath);
                string[] keys = parent.genericGeneralSkills.Keys.ToArray();
                string entry;
                for(int i = 0; i < keys.Length; i++)
                {
                    entry = parent.genericGeneralSkills[keys[i]];
                    this.writer.WriteLine("{0}{1}{2}", keys[i], this.gensksep1, entry);
                }
                this.writer.Close();

                this.writer = new StreamWriter(this.wrskPath);
                keys = parent.genericWrestlingSkills.Keys.ToArray();
                Wrestler.modifier mod;
                for (int i = 0; i < keys.Length; i++)
                {
                    mod = parent.genericWrestlingSkills[keys[i]];
                    entry = keys[i] + this.wrsksep1;
                    for(int j = 0; j < mod.minAtt.Length; j ++)
                    {
                        if (j < (mod.minAtt.Length - 1))
                        {
                            entry += ratingConvert.ConvertToStr(mod.minAtt[j]) + this.wrsksep2;
                        }
                        else
                        {
                            entry += ratingConvert.ConvertToStr(mod.minAtt[j]);
                        }
                    }
                    entry+= this.wrsksep1;
                    for(int j = 0; j < mod.maxAtt.Length; j ++)
                    {
                        if (j < (mod.maxAtt.Length - 1))
                        {
                            entry += ratingConvert.ConvertToStr(mod.maxAtt[j]) + this.wrsksep2;
                        }
                        else
                        {
                            entry += ratingConvert.ConvertToStr(mod.maxAtt[j]);
                        }
                    }
                    entry+= this.wrsksep1;
                    for (int j = 0; j < mod.skillMods.Length; j++ )
                    {
                        if (j < mod.skillMods.Length - 1)
                        {
                            entry += mod.skillMods[j] + this.wrsksep2;
                        }
                        else
                        {
                            entry += mod.skillMods[j];
                        }
                    }
                    this.writer.WriteLine(entry);
                }
                this.writer.Close();
            }

            catch (Exception w)
            {
               Trace.Assert(false, String.Format("Save error:\n {0}", w.Message));
            }
            
            this.Close();
            parent.Close();
        }

        private void load_Click(object sender, EventArgs e)
        {
            try
            {
                this.reader = new StreamReader(this.attPath);
                int i = 0;
                while (!this.reader.EndOfStream)
                {
                    this.reader.ReadLine();
                    i++;
                }
                this.reader.Close();
                this.reader = new StreamReader(this.attPath);
                parent.genericAttributes = new String[i];
                i = 0;
                while (!this.reader.EndOfStream)
                {
                    parent.genericAttributes[i] = this.reader.ReadLine();
                    i++;
                }
                this.reader.Close();

                this.reader = new StreamReader(this.bdpPath);
                i = 0;
                while (!this.reader.EndOfStream)    
                {
                    this.reader.ReadLine();
                    i++;
                }
                this.reader.Close();
                this.reader = new StreamReader(this.bdpPath);
                parent.genericBodyParts = new String[i];
                i = 0;
                while (!this.reader.EndOfStream)
                {
                    parent.genericBodyParts[i] = this.reader.ReadLine();
                    i++;
                }
                this.reader.Close();

                this.reader = new StreamReader(this.genskPath);
                while (!this.reader.EndOfStream)
                {
                    String[] strs = this.reader.ReadLine().Split(this.gensksep1);
                    parent.genericGeneralSkills.Add(strs[0], strs[1]);
                }
                this.reader.Close();

                this.reader = new StreamReader(this.wrskPath);
                while(!this.reader.EndOfStream)
                {
                    String[] strs = this.reader.ReadLine().Split(this.wrsksep1);
                    String[] minAttsStr = strs[1].Split(this.wrsksep2);
                    String[] maxAttsStr = strs[2].Split(this.wrsksep2);
                    String[] skills = strs[3].Split(this.wrsksep2);

                    rating[] minAtt = new rating[minAttsStr.Length];
                    for(i = 0; i < minAtt.Length; i++)
                    {
                        minAtt[i] = ratingConvert.ConvertToRating(minAttsStr[i][0]);
                    }
                    rating[] maxAtt = new rating[minAtt.Length];
                    for(i = 0; i < minAtt.Length; i++)
                    {
                        maxAtt[i] = ratingConvert.ConvertToRating(maxAttsStr[i][0]);
                    }

                    parent.genericWrestlingSkills.Add(strs[0], new Wrestler.modifier
                    (minAtt, maxAtt, ref skills));
                }
                this.reader.Close();
            }

            catch(Exception x)
            {
                Trace.Assert(false, String.Format("Problem loading:\n {0}", x.Message));
            }
            this.Close();
            parent.repopListThings();
        }
    }
}
