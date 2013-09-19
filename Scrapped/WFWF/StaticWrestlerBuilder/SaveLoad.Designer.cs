namespace GameBuilder
{
    partial class SaveLoad
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
            this.load = new System.Windows.Forms.Button();
            this.closeandsave = new System.Windows.Forms.Button();
            this.closewithoutsaving = new System.Windows.Forms.Button();
            this.Cancel = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // load
            // 
            this.load.Location = new System.Drawing.Point(12, 12);
            this.load.Name = "load";
            this.load.Size = new System.Drawing.Size(143, 31);
            this.load.TabIndex = 0;
            this.load.Text = "Load";
            this.load.UseVisualStyleBackColor = true;
            this.load.Click += new System.EventHandler(this.load_Click);
            // 
            // closeandsave
            // 
            this.closeandsave.Location = new System.Drawing.Point(12, 46);
            this.closeandsave.Name = "closeandsave";
            this.closeandsave.Size = new System.Drawing.Size(143, 31);
            this.closeandsave.TabIndex = 1;
            this.closeandsave.Text = "Close And Save";
            this.closeandsave.UseVisualStyleBackColor = true;
            this.closeandsave.Click += new System.EventHandler(this.closeandsave_Click);
            // 
            // closewithoutsaving
            // 
            this.closewithoutsaving.Location = new System.Drawing.Point(12, 83);
            this.closewithoutsaving.Name = "closewithoutsaving";
            this.closewithoutsaving.Size = new System.Drawing.Size(143, 31);
            this.closewithoutsaving.TabIndex = 2;
            this.closewithoutsaving.Text = "Close Without Saving";
            this.closewithoutsaving.UseVisualStyleBackColor = true;
            this.closewithoutsaving.Click += new System.EventHandler(this.closewithoutsaving_Click);
            // 
            // Cancel
            // 
            this.Cancel.Location = new System.Drawing.Point(12, 120);
            this.Cancel.Name = "Cancel";
            this.Cancel.Size = new System.Drawing.Size(143, 31);
            this.Cancel.TabIndex = 3;
            this.Cancel.Text = "Cancel";
            this.Cancel.UseVisualStyleBackColor = true;
            this.Cancel.Click += new System.EventHandler(this.Cancel_Click);
            // 
            // SaveLoad
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(167, 163);
            this.ControlBox = false;
            this.Controls.Add(this.Cancel);
            this.Controls.Add(this.closewithoutsaving);
            this.Controls.Add(this.closeandsave);
            this.Controls.Add(this.load);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.Name = "SaveLoad";
            this.Text = "WFWF";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button load;
        private System.Windows.Forms.Button closeandsave;
        private System.Windows.Forms.Button closewithoutsaving;
        private System.Windows.Forms.Button Cancel;
    }
}