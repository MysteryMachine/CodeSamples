namespace GameBuilder
{
    partial class MainForm
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.attributesButton = new System.Windows.Forms.Button();
            this.gskillsButton = new System.Windows.Forms.Button();
            this.wskillsButton = new System.Windows.Forms.Button();
            this.bpartsButton = new System.Windows.Forms.Button();
            this.infobox = new System.Windows.Forms.TextBox();
            this.listthings = new System.Windows.Forms.ListBox();
            this.listlabel = new System.Windows.Forms.Label();
            this.add = new System.Windows.Forms.Button();
            this.edit = new System.Windows.Forms.Button();
            this.delete = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // attributesButton
            // 
            this.attributesButton.Location = new System.Drawing.Point(9, 8);
            this.attributesButton.Name = "attributesButton";
            this.attributesButton.Size = new System.Drawing.Size(87, 25);
            this.attributesButton.TabIndex = 0;
            this.attributesButton.Text = "Attributes";
            this.attributesButton.UseVisualStyleBackColor = true;
            this.attributesButton.Click += new System.EventHandler(this.attributes_Click);
            // 
            // gskillsButton
            // 
            this.gskillsButton.Location = new System.Drawing.Point(102, 8);
            this.gskillsButton.Name = "gskillsButton";
            this.gskillsButton.Size = new System.Drawing.Size(87, 25);
            this.gskillsButton.TabIndex = 1;
            this.gskillsButton.Text = "G. Skills";
            this.gskillsButton.UseVisualStyleBackColor = true;
            this.gskillsButton.Click += new System.EventHandler(this.gskills_Click);
            // 
            // wskillsButton
            // 
            this.wskillsButton.Location = new System.Drawing.Point(195, 8);
            this.wskillsButton.Name = "wskillsButton";
            this.wskillsButton.Size = new System.Drawing.Size(87, 25);
            this.wskillsButton.TabIndex = 2;
            this.wskillsButton.Text = "W. Skills";
            this.wskillsButton.UseVisualStyleBackColor = true;
            this.wskillsButton.Click += new System.EventHandler(this.wskills_Click);
            // 
            // bpartsButton
            // 
            this.bpartsButton.Location = new System.Drawing.Point(288, 8);
            this.bpartsButton.Name = "bpartsButton";
            this.bpartsButton.Size = new System.Drawing.Size(87, 25);
            this.bpartsButton.TabIndex = 3;
            this.bpartsButton.Text = "B. Parts";
            this.bpartsButton.UseVisualStyleBackColor = true;
            this.bpartsButton.Click += new System.EventHandler(this.bparts_Click);
            // 
            // infobox
            // 
            this.infobox.BackColor = System.Drawing.SystemColors.ControlLight;
            this.infobox.Location = new System.Drawing.Point(9, 39);
            this.infobox.Multiline = true;
            this.infobox.Name = "infobox";
            this.infobox.Size = new System.Drawing.Size(273, 149);
            this.infobox.TabIndex = 4;
            this.infobox.Text = resources.GetString("infobox.Text");
            // 
            // listthings
            // 
            this.listthings.FormattingEnabled = true;
            this.listthings.Location = new System.Drawing.Point(288, 40);
            this.listthings.Name = "listthings";
            this.listthings.Size = new System.Drawing.Size(117, 186);
            this.listthings.Sorted = true;
            this.listthings.TabIndex = 5;
            // 
            // listlabel
            // 
            this.listlabel.AutoSize = true;
            this.listlabel.Location = new System.Drawing.Point(405, 14);
            this.listlabel.Name = "listlabel";
            this.listlabel.Size = new System.Drawing.Size(0, 13);
            this.listlabel.TabIndex = 6;
            // 
            // add
            // 
            this.add.Location = new System.Drawing.Point(12, 194);
            this.add.Name = "add";
            this.add.Size = new System.Drawing.Size(87, 25);
            this.add.TabIndex = 7;
            this.add.Text = "Add";
            this.add.UseVisualStyleBackColor = true;
            this.add.Click += new System.EventHandler(this.add_Click);
            // 
            // edit
            // 
            this.edit.Location = new System.Drawing.Point(105, 194);
            this.edit.Name = "edit";
            this.edit.Size = new System.Drawing.Size(87, 25);
            this.edit.TabIndex = 8;
            this.edit.Text = "Edit";
            this.edit.UseVisualStyleBackColor = true;
            this.edit.Click += new System.EventHandler(this.edit_Click);
            // 
            // delete
            // 
            this.delete.Location = new System.Drawing.Point(195, 194);
            this.delete.Name = "delete";
            this.delete.Size = new System.Drawing.Size(87, 25);
            this.delete.TabIndex = 9;
            this.delete.Text = "Delete";
            this.delete.UseVisualStyleBackColor = true;
            this.delete.Click += new System.EventHandler(this.delete_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(378, 9);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(23, 22);
            this.button1.TabIndex = 10;
            this.button1.Text = "L";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(413, 236);
            this.ControlBox = false;
            this.Controls.Add(this.button1);
            this.Controls.Add(this.delete);
            this.Controls.Add(this.edit);
            this.Controls.Add(this.add);
            this.Controls.Add(this.listlabel);
            this.Controls.Add(this.listthings);
            this.Controls.Add(this.infobox);
            this.Controls.Add(this.bpartsButton);
            this.Controls.Add(this.wskillsButton);
            this.Controls.Add(this.gskillsButton);
            this.Controls.Add(this.attributesButton);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.Name = "MainForm";
            this.Text = "Game Maker";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button attributesButton;
        private System.Windows.Forms.Button gskillsButton;
        private System.Windows.Forms.Button wskillsButton;
        private System.Windows.Forms.Button bpartsButton;
        private System.Windows.Forms.TextBox infobox;
        private System.Windows.Forms.ListBox listthings;
        private System.Windows.Forms.Label listlabel;
        private System.Windows.Forms.Button add;
        private System.Windows.Forms.Button edit;
        private System.Windows.Forms.Button delete;
        private System.Windows.Forms.Button button1;


    }
}

