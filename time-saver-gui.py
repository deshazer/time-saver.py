from Tkinter import *
from time_saver import process_csv_separate_addr
from FileProcessingGui import FileProcessingGui


# MAIN
root = Tk()

w = 720 # width for the Tk root
h = 125 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.resizable(height=False, width=False)
root.wm_title("Time Saver")

# Tk root content
app = FileProcessingGui(root, process_csv_separate_addr)

root.mainloop()
