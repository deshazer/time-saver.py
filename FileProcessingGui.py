# Useful Gui app for accepting one file input, processing the input file,
# and then saving the output.
#
# You must pass the containing widget as the 1st argument and the function
# you wish to run on the input file as the 2nd argument. This is a function
# you will define but currently that function should accept inputfilename
# and outputfilename parameters.
#
# Modify the FileProcessingGui class variables def_out_ext, default_in,
# and default_out to change the extension the output file will as saved as,
# the default input file name and the default output file name respectively.

from tkinter import *  # for all the GUI widgets
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

import os  # for selecting default input/output directory/file
import re  # for manipulating dir/filename
import datetime  # for creating date specific default output filename

# Useful wrapper for setting text in a textbox
def set_text(textbox, text):
    textbox.delete("1.0", END)
    textbox.insert("1.0", text)


class FileProcessingGui:
    def __init__(self, master, runfunction):
        # Default output file extension
        self.def_out_ext = ".csv"

        # Default input path/file (default_in)
        desk_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        desk_path = re.sub(r"\\", r"/", desk_path)  # use '/' for file paths
        default_in = desk_path + "/recalls" + self.def_out_ext

        # Default output path/file (default_out)
        now = datetime.datetime.now()
        default_out = "%s/new-orders-%02d-%02d-%4d%s" % (desk_path, now.month, now.day, now.year, self.def_out_ext)

        # Save function to run on input file in a class variable
        self.process_function = runfunction

        # CREATE GUI

        # Setup different container frames
        frame_infile = Frame(master)
        frame_outfile = Frame(master)
        frame_commands = Frame(master)
        frame_infile.pack(side=TOP)
        frame_outfile.pack()
        frame_commands.pack(side=BOTTOM)

        # Setup frame_infile
        self.inlabel = Label(frame_infile, text="Input File:    ")
        self.inlabel.pack(side=LEFT)

        self.infiletext = Text(frame_infile)
        set_text(self.infiletext, default_in)
        self.infiletext.pack(side=LEFT)
        self.infiletext.config(height=1, width=55, state=NORMAL)

        self.selinfilebtn = Button(frame_infile, text="...", width=4, command=self.sel_input_file)
        self.selinfilebtn.pack(side=RIGHT)

        # Setup frame_outfile
        self.outlabel = Label(frame_outfile, text="Output File: ")
        self.outlabel.pack(side=LEFT)

        self.outfiletext = Text(frame_outfile)
        self.outfiletext.config(height=1, width=55, state=NORMAL)
        self.outfiletext.insert("1.0", default_out)
        self.outfiletext.pack(side=LEFT)

        self.seloutfilebtn = Button(frame_outfile, text="...", width=4, command=self.sel_output_file)
        self.seloutfilebtn.pack(side=RIGHT, padx=5, pady=5)

        # Setup frame_commands
        self.runbtn = Button(frame_commands, text="Run", width=11, bg="green", command=self.process_file)
        self.runbtn.pack(side=LEFT, padx=5, pady=5)

        self.quitbtn = Button(frame_commands, text="Close", width=11, bg="red", command=master.quit)
        self.quitbtn.pack(side=RIGHT)

    # CALLBACK FUNCTIONS

    def sel_input_file(self):
        self.runbtn.config(text="Run")
        filename = askopenfilename()
        if filename != "":
            set_text(self.infiletext, filename)

    def sel_output_file(self):
        self.runbtn.config(text="Run")
        filename = asksaveasfilename(defaultextension=self.def_out_ext)
        if filename != "":
            set_text(self.outfiletext, filename)

    def process_file(self):
        self.runbtn.config(text="Run")
        in_file = self.infiletext.get("1.0", END).strip()
        out_file = self.outfiletext.get("1.0", END).strip()
        inputfile = outputfile = ""

        # Make sure filename ends with correct extension
        if not out_file.lower().endswith(self.def_out_ext):
            out_file = out_file + self.def_out_ext

        try:
            inputfile = open(in_file, 'r')
        except IOError:
            messagebox.showwarning("File Error", "Failed to open file: %s\n"
                                                   "Make sure the filename is correct." % in_file)
            return
        try:
            outputfile = open(out_file, 'w')
        except IOError:
            messagebox.showwarning("File Error", "Failed to create output file!\n"
                                                 "If overwriting, make sure the file is not open.")
            return
        self.process_function(inputfile, outputfile)
        inputfile.close()
        outputfile.close()
        self.runbtn.config(text="DONE!")

    # END OF CALLBACK FUNCTIONS

# END OF CLASS FileProcessingGui
