#File Transfer Project
#Master
#Author: Becky Blue
#Py 3.6.1
#Functions w/db record

from tkinter import *
from tkinter import messagebox
import tkinter as ttk
from datetime import *
from datetime import timedelta
import shutil
import os


import GUI_Main
import GUI_Functions


def load_gui(self):


    self.lbl_header = ttk.Label(self.master, bg='darkgrey', font=('Arial',15,'bold'), text='File Mover Application')
    self.lbl_header.grid(row=0, column=0, columnspan=5, padx=(25,5), pady=(10,10), sticky=N)


    #Pull source direction text & entry field
    self.lbl_transfer_from = ttk.Label(self.master, bg='darkgrey', font=('Arial',12), text='FROM: Select "from" folder')#text
    self.lbl_transfer_from.grid(row=1, column=0, columnspan=2, padx=(20,0), pady=(5,0), sticky=S+W)
    self.entry_transfer_from = ttk.Entry(self.master, width=50, font=('Arial', 10))#entry field
    self.entry_transfer_from.grid(row=2, column=0, columnspan=4, padx=(25, 0), sticky=N+W)

    #Dump source direction text & entry field
    self.lbl_transfer_to = ttk.Label(self.master, bg='darkgrey', font=('Arial',12), text='TO: Select "to" folder')#text
    self.lbl_transfer_to.grid(row=3, column=0, columnspan=2, padx=(20,0), pady=(5,0), sticky=S+W)
    self.entry_transfer_to = ttk.Entry(self.master, width=50, font=('Arial', 10))#entry field
    self.entry_transfer_to.grid(row=4, column=0, columnspan=4,  padx=(25, 0), sticky=N+W)

    #Browse buttons w/directory
    self.btn_browse_from = ttk.Button(self.master, width=10, height=1, bg='darkgrey', text='Browse', command=lambda: GUI_66_Drill_Functions.browse_folder_from(self))
    self.btn_browse_from.grid(row=2, column=4, padx=25, sticky=N+W)

    self.btn_browse_to = ttk.Button(self.master, width=10, height=1, bg='darkgrey', text='Browse',command=lambda: GUI_66_Drill_Functions.browse_folder_to(self))
    self.btn_browse_to.grid(row=4, column=4, padx=25, sticky=N+W)

    # Create and place the Run button, that will execute the file check and transfer
    self.btn_run = ttk.Button(self.master,width=10, height=2, bg='lightgrey', text='Transfer Now', command=lambda: GUI_66_Drill_Functions.run_file_transfer(self))
    self.btn_run.grid(row=5, column=4, rowspan = 3, pady=(12, 10))

    # Create and place label for the last time the file check was run
    self.lbl_last_run = ttk.Label(self.master, bg='darkgrey', font=('Arial',10), text='Last File Transfer:')
    self.lbl_last_run.grid(row=5, column=0, columnspan=2, padx=(25,0), pady=(10,0), sticky=N+W)

    # Create and place the time the last file check was run
    self.lr_time = StringVar()
    self.lr_time.set('XX-XX-XXXX XX:XX:XX XX')
    self.txt_last_run_time = ttk.Label(self.master, bg='lightgrey', font=('Courier',10), width=22, textvariable=self.lr_time)
    self.txt_last_run_time.grid(row=6, column=0, columnspan=5, padx=(25,0), pady=(0,0), sticky=N+W)





if __name__ == "__main__":
    pass
