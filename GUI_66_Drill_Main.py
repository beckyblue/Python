#MAIN GUI for Drill 66
#Author: Becky Blue
#Py 3.6.1
#Master Window

from tkinter import *
from tkinter import messagebox
import tkinter as ttk
from datetime import *
from datetime import timedelta
import shutil
import os
from tkinter.filedialog import askdirectory

import GUI_66_Drill
import GUI_66_Drill_Functions



#GUI Main Window
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        #Main Frame
        self.master = master
        self.master.minsize(500, 260)
        self.master.maxsize(500, 260)

        #Main Window Centered
        GUI_66_Drill_Functions.center_window(self, 500, 260)
        self.master.title("File Mover")
        self.master.configure(bg="darkgrey")

        #Check if User wants to 'X' out of app
        self.master.protocol("WM_DELETE_WINDOW", lambda: GUI_66_Drill_Functions.ask_quit(self))


        #Load mods
        GUI_66_Drill.load_gui(self)
        GUI_66_Drill_Functions.create_db(self)

        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
