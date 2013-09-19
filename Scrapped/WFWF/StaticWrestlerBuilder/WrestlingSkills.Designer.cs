namespace GameBuilder
{
    partial class WrestlingSkills
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.gensklist = new System.Windows.Forms.CheckedListBox();
            this.attlist = new System.Windows.Forms.ListBox();
            this.cancel = new System.Windows.Forms.Button();
            this.sumbit = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.name = new System.Windows.Forms.TextBox();
            this.mintext = new System.Windows.Forms.TextBox();
            this.maxtext = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 12);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(51, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Attributes";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(218, 12);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(71, 13);
            this.label4.TabIndex = 3;
            this.label4.Text = "General Skills";
            // 
            // gensklist
            // 
            this.gensklist.FormattingEnabled = true;
            this.gensklist.Location = new System.Drawing.Point(221, 35);
            this.gensklist.Name = "gensklist";
            this.gensklist.Size = new System.Drawing.Size(146, 244);
            this.gensklist.TabIndex = 4;
            this.gensklist.ItemCheck += new System.Windows.Forms.ItemCheckEventHandler(this.gensklist_OnItemCheck);
            // 
            // attlist
            // 
            this.attlist.FormattingEnabled = true;
            this.attlist.Location = new System.Drawing.Point(12, 28);
            this.attlist.Name = "attlist";
            this.attlist.Size = new System.Drawing.Size(146, 251);
            this.attlist.TabIndex = 5;
            this.attlist.SelectedIndexChanged += new System.EventHandler(this.attlist_SelectedIndexChanged);
            // 
            // cancel
            // 
            this.cancel.Location = new System.Drawing.Point(373, 273);
            this.cancel.Name = "cancel";
            this.cancel.Size = new System.Drawing.Size(70, 30);
            this.cancel.TabIndex = 10;
            this.cancel.Text = "Cancel";
            this.cancel.UseVisualStyleBackColor = true;
            this.cancel.Click += new System.EventHandler(this.cancel_Click);
            // 
            // sumbit
            // 
            this.sumbit.Location = new System.Drawing.Point(373, 237);
            this.sumbit.Name = "sumbit";
            this.sumbit.Size = new System.Drawing.Size(70, 30);
            this.sumbit.TabIndex = 11;
            this.sumbit.Text = "Submit";
            this.sumbit.UseVisualStyleBackColor = true;
            this.sumbit.Click += new System.EventHandler(this.sumbit_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(18, 290);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(104, 13);
            this.label2.TabIndex = 12;
            this.label2.Text = "Wrestling Skill Name";
            // 
            // name
            // 
            this.name.Location = new System.Drawing.Point(128, 290);
            this.name.Name = "name";
            this.name.Size = new System.Drawing.Size(239, 20);
            this.name.TabIndex = 13;
            // 
            // mintext
            // 
            this.mintext.Location = new System.Drawing.Point(173, 42);
            this.mintext.MaxLength = 1;
            this.mintext.Name = "mintext";
            this.mintext.Size = new System.Drawing.Size(36, 20);
            this.mintext.TabIndex = 14;
            this.mintext.TextChanged += new System.EventHandler(this.mintext_TextChanged);
            // 
            // maxtext
            // 
            this.maxtext.Location = new System.Drawing.Point(173, 81);
            this.maxtext.MaxLength = 1;
            this.maxtext.Name = "maxtext";
            this.maxtext.Size = new System.Drawing.Size(36, 20);
            this.maxtext.TabIndex = 15;
            this.maxtext.TextChanged += new System.EventHandler(this.maxtext_TextChanged);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(174, 26);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(24, 13);
            this.label3.TabIndex = 16;
            this.label3.Text = "Min";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(174, 65);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(27, 13);
            this.label5.TabIndex = 17;
            this.label5.Text = "Max";
            // 
            // WrestlingSkills
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(451, 320);
            this.ControlBox = false;
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.maxtext);
            this.Controls.Add(this.mintext);
            this.Controls.Add(this.name);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.sumbit);
            this.Controls.Add(this.cancel);
            this.Controls.Add(this.attlist);
            this.Controls.Add(this.gensklist);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "WrestlingSkills";
            this.Text = "WrestlingSkills";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.CheckedListBox gensklist;
        private System.Windows.Forms.ListBox attlist;
        private System.Windows.Forms.Button cancel;
        private System.Windows.Forms.Button sumbit;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox name;
        private System.Windows.Forms.TextBox mintext;
        private System.Windows.Forms.TextBox maxtext;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label5;
    }
}