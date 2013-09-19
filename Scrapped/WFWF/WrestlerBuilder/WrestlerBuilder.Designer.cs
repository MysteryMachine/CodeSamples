namespace WrestlerBuilder
{
    partial class WrestlerBuilder
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
            this.Load = new System.Windows.Forms.Button();
            this.Close = new System.Windows.Forms.Button();
            this.Save = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.NameLabel = new System.Windows.Forms.Label();
            this.listBox = new System.Windows.Forms.ListBox();
            this.AttributesButton = new System.Windows.Forms.Button();
            this.GenSkillBUtton = new System.Windows.Forms.Button();
            this.WrsSkillButton = new System.Windows.Forms.Button();
            this.New = new System.Windows.Forms.Button();
            this.ValueLabel = new System.Windows.Forms.Label();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // Load
            // 
            this.Load.Location = new System.Drawing.Point(72, 9);
            this.Load.Name = "Load";
            this.Load.Size = new System.Drawing.Size(54, 28);
            this.Load.TabIndex = 0;
            this.Load.Text = "Load";
            this.Load.UseVisualStyleBackColor = true;
            // 
            // Close
            // 
            this.Close.Location = new System.Drawing.Point(215, 9);
            this.Close.Name = "Close";
            this.Close.Size = new System.Drawing.Size(54, 28);
            this.Close.TabIndex = 1;
            this.Close.Text = "Close";
            this.Close.UseVisualStyleBackColor = true;
            this.Close.Click += new System.EventHandler(this.Close_Click);
            // 
            // Save
            // 
            this.Save.Location = new System.Drawing.Point(132, 9);
            this.Save.Name = "Save";
            this.Save.Size = new System.Drawing.Size(54, 28);
            this.Save.TabIndex = 2;
            this.Save.Text = "Save";
            this.Save.UseVisualStyleBackColor = true;
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(59, 43);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(210, 20);
            this.textBox1.TabIndex = 3;
            // 
            // NameLabel
            // 
            this.NameLabel.AutoSize = true;
            this.NameLabel.Location = new System.Drawing.Point(12, 46);
            this.NameLabel.Name = "NameLabel";
            this.NameLabel.Size = new System.Drawing.Size(41, 13);
            this.NameLabel.TabIndex = 4;
            this.NameLabel.Text = "Name: ";
            // 
            // listBox
            // 
            this.listBox.FormattingEnabled = true;
            this.listBox.Location = new System.Drawing.Point(105, 66);
            this.listBox.Name = "listBox";
            this.listBox.Size = new System.Drawing.Size(164, 147);
            this.listBox.TabIndex = 5;
            // 
            // AttributesButton
            // 
            this.AttributesButton.Location = new System.Drawing.Point(12, 66);
            this.AttributesButton.Name = "AttributesButton";
            this.AttributesButton.Size = new System.Drawing.Size(72, 28);
            this.AttributesButton.TabIndex = 6;
            this.AttributesButton.Text = "Attributes";
            this.AttributesButton.UseVisualStyleBackColor = true;
            // 
            // GenSkillBUtton
            // 
            this.GenSkillBUtton.Location = new System.Drawing.Point(12, 100);
            this.GenSkillBUtton.Name = "GenSkillBUtton";
            this.GenSkillBUtton.Size = new System.Drawing.Size(72, 28);
            this.GenSkillBUtton.TabIndex = 7;
            this.GenSkillBUtton.Text = "G. Skills";
            this.GenSkillBUtton.UseVisualStyleBackColor = true;
            // 
            // WrsSkillButton
            // 
            this.WrsSkillButton.Location = new System.Drawing.Point(12, 134);
            this.WrsSkillButton.Name = "WrsSkillButton";
            this.WrsSkillButton.Size = new System.Drawing.Size(72, 28);
            this.WrsSkillButton.TabIndex = 8;
            this.WrsSkillButton.Text = "W. Skills";
            this.WrsSkillButton.UseVisualStyleBackColor = true;
            // 
            // New
            // 
            this.New.Location = new System.Drawing.Point(12, 9);
            this.New.Name = "New";
            this.New.Size = new System.Drawing.Size(54, 28);
            this.New.TabIndex = 9;
            this.New.Text = "New";
            this.New.UseVisualStyleBackColor = true;
            // 
            // ValueLabel
            // 
            this.ValueLabel.AutoSize = true;
            this.ValueLabel.Location = new System.Drawing.Point(9, 191);
            this.ValueLabel.Name = "ValueLabel";
            this.ValueLabel.Size = new System.Drawing.Size(37, 13);
            this.ValueLabel.TabIndex = 10;
            this.ValueLabel.Text = "Value:";
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(52, 188);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(46, 20);
            this.textBox2.TabIndex = 11;
            // 
            // WrestlerBuilder
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(281, 230);
            this.ControlBox = false;
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.ValueLabel);
            this.Controls.Add(this.New);
            this.Controls.Add(this.WrsSkillButton);
            this.Controls.Add(this.GenSkillBUtton);
            this.Controls.Add(this.AttributesButton);
            this.Controls.Add(this.listBox);
            this.Controls.Add(this.NameLabel);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.Save);
            this.Controls.Add(this.Close);
            this.Controls.Add(this.Load);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MinimizeBox = false;
            this.Name = "WrestlerBuilder";
            this.Text = "Wrestler Builder";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button Load;
        private System.Windows.Forms.Button Close;
        private System.Windows.Forms.Button Save;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Label NameLabel;
        private System.Windows.Forms.ListBox listBox;
        private System.Windows.Forms.Button AttributesButton;
        private System.Windows.Forms.Button GenSkillBUtton;
        private System.Windows.Forms.Button WrsSkillButton;
        private System.Windows.Forms.Button New;
        private System.Windows.Forms.Label ValueLabel;
        private System.Windows.Forms.TextBox textBox2;
    }
}

