namespace GameBuilder
{
    partial class GeneralSkills
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
            this.textBox = new System.Windows.Forms.TextBox();
            this.sumbit = new System.Windows.Forms.Button();
            this.name = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.cancel = new System.Windows.Forms.Button();
            this.attlist = new System.Windows.Forms.ListBox();
            this.selectedatt = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // textBox
            // 
            this.textBox.Location = new System.Drawing.Point(6, 22);
            this.textBox.Name = "textBox";
            this.textBox.Size = new System.Drawing.Size(173, 20);
            this.textBox.TabIndex = 5;
            // 
            // sumbit
            // 
            this.sumbit.Location = new System.Drawing.Point(15, 242);
            this.sumbit.Name = "sumbit";
            this.sumbit.Size = new System.Drawing.Size(70, 30);
            this.sumbit.TabIndex = 4;
            this.sumbit.Text = "Submit";
            this.sumbit.UseVisualStyleBackColor = true;
            this.sumbit.Click += new System.EventHandler(this.sumbit_Click);
            // 
            // name
            // 
            this.name.AutoSize = true;
            this.name.Location = new System.Drawing.Point(12, 6);
            this.name.Name = "name";
            this.name.Size = new System.Drawing.Size(71, 13);
            this.name.TabIndex = 3;
            this.name.Text = "G. Skill Name";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 45);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(52, 13);
            this.label1.TabIndex = 6;
            this.label1.Text = "Attribute: ";
            // 
            // cancel
            // 
            this.cancel.Location = new System.Drawing.Point(111, 242);
            this.cancel.Name = "cancel";
            this.cancel.Size = new System.Drawing.Size(70, 30);
            this.cancel.TabIndex = 8;
            this.cancel.Text = "Cancel";
            this.cancel.UseVisualStyleBackColor = true;
            this.cancel.Click += new System.EventHandler(this.cancel_Click);
            // 
            // attlist
            // 
            this.attlist.FormattingEnabled = true;
            this.attlist.Location = new System.Drawing.Point(12, 66);
            this.attlist.Name = "attlist";
            this.attlist.Size = new System.Drawing.Size(169, 160);
            this.attlist.TabIndex = 9;
            this.attlist.SelectedIndexChanged += new System.EventHandler(this.attlist_SelectedIndexChanged);
            // 
            // selectedatt
            // 
            this.selectedatt.AutoSize = true;
            this.selectedatt.Location = new System.Drawing.Point(71, 45);
            this.selectedatt.Name = "selectedatt";
            this.selectedatt.Size = new System.Drawing.Size(0, 13);
            this.selectedatt.TabIndex = 10;
            // 
            // GeneralSkills
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(193, 284);
            this.ControlBox = false;
            this.Controls.Add(this.selectedatt);
            this.Controls.Add(this.attlist);
            this.Controls.Add(this.cancel);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBox);
            this.Controls.Add(this.sumbit);
            this.Controls.Add(this.name);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.Name = "GeneralSkills";
            this.Text = "General Skills";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textBox;
        private System.Windows.Forms.Button sumbit;
        private System.Windows.Forms.Label name;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button cancel;
        private System.Windows.Forms.ListBox attlist;
        private System.Windows.Forms.Label selectedatt;
    }
}